
ROOTDIR=`readlink -f -- .`

PY3BUILD=${ROOTDIR}/tools/py3build

all: build

build:
	if [ ! -f ${PY3BUILD}; then \
		echo "ERROR: ${PY3BUILD} not found."; \
		exit 1; \
	fi
	mkdir -p ${ROOTDIR}/build
	${PY3BUILD} -i ${ROOTDIR} -o ${ROOTDIR}/build/cutter
	echo "Done"
	exit 0

install:
	if [ ! -x ${ROOTDIR}/build/cutter ]; then \
		echo "ERROR: run make build first."; \
		exit 1; \
	fi
	if [ -d /usr/local/bin ]; then \
		cp -avf ${ROOTDIR}/build/cutter /usr/local/bin \
	elif [ -d /usr/bin ]; then \
		cp -avf ${ROOTDIR}/build/cutter /usr/bin \
	elif [ -d /bin ]; then
		cp -avf ${ROOTDIR}/build/cutter /bin \
	else 
		echo "ERROR: cannot install binary file."; \
		exit 1; \
	fi \
	echo "Done"
	exit 0

uninstall:
	if [ -f /usr/local/bin/cutter ]; then \
		rm -vf /usr/local/bin/cutter \
	elif [ -f /usr/bin/cutter ]; then \
		rm -vf /usr/bin/cutter \
	elif [ -f /bin/cutter ]; then
		rm -vf /bin/cutter \
	else \
		echo "ERROR: cannot install binary file."; \
		exit 1; \
	fi
	echo "Done"
	exit 0
