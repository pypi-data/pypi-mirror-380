import os
import sys

os.environ["nnUNet_raw"] = ""
os.environ["nnUNet_preprocessed"] = ""
os.environ["nnUNet_results"] = ""

import argparse
from multiprocessing import set_start_method

from loguru import logger

from mircat_v2.configs import logger_setup, add_config_subparser
from mircat_v2.dicom_conversion import add_dicom_conversion_subparser
from mircat_v2.dbase import add_dbase_subparser
from mircat_v2.segmentation import add_segmentation_subparser
from mircat_v2.segmentation.models import (
    add_models_subparser,
    update_models_config,
    add_models_to_mircat,
    list_mircat_models,
)
from mircat_v2.stats import add_stats_subparser

__version__ = "0.6.0"


def main() -> None:
    ## We have to do local imports so that optional dependencies are not loaded
    """Mirshahi Lab CT Analysis Toolkit (v2) CLI entry point."""
    set_start_method("forkserver", force=True)
    parser = argparse.ArgumentParser(
        description="Mirshahi Lab CT Analysis Toolkit (v2)"
    )
    verbose_parser = parser.add_mutually_exclusive_group()
    verbose_parser.add_argument(
        "--verbose",
        "-v",
        action="store_true",
        help="Write debugging logs in the terminal.",
    )
    verbose_parser.add_argument(
        "--quiet",
        "-q",
        action="store_true",
        help="Reduce output logs in the terminal to only success and error messages.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)
    # Add all the subparsers
    add_dicom_conversion_subparser(subparsers)
    add_dbase_subparser(subparsers)
    add_models_subparser(subparsers)
    add_segmentation_subparser(subparsers)
    add_stats_subparser(subparsers)
    add_config_subparser(subparsers)
    # Parse the command line arguments
    args = parser.parse_args()
    logger_setup(args.verbose, args.quiet)
    # Handle the commands
    # Convert dicoms to nifti
    if args.command == "convert":
        try:
            from mircat_v2.dicom_conversion.converter import convert_dicoms_to_nifti

            convert_dicoms_to_nifti(args)
        except ImportError as e:
            logger.error(
                "DICOM conversion functionality requires the 'dicom' extra. "
                "Please install with: pip install mircat-v2[dicom]"
            )
            exit(1)

    # Perform a database operation
    elif args.command == "dbase":
        try:
            from mircat_v2.dbase import run_dbase_command

            run_dbase_command(args)
        except ImportError as e:
            logger.error(
                "Database functionality requires the 'dbase' extra. "
                "Please install with: pip install mircat-v2[dbase]"
            )
            exit(1)

    # Segment nifti files using a model
    elif args.command == "segment":
        try:
            from mircat_v2.segmentation import segment_nifti_files

            segment_nifti_files(args)
        except ImportError as e:
            logger.error(
                "Segmentation functionality requires the 'seg' extra. "
                "Please install with: pip install mircat-v2[seg]"
            )
            exit(1)

    # Look into segmentation models
    elif args.command == "models":
        if args.models_command == "list":
            list_mircat_models(args)
        elif args.models_command == "update":
            update_models_config()
        elif args.models_command == "add":
            add_models_to_mircat(args)

    # Run stats on niftis with segmentations
    elif args.command == "stats":
        try:
            from mircat_v2.stats import run_stats

            run_stats(args)
        except ImportError as e:
            logger.error(
                "Stats functionality requires the 'stats' extra. "
                "Please install with: pip install mircat-v2[stats]"
            )
            exit(1)

    elif args.command == "config":
        from mircat_v2.configs import print_config

        print_config(args.key, args.subkey)
    else:
        logger.error(f"Unknown command: {args.command}")
        parser.print_help()
        exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        logger.warning("Process interrupted by user. Exiting...")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)