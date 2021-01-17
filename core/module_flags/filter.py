
import os
import sys

NAME = "filter"
HELP = """--filter="TEXT"
		Use "TEXT" to include lines.
"""


def on_start(line: str, argument: str) -> str:
	if "__DEBUG__" in os.environ:
		print("DEBUG: filter: {}".format(NAME), file=sys.stderr)
		print("DEBUG: input: {}".format(line), file=sys.stderr)

	output_line = None
	if argument in line:
		output_line = line

	if "__DEBUG__" in os.environ:
		print("DEBUG: output: {}".format(output_line), file=sys.stderr)

	return output_line
