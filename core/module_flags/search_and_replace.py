
import os
import sys

NAME = "search-and-replace"
HELP = '--' + NAME + '="SRCH","RPLC"    Search SRCH and replace by RPLC into the line.'


def on_start(line: str, argument: str) -> str:
	if "__DEBUG__" in os.environ:
		print("DEBUG: filter: {}".format(NAME), file=sys.stderr)
		print("DEBUG: input: {}".format(line), file=sys.stderr)

	if "," not in argument:
		string_search = argument
		string_replace = ""
	else:
		array = argument.split(",")
		string_search = array[0]
		string_replace = array[1]

	output_line = line.replace(string_search, string_replace)

	if "__DEBUG__" in os.environ:
		print("DEBUG: output: {}".format(output_line), file=sys.stderr)

	return output_line
