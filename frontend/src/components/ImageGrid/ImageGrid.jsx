import fallbackImg from "@assets/images/image-fallback.jpg";
import "./ImageGrid.css";

export default function ImageGrid({ images, onSelect, selectedImage }) {
  return (
    <div className="image-grid">
      {images.map((img) => {
        const isActive = selectedImage?.id === img.id;

        return (
          <div
            key={img.id}
            onClick={() => onSelect(img)}
            className={`image-item ${isActive ? "active" : ""}`}
          >
            <img
              src={img.image_url}
              alt={img.title}
              loading="lazy"
              width={400}
              height={300}
              className="image-thumb"
              onError={(e) => {
                e.target.src = fallbackImg;
              }}
            />
          </div>
        );
      })}
    </div>
  );
}