# Lessons learned
Don't try this. 
Building a gcc version for centos 7 that allows for python3 to be built with --enable-optimizations is not worth it.
There must be a better way without having to shift to a different platform or using python3 docker images that aren't centos based.

Building everything took 1390.1s for the first 8 layers and resulted in a 9.8 GiB image.