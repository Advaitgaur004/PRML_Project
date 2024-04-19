import React, { useEffect, useState } from 'react';
import './ImageSlider.css'; 
import test from '../Image/test.png'
import intro from '../Image/intro.png'
import supp_sketch from '../Image/supp_sketch.png'

function ImageScroll() {
    const [currentIndex, setCurrentIndex] = useState(0);
   const images=[supp_sketch,test,intro,supp_sketch]
  const scrollLeft = () => {
    setCurrentIndex((prevIndex) => Math.max(prevIndex - 1, 0));
  };
  const interval = 2000;
  useEffect(() => {
    const intervalId = setInterval(() => {
        if (currentIndex === images.length - 1) {
            setCurrentIndex(0);
        }
      scrollRight();
    }, interval);

    return () => clearInterval(intervalId);
  }, [currentIndex, interval]);

  const scrollRight = () => {
    setCurrentIndex((prevIndex) => Math.min(prevIndex + 1, images.length - 1));
  };
  return (
    <div className="image-slider">
        <div className="controls">
      <button onClick={scrollLeft} disabled={currentIndex === 0}>
        &lt;
      </button>
    </div>

    <div className="image-container">
      {images.map((image, index) => (
        <img
          key={index}
          src={image}
          alt={`Image ${index}`}
          className={index === currentIndex ? 'add visible' : 'add notvisible'}
        />
      ))}
    </div>
    <div className="controls">
      <button onClick={scrollRight} disabled={currentIndex === images.length - 1}>
        &gt;
      </button>
    </div>
  </div>
  )
}

export default ImageScroll
