# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_AdaptiveFilter_swig', [dirname(__file__)])
        except ImportError:
            import _AdaptiveFilter_swig
            return _AdaptiveFilter_swig
        if fp is not None:
            try:
                _mod = imp.load_module('_AdaptiveFilter_swig', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _AdaptiveFilter_swig = swig_import_helper()
    del swig_import_helper
else:
    import _AdaptiveFilter_swig
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _swig_setattr_nondynamic_method(set):
    def set_attr(self,name,value):
        if (name == "thisown"): return self.this.own(value)
        if hasattr(self,name) or (name == "this"):
            set(self,name,value)
        else:
            raise AttributeError("You cannot add attributes to %s" % self)
    return set_attr



def high_res_timer_now():
  """high_res_timer_now() -> gr::high_res_timer_type"""
  return _AdaptiveFilter_swig.high_res_timer_now()

def high_res_timer_now_perfmon():
  """high_res_timer_now_perfmon() -> gr::high_res_timer_type"""
  return _AdaptiveFilter_swig.high_res_timer_now_perfmon()

def high_res_timer_tps():
  """high_res_timer_tps() -> gr::high_res_timer_type"""
  return _AdaptiveFilter_swig.high_res_timer_tps()

def high_res_timer_epoch():
  """high_res_timer_epoch() -> gr::high_res_timer_type"""
  return _AdaptiveFilter_swig.high_res_timer_epoch()
class nlms(object):
    """
    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of AdaptiveFilter::nlms.

    To avoid accidental use of raw pointers, AdaptiveFilter::nlms's constructor is in a private implementation class. AdaptiveFilter::nlms::make is the public interface for creating new instances.

    Args:
        mu : 
        FilterLen : 
    """
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined")
    __repr__ = _swig_repr
    def make(*args, **kwargs):
        """
        make(float mu, int FilterLen) -> nlms_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of AdaptiveFilter::nlms.

        To avoid accidental use of raw pointers, AdaptiveFilter::nlms's constructor is in a private implementation class. AdaptiveFilter::nlms::make is the public interface for creating new instances.

        Args:
            mu : 
            FilterLen : 
        """
        return _AdaptiveFilter_swig.nlms_make(*args, **kwargs)

    make = staticmethod(make)
    __swig_destroy__ = _AdaptiveFilter_swig.delete_nlms
    __del__ = lambda self : None;
nlms_swigregister = _AdaptiveFilter_swig.nlms_swigregister
nlms_swigregister(nlms)

def nlms_make(*args, **kwargs):
  """
    nlms_make(float mu, int FilterLen) -> nlms_sptr

    <+description of block+>

    Constructor Specific Documentation:

    Return a shared_ptr to a new instance of AdaptiveFilter::nlms.

    To avoid accidental use of raw pointers, AdaptiveFilter::nlms's constructor is in a private implementation class. AdaptiveFilter::nlms::make is the public interface for creating new instances.

    Args:
        mu : 
        FilterLen : 
    """
  return _AdaptiveFilter_swig.nlms_make(*args, **kwargs)

class nlms_sptr(object):
    """Proxy of C++ boost::shared_ptr<(gr::AdaptiveFilter::nlms)> class"""
    thisown = _swig_property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc='The membership flag')
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(boost::shared_ptr<(gr::AdaptiveFilter::nlms)> self) -> nlms_sptr
        __init__(boost::shared_ptr<(gr::AdaptiveFilter::nlms)> self, nlms p) -> nlms_sptr
        """
        this = _AdaptiveFilter_swig.new_nlms_sptr(*args)
        try: self.this.append(this)
        except: self.this = this
    def __deref__(self):
        """__deref__(nlms_sptr self) -> nlms"""
        return _AdaptiveFilter_swig.nlms_sptr___deref__(self)

    __swig_destroy__ = _AdaptiveFilter_swig.delete_nlms_sptr
    __del__ = lambda self : None;
    def make(self, *args, **kwargs):
        """
        make(nlms_sptr self, float mu, int FilterLen) -> nlms_sptr

        <+description of block+>

        Constructor Specific Documentation:

        Return a shared_ptr to a new instance of AdaptiveFilter::nlms.

        To avoid accidental use of raw pointers, AdaptiveFilter::nlms's constructor is in a private implementation class. AdaptiveFilter::nlms::make is the public interface for creating new instances.

        Args:
            mu : 
            FilterLen : 
        """
        return _AdaptiveFilter_swig.nlms_sptr_make(self, *args, **kwargs)

    def history(self):
        """history(nlms_sptr self) -> unsigned int"""
        return _AdaptiveFilter_swig.nlms_sptr_history(self)

    def declare_sample_delay(self, *args):
        """
        declare_sample_delay(nlms_sptr self, int which, int delay)
        declare_sample_delay(nlms_sptr self, unsigned int delay)
        """
        return _AdaptiveFilter_swig.nlms_sptr_declare_sample_delay(self, *args)

    def sample_delay(self, *args, **kwargs):
        """sample_delay(nlms_sptr self, int which) -> unsigned int"""
        return _AdaptiveFilter_swig.nlms_sptr_sample_delay(self, *args, **kwargs)

    def output_multiple(self):
        """output_multiple(nlms_sptr self) -> int"""
        return _AdaptiveFilter_swig.nlms_sptr_output_multiple(self)

    def relative_rate(self):
        """relative_rate(nlms_sptr self) -> double"""
        return _AdaptiveFilter_swig.nlms_sptr_relative_rate(self)

    def start(self):
        """start(nlms_sptr self) -> bool"""
        return _AdaptiveFilter_swig.nlms_sptr_start(self)

    def stop(self):
        """stop(nlms_sptr self) -> bool"""
        return _AdaptiveFilter_swig.nlms_sptr_stop(self)

    def nitems_read(self, *args, **kwargs):
        """nitems_read(nlms_sptr self, unsigned int which_input) -> uint64_t"""
        return _AdaptiveFilter_swig.nlms_sptr_nitems_read(self, *args, **kwargs)

    def nitems_written(self, *args, **kwargs):
        """nitems_written(nlms_sptr self, unsigned int which_output) -> uint64_t"""
        return _AdaptiveFilter_swig.nlms_sptr_nitems_written(self, *args, **kwargs)

    def max_noutput_items(self):
        """max_noutput_items(nlms_sptr self) -> int"""
        return _AdaptiveFilter_swig.nlms_sptr_max_noutput_items(self)

    def set_max_noutput_items(self, *args, **kwargs):
        """set_max_noutput_items(nlms_sptr self, int m)"""
        return _AdaptiveFilter_swig.nlms_sptr_set_max_noutput_items(self, *args, **kwargs)

    def unset_max_noutput_items(self):
        """unset_max_noutput_items(nlms_sptr self)"""
        return _AdaptiveFilter_swig.nlms_sptr_unset_max_noutput_items(self)

    def is_set_max_noutput_items(self):
        """is_set_max_noutput_items(nlms_sptr self) -> bool"""
        return _AdaptiveFilter_swig.nlms_sptr_is_set_max_noutput_items(self)

    def set_min_noutput_items(self, *args, **kwargs):
        """set_min_noutput_items(nlms_sptr self, int m)"""
        return _AdaptiveFilter_swig.nlms_sptr_set_min_noutput_items(self, *args, **kwargs)

    def min_noutput_items(self):
        """min_noutput_items(nlms_sptr self) -> int"""
        return _AdaptiveFilter_swig.nlms_sptr_min_noutput_items(self)

    def max_output_buffer(self, *args, **kwargs):
        """max_output_buffer(nlms_sptr self, int i) -> long"""
        return _AdaptiveFilter_swig.nlms_sptr_max_output_buffer(self, *args, **kwargs)

    def set_max_output_buffer(self, *args):
        """
        set_max_output_buffer(nlms_sptr self, long max_output_buffer)
        set_max_output_buffer(nlms_sptr self, int port, long max_output_buffer)
        """
        return _AdaptiveFilter_swig.nlms_sptr_set_max_output_buffer(self, *args)

    def min_output_buffer(self, *args, **kwargs):
        """min_output_buffer(nlms_sptr self, int i) -> long"""
        return _AdaptiveFilter_swig.nlms_sptr_min_output_buffer(self, *args, **kwargs)

    def set_min_output_buffer(self, *args):
        """
        set_min_output_buffer(nlms_sptr self, long min_output_buffer)
        set_min_output_buffer(nlms_sptr self, int port, long min_output_buffer)
        """
        return _AdaptiveFilter_swig.nlms_sptr_set_min_output_buffer(self, *args)

    def pc_noutput_items(self):
        """pc_noutput_items(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_noutput_items(self)

    def pc_noutput_items_avg(self):
        """pc_noutput_items_avg(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_noutput_items_avg(self)

    def pc_noutput_items_var(self):
        """pc_noutput_items_var(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_noutput_items_var(self)

    def pc_nproduced(self):
        """pc_nproduced(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_nproduced(self)

    def pc_nproduced_avg(self):
        """pc_nproduced_avg(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_nproduced_avg(self)

    def pc_nproduced_var(self):
        """pc_nproduced_var(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_nproduced_var(self)

    def pc_input_buffers_full(self, *args):
        """
        pc_input_buffers_full(nlms_sptr self, int which) -> float
        pc_input_buffers_full(nlms_sptr self) -> pmt_vector_float
        """
        return _AdaptiveFilter_swig.nlms_sptr_pc_input_buffers_full(self, *args)

    def pc_input_buffers_full_avg(self, *args):
        """
        pc_input_buffers_full_avg(nlms_sptr self, int which) -> float
        pc_input_buffers_full_avg(nlms_sptr self) -> pmt_vector_float
        """
        return _AdaptiveFilter_swig.nlms_sptr_pc_input_buffers_full_avg(self, *args)

    def pc_input_buffers_full_var(self, *args):
        """
        pc_input_buffers_full_var(nlms_sptr self, int which) -> float
        pc_input_buffers_full_var(nlms_sptr self) -> pmt_vector_float
        """
        return _AdaptiveFilter_swig.nlms_sptr_pc_input_buffers_full_var(self, *args)

    def pc_output_buffers_full(self, *args):
        """
        pc_output_buffers_full(nlms_sptr self, int which) -> float
        pc_output_buffers_full(nlms_sptr self) -> pmt_vector_float
        """
        return _AdaptiveFilter_swig.nlms_sptr_pc_output_buffers_full(self, *args)

    def pc_output_buffers_full_avg(self, *args):
        """
        pc_output_buffers_full_avg(nlms_sptr self, int which) -> float
        pc_output_buffers_full_avg(nlms_sptr self) -> pmt_vector_float
        """
        return _AdaptiveFilter_swig.nlms_sptr_pc_output_buffers_full_avg(self, *args)

    def pc_output_buffers_full_var(self, *args):
        """
        pc_output_buffers_full_var(nlms_sptr self, int which) -> float
        pc_output_buffers_full_var(nlms_sptr self) -> pmt_vector_float
        """
        return _AdaptiveFilter_swig.nlms_sptr_pc_output_buffers_full_var(self, *args)

    def pc_work_time(self):
        """pc_work_time(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_work_time(self)

    def pc_work_time_avg(self):
        """pc_work_time_avg(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_work_time_avg(self)

    def pc_work_time_var(self):
        """pc_work_time_var(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_work_time_var(self)

    def pc_work_time_total(self):
        """pc_work_time_total(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_work_time_total(self)

    def pc_throughput_avg(self):
        """pc_throughput_avg(nlms_sptr self) -> float"""
        return _AdaptiveFilter_swig.nlms_sptr_pc_throughput_avg(self)

    def set_processor_affinity(self, *args, **kwargs):
        """set_processor_affinity(nlms_sptr self, std::vector< int,std::allocator< int > > const & mask)"""
        return _AdaptiveFilter_swig.nlms_sptr_set_processor_affinity(self, *args, **kwargs)

    def unset_processor_affinity(self):
        """unset_processor_affinity(nlms_sptr self)"""
        return _AdaptiveFilter_swig.nlms_sptr_unset_processor_affinity(self)

    def processor_affinity(self):
        """processor_affinity(nlms_sptr self) -> std::vector< int,std::allocator< int > >"""
        return _AdaptiveFilter_swig.nlms_sptr_processor_affinity(self)

    def active_thread_priority(self):
        """active_thread_priority(nlms_sptr self) -> int"""
        return _AdaptiveFilter_swig.nlms_sptr_active_thread_priority(self)

    def thread_priority(self):
        """thread_priority(nlms_sptr self) -> int"""
        return _AdaptiveFilter_swig.nlms_sptr_thread_priority(self)

    def set_thread_priority(self, *args, **kwargs):
        """set_thread_priority(nlms_sptr self, int priority) -> int"""
        return _AdaptiveFilter_swig.nlms_sptr_set_thread_priority(self, *args, **kwargs)

    def name(self):
        """name(nlms_sptr self) -> std::string"""
        return _AdaptiveFilter_swig.nlms_sptr_name(self)

    def symbol_name(self):
        """symbol_name(nlms_sptr self) -> std::string"""
        return _AdaptiveFilter_swig.nlms_sptr_symbol_name(self)

    def input_signature(self):
        """input_signature(nlms_sptr self) -> io_signature_sptr"""
        return _AdaptiveFilter_swig.nlms_sptr_input_signature(self)

    def output_signature(self):
        """output_signature(nlms_sptr self) -> io_signature_sptr"""
        return _AdaptiveFilter_swig.nlms_sptr_output_signature(self)

    def unique_id(self):
        """unique_id(nlms_sptr self) -> long"""
        return _AdaptiveFilter_swig.nlms_sptr_unique_id(self)

    def to_basic_block(self):
        """to_basic_block(nlms_sptr self) -> basic_block_sptr"""
        return _AdaptiveFilter_swig.nlms_sptr_to_basic_block(self)

    def check_topology(self, *args, **kwargs):
        """check_topology(nlms_sptr self, int ninputs, int noutputs) -> bool"""
        return _AdaptiveFilter_swig.nlms_sptr_check_topology(self, *args, **kwargs)

    def alias(self):
        """alias(nlms_sptr self) -> std::string"""
        return _AdaptiveFilter_swig.nlms_sptr_alias(self)

    def set_block_alias(self, *args, **kwargs):
        """set_block_alias(nlms_sptr self, std::string name)"""
        return _AdaptiveFilter_swig.nlms_sptr_set_block_alias(self, *args, **kwargs)

    def _post(self, *args, **kwargs):
        """_post(nlms_sptr self, swig_int_ptr which_port, swig_int_ptr msg)"""
        return _AdaptiveFilter_swig.nlms_sptr__post(self, *args, **kwargs)

    def message_ports_in(self):
        """message_ports_in(nlms_sptr self) -> swig_int_ptr"""
        return _AdaptiveFilter_swig.nlms_sptr_message_ports_in(self)

    def message_ports_out(self):
        """message_ports_out(nlms_sptr self) -> swig_int_ptr"""
        return _AdaptiveFilter_swig.nlms_sptr_message_ports_out(self)

    def message_subscribers(self, *args, **kwargs):
        """message_subscribers(nlms_sptr self, swig_int_ptr which_port) -> swig_int_ptr"""
        return _AdaptiveFilter_swig.nlms_sptr_message_subscribers(self, *args, **kwargs)

nlms_sptr_swigregister = _AdaptiveFilter_swig.nlms_sptr_swigregister
nlms_sptr_swigregister(nlms_sptr)

nlms_sptr.__repr__ = lambda self: "<gr_block %s (%d)>" % (self.name(), self.unique_id())
nlms = nlms.make;



