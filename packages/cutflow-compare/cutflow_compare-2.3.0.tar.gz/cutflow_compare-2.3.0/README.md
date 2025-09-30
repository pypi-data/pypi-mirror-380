# cutflow_compare

## Overview
`cutflow_compare` is a Python package designed to simplify the comparison of cutflow histograms from ROOT files. It provides an intuitive command-line interface for analyzing and visualizing differences in cutflow data across multiple regions and files. Whether you're working with high-energy physics datasets or other ROOT-based analyses, `cutflow_compare` helps you streamline your workflow by automating comparisons and generating detailed reports.

Version 2.3.0 adds:
- `--regions-from-file` to map different region names between files (per-line column mapping)
- `--list-regions` to discover region directories containing a `cutflow` histogram
- Improved error messages with closest region suggestions when a region is missing
- Optional separate selection columns via `--separate-selections` with padding of unequal lengths
- Strict non-separated mode that now rejects differing selection lengths (use `--separate-selections` if they differ)

## Features
- Compare cutflow histograms from multiple ROOT files.
- Compare cutflow histograms with countflow histograms within the same file.
- Map differing region names across files with `--regions-from-file`.
- Discover available regions with `--list-regions`.
- Custom labels for each file using the `--labels` argument.
- Generate separate CSV reports for each region.
- Calculate relative errors and standard deviations across all files for each selection.
- Calculate cumulative error between cutflow and countflow histograms.
- Optional colored output for readability.
- Choice between merged selection column or per-file selection columns (`--separate-selections`).

## Installation
You can install the package using pip:

```sh
pip install cutflow_compare
```

Alternatively, you can clone the repository and install it manually:

```sh
git clone https://github.com/ibeuler/cutflow_compare.git
cd cutflow_compare
```

Or, if running from source:

```sh
python cutflow_compare.py --files histoOut-compared.root histoOut-reference.root -r region1 region2 region3 --labels Compared Reference
```

## Usage

After installation, you can use the command-line tool directly:

```sh
cutflow_compare --files histoOut-compared.root histoOut-reference.root -r region1 region2 region3 --labels Compared Reference
```

Or, if running from source:

```sh
python cutflow_compare.py --files histoOut-compared.root histoOut-reference.root -r region1 region2 region3 --labels Compared Reference
```

### Note:
If region names differ between files, use `--regions-from-file` instead of `-r/--regions`.

### Arguments
- `--files`: List of input ROOT files to compare. **Required.**
- `--regions`: List of regions to compare within the cutflow histograms. **Required unless using `--regions-from-file`.**
- `--regions-from-file`: Text file describing per-file region name mappings (one region mapping per line; columns correspond to order of `--files`).
- `--list-regions`: List discovered region directories (those containing a `cutflow` histogram) for each file and exit.
- `--labels`: Custom labels for each file, used in the output CSV and terminal display. **Optional.**
- `--separate-selections`: Keep selections separate instead of merging them. **Optional.**
- `--relative-error`: Include relative error calculations in the output. **Optional.**
- `--save`: Save the results to CSV files. Optionally, specify a custom filename prefix. **Optional.**
- `--colored`: Display table with colored columns for better contrast in the terminal. **Optional.**
- `--counts`: Compare cutflow output with specified countflow histograms (names provided). **Optional.**
- `--comulative-error`: Calculate cumulative error between cutflow and countflow (only valid with `--counts`). **Optional.**
- `--version`: Check the current version of cutflow_compare. **Optional.**

### Output
The tool generates **separate CSV files for each region** when the `--save` option is used. Each CSV file contains:
- Columns for each file's event counts after cuts.
- Calculated relative errors and standard deviations for each selection (if multiple files are compared).
- Calculated cumulative error between cutflow and countflow (if `--counts` and `--comulative-error` are used).

### Example Output (matching region names)
For a region `WZ` and files `histoOut-compared.root`, `histoOut-reference.root`, and `histoOut-third.root`, the output CSV might look like this:

| Selection       | Compared_Event_After_Cut | Reference_Event_After_Cut | Third_Event_After_Cut | RelativeError_AllFiles |
|------------------|--------------------------|---------------------------|-----------------------|-------------------------|
| Selection 1      | 100 ± 5                 | 105 ± 6                   | 102 ± 4              | 0.03                   |
| Selection 2      | 200 ± 10                | 195 ± 9                   | 198 ± 8              | 0.02                   |


