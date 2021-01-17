
import os
import sys

NAME = "format"
HELP = """--format="FORMAT"
		Use "FORMAT" to formatting line output. Use {N} to print N column number. 
		The default character separator is the whitespaces.
		Example: --format="{0}; {1}; {3}; {4}".
"""


def on_start(line: str, argument: str) -> str:
	if "__DEBUG__" in os.environ:
		print("DEBUG: filter: {}".format(NAME), file=sys.stderr)
		print("DEBUG: input: {}".format(line), file=sys.stderr)

	line_array = line.split()

	try:
		output_line = argument.format(*line_array)  # Passing line to *args
	except Exception as ex:
		print("ERROR: {} line:{} argument:{} exception:{}".format(NAME, line, argument, ex), file=sys.stderr)
		sys.exit(1)

	output_line = " ".join(output_line)

	if "__DEBUG__" in os.environ:
		print("DEBUG: output: {}".format(output_line), file=sys.stderr)

	return output_line
