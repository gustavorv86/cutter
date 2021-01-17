
import os
import sys
import core.cmdparser as cmdparser


NAME = "search-and-replace"
HELP = """--search-and-replace="/SRCH/RPLC/"
		Search "SRCH" and replace by "RPLC" into the line.
		Use "/" as a separator character.
"""


def on_start(line: str, argument: str) -> str:
	if "__DEBUG__" in os.environ:
		print("DEBUG: filter: {}".format(NAME), file=sys.stderr)
		print("DEBUG: input: {}".format(line), file=sys.stderr)

	array = cmdparser.split_flag_arguments(argument)
	if len(array) < 2:
		print("ERROR: {}, line:{}, argument:{}".format(NAME, line, argument))
		sys.exit(1)

	string_search = array[0]
	string_replace = array[1]

	output_line = line
	while string_search in line:
		output_line = line.replace(string_search, string_replace)

	if "__DEBUG__" in os.environ:
		print("DEBUG: output: {}".format(output_line), file=sys.stderr)

	return output_line
