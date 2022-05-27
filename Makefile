

install:
	bash scripts/install-sipp.sh

run:
	export PATH=$$PATH:$$PWD/sipp && \
	python3 main.py