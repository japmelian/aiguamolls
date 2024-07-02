import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import folium_static, st_folium


st.set_page_config(layout = "wide",  initial_sidebar_state="collapsed", page_title="Parc Natural dels Aiguamolls de l'Empordà - Itinerario 3")

with st.container():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image('static/images/logo.webp', use_column_width = 'always')
    
    with col2:
        st.markdown("""
            <div style="background-color: #219c90; border-radius: 20px; padding: 20px; color: white; cursor: pointer;">
                <p style="font-weight: bold; font-size: 40px;">Itinerario 3</p>
                <p style="font-size: 20px;">Ruta alrededor de la Reserva Integral de las «Llaunes»</p>
            </div>
        """, unsafe_allow_html=True)

st.divider()
st.write("")
st.write("")

with st.container():
    itinerario = gpd.read_file('static/geo/itinerario3.geojson')
    puntos_interes = gpd.read_file('static/geo/puntos_interes.geojson')


    mapa_itinerario = folium.Map(location=[itinerario.centroid.y.mean(), itinerario.centroid.x.mean()], zoom_start=13)

    # Define una función para agregar puntos con diferentes iconos según la columna 'tipo'
    def agregar_punto(row):
        icono = None

        if row['tipo'] == 'Observatorio':
            icono = folium.features.CustomIcon('static/images/icon_photo.png', icon_size=(32, 32))
        elif row['tipo'] == 'Información':
            icono = folium.features.CustomIcon('static/images/icon_info.png', icon_size=(32, 32))
        elif row['tipo'] == 'Baños':
            icono = folium.features.CustomIcon('static/images/icon_toilet.png', icon_size=(32, 32))
        elif row['tipo'] == 'Picnic':
            icono = folium.features.CustomIcon('static/images/icon_picnic.png', icon_size=(32, 32))
        elif row['tipo'] == 'Aparcamientos':
            icono = folium.features.CustomIcon('static/images/icon_parking.png', icon_size=(32, 32))
            
        # Agregar el marcador al mapa con el icono correspondiente
        folium.Marker(location=[row.geometry.y, row.geometry.x], icon=icono).add_to(mapa_itinerario)

    # Aplicar la función a cada fila del GeoDataFrame
    puntos_interes.apply(agregar_punto, axis=1)

    folium.GeoJson(itinerario).add_to(mapa_itinerario)

    st_folium(mapa_itinerario, width=1800)

    descripciones = {
        'static/images/icon_photo.png': 'Observatorios',
        'static/images/icon_info.png': 'Puntos de información',
        'static/images/icon_toilet.png': 'Aseos',
        'static/images/icon_picnic.png': 'Áreas de picnic',
        'static/images/icon_parking.png': 'Aparcamientos'
    }

    # Dividir la pantalla en varias columnas
    columnas = st.columns(len(descripciones))

    # Mostrar las imágenes y descripciones en una misma línea
    i = 0
    for _image, _desc in descripciones.items():
        # En cada columna, mostrar la imagen y la descripción
        with columnas[i]:
            st.image(_image, width=30)
            st.write(_desc)

            i += 1

st.divider()

with st.container():
    col1, col2 = st.columns([2, 3])

    with col1:
        detalles_recorrido = """
            <div style="background-color: #2a2a2a; border-radius: 20px; padding: 20px; color: white;">
                <h2 style="color: white;">Detalles</h2>
                <ul>
                    <li>Longitud: 9 kilómetros </li>
                    <li>Dificultad: Fácil</li>
                    <li>Duración: Entre 2 y 3 horas, dependiendo del ritmo y las paradas</li>
                    <li>Inicio y Fin del Recorrido: El itinerario comienza en el Centro de Recepción del parque y sigue un sendero bien señalizado que rodea la Reserva Integral de las Llaunes.</li>
                </ul>
            </div>
        """

        # Mostrar los detalles del recorrido
        st.write(detalles_recorrido, unsafe_allow_html=True)
    
    with col2:
        explicacion_recorrido = """
            <p style="font-size: 16px;">
                Este itinerario es la continuación de los itinerarios 1 y 2. Transcurre a lo largo de la franja litoral de la Reserva Integral, donde puede observarse prácticamente intacta la vegetación típica de los suelos arenosos y salinos.
                A lo largo de su recorrido encontraremos unas torres de observación que nos permitirán contemplar la diversidad de ambientes de estas lagunas litorales. El recorrido describe una vuelta alrededor de la Reserva Integral hasta llegar al punto de origen (8,2 km).
            </p>
            <p style="font-size: 16px;">El tramo de este itinerario que transcurre por el camino de la playa de Can Comas puede inundarse en cualquier momento del año y podríamos encontrarlo impracticable. 
            En caso de encontrarlo inundado habría que regresar por el mismo camino de ida o intentar completar la vuelta yendo hasta el camping La Laguna.</p>
        """

        st.write(explicacion_recorrido, unsafe_allow_html=True)

        estilo_div = """
            <div style="background-color: #ff0000; color: white; padding: 20px; border-radius: 10px;">
            Queda totalmente prohibido el paso por el tramo de playa de este itinerario desde el 1 de de abril al 30 de junio por ser época de nidificación.
            </div>
        """

        # Mostrar el div
        st.markdown(estilo_div, unsafe_allow_html=True)

st.divider()

with st.container():
    st.markdown('# Algunas imágenes')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.image('static/images/foto2.jpg', use_column_width = 'always', caption = "Créditos: Parc Natural dels Aiguamolls de l'Empordà")

    with col2:
        st.image('static/images/foto3.jpg', use_column_width = 'always', caption = "Créditos: Parc Natural dels Aiguamolls de l'Empordà")

    with col3:
        st.image('static/images/foto4.jpg', use_column_width = 'always', caption = "Créditos: Parc Natural dels Aiguamolls de l'Empordà")

    with col4:
        st.image('static/images/foto5.jpg', use_column_width = 'always', caption = "Créditos: Parc Natural dels Aiguamolls de l'Empordà")


st.divider()

st.write('José Alberto Pérez Melián - Junio 2024')