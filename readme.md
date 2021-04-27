# How to build rpm
make rpm should create and copy the rpms to working directory

Setting these environmental variables will change parts of the build, defaults are shown.
```bash
APP_NAME?="python3-rpm"
BRANCH?="3.9"
PREFIX?="/opt/python3"
```

Example build lines to create an rpm based off of the 3.9 branch, could easily substituted for v3.9.4 to use the tag
python3_branch also takes tag lines.
```bash
docker build --build-arg python3_prefix="/opt/python3" --build-arg python3_branch="3.9" -f Dockerfile.python3-rpm -t python3-rpm:3.9
docker create --name python3-rpm-3.9-temp python3-rpm:3.9
docker cp python3-rpm-3.9-temp:/tmp/rpm/RPMS RPMS/
docker rm -f python3-rpm-3.9-temp
```

## Lessons learned

### Trying with custom build of GCC version 10
Don't try this. 
Building a gcc version for centos 7 that allows for python3 to be built with --enable-optimizations is not worth it.
There must be a better way without having to shift to a different platform or using python3 docker images that aren't centos based.

Building everything took 1390.1s for the first 8 layers and resulted in a 9.8 GiB image.
Removing the source directories brought it down to 2Gib.
Attempt for that is in Dockerfile.python-3-9_gcc-10


### Trying built in GCC in CentOS7
Reasonable.
Build took about 173.2s and required different flags. Resulted in a 812.59MiB image that honestly can be shrunk down if desired.
The actual built folder for python3 takes up 231MiB.

Thinking of removing builddep because it relies on the source RPMS which might add to the weight of the image.