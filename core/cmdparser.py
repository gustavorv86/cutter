
import os
import sys


def argument_parser(command_line: list, flag_methods: dict):

	flag_options = list()
	filenames = list()

	while command_line and command_line[0].startswith("--"):
		command_option = command_line.pop(0)

		array = command_option[2:].split("=")
		flag_cmd = array[0]
		if len(array) > 1:
			flag_args = array[1]
		else:
			flag_args = None

		if flag_cmd not in flag_methods:
			print("ERROR: flag {} not recognized.".format(flag_cmd), file=sys.stderr)
			sys.exit(1)

		flag_options.append((flag_cmd, flag_args))

	while command_line:
		filename = command_line.pop(0)
		if not os.path.isfile(filename):
			print("ERROR: file {} not found.".format(filename), file=sys.stderr)
			sys.exit(1)

		filenames.append(filename)

	return flag_options, filenames


def split_flag_arguments(flag_arguments: str):
	char_separator = flag_arguments[0]

	if char_separator != flag_arguments[-1]:
		print('ERROR: invalid format "{}"'.format(flag_arguments), file=sys.stderr)
		sys.exit(1)

	return flag_arguments[1:-1].split(char_separator)
