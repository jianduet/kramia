import axios from "axios";

const API = axios.create({
  baseURL: "http://localhost:8000",
});

// 🔐 Interceptor para token
API.interceptors.request.use((config) => {
  const token = localStorage.getItem("token");

  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }

  return config;
});

// 📦 CRUD

export const getCotizaciones = () => API.get("/cotizaciones");

export const createCotizacion = (data) =>
  API.post("/cotizaciones", data);

export const getCotizacion = (id) =>
  API.get(`/cotizaciones/${id}`);

export const updateCotizacion = (id, data) =>
  API.put(`/cotizaciones/${id}`, data);

export const deleteCotizacion = (id) =>
  API.delete(`/cotizaciones/${id}`);