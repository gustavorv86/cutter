
import pkgutil
import os
import sys

import core.module_flags


def get_flags():

	flag_methods = dict()

	for _, modname, _ in pkgutil.iter_modules(core.module_flags.__path__):
		module_path = "core.module_flags." + modname

		if "__DEBUG__" in os.environ:
			print("DEBUG: import {}".format(module_path), file=sys.stderr)

		module = __import__(module_path, fromlist="dummy")

		function_name = module.NAME

		flag_methods[function_name] = module

	return flag_methods
