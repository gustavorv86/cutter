
import os
import sys

NAME = "nfilter"
HELP = """--nfilter="TEXT"
		Use "TEXT" to exclude lines.
"""


def on_start(line: str, argument: str) -> str:
	if "__DEBUG__" in os.environ:
		print("DEBUG: filter: {}".format(NAME), file=sys.stderr)
		print("DEBUG: input: {}".format(line), file=sys.stderr)

	output_line = None
	if argument not in line:
		output_line = line

	if "__DEBUG__" in os.environ:
		print("DEBUG: output: {}".format(output_line), file=sys.stderr)

	return output_line
