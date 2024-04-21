import React from 'react'

function Youtube() {
  return (
    <div>
      <p className='header_Problem'>Spolight Video</p>

      <iframe  className='youtube_video'  src="https://www.youtube.in/embed/lCZSry91v_Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    </div>
  )
}

export default Youtube
