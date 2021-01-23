
import sys
import core.debug as debug

NAME = "join"
HELP = """in:LIST --join="TEXT" out:STRING
		Join the input word LIST by TEXT and return a STRING.
"""


def _flag_function(line: list, string_join: str) -> str:
	return string_join.join(line)


def on_start(line: list, argument: str) -> str:
	debug.module(NAME)
	debug.input(line)

	if not isinstance(line, list):
		print("ERROR: {} LIST input expected.".format(NAME), file=sys.stderr)
		sys.exit(1)

	output = _flag_function(line, argument)

	debug.output(output)
	return output
