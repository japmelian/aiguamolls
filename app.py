import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import folium_static, st_folium


st.set_page_config(layout = "wide", initial_sidebar_state="collapsed", page_title="Parc Natural dels Aiguamolls de l'Empordà")

with st.container():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image('static/images/logo.webp', use_column_width = 'always')
    
    with col2:
        cita = '“Els Aiguamolls són molt valorats per raons de caire natural, però poques vegades es té en compte que aquí hi trobaràs la llum, el color, l’harmonia, l’equilibri, la proporció i la serenor, fruit de l’evolució de milers d’anys, que et permeten evadir-te, descansar, renovar-te i enfortir-te d’una manera absolutament lliure.”'
        st.markdown(f"<p style='font-size:25px;'>{cita} -<i style='font-size:25px;'>Eduard Marquès</i></p>", unsafe_allow_html = True)


st.divider()
st.write("")
st.write("")

with st.container():
    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(use_column_width = 'always', image = 'static/images/foto1.jpg', caption = "Créditos: Parc Natural dels Aiguamolls de l'Empordà") 

    with col2:
        st.markdown("### Déjate cautivar por la belleza natural del Parc Natural dels Aiguamolls de l'Empordà, un oasis de vida silvestre en la región de la Costa Brava de Cataluña. Este espacio protegido ofrece un vistazo a un mundo donde la naturaleza es la protagonista indiscutible.")
        
        st.divider()

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('#### Explora la naturaleza en estado puro')
                st.write("Sumérgete en un entorno donde la tierra y el agua se entrelazan para crear un hábitat único. Desde extensas marismas hasta densos bosques de ribera, cada rincón del parque ofrece una experiencia natural inolvidable.")

            with col2:
                st.markdown('#### Tesoro de Biodiversidad')
                st.write("Los Aiguamolls de l'Empordà albergan una diversidad increíble de flora y fauna. Con más de 300 especies de aves, así como una variedad de mamíferos, anfibios e insectos, es un paraíso para los amantes de la naturaleza y los observadores de aves.")

        with st.container():
            col1, col2 = st.columns(2)

            with col1:
                st.markdown('#### Descubre su encanto natural')
                st.write("Adéntrate en sus senderos serpenteantes, descubre sus miradores panorámicos y maravíllate con la vida silvestre que habita en este santuario natural. Desde el majestuoso vuelo de las aves rapaces hasta el suave graznido de las cigüeñas, cada momento aquí es único.")

            with col2:
                st.markdown('#### Compromiso con la conservación')
                st.write("Descubre cómo se conserva este preciado ecosistema y cómo se trabaja para protegerlo de amenazas. El Parc Natural dels Aiguamolls de l'Empordà es mucho más que un lugar de belleza natural, es un testimonio del compromiso humano con la preservación del medio ambiente.")

st.divider()

