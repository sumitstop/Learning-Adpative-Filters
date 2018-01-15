/* -*- c++ -*- */
/* 
 * Copyright 2018 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "nlms_impl.h"

namespace gr {
  namespace AdaptiveFilter {

    using namespace filter::kernel;
    nlms::sptr nlms::make(float mu,int FilterLen)
    {
      return gnuradio::get_initial_sptr (new nlms_impl(mu, FilterLen));
    }

    /*
     * The private constructor
     */
    nlms_impl::nlms_impl(float mu,int FilterLen)
      : gr::sync_block("nlms",
              gr::io_signature::make(2,2, sizeof(gr_complex)),
              gr::io_signature::make(1,1, sizeof(gr_complex))),
              fir_filter_ccc(1, std::vector<gr_complex>(FilterLen, gr_complex(0,0))),
              d_new_taps(FilterLen, gr_complex(0,0)),
              d_updated(false), d_error(gr_complex(0,0))
	{
		set_gain(mu);
 		if (FilterLen > 0)
		{
			d_taps[0] = 1.0;
			std::cout << DEMANGLE_TYPEID_NAME(d_taps)<< std::endl;
			d_new_taps[0]= 1.0;
		}
		fir_filter_ccc::set_taps(d_new_taps);
		set_history(FilterLen);
	}

    /*
     * Our virtual destructor.
     */
    nlms_impl::~nlms_impl()
    {
    }

	void nlms_impl::set_taps(const std::vector<gr_complex> &taps) // becz nlms_impl is publically derieved from nlms as well as filter::kernel::fir_filter_ccc, hence nlms_impl has its own set_taps() in its namespace
	{
		d_new_taps = taps; // nlms_impl specific
		d_updated = true; // nlms_impl specific 
	}
	std::vector<gr_complex> nlms_impl::taps() const
	{
		return d_taps;
	} 

	void nlms_impl::update_tap(gr_complex &tap, const gr_complex &in) // nlms_impl specific func
	{
		tap = std::conj(tap);
		tap += d_mu*std::conj(d_error)*in/(d_norm+.0001f);
	}

	gr_complex nlms_impl::error(const gr_complex &sig)
	{
		gr_complex error = sig - d_FilterOutput;
		return error;
	}

    int nlms_impl::work(int noutput_items, 
			gr_vector_const_void_star &input_items, 
			gr_vector_void_star &output_items)
    {
      const gr_complex *ref = (const gr_complex *) input_items[0];
      const gr_complex *sig = (const gr_complex *) input_items[1];	
      gr_complex *out = (gr_complex *) output_items[0];

	if(d_updated) 
	{
		d_taps = d_new_taps;
		set_history(d_taps.size());
		d_updated = false;
		return 0; // history requirements may have changed.
	}

	size_t k, l = d_taps.size();
	size_t m = d_new_taps.size();

	for ( int i = 0; i < noutput_items; i++) 
	{
	d_norm = gr_complex(0.0f,0.0f);	
        d_FilterOutput = gr_complex(0.0f,0.0f);
        d_FilterOutput = filter(&ref[i]);
	d_error = error(sig[i]); 
	//Calculate the norm
	for( k = 0; k < l; k++) 
	{
		d_norm += ref[i - k]*std::conj(ref[i - k]);
	}
	d_error = error(ref[i]);
	out[i] = d_error;

	for(k = 0; k < l; k++) 
	{
	// Update tap locally from error.
		update_tap(d_taps[k], ref[i-k]);
	// Update aligned taps in filter object.
		fir_filter_ccc::update_tap(std::conj(d_taps[k]), k);
	}

	}

      // Tell runtime system how many output items we produced.
      return noutput_items;
    }

  } /* namespace AdaptiveFilter */
} /* namespace gr */

