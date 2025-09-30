import ROOT
import argparse
import pandas as pd
from uncertainties import ufloat
import prettytable as pt
import sys  # Import the sys module
from typing import List, Optional, Dict
import difflib

"""
Usage:
        (Matching regions across files)
            cutflow_compare --files histoOut-compared.root histoOut-reference.root -r region1 region2 region3 \
                    --labels Compared Reference --separate-selections --relative-error --save my_results --colored

        (Different region names per file using a mapping file)
            cutflow_compare --files fileA.root fileB.root --regions-from-file region_map.txt --labels A B

Description:
    This script compares cutflow histograms from multiple ROOT files across specified regions. It displays the results in a table format, optionally with colored columns for better contrast, and can save the results to CSV files.

Arguments:
    --files (-f): List of input ROOT files containing cutflow histograms.
    --regions (-r): List of regions to compare (only when region names MATCH across all files).
    --labels: Optional labels for input files. If not provided, filenames are used.
    --save: Saves the results to CSV files. Optionally specify a custom filename prefix.
    --relative-error: If set, calculates and displays the relative error between files for each selection.
    --comulative-error: It calculates the comulative error for each selection.
    --counts: Compares with counts instead of other ROOT files.
    --colored: Displays the output table with colored columns for better contrast.
    --separate-selections: If set, keeps selections separate instead of merging.
    --version: Shows the version of cutflow_compare.
    --regions-from-file: Reads region mappings from a specified text file when region names DIFFER across files.
        Format: Each non-empty, non-comment line has one region name per file, separated by spaces.
        Example for two files (fileA.root fileB.root):
            SR4JBT 4JB
            SR2JBT 2JB
        (Columns = files in the SAME order as provided to --files)

Example:
    Matching names:
        cutflow_compare --files histoOut-compared.root histoOut-reference.root -r region1 region2 region3 --labels Compared Reference --relative-error --save my_results
    Different names via mapping file:
        cutflow_compare --files histoOut-compared.root histoOut-reference.root --regions-from-file regions.txt --labels Compared Reference

Notes:
    - Use -r only if region names are identical across files.
    - Use --regions-from-file when region names differ per file (one region mapping per line).
    - To save the table, use the --save option. Optionally, add a custom filename: --save my_filename
"""

def get_file_name(file_path):
    """Extracts the file name without extension from a given file path."""
    try:
        file_name = file_path.split("/")[-1]
        file_name = file_name.replace("histoOut-", "")
        file_name = file_name.replace(".root", "")
        return file_name
    except Exception as e:
        print(f"Error extracting file name from {file_path}: {e}")
        raise

def extract_histogram_data(hist, region):
    """Extracts data (labels, contents, errors) from a ROOT histogram."""
    try:
        if not hist:
            raise ValueError(f"Histogram is None for region: {region}")
        
        nbins = hist.GetXaxis().GetNbins()
        labels_list = []
        contents = []
        contents_errored = []
        
        for i in range(1, nbins + 1):
            label = hist.GetXaxis().GetBinLabel(i)
            content = hist.GetBinContent(i)
            error = hist.GetBinError(i)
            
            labels_list.append(label)
            contents.append(ufloat(content, error))
            contents_errored.append(f"{content} ±{format(error,'.2f')}")
        
        return labels_list, contents, contents_errored
    except Exception as e:
        print(f"Error extracting histogram data for region {region}: {e}")
        raise