with st.container():
    col1, col2 = st.columns([1, 2])

    with col1:
        st.title('Información sobre el parque')

        # Dirección
        st.write("**Dirección:**")
        st.write("Crta/ de Castelló d’Empúries a Sant Pere Pescador")
        st.write("17486 Castelló d’Empúries")

        # Teléfono
        st.write("**Teléfono:** 972 454 222")

        # Horario
        st.write("**Horario del centro de información:**")
        st.write("Abierto cada día de 9h a 16h (invierno) y de 9h a 18,30h (verano).")
        st.write("*Puedes consultar horario por teléfono.*")

        # Enlaces
        st.write("**Enlaces:**")
        st.write("- Web: [Parcs Naturals - Aiguamolls de l’Empordà](http://parcsnaturals.gencat.cat/ca/aiguamolls-emporda)")
        st.write("- Email: pnaiguamolls@gencat.cat")
        st.write("- Facebook: [PNAiguamollsEmporda](https://www.facebook.com/PNAiguamollsEmporda)")
        st.write("- Wikiloc: [Aiguamolls de l’Empordà en Wikiloc](http://ca.wikiloc.com/wikiloc/find.do?q=aiguamolls+emporda)")

    with col2:
        mapa_localizacion = gpd.read_file('static/geo/clean_pein.geojson')
        puntos_interes = gpd.read_file('static/geo/puntos_interes.geojson')

        # Crear un mapa con Folium
        mapa_info = folium.Map(location=[mapa_localizacion.centroid.y.mean(), mapa_localizacion.centroid.x.mean()], zoom_start=11)

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
            folium.Marker(location=[row.geometry.y, row.geometry.x], icon=icono).add_to(mapa_info)

        # Aplicar la función a cada fila del GeoDataFrame
        puntos_interes.apply(agregar_punto, axis=1)

        # Añadir los polígonos al mapa
        folium.GeoJson(mapa_localizacion).add_to(mapa_info)

        st_folium(mapa_info, width=1200)

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
    st.markdown('# Descubre los itinerarios')

    st.write("Sumérgete en la diversidad paisajística y la riqueza natural del Parc Natural dels Aiguamolls de l'Empordà a través de sus diversos itinerarios. Desde paseos suaves hasta aventuras más intensas, cada sendero te ofrece la oportunidad de explorar y disfrutar de este maravilloso entorno.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
            <div style="background-color: #ee4e4e; border-radius: 20px; padding: 20px; color: white; cursor: pointer;">
                <p style="font-weight: bold; font-size: 40px;">Itinerario 1</p>
                <p style="font-size: 20px;">Desde el Cortalet hasta el mas del Matà</p>
                <a href="/itinerario3" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #ffffff; color: "#a2a2a2"; padding: 10px 20px; border-radius: 5px; border: none; cursor: pointer;">
                        Ver más
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="background-color: #1679ab; border-radius: 20px; padding: 20px; color: white; cursor: pointer;">
                <p style="font-weight: bold; font-size: 40px;">Itinerario 2</p>
                <p style="font-size: 20px;">Desde mas del Matà a las «Llaunes»</p>
                <a href="/itinerario3" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #ffffff; color: "#a2a2a2"; padding: 10px 20px; border-radius: 5px; border: none; cursor: pointer;">
                        Ver más
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
            <div style="background-color: #219c90; border-radius: 20px; padding: 20px; color: white; cursor: pointer;">
                <p style="font-weight: bold; font-size: 40px;">Itinerario 3</p>
                <p style="font-size: 20px;">Ruta alrededor de la Reserva Integral de las «Llaunes»</p>
                <a href="/itinerario3" target="_blank" style="text-decoration: none;">
                    <button style="background-color: #ffffff; color: "#a2a2a2"; padding: 10px 20px; border-radius: 5px; border: none; cursor: pointer;">
                        Ver más
                    </button>
                </a>
            </div>
        """, unsafe_allow_html=True)

st.divider()

with st.container():
    st.markdown('# Conoce los distintos hábitats del parque')

    col1, col2 = st.columns([1, 2])
    st.write("")
    st.write("")

    with col1:
        st.image('static/images/foto2.jpg', use_column_width = 'always')

    with col2:
        st.markdown('### Marismas')
        st.write("""
            <p style="font-size: 20px;">
            Las marismas son uno de los hábitats más emblemáticos de los Aiguamolls de l'Empordà. Estas áreas se caracterizan por ser zonas inundadas que pueden estar cubiertas de agua salada, salobre o dulce, dependiendo de la proximidad al mar y de la estación del año. Las marismas del parque proporcionan un refugio crucial para una variedad de aves acuáticas, tanto residentes como migratorias. Aquí se pueden encontrar especies como la cigüeña blanca, el avetorillo y diversas especies de patos y garzas. Las plantas halófitas, que toleran altas concentraciones de sal, son comunes en estas áreas, incluyendo el carrizo y el salicornio. Además, las marismas juegan un papel vital en la regulación del agua, ayudando a prevenir inundaciones y a mantener la calidad del agua mediante la filtración de sedimentos y contaminantes. Este ecosistema también es esencial para la reproducción de muchas especies de peces y anfibios, que encuentran en las marismas un lugar seguro para desovar.
            </p>""", unsafe_allow_html=True)
        
    col1, col2 = st.columns([2, 1])
    st.write("")
    st.write("")

    with col2:
        st.image('static/images/foto3.jpg', use_column_width = 'always')

    with col1:
        st.markdown('### Lagunas y Estanques')
        st.write("""
            <p style="font-size: 20px;">
            Las lagunas y estanques del Parc Natural dels Aiguamolls de l'Empordà son cuerpos de agua estacionales o permanentes que sirven como hábitats cruciales para numerosas especies. Estos cuerpos de agua son especialmente importantes durante los periodos de migración de aves, proporcionando lugares de descanso y alimentación. Flamencos, somormujos y ánades reales son solo algunas de las especies que se pueden avistar en estas áreas. Las lagunas y estanques también son ricas en biodiversidad acuática. Aquí se encuentran diversas especies de peces, como la anguila europea, y una variedad de invertebrados que forman la base de la cadena alimentaria. Además, las plantas acuáticas como los nenúfares y las eneas contribuyen a la salud del ecosistema al ofrecer refugio y alimento a muchas criaturas.
            </p>""", unsafe_allow_html=True)
        
    col1, col2 = st.columns([1, 2])
    st.write("")
    st.write("")

    with col1:
        st.image('static/images/foto4.jpg', use_column_width = 'always')

    with col2:
        st.markdown('### Dunas Costeras')
        st.write("""
            <p style="font-size: 20px;">
            Las dunas costeras del parque son formaciones de arena que se encuentran a lo largo del litoral y están sujetas a la acción del viento y del mar. Este hábitat dinámico es crucial para proteger las áreas interiores de la erosión y las tormentas marinas. Las dunas albergan una flora especializada que puede soportar condiciones extremas de salinidad y falta de agua, como el barrón y el cardo marino. Además de su función protectora, las dunas costeras son hábitats importantes para la fauna. Insectos, reptiles y aves encuentran refugio y alimento en estas áreas. La vegetación de las dunas también juega un papel importante en la estabilización de la arena, ayudando a mantener la estructura del hábitat y permitiendo la colonización de nuevas especies vegetales.
            </p>""", unsafe_allow_html=True)
st.divider()

st.write('José Alberto Pérez Melián - Junio 2024')
                
