build:
	docker build .

run:
	docker run --gpus all -it -v $(PWD):/src tensorflow/tensorflow:latest-gpu bash

install:
	pip install -r requirements.txt