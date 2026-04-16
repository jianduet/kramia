import { useEffect } from "react";
import { getProfile, logout } from "../services/authService";
import { useNavigate } from "react-router-dom";
import { useAuthStore } from "../store/authStore";

function Dashboard() {
  const navigate = useNavigate();

  const user = useAuthStore((state) => state.user);
  const empresaId = useAuthStore((state) => state.empresaId);
  const setUser = useAuthStore((state) => state.setUser);
  const logoutStore = useAuthStore((state) => state.logout);

  useEffect(() => {
    const fetchUser = async () => {
      try {
        if (!user) {
          const data = await getProfile();
          setUser(data);
        }
      } catch (error) {
        logout();
        logoutStore();
        navigate("/");
      }
    };

    fetchUser();
  }, [user]);

  useEffect(() => {
    if (user) {
      console.log("Usuario:", user);
      console.log("Empresa ID:", empresaId);
    }
  }, [user, empresaId]);

  const handleLogout = () => {
    logout();
    logoutStore();
    navigate("/");
  };

  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-4">Dashboard</h1>

      {user && (
        <div className="mb-4">
          <p><strong>Nombre:</strong> {user.nombre}</p>
          <p><strong>Email:</strong> {user.email}</p>
          <p><strong>Empresa ID:</strong> {empresaId}</p> {}
        </div>
      )}

      <button
        onClick={handleLogout}
        className="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600 transition-colors"
      >
        Cerrar sesión
      </button>
    </div>
  );
}

export default Dashboard;