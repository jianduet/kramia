import { useEffect } from "react";
import { useCotizacionStore } from "../store/cotizacionStore";
import Layout from "../components/Layout";

export default function Cotizaciones() {
  const { cotizaciones, fetchCotizaciones, addCotizacion } =
    useCotizacionStore();

  useEffect(() => {
    fetchCotizaciones();
  }, []);

  return (
    <Layout>
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-semibold">Cotizaciones</h1>

        <button
          onClick={() =>
            addCotizacion({
              nombre: "Nueva",
              descripcion: "Auto",
              cliente: "Demo",
            })
          }
          className="bg-black text-white px-4 py-2 rounded hover:bg-gray-800"
        >
          + Nueva
        </button>
      </div>

      <div className="bg-white rounded shadow">
        <table className="w-full text-left">
          <thead className="border-b">
            <tr>
              <th className="p-3">Nombre</th>
              <th className="p-3">Cliente</th>
              <th className="p-3">Estado</th>
            </tr>
          </thead>

          <tbody>
            {cotizaciones.map((c) => (
              <tr key={c.id} className="border-b hover:bg-gray-50">
                <td className="p-3">{c.nombre}</td>
                <td className="p-3">{c.cliente}</td>
                <td className="p-3">{c.estado}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Layout>
  );
}