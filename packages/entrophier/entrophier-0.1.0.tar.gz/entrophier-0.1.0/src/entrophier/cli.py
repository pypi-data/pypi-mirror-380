"""
Command-line interface for the entropy redaction tool.
"""

import argparse
import sys

from .config import load_config
from .core import redact_high_entropy_tokens, redact_high_entropy_strings


def main():
    """Command-line interface for processing files or stdin."""
    parser = argparse.ArgumentParser(
        description="Redact high-entropy strings from text files or stdin",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.txt                    # Redact file, output redacted strings only
  %(prog)s -c input.txt                 # Comparative mode (original vs redacted)
  cat logfile.txt | %(prog)s            # Process stdin
  %(prog)s -c -o output.txt input.txt   # Save comparative output to file
        """,
    )

    parser.add_argument(
        "input_file",
        nargs="?",
        help='Input file path (use "-" or omit for stdin)',
    )
    parser.add_argument(
        "-c",
        "--comparative",
        action="store_true",
        help="Show both original and redacted strings (default: redacted only)",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file path (default: stdout)",
    )
    parser.add_argument(
        "--method",
        choices=["token", "sliding"],
        default="token",
        help="Redaction method (default: token)",
    )
    parser.add_argument(
        "--threshold",
        type=float,
        help="Override entropy threshold from config",
    )
    parser.add_argument(
        "--min-length",
        type=int,
        help="Override minimum length from config",
    )
    parser.add_argument(
        "--condense-asterisks",
        action="store_true",
        help="Condense consecutive asterisks to single asterisk",
    )
    parser.add_argument(
        "--config-dir",
        help="Directory containing configuration files (default: module directory)",
    )

    args = parser.parse_args()

    # Load configuration
    try:
        load_config(config_dir=args.config_dir)
    except SystemExit:
        sys.stderr.write(
            "Error: Failed to load configuration files. See above for details.\n"
        )
        sys.exit(1)

    # Choose redaction function
    if args.method == "token":
        redact_func = redact_high_entropy_tokens
    else:
        redact_func = redact_high_entropy_strings

    # Setup input
    if args.input_file and args.input_file != "-":
        try:
            input_file = open(args.input_file, "r", encoding="utf-8")
        except IOError as e:
            sys.stderr.write(f"Error opening input file: {e}\n")
            sys.exit(1)
    else:
        input_file = sys.stdin

    # Setup output
    if args.output:
        try:
            output_file = open(args.output, "w", encoding="utf-8")
        except IOError as e:
            sys.stderr.write(f"Error opening output file: {e}\n")
            sys.exit(1)
    else:
        output_file = sys.stdout

    # Process input line by line
    try:
        for line_num, line in enumerate(input_file, 1):
            line = line.rstrip("\n\r")
            if not line.strip():  # Skip empty lines
                continue

            try:
                # Apply redaction with optional parameter overrides
                kwargs = {}
                if args.threshold is not None:
                    kwargs["entropy_threshold"] = args.threshold
                if args.min_length is not None:
                    kwargs["min_length"] = args.min_length
                if args.condense_asterisks:
                    kwargs["condense_asterisks"] = True

                redacted = redact_func(line, **kwargs)

                if args.comparative:
                    output_file.write(f"Original:  {line}\n")
                    output_file.write(f"Redacted:  {redacted}\n")
                    output_file.write("\n")
                else:
                    output_file.write(f"{redacted}\n")

            except Exception as e:
                sys.stderr.write(f"Error processing line {line_num}: {e}\n")

    except KeyboardInterrupt:
        sys.stderr.write("\nInterrupted by user\n")
        sys.exit(1)
    finally:
        if input_file != sys.stdin:
            input_file.close()
        if output_file != sys.stdout:
            output_file.close()


if __name__ == "__main__":
    main()
