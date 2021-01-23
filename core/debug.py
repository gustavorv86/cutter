
import os
import sys
import core.const as const


def module(module_name: str):
	if const.ENV_DEBUG in os.environ:
		print("DEBUG: module: {}".format(module_name), file=sys.stderr)


def input(line):
	if const.ENV_DEBUG in os.environ:
		print("DEBUG: input: {}".format(line), file=sys.stderr)


def output(line):
	if const.ENV_DEBUG in os.environ:
		print("DEBUG: output: {}".format(line), file=sys.stderr)
