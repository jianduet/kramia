import { BrowserRouter, Routes, Route } from "react-router-dom";
import { useEffect } from "react";

import Login from "./pages/Login";
import Dashboard from "./pages/Dashboard";
import Cotizaciones from "./pages/Cotizaciones";
import PrivateRoute from "./components/PrivateRoute";

import { useAuthStore } from "./store/authStore";
import { getProfile } from "./services/authService";

function App() {
  const token = useAuthStore((state) => state.token);
  const setUser = useAuthStore((state) => state.setUser);
  const logout = useAuthStore((state) => state.logout);

  useEffect(() => {
    const initAuth = async () => {
      if (token) {
        try {
          const user = await getProfile();
          setUser(user);
        } catch (error) {
          logout();
        }
      }
    };

    initAuth();
  }, [token]);

  return (
    <BrowserRouter>
      <Routes>
        {}
        <Route path="/" element={<Login />} />

        {}
        <Route
          path="/dashboard"
          element={
            <PrivateRoute>
              <Dashboard />
            </PrivateRoute>
          }
        />

        <Route
          path="/cotizaciones"
          element={
            <PrivateRoute>
              <Cotizaciones />
            </PrivateRoute>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}

export default App;