#!/bin/bash

setenv LD_LIBRARY_PATH /tmp/CONDA/lib:/usr/lib64/openmpi/lib:/usr/lib64/mpich/lib:${LD_LIBRARY_PATH}
setenv PATH /usr/lib64/mpich/bin:/tmp/pyMPI/bin:${PATH}
setenv PYTHONPATH /tmp/CONDA/lib/python2.7/lib-tk/:/tmp/MATPLOTLIB/:/tmp/NUMPY_CHIEFS/lib64/python2.7/site-packages/:/tmp/PANDAS_DATAREADER/:/tmp/TENSORFLOW/:/tmp/PROTOBUF