def compare_cutflows(args, files, regions, labels, colors, reset, region_mappings: Optional[List[List[str]]] = None):
    """Compares cutflow histograms from multiple ROOT files.

    Parameters:
        args: argparse.Namespace
        files: list of ROOT file paths
        regions: list of canonical region names (used when region_mappings is None)
        labels: labels for files
        colors/reset: coloring codes
        region_mappings: Optional list of lists. Each inner list has length == len(files) and
            contains the region name for each file in order. The first element becomes the
            canonical display region name.
    """
    if region_mappings:
        iterable = [(mapping[0], mapping) for mapping in region_mappings]
    else:
        iterable = [(region, None) for region in regions]

    # Cache discovered regions per file to avoid repeated scans
    discovered_regions: Dict[str, List[str]] = {}

    def list_regions_in_file(path: str) -> List[str]:
        if path in discovered_regions:
            return discovered_regions[path]
        regions_found = []
        try:
            tf = ROOT.TFile(path)
            if not tf or not tf.IsOpen():
                return regions_found
            for key in tf.GetListOfKeys():
                obj = key.ReadObj()
                if obj.InheritsFrom('TDirectory'):
                    # look for 'cutflow' inside
                    cut = obj.Get('cutflow')
                    if cut:
                        regions_found.append(obj.GetName())
            tf.Close()
        except Exception:
            pass
        discovered_regions[path] = regions_found
        return regions_found

    for region, mapping in iterable:
        df = pd.DataFrame()
        cont_dict = {}
        mismatched_lengths = False  # Track if any file has different number of selections when --separate-selections
        mismatch_nonsep = False     # Track mismatch in non-separated mode
        base_length = None          # Expected length in non-separated mode
        
        print(f"\n*** Processing region: {region} ***")
        
        for idx, (file, label) in enumerate(zip(files, labels)):
            try:
                f = ROOT.TFile(file)
                if not f or not f.IsOpen():
                    raise FileNotFoundError(f"Could not open file: {file}")

                # Determine actual region name for this file
                actual_region = mapping[idx] if mapping else region

                print(f"*** Starting analysis for file: {file}, region: {actual_region} (display as {region}) ***")

                hc = f.Get(actual_region + "/" + "cutflow")
                if not hc:
                    available = list_regions_in_file(file)
                    suggestion = ''
                    if available:
                        close = difflib.get_close_matches(actual_region, available, n=3, cutoff=0.4)
                        if close:
                            # Highlight closest matches in yellow
                            suggestion = " Closest existing region(s): " + ", ".join(f"\033[93m{c}\033[0m" for c in close) + "."
                        else:
                            # List all available regions in cyan
                            colored_avail = ", ".join(f"\033[96m{r}\033[0m" for r in available)
                            suggestion = f" Available regions: {colored_avail}"
                    raise ValueError(f"No 'cutflow' histogram found under region directory '{actual_region}' in file {file}.{suggestion}")
                
                labels_list, contents, contents_errored = extract_histogram_data(hc, actual_region)

                if args.separate_selections:
                    # Handle potential differing lengths across files by padding with empty strings
                    new_len = len(labels_list)
                    if df.empty:
                        df[f"{label}_Selection"] = labels_list
                        df[f"{label}_Cutflow"] = contents_errored
                    else:
                        current_len = len(df)
                        if current_len != new_len:
                            mismatched_lengths = True
                        max_len = max(current_len, new_len)
                        if current_len < max_len:
                            # Extend existing rows
                            df = df.reindex(range(max_len))
                        # Pad new lists
                        padded_labels = labels_list + [''] * (max_len - new_len)
                        padded_values = contents_errored + [''] * (max_len - new_len)
                        df[f"{label}_Selection"] = padded_labels
                        df[f"{label}_Cutflow"] = padded_values
                    # Store ufloat lists (pad with ufloat(0,0) if needed) only if lengths match so far
                    if mismatched_lengths:
                        # Skip storing for relative error if mismatch (to avoid misleading numbers)
                        pass
                    else:
                        cont_dict[f"{label}_Cutflow_ufloat"] = contents
                else:
                    # Non-separated mode: REQUIRE identical lengths; do NOT pad.
                    current_length = len(labels_list)
                    if base_length is None:
                        base_length = current_length
                        # Initialize selection column
                        df[f"Selection in region {region}"] = labels_list
                        df[f"{label}_Cutflow"] = contents_errored
                        cont_dict[f"{label}_Cutflow_ufloat"] = contents
                    else:
                        if current_length != base_length:
                            mismatch_nonsep = True
                            print(
                                f"\033[91mError:\033[0m Selection count mismatch in region '{region}' for file '{file}'. "
                                f"Expected {base_length}, got {current_length}. Use --separate-selections to allow differing lengths."
                            )
                            # Stop processing further files for this region
                            break
                        # Length matches: we can safely add cutflow column
                        df[f"{label}_Cutflow"] = contents_errored
                        cont_dict[f"{label}_Cutflow_ufloat"] = contents
            except Exception as e:
                err_msg = str(e)
                # Colored error reporting
                RED = "\033[91m"
                YELLOW = "\033[93m"
                CYAN = "\033[96m"
                BOLD = "\033[1m"
                RESET = "\033[0m"

                if 'Length of values' in err_msg and 'does not match length of index' in err_msg and not args.separate_selections:
                    print(
                        f"{RED}{BOLD}Error:{RESET} processing file {CYAN}{file}{RESET}, region {YELLOW}{region}{RESET}: {err_msg}\n"
                        f"{YELLOW}Hint:{RESET} The number of selection bins differs across files for region "
                        f"'{YELLOW}{region}{RESET}'. Re-run with {CYAN}--separate-selections{RESET} to allow differing lengths (they will be padded)."
                    )
                else:
                    print(f"{RED}{BOLD}Error:{RESET} processing file {CYAN}{file}{RESET}, region {YELLOW}{region}{RESET}: {err_msg}")
            finally:
                if f:
                    f.Close()

        if args.relative_error and len(cont_dict) > 1:
            if mismatched_lengths:
                print(f"*** Skipping relative error for region {region} due to differing number of selections across files in --separate-selections mode. ***")
            else:
                print(f"*** Calculating relative error for region: {region} ***")
                error_df = pd.DataFrame.from_dict(cont_dict)
                # Collect all columns for this region
                cols = [f"{label}_Cutflow_ufloat" for label in labels if f"{label}_Cutflow_ufloat" in error_df.columns]
                if len(cols) > 1:
                    # Get the nominal values for each file/selection
                    values = error_df[cols].apply(lambda row: [x.n for x in row], axis=1)
                    # Calculate mean and std for each selection
                    means = values.apply(lambda x: sum(x)/len(x))
                    stds = values.apply(lambda x: pd.Series(x).std())
                    # Relative error: std/mean
                    rel_error = stds / means
                    df[f"{region}_relative_error_std"] = rel_error

        # If mismatch in non-separated mode, skip printing an empty/partial table
        if mismatch_nonsep:
            # Enhanced colored warning banner for mismatch in non-separated mode
            warn = "\033[93m"   # Yellow
            err = "\033[91m"    # Red
            info = "\033[96m"   # Cyan
            bold = "\033[1m"
            reset = "\033[0m"
            border_color =  warn
            title_color = colors[1] if len(colors) > 1 else info

            message_lines = [
                f"{bold}{err}Selection length mismatch detected!{reset}",
                f"In region {title_color}{region}{reset} the number of selections differs between files.",
                f"This mode (non {bold}--separate-selections{reset}) requires identical selection lists.",
                f"Hint: Re-run with {info}--separate-selections{reset} to pad and compare differing lengths."
            ]
            width = max(len(_l.replace('\033','')) for _l in message_lines) + 4
            border = border_color + "=" * width + reset
            print(border)
            for line in message_lines:
                print(f"{border_color}|{reset} {line.ljust(width-3)}{border_color}{reset}")
            print(border)
            continue

        # Print results (default behavior)
        print(f"\n*** Results for region: {region} ***")
        table = pt.PrettyTable()
        table.field_names = df.columns.tolist()
        
        for _, row in df.iterrows():
            if args.colored:
                colored_row = []
                for i, cell in enumerate(row.tolist()):
                    # Color each file's data with different colors
                    if i == 0:  # Selection column stays uncolored
                        colored_row.append(str(cell))
                    else:
                        # Determine which file this column belongs to
                        file_index = (i - 1) % len(labels)
                        colored_row.append(f"{colors[file_index % len(colors)]}{cell}{reset}")
                table.add_row(colored_row)
            else:
                table.add_row(row.tolist())
        print(table)
        if args.save:
            # Determine filename
            if isinstance(args.save, str):
                # Custom filename prefix provided
                output_filename = f"{args.save}_{region}.csv"
            else:
                # Default filename
                output_filename = f"cutflow_comparison_{region}.csv"
        
            df.to_csv(output_filename, index=False)
            print(f"*** Results for region {region} saved to \033[92m{output_filename}\033[0m ***")

