import argparse
import os
import pandas as pd
from rich.progress import Progress, SpinnerColumn, TextColumn
from .data_cleaning import clean_data
from .trend_analysis import determine_trend
from .visualization import create_scatter


def main():
    """
    Command-line interface for PyGSODTrend package.

    Loads GSOD CSV data, cleans it, performs trend analysis for PRCP, MAX, and MIN,
    and generates geographic trend maps saved as image files.
    """
    parser = argparse.ArgumentParser(
        description="Analyze GSOD climate data trends and generate geographic trend maps for PRCP, MAX, and MIN."
    )

    parser.add_argument("input_file", help="Path to the input GSOD CSV file")
    parser.add_argument("--temp_min", type=float, default=-
                        50.0, help="Minimum valid temperature (°F)")
    parser.add_argument("--temp_max", type=float, default=130.0,
                        help="Maximum valid temperature (°F)")
    parser.add_argument("--prcp_max", type=float, default=500.0,
                        help="Maximum valid precipitation (mm)")
    parser.add_argument("--alpha", type=float, default=0.05,
                        help="Significance level for Mann-Kendall test")

    args = parser.parse_args()

    # Load CSV file
    df = pd.read_csv(args.input_file)

    # Clean CSV input data
    valid_data, _ = clean_data(df, args.temp_min, args.temp_max, args.prcp_max)

    # Attributes to analyze
    attributes = ["PRCP", "MAX", "MIN"]

    # Use Rich spinner for CLI feedback
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:

        for attr in attributes:
            task = progress.add_task(
                f"Analyzing trend for {attr}...", total=None)

            trend_df = determine_trend(valid_data, attr, args.alpha)

            if trend_df.empty:
                progress.console.print(
                    f"⚠ No trend data generated for {attr} (possibly due to insufficient valid data).")
                progress.remove_task(task)
                continue

            output_filename = f"trend_map_{attr.lower()}.png"
            create_scatter(trend_df, output_filename)

            progress.console.print(
                f"✔ Trend map for {attr} saved to: results/{output_filename}")
            progress.remove_task(task)

    print("All trend maps generated.")


if __name__ == "__main__":
    main()
