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

#ifndef INCLUDED_ADAPTIVEFILTER_NLMS_IMPL_H
#define INCLUDED_ADAPTIVEFILTER_NLMS_IMPL_H

#include <AdaptiveFilter/nlms.h>
#include <gnuradio/filter/fir_filter.h>
#include <gnuradio/math.h>
#include <vector>
#include <stdexcept>
#include <gnuradio/gr_complex.h>
#define DEMANGLE_TYPEID_NAME(x) abi::__cxa_demangle(typeid((x)).name(), NULL, NULL, NULL)

namespace gr {
  namespace AdaptiveFilter {

    class nlms_impl : public nlms, filter::kernel::fir_filter_ccc
    {
     private:
        float d_FilterLen;
	float d_mu;
	gr_complex d_error;
	gr_complex d_FilterOutput;
	gr_complex d_norm;
	std::vector<gr_complex> d_new_taps;
	bool d_updated;

     protected:
     gr_complex error(const gr_complex &in);
     void update_tap(gr_complex &tap, const gr_complex &in);

     public:
      nlms_impl(float mu,int FilterLen);
      ~nlms_impl();

      void set_taps(const std::vector<gr_complex> &taps); // setter 
      std::vector<gr_complex> taps() const; // getter

      	float gain() const
      	{
        	return d_mu;
      	}

       	void set_gain(float mu)
      	{
	if(mu < 0.0f || mu > 1.0f) 
	{
		throw std::out_of_range("NLMS::set_gain: Gain value must be in [0,1]");
       	}
		d_mu = mu;
 	}

      // Where all the action really happens
      int work(int noutput_items,
         gr_vector_const_void_star &input_items,
         gr_vector_void_star &output_items);
    };

  } // namespace AdaptiveFilter
} // namespace gr

#endif /* INCLUDED_ADAPTIVEFILTER_NLMS_IMPL_H */

