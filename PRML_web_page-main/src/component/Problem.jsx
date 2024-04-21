import React from 'react'
import intro from '../Image/intro.png'
import supp_sketch from '../Image/supp_sketch.png'
import website from '../Image/website.png'
import movielen from '../Image/movielen.png'
function Problem() {
  return (
    <div>
      <p className='header_Problem'>Movie Lens dataset</p>
      <img src={movielen} alt=""  className='pro_imag'/>
      <p>
      The MovieLens dataset, available on Kaggle, is a widely-used and comprehensive collection of movie ratings and metadata. It encompasses a vast array of user interactions with movies, including ratings, tags, and demographic information. The dataset is particularly valuable for research and development in recommendation systems, machine learning, and data analysis related to movies and user preferences.</p>
<p className='header_Problem'>Images of the website</p>
      <img src={website} alt=""  className='pro_imag'/>
      <p>Examples of movie recommendation.</p>
    </div>
  )
}

export default Problem
