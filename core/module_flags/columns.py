

import os
import sys
import core.cmdparser as cmdparser


NAME = "columns"
HELP = """--columns="/N/M/"
		Select from the N column to the M column. The default character separator is the whitespaces.
		Use "/" as a separator character.
		From select "N" column to last column use the next expression: "/N//".
		Frome select the first column to "M" column use the next expression: "//M/".
"""


def on_start(line: str, argument: str) -> str:
	if "__DEBUG__" in os.environ:
		print("DEBUG: filter: {}".format(NAME), file=sys.stderr)
		print("DEBUG: input: {}".format(line), file=sys.stderr)

	array = cmdparser.split_flag_arguments(argument)
	if len(array) < 2:
		print("ERROR: {}, line:{}, argument:{}".format(NAME, line, argument))
		sys.exit(1)

	index_start = array[0]
	index_end = array[1]

	if index_start:
		index_start = int(index_start)

	if index_end:
		index_end = int(index_end)

	line_array = line.split()

	if index_start and index_end:
		line_array = line_array[index_start:index_end]
	elif index_start:
		line_array = line_array[index_start:]
	elif index_end:
		line_array = line_array[:index_end]

	output_line = " ".join(line_array)

	if "__DEBUG__" in os.environ:
		print("DEBUG: output: {}".format(output_line), file=sys.stderr)

	return output_line
