import axios from "axios";

const API_BASE = import.meta.env.VITE_API_BASE_URL;

export const fetchImages = async () => {
  const res = await axios.get(`${API_BASE}/api/images`);
  console.log(res)
  return res.data.filter(img => img.image_url);
};

export const fetchImageById = async (id) => {
  const res = await axios.get(`${API_BASE}/api/images/${id}`);
  return res.data;
}