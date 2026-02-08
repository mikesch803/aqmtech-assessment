import { useEffect, useState } from "react";
import { fetchImages } from "@api/imageApi";
import ImageGrid from "@components/ImageGrid/ImageGrid";
import ImagePreview from "@components/ImagePreview/ImagePreview";

export default function Gallery() {
  const [images, setImages] = useState([]);
  const [selectedImage, setSelectedImage] = useState(null);

  useEffect(() => {
    fetchImages().then(setImages);
  }, []);

  return (
   <div className={`gallery-container ${selectedImage ? "preview-open" : ""}`}>
  <div className="gallery-grid">

        <ImageGrid
          images={images}
          onSelect={setSelectedImage}
          selectedImage={selectedImage}
        />
      </div>

      <ImagePreview  className={`image-preview-panel ${selectedImage ? "open" : ""}`}
        image={selectedImage}
        onClose={() => setSelectedImage(null)}
      />
    </div>
  );
}
