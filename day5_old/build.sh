#!/bin/sh

g++ -fPIC --shared -std=c++11 -Wall temperature.cpp export.cpp \
    -I${CONDA_PREFIX}/include \
    -I${CONDA_PREFIX}/include/python3.7m \
    -I${CONDA_PREFIX}/include/eigen3 \
    -L${CONDA_PREFIX}/lib -lpython3.7m \
    -o sss_cpp.so

#PIC allows other paograms to view objects
#shared allows location independent calls to these files
# G++ -std=c++11 -Wall - I${CONDA_PREFIX}/include/eigen *.cpp -o hello_world
