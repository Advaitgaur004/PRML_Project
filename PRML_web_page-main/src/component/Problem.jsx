import React from 'react'
import intro from '../Image/intro.png'
import supp_sketch from '../Image/supp_sketch.png'
function Problem() {
  return (
    <div>
      <p className='header_Problem'>The CSTBIR Problem</p>
      <img src={intro} alt=""  className='pro_imag'/>
      <p>
Composite Sketch+Text Based Image Retrieval: A user wants to search “Numbat digging in the ground” but does not know the word “numbat”, and the interaction “digging in the ground” is not easy to sketch. Thus, the user may use a hand-drawn sketch of "numbat" along with the text "digging in the ground" to retrieve the desired images.</p>
<p className='header_Problem'>Sketches in CSTBIR</p>
      <img src={supp_sketch} alt=""  className='pro_imag'/>
      <p>Examples of sketches.</p>
    </div>
  )
}

export default Problem
