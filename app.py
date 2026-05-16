import streamlit as st
import pandas as pd
import plotly.express as px

# Configuración de la página
st.set_page_config(page_title="LEAN APP SUPERIOR GYM", layout="wide")

# Título Principal
st.title("🏋️‍♂️ LEAN APP SUPERIOR GYM")
st.markdown("---")

# Menú Lateral para Navegación
menu = [
    "Inicio", 
    "Auditoría 5S", 
    "Takt Time (Flujo de Clientes)", 
    "Control de Inventario (Kanban)",
    "Análisis de Desperdicios (Muda)"
]
choice = st.sidebar.selectbox("Selecciona una Herramienta Lean", menu)

# --- SECCIÓN: INICIO ---
if choice == "Inicio":
    st.subheader("Bienvenido al Sistema de Gestión de Calidad")
    st.write("""
    Esta plataforma está diseñada para optimizar los procesos de **Superior Gym** 
    aplicando metodologías Lean Manufacturing para mejorar la experiencia del socio y 
    la rentabilidad del negocio.
    """)
    st.info("Selecciona una herramienta en el menú de la izquierda para comenzar.")

# --- SECCIÓN: AUDITORÍA 5S ---
elif choice == "Auditoría 5S":
    st.subheader("📋 Checksheet de Auditoría 5S - Área de Pesas/Cardio")
    
    col1, col2 = st.columns(2)
    with col1:
        seiri = st.checkbox("Seiri (Clasificar): ¿Solo hay equipo necesario en sala?")
        seiton = st.checkbox("Seiton (Orden): ¿Las mancuernas están en sus racks?")
        seiso = st.checkbox("Seiso (Limpieza): ¿El equipo está desinfectado?")
    
    with col2:
        seiketsu = st.checkbox("Seiketsu (Estandarizar): ¿Existen etiquetas de peso?")
        shitsuke = st.checkbox("Shitsuke (Disciplina): ¿El staff sigue el rol de limpieza?")

    score = sum([seiri, seiton, seiso, seiketsu, shitsuke])
    st.metric("Puntaje de Calidad 5S", f"{score}/5")
    
    if score == 5:
        st.success("¡Excelente! El área cumple con los estándares Lean.")
    else:
        st.warning("Hay áreas de oportunidad para mejorar el flujo de trabajo.")

# --- SECCIÓN: TAKT TIME ---
elif choice == "Takt Time (Flujo de Clientes)":
    st.subheader("⏱️ Calculadora de Takt Time")
    st.write("Define el ritmo al que el gimnasio debe atender a los socios para evitar saturación.")
    
    tiempo_disponible = st.number_input("Minutos de apertura por turno (ej. 360 min)", min_value=1)
    demanda_clientes = st.number_input("Número de socios esperados por turno", min_value=1)
    
    takt_time = tiempo_disponible / demanda_clientes
    st.metric("Takt Time (Minutos por Socio)", f"{takt_time:.2f} min")
    st.info(f"Para no saturar el equipo, deberías recibir o procesar la entrada de un socio cada {takt_time:.2f} minutos.")

# --- SECCIÓN: KANBAN ---
elif choice == "Control de Inventario (Kanban)":
    st.subheader("📦 Sistema Kanban de Suplementos y Limpieza")
    
    # Simulación de datos
    data = {
        "Producto": ["Whey Protein", "Creatina", "Toallas Papel", "Desinfectante"],
        "Stock Actual": [5, 2, 15, 3],
        "Punto de Reorden": [4, 5, 10, 5]
    }
    df = pd.DataFrame(data)
    
    # Lógica de semáforo Lean
    df['Estado'] = df.apply(lambda x: "🔴 REORDEN" if x['Stock Actual'] <= x['Punto de Reorden'] else "🟢 OK", axis=1)
    
    st.table(df)

# --- SECCIÓN: MUDA ---
elif choice == "Análisis de Desperdicios (Muda)":
    st.subheader("🗑️ Identificación de Desperdicios en el Gimnasio")
    muda_tipo = st.selectbox("Tipo de Desperdicio", ["Esperas", "Movimientos innecesarios", "Defectos", "Talento no utilizado"])
    
    observacion = st.text_area(f"Describe el desperdicio de tipo '{muda_tipo}' observado:")
    if st.button("Registrar para Plan de Acción"):
        st.success("Registrado. Esto se usará para tu próximo Kaizen.")
