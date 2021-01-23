
import sys
import core.debug as debug
import core.cmdparser as cmdparser


NAME = "search-and-replace"
HELP = """in:STRING --search-and-replace="/SRCH/RPLC/" out:STRING
		Search "SRCH" and replace by "RPLC" into the line.
		Use "/" as a separator character.
"""


def _flag_function(line: str, search: str, replace: str) -> str:
	if search == replace:
		return line

	output = line
	while search in output:
		output = output.replace(search, replace)

	return output


def on_start(line: str, argument: str) -> str:
	debug.module(NAME)
	debug.input(line)

	if not isinstance(line, str):
		print("ERROR: {} STRING input expected.".format(NAME), file=sys.stderr)
		sys.exit(1)

	array = cmdparser.split_flag_arguments(argument)
	if len(array) < 2:
		print("ERROR: {}, line:{}, argument:{}".format(NAME, line, argument), file=sys.stderr)
		sys.exit(1)

	output = _flag_function(line, array[0], array[1])

	debug.output(output)
	return output
