# Sea Level Predictor

This project analyzes historical sea level data sourced from the EPA (Environmental Protection Agency) to visualize and predict trends in sea level rise. The data spans from 1880 to the present and includes measurements of the CSIRO Adjusted Sea Level.

## Files

### `sea_level_predictor.py`

- **Description:** Python script for analyzing sea level data and generating plots.
- **Libraries Used:**
  1. `pandas`: Data manipulation and analysis.
  2. `matplotlib`: Plotting data and visualizations.
  3. `scipy.stats`: Performing linear regression for trend analysis.
- **Functionality:** Reads sea level data from `epa-sea-level.csv`, creates a scatter plot, fits two lines of best fit (1880-2050 and 2000-2050), and saves the plot as `sea_level_plot.png`.

### `epa-sea-level.csv`

- **Description:** CSV file containing historical sea level data.
- **Data:** Includes columns for Year, CSIRO Adjusted Sea Level, Lower Error Bound, Upper Error Bound, and NOAA Adjusted Sea Level.

### `test_module.py`

- **Description:** Unit tests for verifying the functionality of `sea_level_predictor.py`.
- **Tests:** Includes tests for plot title, labels, x-tick labels, data points, and lines of best fit.

### `main.py`
- **Description:** Python script for running the `sea_level_predictor.py` and the `test_module.py` .

## Usage

1. Ensure Python and necessary libraries (`pandas`, `matplotlib`, `scipy`) are installed.
2. Run `main.py` to invoke both `sea_level_predictor.py` and the `test_module.py`, then generate `sea_level_plot.png` as output.
3. Verify functionality using `test_module.py`.

## Results

The generated `sea_level_plot.png` visually represents historical trends and projected changes in global sea levels based on the provided data.

## Credits

- Data sourced from the Environmental Protection Agency (EPA).
- Project is part of Data Analysis with Python Free Code Camp Course assesments
- Developed by Nhapo Nkululeko .

