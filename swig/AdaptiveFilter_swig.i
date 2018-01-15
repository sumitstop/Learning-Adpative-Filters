/* -*- c++ -*- */

#define ADAPTIVEFILTER_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "AdaptiveFilter_swig_doc.i"

%{
#include "AdaptiveFilter/nlms.h"
%}


%include "AdaptiveFilter/nlms.h"
GR_SWIG_BLOCK_MAGIC2(AdaptiveFilter, nlms);
