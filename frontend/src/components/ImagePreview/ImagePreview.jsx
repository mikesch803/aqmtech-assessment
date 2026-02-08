import { Drawer } from "antd";
import { CloseOutlined } from "@ant-design/icons";
import "./ImagePreview.css";
export default function ImagePreview({ image, onClose }) {
  return (
    <Drawer
      open={!!image}
      onClose={onClose}
      size="70%"
      closable={false}
      bodyStyle={{
        backgroundColor: "#181818",
        padding: "16px",
        color: "white",
        overflow: "hidden", // 🔴 important: no scroll
      }}
    >
      {image && (
        <>
          {/* Header */}
          <div className="preview-header">
            <div className="preview-title">{image.title}</div>
            <CloseOutlined onClick={onClose} className="preview-close" />
          </div>

          {/* Image */}
          <div className="preview-image-wrapper">
            <img
              src={image.image_url}
              alt={image.title}
              className="preview-image"
            />
          </div>

          {/* Meta */}
          <div className="preview-meta">
            <div className="preview-meta-title">{image.title}</div>
            {image.description && (
              <div className="preview-meta-description">
                {image.description}
              </div>
            )}
          </div>
        </>
      )}
    </Drawer>
  );
}
