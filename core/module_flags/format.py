
import os
import sys

NAME = "format"
HELP = '--' + NAME + '="FORMAT"    Use FORMAT to formatting line output. Use {NUM} to print NUM column number.'


def on_start(line, argument: str) -> str:
	if "__DEBUG__" in os.environ:
		print("DEBUG: filter: {}".format(NAME), file=sys.stderr)
		print("DEBUG: input: {}".format(line), file=sys.stderr)

	if isinstance(line, str):
		line = line.split()

	try:
		output_line = argument.format(*line)  # Passing line to *args
	except Exception as ex:
		print("ERROR: {}".format(ex))
		sys.exit(1)

	if "__DEBUG__" in os.environ:
		print("DEBUG: output: {}".format(output_line), file=sys.stderr)

	return output_line
