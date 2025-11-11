import streamlit as st
import folium
from streamlit_folium import st_folium
from data import CUENCA_NODES, GRAPH_EDGES
from astar import AStarPathFinder

st.set_page_config(page_title="Búsqueda de Rutas Óptimas en Cuenca - Algoritmo A*", layout="wide")

# 🎯 Encabezado
st.markdown("""
<style>
h1 {
    color: #2E86C1;
}
.stButton>button {
    background-color: #2E86C1;
    color: white;
    border-radius: 8px;
}
.stMetric {
    background-color: #F2F3F4;
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

st.title("🧭 Búsqueda de Rutas Óptimas en Cuenca - Algoritmo A*")

# 🧭 Panel de configuración
with st.sidebar:
    st.header("⚙️ Configuración de Búsqueda")
    start = st.selectbox("📍 Punto de inicio", CUENCA_NODES.keys())
    goal = st.selectbox("🏁 Punto de destino", CUENCA_NODES.keys())
    show_unvisited = st.checkbox("Mostrar nodos no visitados en el mapa", value=False)
    buscar = st.button("🔍 Buscar Ruta Óptima")
    limpiar = st.button("🧹 Limpiar")

# 🧠 Ejecución del algoritmo
if buscar:
    pathfinder = AStarPathFinder(CUENCA_NODES, GRAPH_EDGES)
    path, cost, explored = pathfinder.find_path(start, goal)

    if path:
        st.success("✅ ¡Ruta encontrada!")
        st.markdown(f"**Ruta:** {' → '.join(path)}")

        # 📊 Métricas
        col1, col2 = st.columns(2)
        col1.metric("📏 Distancia total", f"{cost:.2f} km")
        col2.metric("🔎 Nodos explorados", explored)

        # 📋 Tabla de pasos
        st.subheader("📋 Detalles de la Ruta")
        total = 0.0
        table_data = []
        for i, lugar in enumerate(path):
            lat = CUENCA_NODES[lugar]["lat"]
            lon = CUENCA_NODES[lugar]["lon"]
            desc = CUENCA_NODES[lugar]["descripcion"]
            if i == 0:
                dist = 0.0
            else:
                dist = pathfinder.get_distance(path[i-1], lugar)
            total += dist
            table_data.append([i+1, lugar, desc, lat, lon, round(dist, 3), round(total, 3)])

        st.dataframe(
            table_data,
            column_config={
                0: "Paso",
                1: "Lugar",
                2: "Descripción",
                3: "Lat",
                4: "Lon",
                5: "Distancia Segmento (km)",
                6: "Distancia Acumulada (km)"
            },
            use_container_width=True
        )

        # 🗺️ Mapa
        st.subheader("🗺️ Mapa de la Ruta")
        m = folium.Map(location=[CUENCA_NODES[start]["lat"], CUENCA_NODES[start]["lon"]], zoom_start=14)

        # Marcadores y ruta
        for p in path:
            folium.Marker([CUENCA_NODES[p]["lat"], CUENCA_NODES[p]["lon"]], popup=p).add_to(m)
        for i in range(len(path) - 1):
            folium.PolyLine([
                [CUENCA_NODES[path[i]]["lat"], CUENCA_NODES[path[i]]["lon"]],
                [CUENCA_NODES[path[i+1]]["lat"], CUENCA_NODES[path[i+1]]["lon"]]
            ], color="blue", weight=5).add_to(m)

        # Nodos no visitados (opcional)
        if show_unvisited:
            visited_set = set(path)
            for node in CUENCA_NODES:
                if node not in visited_set:
                    folium.CircleMarker(
                        location=[CUENCA_NODES[node]["lat"], CUENCA_NODES[node]["lon"]],
                        radius=5,
                        color="gray",
                        fill=True,
                        fill_opacity=0.5,
                        popup=node
                    ).add_to(m)

        st_folium(m, width=900, height=500)

    else:
        st.error("❌ No se encontró una ruta.")

elif limpiar:
    st.rerun()

