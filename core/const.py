
PROGNAME = "cutter"

ENV_DEBUG = "CUTTER_DEBUG"

HELP_HEADER = """
Usage: """ + PROGNAME + """ [OPTION]... [FILE]...
Print lines search and manipulate text in each FILE or standard input.
Example: """ + PROGNAME + """ --filter="Yes" --nfilter="No" --search-and-replace="foo","bar" --format="{0}, {1}, {2}" inputfile.txt

Options:
"""


def print_help(flag_modules: dict):
	print(HELP_HEADER)

	for key in sorted(flag_modules):
		print("  " + flag_modules[key].HELP)

	print("")
