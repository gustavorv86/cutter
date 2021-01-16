
import os
import sys

NAME = "split"
HELP = '--' + NAME + '="SEP"    Use SEP to split the lines.'


def on_start(line: str, argument: str):
	if "__DEBUG__" in os.environ:
		print("DEBUG: filter: {}".format(NAME), file=sys.stderr)
		print("DEBUG: input: {}".format(line), file=sys.stderr)

	output_line = line.split(argument)

	if "__DEBUG__" in os.environ:
		print("DEBUG: output: {}".format(output_line), file=sys.stderr)

	return output_line
