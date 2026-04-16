import { create } from "zustand";
import {
  getCotizaciones,
  createCotizacion,
} from "../api/cotizaciones";

export const useCotizacionStore = create((set) => ({
  cotizaciones: [],
  loading: false,

  fetchCotizaciones: async () => {
    set({ loading: true });
    const res = await getCotizaciones();
    set({ cotizaciones: res.data, loading: false });
  },

  addCotizacion: async (data) => {
    const res = await createCotizacion(data);
    set((state) => ({
      cotizaciones: [...state.cotizaciones, res.data],
    }));
  },
}));