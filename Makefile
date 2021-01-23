SHELL=/bin/bash

PY3BUILD=./tools/py3build

.PHONY: build

build:
	@if [ ! -f ${PY3BUILD} ]; then \
		echo "ERROR: ${PY3BUILD} not found."; \
		exit 1; \
	fi
	@mkdir -p ./build
	@ln -sf main.py __main__.py
	${PY3BUILD} -i . -o ./build/cutter
	@unlink __main__.py
	@echo "Done"
	@exit 0

install:
	@if [ ! -x ./build/cutter ]; then \
		echo "ERROR: run make build first."; \
		exit 1; \
	fi
	@if [ -d /usr/local/bin ]; then \
		cp -avf ./build/cutter /usr/local/bin; \
	elif [ -d /usr/bin ]; then \
		cp -avf ./build/cutter /usr/bin; \
	elif [ -d /bin ]; then \
		cp -avf ./build/cutter /bin; \
	else \
		echo "ERROR: cannot install binary file."; \
		exit 1; \
	fi
	@echo "Done"
	@exit 0

uninstall:
	@if [ -f /usr/local/bin/cutter ]; then \
		rm -vf /usr/local/bin/cutter; \
	elif [ -f /usr/bin/cutter ]; then \
		rm -vf /usr/bin/cutter; \
	elif [ -f /bin/cutter ]; then \
		rm -vf /bin/cutter; \
	else \
		echo "ERROR: cannot install binary file."; \
		exit 1; \
	fi
	@echo "Done"
	@exit 0


