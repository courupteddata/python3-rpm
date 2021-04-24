# Lessons learned

## Trying with custom build of GCC version 10
Don't try this. 
Building a gcc version for centos 7 that allows for python3 to be built with --enable-optimizations is not worth it.
There must be a better way without having to shift to a different platform or using python3 docker images that aren't centos based.

Building everything took 1390.1s for the first 8 layers and resulted in a 9.8 GiB image.
Removing the source directories brought it down to 2Gib.
Attempt for that is in Dockerfile.python-3-9_gcc-10


## Trying built in GCC in CentOS7
Reasonable.
Build took about 173.2s and required different flags. Resulted in a 812.59MiB image that honestly can be shrunk down if desired.
The actual built folder for python3 takes up 231MiB.

Thinking of removing builddep because it relies on the source RPMS which might add to the weight of the image.