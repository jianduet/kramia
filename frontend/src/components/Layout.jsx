import { Link } from "react-router-dom";

export default function Layout({ children }) {
  return (
    <div className="flex h-screen bg-gray-100">

      {/* Sidebar */}
      <aside className="w-64 bg-gray-900 text-white p-5">
        <h2 className="text-2xl font-bold mb-6">Kramia</h2>

        <nav className="space-y-2">
          <Link
            to="/dashboard"
            className="block px-3 py-2 rounded hover:bg-gray-700"
          >
            Dashboard
          </Link>

          <Link
            to="/cotizaciones"
            className="block px-3 py-2 rounded hover:bg-gray-700"
          >
            Cotizaciones
          </Link>
        </nav>
      </aside>

      {/* Contenido */}
      <main className="flex-1 p-6 overflow-auto">
        {children}
      </main>

    </div>
  );
}