
import sys
import core.debug as debug


NAME = "split"
HELP = """in:STRING --split="TEXT" out:LIST
		Split the input STRING by TEXT and return a word LIST.
		If split not contains arguments, the separator is one or more whitespaces.
"""


def _flag_function(line: str, string_split: str) -> list:
	if not string_split:
		return line.split()
	else:
		return line.split(string_split)


def on_start(line: str, argument: str) -> list:
	debug.module(NAME)
	debug.input(line)

	if not isinstance(line, str):
		print("ERROR: {} STRING input expected.".format(NAME), file=sys.stderr)
		sys.exit(1)

	output = _flag_function(line, argument)

	debug.output(output)
	return output