When comparing with countflow, the output might look like this:
### Region Mapping Example (`--regions-from-file`)
Suppose file A has regions `SR2JBT`, `SR2JBV` and file B uses `2JB`, `2JBveto` for the same physics regions.

Create `regions.txt`:
```
SR2JBT 2JB
SR2JBV 2JBveto
```

Run:
```sh
cutflow_compare --files fileA.root fileB.root --regions-from-file regions.txt --labels A B
```

The first column in each line becomes the canonical display/output region name.

### Discover Regions
```sh
cutflow_compare --files fileA.root fileB.root --list-regions
```
Lists all top-level directories containing a `cutflow` histogram.

### Handling Selection Length Mismatches
- In default (merged) mode: differing numbers of selection bins across files cause the region to be skipped with an error message recommending `--separate-selections`.
- With `--separate-selections`: rows are padded with blanks for files that have fewer selections.


| Selection       | Cutflow_Event_After_Cut | countflow1_countflow | countflow2_countflow |
|------------------|--------------------------|----------------------|----------------------|
| Selection 1      | 100 ± 5                 | 98 ± 3               | 101 ± 4              |
| Selection 2      | 200 ± 10                | 195 ± 8              | 202 ± 9              |


---

## Examples

### Basic Comparison
```sh
cutflow_compare --files histoOut-compared.root histoOut-reference.root -r region1 region2
```
This compares `region1` and `region2` in the two ROOT files and prints the results to the terminal.

### Save Results to CSV
```sh
cutflow_compare --files histoOut-compared.root histoOut-reference.root -r region1 region2 --save
```
This saves the results for each region to separate CSV files, e.g., `cutflow_comparison_region1.csv` and `cutflow_comparison_region2.csv`.

### Custom Filename for Saved Results
```sh
cutflow_compare --files histoOut-compared.root histoOut-reference.root -r region1 region2 --save my_results
```
This saves the results to `my_results_region1.csv` and `my_results_region2.csv`.

### Colored Output
```sh
cutflow_compare --files histoOut-compared.root histoOut-reference.root -r region1 region2 --colored
```
This displays the results in the terminal with contrasting colors for each file's data.

#### Compare with Countflow
```sh
cutflow_compare --files histoOut-compared.root -r region1 region2 --counts countflow
```
This compares the cutflow histogram with `countflow` in `histoOut-compared.root` for `region1` and `region2`.

#### Calculate Cumulative Error
#### Different Region Names Between Files
```sh
cutflow_compare --files fileA.root fileB.root --regions-from-file regions.txt --labels A B --relative-error
```

#### Separate Selection Columns & Padding
```sh
cutflow_compare --files fileA.root fileB.root -r SR1 SR2 --separate-selections --colored
```

#### List Regions Containing a Cutflow Histogram
```sh
cutflow_compare --files fileA.root fileB.root --list-regions
```

```sh
cutflow_compare --files histoOut-compared.root -r region1 --counts countflow --comulative-error
```
This compares the cutflow histogram with `countflow` in `histoOut-compared.root` for `region1` and calculates the cumulative error.

---

## Requirements

- Python 3.6+
- [ROOT](https://root.cern/) (must be installed separately, e.g., via conda: `conda install -c conda-forge root`)
- pandas (automatically installed with the package)
- uncertainties (automatically installed with the package)
- prettytable (automatically installed with the package)

---

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

---

## Contributing
Contributions are welcome! If you have ideas for new features, bug fixes, or improvements, feel free to submit a pull request or open an issue on the [GitHub repository](https://github.com/ibeuler/cutflow_compare).

---

## Acknowledgments
## Publishing (Maintainer Notes)

To build and upload a new release (ensure version is bumped in both `setup.py` and `pyproject.toml`):

```sh
python -m pip install --upgrade build twine
rm -rf dist build *.egg-info
python -m build
twine check dist/*
twine upload dist/*
```

Test upload to TestPyPI first (optional):
```sh
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
pip install --index-url https://test.pypi.org/simple/ cutflow_compare==2.3.0
```

Tag the release:
```sh
git tag -a v2.3.0 -m "cutflow_compare 2.3.0"
git push origin v2.3.0
```

If you change console entry points, confirm `cutflow_compare` still resolves to `cutflow_compare.cutflow_compare:main`.
This package leverages the ROOT framework for data analysis and visualization. Special thanks to the open-source community for providing the tools and libraries that make this project possible.
