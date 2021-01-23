
import sys
import core.debug as debug

NAME = "nfilter"
HELP = """in:STRING --nfilter="TEXT" out:STRING
		Use TEXT to include lines.
"""


def _flag_function(line: str, search: str) -> str:
	if search not in line:
		return line
	else:
		return ""


def on_start(line: str, argument: str):
	debug.module(NAME)
	debug.input(line)

	if not isinstance(line, str):
		print("ERROR: {} STRING input expected.".format(NAME), file=sys.stderr)
		sys.exit(1)

	output = _flag_function(line, argument)

	debug.output(output)
	return output
