"""Module for running snakemake workflow for the ARI3D project."""
import argparse
import runpy
import sys
from pathlib import Path

# this file
cur_file = Path(__file__).resolve()


def run_snakemake(args):
    """Run the Snakemake workflow with the provided arguments."""
    # create necessary output directories, must exist before snakemake is called
    import os
    os.makedirs(args.project_dir, exist_ok=True)

    sys.argv = [
        "snakemake",
        "all",
        "--snakefile",
        str(cur_file.parent.joinpath("Snakefile")),
        "--cores",
        str(args.cores),
        "--config",
        f"input_dir={args.input_dir}",
        f"project_dir={args.project_dir}",
        f"parameters_file={args.parameters_file}",
        f"loglevel={args.loglevel}",
    ]

    # Run Snakemake as module
    runpy.run_module("snakemake", run_name="__main__")


def main():
    """Parse arguments and run the Snakemake workflow."""
    parser = argparse.ArgumentParser(
        prog="ari3d", description="ari3d snakemake workflow entry point", add_help=True
    )

    parser.add_argument("--input_dir", help="Input directory containing the data files")
    parser.add_argument("--project_dir", help="Directory to create the project in")
    parser.add_argument("--parameters_file", help="Path to the parameters file")
    parser.add_argument(
        "--cores",
        type=int,
        help="Number of cores to use for the workflow",
        default=1,
        required=False,
    )
    parser.add_argument(
        "--loglevel", type=str, help="Logging level", default="INFO", required=False
    )

    # Show help if no arguments are passed
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    run_snakemake(args)


if __name__ == "__main__":
    main()
