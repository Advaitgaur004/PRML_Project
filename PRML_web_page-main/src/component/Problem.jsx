import React from 'react'
import intro from '../Image/intro.png'
import supp_sketch from '../Image/supp_sketch.png'
function Problem() {
  return (
    <div>
      <p className='header_Problem'>Movie Lens dataset</p>
      <img src={intro} alt=""  className='pro_imag'/>
      <p>
      The MovieLens dataset, available on Kaggle, is a widely-used and comprehensive collection of movie ratings and metadata. It encompasses a vast array of user interactions with movies, including ratings, tags, and demographic information. The dataset is particularly valuable for research and development in recommendation systems, machine learning, and data analysis related to movies and user preferences.</p>
<p className='header_Problem'>Images of the website</p>
      <img src={supp_sketch} alt=""  className='pro_imag'/>
      <p>Examples of sketches.</p>
    </div>
  )
}

export default Problem
