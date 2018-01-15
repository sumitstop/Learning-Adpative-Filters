#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/john/nuradio/src/gr-AdaptiveFilter/lib
export PATH=/home/john/nuradio/src/gr-AdaptiveFilter/build/lib:$PATH
export LD_LIBRARY_PATH=/home/john/nuradio/src/gr-AdaptiveFilter/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-AdaptiveFilter 
