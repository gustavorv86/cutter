
import sys
import core.debug as debug

NAME = "format"
HELP = """in:LIST --format="FORMAT" out:STRING
		Use "FORMAT" to formatting line output. Use {N} to print N word LIST. 
		Example: --format="{0}; {1}; {3}; {4}".
"""


def _flag_function(line: list, string_format: str) -> str:
	try:
		return string_format.format(*line)  # Passing line to *args
	except Exception as ex:
		print("ERROR: {} line:{} argument:{} exception:{}".format(NAME, line, string_format, ex), file=sys.stderr)
		sys.exit(1)


def on_start(line: list, argument: str) -> str:
	debug.module(NAME)
	debug.input(line)

	if not isinstance(line, list):
		print("ERROR: {} LIST input expected.".format(NAME), file=sys.stderr)
		sys.exit(1)

	output = _flag_function(line, argument)

	debug.output(output)
	return output