def compare_with_countflow(args, regions, labels, colors, reset):
    """Compares cutflow histograms with countflow histograms within the same file."""
    file = args.files[0]
    try:
        f = ROOT.TFile(file)
        if not f or not f.IsOpen():
            raise FileNotFoundError(f"Could not open file: {file}")
        
        for region in regions:
            df = pd.DataFrame()
            cont_dict = {}
            
            print(f"\n*** Processing region: {region} ***")
            
            hc = f.Get(region + "/" + "cutflow")
            if not hc:
                raise ValueError(f"No cutflow histogram found in file {file} for region {region}.")
            
            cutflow_labels, cutflow_contents, cutflow_contents_errored = extract_histogram_data(hc, region)

            # Pop the first item only if in --counts mode
            if args.counts:
                if cutflow_labels:
                    cutflow_labels.pop(0)
                if cutflow_contents:
                    cutflow_contents.pop(0)
                if cutflow_contents_errored:
                    cutflow_contents_errored.pop(0)

            if args.separate_selections:
                df[f"Selection"] = cutflow_labels
            else:
                df[f"Selection in region {region}"] = cutflow_labels
            df[f"{labels[0]}_Cutflow"] = cutflow_contents_errored
            cont_dict[f"{labels[0]}_Cutflow_ufloat"] = cutflow_contents
            
            for countflow_name in args.counts:
                hp = f.Get(region + "/" + countflow_name)
                if not hp:
                    print(f"Warning: No countflow histogram '{countflow_name}' found in file {file} for region {region}.")
                    continue
                
                countflow_labels, countflow_contents, countflow_contents_errored = extract_histogram_data(hp, region)
                
                df[f"{labels[0]}_{countflow_name}_Countflow"] = countflow_contents_errored
                cont_dict[f"{labels[0]}_{countflow_name}_Countflow_ufloat"] = countflow_contents
            
            # Relative error calculation (only if multiple countflows or cutflows are present)
            if args.relative_error and len(cont_dict) > 1:
                print(f"*** Calculating relative error for region: {region} ***")
                error_df = pd.DataFrame.from_dict(cont_dict)
                
                # Select relevant columns for relative error calculation
                cols = [col for col in error_df.columns if '_ufloat' in col]
                
                if len(cols) > 1:
                    values = error_df[cols].apply(lambda row: [x.n for x in row], axis=1)
                    means = values.apply(lambda x: sum(x)/len(x))
                    stds = values.apply(lambda x: pd.Series(x).std())
                    rel_error = stds / means
                    df[f"{region}_relative_error_std"] = rel_error

            # Comulative error calculation (only if multiple countflows or cutflows are present)
            if args.comulative_error and len(cont_dict) > 1:
                print(f"*** Calculating comulative error for region: {region} ***")
                error_df = pd.DataFrame.from_dict(cont_dict)
                
                # Select relevant columns for comulative error calculation
                cols = [col for col in error_df.columns if '_ufloat' in col]
                
                if len(cols) == 2:
                    values = error_df[cols].apply(lambda row: [x.n for x in row], axis=1)
                    
                    comu_error = values.apply(lambda x: (x[0]-x[1])/x[1] if x[0] != 0 else 0 if x[1] == 0 else 99999999999 )
                    df[f"{region}_comulative_error"] = comu_error
            
            # Print results (default behavior)
            print(f"\n*** Results for region: {region} ***")
            table = pt.PrettyTable()
            table.field_names = df.columns.tolist()
            
            for _, row in df.iterrows():
                if args.colored:
                    colored_row = []
                    for i, cell in enumerate(row.tolist()):
                        # Color each file's data with different colors
                        if i == 0:  # Selection column stays uncolored
                            colored_row.append(str(cell))
                        else:
                            # Determine which file this column belongs to
                            file_index = (i - 1) % (len(args.counts)+1)
                            colored_row.append(f"{colors[file_index % len(colors)]}{cell}{reset}")
                    table.add_row(colored_row)
                else:
                    table.add_row(row.tolist())
            print(table)
            
            if args.save:
                # Determine filename
                if isinstance(args.save, str):
                    # Custom filename prefix provided
                    output_filename = f"{args.save}_{region}.csv"
                else:
                    # Default filename
                    output_filename = f"cutflow_comparison_{region}.csv"
            
                df.to_csv(output_filename, index=False)
                print(f"*** Results for region {region} saved to \033[92m{output_filename}\033[0m ***")
    except Exception as e:
        print(f"Error processing file {file}: {e}")
    finally:
        if f:
            f.Close()

