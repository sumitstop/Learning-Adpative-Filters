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


#ifndef INCLUDED_ADAPTIVEFILTER_NLMS_H
#define INCLUDED_ADAPTIVEFILTER_NLMS_H

#include <AdaptiveFilter/api.h>
#include <gnuradio/sync_block.h>

namespace gr {
  namespace AdaptiveFilter {

    /*!
     * \brief <+description of block+>
     * \ingroup AdaptiveFilter
     *
     */
    class ADAPTIVEFILTER_API nlms : virtual public gr::sync_block
/*
#ifdef gnuradio_AdaptiveFilter_EXPORTS
#  define ADAPTIVEFILTER_API __GR_ATTR_EXPORT
#else
#  define ADAPTIVEFILTER_API __GR_ATTR_IMPORT
#endif
*/
    {
     public:
      typedef boost::shared_ptr<nlms> sptr; // boost shared pointer to nlms will be known as sptr

      /*!
       * \brief Return a shared_ptr to a new instance of AdaptiveFilter::nlms.
       *
       * To avoid accidental use of raw pointers, AdaptiveFilter::nlms's
       * constructor is in a private implementation
       * class. AdaptiveFilter::nlms::make is the public interface for
       * creating new instances.
       */
      static sptr make(float mu,int FilterLen);
    };

  } // namespace AdaptiveFilter
} // namespace gr

#endif /* INCLUDED_ADAPTIVEFILTER_NLMS_H */

