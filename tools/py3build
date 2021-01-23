#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "Gustavo Romero Vazquez"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Gustavo Romero Vazquez"
__email__ = "gustavorv86@gmail.com"
__status__ = "Release"

import argparse
import glob
import os
import py_compile
import shutil
import sys
import uuid
import zipfile

PROGNAME = os.path.basename(sys.argv[0]).replace(".py", "")

DEFAULT_SHEBANG = "#!/usr/bin/env python3\n"


def make_zip(source_directory, zip_filename):
	fd_zip = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)

	for root, dirs, files in os.walk(source_directory):
		for file in files:
			source_path = os.path.join(root, file)
			destination_path = source_path.replace(source_directory, "")
			fd_zip.write(source_path, destination_path)

	fd_zip.close()


def make_binary(zip_filename, bin_filename):
	fdw = open(bin_filename, "wb")
	fdr = open(zip_filename, "rb")

	fdw.write(DEFAULT_SHEBANG.encode("utf-8"))
	while True:
		buffer_bytes = fdr.read(4096)
		if len(buffer_bytes) <= 0:
			break
		fdw.write(buffer_bytes)

	fdr.close()
	fdw.close()

	os.chmod(bin_filename, 0o750)


def build_from_file(main_filename: str, build_directory: str, bin_filename: str):
	os.makedirs(build_directory, exist_ok=True)

	pyc_filename = os.path.join(build_directory, os.path.basename(main_filename) + "c")
	py_compile.compile(main_filename, pyc_filename)

	zip_filename = build_directory + "_pack.zip"
	fd_zip = zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED)
	fd_zip.write(pyc_filename, "__main__.pyc")
	fd_zip.close()

	make_binary(zip_filename, bin_filename)

	os.remove(zip_filename)
	shutil.rmtree(build_directory, ignore_errors=True)


def build_from_python_project(project_directory: str, build_directory: str, bin_filename: str):
	os.makedirs(build_directory, exist_ok=True)

	main_filename = os.path.join(project_directory, "__main__.py")

	if not os.path.isfile(main_filename):
		print("ERROR: __main__.py file not found. Abort.".format(project_directory), file=sys.stderr)
		sys.exit(1)

	py_filenames = [f for f in glob.glob(project_directory + "/**/*.py", recursive=True)]

	for py_filename in py_filenames:
		pyc_filename = py_filename.replace(project_directory, build_directory) + "c"
		py_compile.compile(py_filename, pyc_filename)

	zip_filename = build_directory + "_pack.zip"
	make_zip(build_directory, zip_filename)

	make_binary(zip_filename, bin_filename)

	os.remove(zip_filename)
	shutil.rmtree(build_directory, ignore_errors=True)


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description="Byte compile and binary application package Python 3 source files")
	parser.add_argument("-i", "--input", type=str, required=True, help="Input source file or pythonic project directory")
	parser.add_argument("-o", "--output", type=str, required=True, help="Output binary application package file")
	args = parser.parse_args()

	arg_input = args.input
	arg_output = args.output

	build_directory = "/tmp/pybuild_" + uuid.uuid4().hex
	zip_package = build_directory + ".zip"

	if os.path.isfile(arg_input):
		main_filename = os.path.abspath(arg_input)
		build_from_file(main_filename, build_directory, arg_output)

	elif os.path.isdir(arg_input):
		project_directory = os.path.abspath(arg_input)
		build_from_python_project(project_directory, build_directory, arg_output)

	else:
		print("ERROR: invalid input {}. Abort.".format(arg_input), file=sys.stderr)
		sys.exit(1)
