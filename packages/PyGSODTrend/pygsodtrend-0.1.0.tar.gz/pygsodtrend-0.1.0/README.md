# PyGSODTrend

PyGSODTrend is a command-line tool for analyzing **climate trends** from NOAA's GSOD (Global Summary of the Day) datasets.  
It cleans raw GSOD CSV data, performs **Mann-Kendall trend analysis** on precipitation (PRCP), maximum temperature (MAX), and minimum temperature (MIN), and generates **geographic scatter plots** of detected trends.

---

## Features
- ✅ Cleans GSOD input data by filtering invalid temperature and precipitation values.  
- ✅ Performs **trend analysis** using the Mann-Kendall statistical test.  
- ✅ Generates **geographic trend maps** for PRCP, MAX, and MIN.  
- ✅ Provides real-time CLI feedback with progress spinners.  
- ✅ Saves output plots as PNG images in the `results/` directory.  

---

## Installation

```bash
pip install pygsodtrend
```

---

## Usage

Run the tool on a GSOD CSV file:

```bash
pygsodtrend path/to/input.csv input_file --temp_min --temp_max --prcp_max --alpha
```

### Arguments

| Argument        | Type   | Default | Description |
|-----------------|--------|---------|-------------|
| `input_file`    | str    | —       | Path to the input GSOD CSV file. |
| `--temp_min`    | float  | -50.0   | Minimum valid temperature (°F). |
| `--temp_max`    | float  | 130.0   | Maximum valid temperature (°F). |
| `--prcp_max`    | float  | 500.0   | Maximum valid precipitation (mm). |
| `--alpha`       | float  | 0.05    | Significance level for Mann-Kendall test. |

---

## Example CLI Output

```bash
Analyzing trend for PRCP...
✔ Trend map for PRCP saved to: results/trendmapprcp.png
Analyzing trend for MAX...
✔ Trend map for MAX saved to: results/trendmapmax.png
Analyzing trend for MIN...
✔ Trend map for MIN saved to: results/trendmapmin.png
All trend maps generated.
```

---

## License
This project is licensed under the MIT License.  
Feel free to use, modify, and distribute.