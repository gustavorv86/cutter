
import os
import sys
import core.cmdparser as cmdparser


NAME = "substring"
HELP = """--substring="/START/END/"
		Get the substring from "START" to "END".
		"START" and "END" can be a number or substring sequence.
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

	str_start = array[0]
	str_end = array[1]

	index_start = 0
	index_end = len(line)

	if str_start:
		if str_start.isnumeric():
			index_start = int(str_start)

		elif str_start and str_start in line:
			index_start = line.index(str_start) + len(str_start)

	if str_end:
		if str_end.isnumeric():
			index_end = int(index_end)

		elif str_end and str_end in line:
			index_end = line.index(str_end)

	if index_start < index_end:
		output_line = line[index_start:index_end]
	else:
		output_line = line

	if "__DEBUG__" in os.environ:
		print("DEBUG: output: {}".format(output_line), file=sys.stderr)

	return output_line
