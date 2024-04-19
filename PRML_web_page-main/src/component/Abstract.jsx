import React from 'react'

function Abstract() {
  return (
    <div>
      <p className='header_context'>Abstract</p>
      <p className='context'>
      Non-native speakers with limited vocabulary often struggle to name specific objects despite being able to visualize them clearly, e.g., people outside Australia searching for ‘numbats.’ Further, users may want to search for such elusive objects with difficult-to-sketch interactions, e.g., “numbat digging in the ground.” In such common but complex situations, users desire a search interface that accepts composite multimodal queries comprising hand-drawn sketches of “difficult-to-name but easy-to-draw” objects along with text describing “difficult-to-sketch but easy-to-verbalize” object’s attributes or interaction with the scene. This novel problem statement is distinctly different from the previously well-researched TBIR (text-based image retrieval) and SBIR (sketch-based image retrieval) problems. To study this under-explored task, we curate a dataset, CSTBIR (Composite Sketch+Text Based Image Retrieval), consisting of ∼2M queries and 108K natural scene images. Further, as a solution to this problem, we propose a pretrained multimodal transformer-based baseline, STNET (Sketch+Text Network), that uses a hand-drawn sketch to localize relevant objects in the natural scene image, and encodes the text and image to perform image retrieval. In addition to contrastive learning, we propose multiple train- ing objectives that improve the performance of our model. Extensive experiments show that our proposed method outperforms several state-of-the-art retrieval methods for text-only, sketch-only, as well as composite query modalities
      </p>
    </div>
  )
}

export default Abstract
