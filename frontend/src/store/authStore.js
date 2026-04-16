import { create } from "zustand";

export const useAuthStore = create((set) => ({
  user: null,
  empresaId: null,
  token: localStorage.getItem("token") || null,

  setUser: (user) =>
    set({
      user,
      empresaId: user?.empresa_id, // 👈 CLAVE
    }),

  setToken: (token) => {
    localStorage.setItem("token", token);
    set({ token });
  },

  logout: () => {
    localStorage.removeItem("token");
    set({ user: null, token: null, empresaId: null });
  },
}));