def parse_region_mapping_file(path: str, num_files: int) -> List[List[str]]:
    """Parses a region mapping file.

    Each non-empty, non-comment line must contain exactly one region name per file.
    Order of columns must match the order of files passed via --files.
    Returns list of lists; first element in each inner list is the canonical display region name.
    """
    mappings: List[List[str]] = []
    try:
        with open(path, 'r') as fh:
            for line_no, raw in enumerate(fh, start=1):
                line = raw.strip()
                if not line or line.startswith('#'):
                    continue
                parts = line.split()
                if len(parts) != num_files:
                    raise ValueError(
                        f"Region mapping file '{path}' line {line_no}: expected {num_files} columns (files), got {len(parts)} -> '{line}'"
                    )
                mappings.append(parts)
    except FileNotFoundError:
        raise
    except Exception as e:
        raise RuntimeError(f"Failed to parse region mapping file '{path}': {e}") from e
    if not mappings:
        raise ValueError(f"Region mapping file '{path}' produced no mappings (after ignoring comments / blank lines).")
    return mappings


def main():
    parser = argparse.ArgumentParser(description='Compare cutflow histograms')
    parser.add_argument('-f', '--files', nargs='+', required=True, help='Input ROOT files')
    parser.add_argument('-r', '--regions', nargs='+', required=False, help='Regions to compare (all files share these names)')
    parser.add_argument('--labels', nargs='+', required=False, help='Labels for input files')
    parser.add_argument('--separate-selections', action='store_true', help='Keep selections separate instead of merging')
    parser.add_argument('--relative-error', action='store_true', help='Include std in the output')
    parser.add_argument('--save', nargs='?', const=True, help='Save the results to CSV files. Optionally specify a custom filename prefix.')
    parser.add_argument('--colored', action='store_true', help='Display table with colored columns for better contrast')
    parser.add_argument('--version', action='version', version='cutflow_compare 2.3.0', help='Show the version of cutflow_compare')
    parser.add_argument('--counts', nargs='+', help='Compare with countflow histograms (names provided).')
    parser.add_argument('--comulative-error', action='store_true', help='Include comulative error in the output')
    parser.add_argument('--regions-from-file', type=str, help='Read differing region names per file from mapping file (one row per region, columns = files).')
    parser.add_argument('--list-regions', action='store_true', help='List discovered region directories (those containing a cutflow) for each file and exit.')
    args = parser.parse_args()    
    
    # Color codes for different files
    colors = ['\033[92m', '\033[94m', '\033[95m', '\033[96m', '\033[93m']  # Green, Blue, Magenta, Cyan, Yellow
    reset = '\033[0m'

    # Parse the input arguments
    files = args.files
    region_mappings: Optional[List[List[str]]] = None
    regions: List[str] = []

    # Early handling of --list-regions (no regions required)
    if args.list_regions:
        print("Listing region directories (with a 'cutflow' histogram) per file:\n")
        for file in files:
            try:
                tf = ROOT.TFile(file)
                if not tf or not tf.IsOpen():
                    print(f"File not open: {file}")
                    continue
                regions_found = []
                for key in tf.GetListOfKeys():
                    obj = key.ReadObj()
                    if obj.InheritsFrom('TDirectory') and obj.Get('cutflow'):
                        regions_found.append(obj.GetName())
                tf.Close()
                if regions_found:
                    print(f"{file}:")
                    for r in sorted(regions_found):
                        print(f"  {r}")
                else:
                    print(f"{file}: (no region directories with a 'cutflow' histogram found)")
            except Exception as e:
                print(f"Error reading {file}: {e}")
        return

    # Determine regions / mappings source (after list-regions early exit)
    if args.regions_from_file:
        region_mappings = parse_region_mapping_file(args.regions_from_file, len(files))
        if args.regions:
            print("Warning: Both -r/--regions and --regions-from-file provided. Ignoring --regions in favor of mapping file.")
        regions = [m[0] for m in region_mappings]
    else:
        if not args.regions:
            print("Error: You must provide either -r/--regions or --regions-from-file (or use --list-regions).")
            sys.exit(1)
        regions = args.regions
    labels = args.labels if args.labels else [get_file_name(file) for file in files]


    if len(labels) != len(files):
        print("Error: Number of labels must match number of files.")
        sys.exit(1)

    if args.counts:
        if len(args.files) != 1:
            print("Error: --counts option is only valid with a single file.")
            sys.exit(1)
        # In counts mode we only have one file; if mappings provided, we just use canonical region list
        compare_with_countflow(args, regions, labels, colors, reset)
    else:
        compare_cutflows(args, files, regions, labels, colors, reset, region_mappings=region_mappings)
        if args.comulative_error:
            print("\033[91m Note:\033[0m comulative error is only calculated with --counts option!")

    if args.save:
        print("\n" + "*" * 50)
        print("*** All comparison results saved successfully! ***")
        print("*" * 50 + "\n")
    else:
        print("\033[91m The Table is not saved!")
        print("\033[0m*** To save the table, use \033[92m--save\033[0m option. Optionally, add a custom filename: \033[92m--save my_filename\033[0m ***\033[0m")
        
if __name__ == "__main__":
    main()