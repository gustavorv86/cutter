
import sys
import core.debug as debug
import core.cmdparser as cmdparser


NAME = "substring"
HELP = """in:STRING --substring="/START/END/" out:STRING
		Return the substring into START and END.
		START and END are the index numbers into the STRING.
		If start index not specified then return the STRING from the head.
		If end index not specified then return the String to the tail.
		Use "/" as a separator character.
		Example: foobar --substring=/2/3/    (output: ob)
		Example: foobar --substring=/3//     (output: bar)
		Example: foobar --substring=//3/     (output: foo)
"""


def _flag_function(line: str, index_start, index_end) -> str:
	if index_start and index_end:
		return line[index_start:index_end]
	elif index_start:
		return line[index_start:]
	elif index_end:
		return line[:index_end]
	else:
		return line


def on_start(line: str, argument: str) -> str:
	debug.module(NAME)
	debug.input(line)

	if not isinstance(line, str):
		print("ERROR: {} STRING input expected.".format(NAME), file=sys.stderr)
		sys.exit(1)

	array = cmdparser.split_flag_arguments(argument)
	if len(array) < 2:
		print("ERROR: {}, line:{}, argument:{}.".format(NAME, line, argument), file=sys.stderr)
		sys.exit(1)
	
	index_start = array[0]
	index_end = array[1]
	
	if index_start and index_start.isnumeric():
		index_start = int(index_start)
	else:
		index_start = None

	if index_end and index_end.isnumeric():
		index_end = int(index_end)
	else:
		index_end = None

	if not index_start and not index_end:
		print("ERROR: {}, line:{}, argument:{}.".format(NAME, line, argument), file=sys.stderr)
		sys.exit(1)

	output = _flag_function(line, index_start, index_end)

	debug.output(output)
	return output

