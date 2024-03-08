# Define a variable for the image name and tag
IMAGE_NAME = py-map-api
IMAGE_TAG = latest
VENV := venv
PYTHON := python3.12

SRC_FILES := $(shell find src/ -type f)
DOCKER_IMAGE_MARKER := .docker_image_built

setup:
	$(PYTHON) -m venv $(VENV)
	$(VENV)/bin/pip install -r requirements.txt

activate:
	@echo "To activate the virtual environment, execute 'source $(VENV)/bin/activate'"

# Define the usage output
.PHONY: help
help:
	@echo "Usage: make [target]"
	@echo " "
	@echo "Targets:"
	@echo "setup        Setup the virtual environment"
	@echo "activate     Activate the virtual environment"
	@echo "docker-build Build the Docker image"
	@echo "docker-run   Run the Docker image"
	@echo "run          Run the application in the virtual environment"
	@echo "clean        Remove the Docker image"

# Define the default target
.PHONY: all
all: help

$(DOCKER_IMAGE_MARKER): $(SRC_FILES) docker/Dockerfile
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) -f docker/Dockerfile .
	@touch $(DOCKER_IMAGE_MARKER)

# Define the build target
.PHONY: docker-build
docker-build: $(DOCKER_IMAGE_MARKER)

.PHONY: docker-run
docker-run: docker-build
	docker run -p 8000:8000/tcp -it $(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: run
run:
	uvicorn --app-dir src app.api:app --host 0.0.0.0 --port 8000 --reload

# Define the clean target
.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME):$(IMAGE_TAG)
