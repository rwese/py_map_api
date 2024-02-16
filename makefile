# Define a variable for the image name and tag
IMAGE_NAME = py_map_api
IMAGE_TAG = latest

# Define the default target
.PHONY: all
all: build

# Define the build target
.PHONY: docker-build
build:
	docker build -t $(IMAGE_NAME):$(IMAGE_TAG) -f docker/Dockerfile .

.PHONY: docker-run
run:
	docker run -p 8000:8000/tcp -it $(IMAGE_NAME):$(IMAGE_TAG)

.PHONY: run
run:
	uvicorn --app-dir src main:app --host 0.0.0.0 --port 8000 --reload

# Define the clean target
.PHONY: clean
clean:
	docker rmi $(IMAGE_NAME):$(IMAGE_TAG)