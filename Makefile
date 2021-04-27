# Allows changing them via an environmental variable
APP_NAME?="python3-rpm"
BRANCH?="3.9"
PREFIX?="/opt/python3"

BUILD_TAG="$(APP_NAME):$(BRANCH)"

BUILD_INSTANCE="$(APP_NAME)-$(BRANCH)-temp"

.PHONY clean

all:
	release

release:
	rpm

rpm: build-image create-instance copy-rpm remove-instance
	
build-image:
	## To do a tag just set the branch to v3.9.4
	## Build the image with the tags
	## docker build --build-arg python3_prefix="/opt/python3" --build-arg python3_branch="3.9" -f Dockerfile.python3-rpm -t python3-rpm:3.9 .
	docker build --build-arg python3_prefix=$(PREFIX) --build-arg python3_branch=$(BRANCH) -f Dockerfile.python3-rpm -t $(BUILD_TAG) .

create-instance:
	## Create an instance to read from
	## docker create --name python3-rpm-3.9-temp python3-rpm:3.9
	docker create --name $(BUILD_INSTANCE) $(BUILD_TAG)

copy-rpm:
	## Copy the RPMS folder
	## docker cp python3-rpm-3.9-temp:/tmp/rpm/RPMS RPMS/
	docker cp $(BUILD_INSTANCE):/tmp/rpm/RPMS RPMS/

remove-instance:
	## Delete the copy instance
	## docker rm -f python3-rpm-3.9-temp
	docker rm -f $(BUILD_INSTANCE)

clean:
	rm -rf RPMS/