#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Gustavo Romero Vazquez"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Gustavo Romero Vazquez"
__email__ = "gustavorv86@gmail.com"
__status__ = "Release"


import os
import sys

import core.const as const
import core.flags_loader as flags_loader
import core.cmdparser as cmdparser


def main(cmd_line: list):

	if "__DEBUG__" in os.environ:
		for cmd in cmd_line:
			print("DEBUG: argument line: {}".format(cmd), file=sys.stderr)

	flag_methods = flags_loader.get_flags()

	if not cmd_line or cmd_line[0] == "-h" or cmd_line[0] == "--help":
		const.print_help(flag_methods)
		sys.exit(0)

	flag_options, filenames = cmdparser.argument_parser(cmd_line, flag_methods)

	for file in filenames:
		fd = open(file, "r")
		for line in fd.readlines():
			line = line.replace("\r", "").replace("\n", "")
			for option in flag_options:
				flag_cmd = option[0]
				flag_args = option[1]

				line = flag_methods[flag_cmd].on_start(line, flag_args)
				if not line:
					break

			if line:
				print(line)

	sys.exit(0)


if __name__ == '__main__':
	main(sys.argv[1:])
