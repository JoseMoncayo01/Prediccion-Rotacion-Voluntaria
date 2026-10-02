import pandas as pd
import matplotlib.pyplot as plt
import math
import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="Predicción de Rotación Voluntaria",
    layout="wide"
)

st.title("📊 Predicción de Rotación Voluntaria")
st.subheader("Análisis exploratorio de datos aplicado a People Analytics")

st.write("**Asignatura:** Análisis de Datos I")
st.write("**Taller 1:** Comparte tu análisis exploratorio de datos")


# ============================================================
# 1. DESCRIPCIÓN DEL PROBLEMA E IMPACTO
# ============================================================

st.header("1. 🎯 Descripción del problema e impacto")

st.subheader("1.1 Contexto organizacional")

st.write("""
La organización cuenta con diferentes colaboradores y áreas que son importantes
para el funcionamiento de sus procesos. La salida inesperada de un colaborador
puede generar dificultades para continuar las actividades y cubrir rápidamente
su puesto.
""")

st.subheader("1.2 Problema identificado")

st.write("""
Actualmente no se puede anticipar con suficiente tiempo qué colaboradores
podrían presentar una renuncia voluntaria. Esto dificulta preparar reemplazos
y puede generar pérdida de conocimiento y afectar la continuidad de algunos procesos.
""")

st.subheader("1.3 Áreas y procesos afectados")

st.write("""
Puede afectar a cualquiera de las áreas del banco donde se presentan las
salidas, especialmente cuando se trata de cargos importantes.
""")

st.subheader("1.4 Impacto en la organización")

st.write("""
Una renuncia no anticipada puede generar:
""")

st.markdown("""
- Pérdida de conocimiento y experiencia.
- Sobrecarga de trabajo para otros colaboradores.
- Posibles interrupciones en procesos importantes.
""")

st.subheader("1.5 Indicadores (KPI)")

st.write("""
El principal indicador que se busca mejorar es el porcentaje de renuncias
voluntarias no anticipadas, expresada entre 0 % y 100 %, para identificar
quiénes presentan mayor riesgo.
""")


# ============================================================
# 2. COMPLEJIDAD Y DISPONIBILIDAD DE LOS DATOS
# ============================================================

st.header("2. 🗂️ Complejidad y disponibilidad de los datos")

st.subheader("2.1 Datos requeridos")

st.write("""
Para analizar la rotación de empleados necesitamos información relacionada
con sus características personales, laborales y de satisfacción.
""")

st.markdown("""
- Edad y estado civil.
- Área y cargo.
- Salario.
- Antigüedad en la empresa.
- Satisfacción laboral.
- Desempeño.
- Horas extras.
- Viajes de trabajo.
- Formación.
- Tiempo en el cargo.
- Promociones.
- Attrition, que indica si el empleado se retiró.
""")


st.subheader("2.2 Fuente de los datos")

st.write("""
Los datos utilizados fueron obtenidos de Kaggle, en el conjunto IBM HR
Analytics Employee Attrition & Performance. Es importante aclarar que se
trata de un conjunto de datos ficticio, por lo que será utilizado como
referencia para desarrollar el análisis y el prototipo.
""")


st.subheader("2.3 Descripción del conjunto de datos")

st.write("""
El conjunto de datos tiene 1.470 registros de empleados y 35 variables.
Incluye información relacionada con aspectos personales, laborales,
económicos y de satisfacción de los empleados.
""")

st.write("La variable que nos interesa principalmente es:")

st.markdown("""
**Attrition →** indica si el empleado se retiró de la empresa (Yes) o permaneció (No).
""")


st.subheader("2.4 Variables disponibles")

st.write("""
El conjunto de datos contiene **35 variables** relacionadas con las
características personales, laborales y de satisfacción de los empleados.
""")


st.subheader("2.5 Complejidad del problema")

st.write("""
El problema tiene una complejidad media, porque tenemos diferentes tipos
de variables y debemos analizar cómo se relacionan con la rotación.
Además, algunas variables son numéricas y otras son categóricas, por lo
que será necesario preparar los datos antes de realizar el análisis.
""")

st.write("""
En este taller comenzaremos con un análisis exploratorio para identificar
patrones y posibles factores relacionados con la rotación voluntaria.
""")


# ============================================================
# 3. JUSTIFICACIÓN DEL USO DE IA Y CIENCIA DE DATOS
# ============================================================

st.header("3. 🤖 Justificación del uso de IA y Ciencia de Datos")

st.subheader("3.1 Enfoque analítico")

st.write("""
Se utilizarán técnicas de **Ciencia de Datos** para analizar la información
de los empleados e identificar posibles factores relacionados con la rotación.
""")


st.subheader("3.2 Técnica de Ciencia de Datos propuesta")

st.write("""
Se propone utilizar un modelo de **clasificación**, ya que queremos predecir
si un empleado tiene mayor o menor probabilidad de presentar una renuncia.
El modelo permitirá obtener una **probabilidad de rotación** para cada empleado.
""")


st.subheader("3.3 Aplicación al problema de rotación voluntaria")

st.write("""
El modelo analizará variables como la edad, salario, satisfacción laboral,
horas extras, antigüedad, cargo y otros factores disponibles en los datos.
Con esta información se buscará identificar patrones que puedan estar
relacionados con la decisión de un empleado de retirarse.
""")


st.subheader("3.4 Beneficios esperados")

st.markdown("""
- Identificar empleados con mayor probabilidad de rotación.
- Conocer algunos factores relacionados con las renuncias.
- Apoyar la toma de decisiones de Gestión Humana.
- Facilitar la creación de estrategias de retención.
- Anticipar posibles necesidades de reemplazo.
""")


# ============================================================
# 4. PREGUNTA DE ANÁLISIS SMART
# ============================================================

st.header("4. 🎯 Pregunta de análisis SMART")

st.subheader("4.1 Pregunta SMART")

st.info("""
¿Podemos identificar, a partir de las características laborales y personales
de los empleados, cuáles presentan una mayor probabilidad de rotación
voluntaria, con el fin de apoyar las decisiones de Gestión Humana?
""")


st.subheader("4.2 Específica (Specific)")
st.write("""
La pregunta se enfoca en identificar los empleados que presentan una mayor
probabilidad de rotación voluntaria.
""")


st.subheader("4.3 Medible (Measurable)")
st.write("""
El resultado se podrá medir mediante la **probabilidad de rotación**,
expresada como un porcentaje entre 0 % y 100 %.
""")


# Carga dinámica del dataset buscando en data/ o en el directorio actual
RUTA_DATOS = Path(__file__).resolve().parent.parent / "data" / "HR-Employee-Attrition.csv"
if not RUTA_DATOS.exists():
    RUTA_DATOS = Path("data/HR-Employee-Attrition.csv")
if not RUTA_DATOS.exists():
    RUTA_DATOS = Path("HR-Employee-Attrition.csv")

df = pd.read_csv(RUTA_DATOS)

# ============================================================
# 5. ANÁLISIS EXPLORATORIO DE DATOS
# ============================================================

st.header("5. 🔎 Análisis Exploratorio de Datos")

st.subheader("5.1 Carga de las librerías")

st.code("""
import pandas as pd
import matplotlib.pyplot as plt
import math
import streamlit as st
""")


st.subheader("5.2 Carga del conjunto de datos")

st.code("""
pd.read_csv("HR-Employee-Attrition.csv")
""")

# ============================================================
# RENOMBRAR COLUMNAS
# ============================================================

df = df.rename(columns={
    "Age": "edad",
    "Attrition": "rotacion",
    "BusinessTravel": "viaje_negocio",
    "DailyRate": "tarifa_diaria",
    "Department": "departamento",
    "DistanceFromHome": "distancia_casa",
    "Education": "nivel_educativo",
    "EducationField": "area_estudio",
    "EmployeeCount": "total_empleados",
    "EmployeeNumber": "id_empleado",
    "EnvironmentSatisfaction": "satisfaccion_ambiente",
    "Gender": "genero",
    "HourlyRate": "tarifa_hora",
    "JobInvolvement": "compromiso_trabajo",
    "JobLevel": "nivel_cargo",
    "JobRole": "cargo",
    "JobSatisfaction": "satisfaccion_trabajo",
    "MaritalStatus": "estado_civil",
    "MonthlyIncome": "ingreso_mensual",
    "MonthlyRate": "tarifa_mensual",
    "NumCompaniesWorked": "empresas_trabajadas",
    "Over18": "mayor_18",
    "OverTime": "horas_extras",
    "PercentSalaryHike": "aumento_salarial",
    "PerformanceRating": "evaluacion_desempeno",
    "RelationshipSatisfaction": "satisfaccion_relaciones",
    "StandardHours": "horas_estandar",
    "StockOptionLevel": "nivel_opciones_acciones",
    "TotalWorkingYears": "anios_experiencia",
    "TrainingTimesLastYear": "capacitaciones_ultimo_año",
    "WorkLifeBalance": "equilibrio_vida_trabajo",
    "YearsAtCompany": "anios_empresa",
    "YearsInCurrentRole": "anios_cargo_actual",
    "YearsSinceLastPromotion": "anios_ultima_promocion",
    "YearsWithCurrManager": "anios_jefe_actual"
})




st.subheader("5.3 Exploración inicial")

st.markdown("**Primeros 10 registros del conjunto de datos:**")

col1, col2, col3 = st.columns(3)

col1.metric("Empleados", df.shape[0])
col2.metric("Variables", df.shape[1])
col3.metric("Duplicados", df.duplicated().sum())



st.dataframe(df.head(10), use_container_width=True)



# ============================================================
# 5.4 CALIDAD Y ESTRUCTURA DE LOS DATOS
# ============================================================



st.subheader("5.4 Calidad y estructura de los datos")


st.write(
    """
    El conjunto de datos está compuesto por **1.470 registros y 35
    variables**, que contienen información personal y laboral de los
    empleados. Se encuentran variables **numéricas y categóricas**, lo
    que permite analizar diferentes características de los empleados y
    su posible relación con la rotación. En la revisión inicial
    **no se encontraron valores faltantes ni registros duplicados**,
    por lo que los datos presentan una buena calidad para continuar con
    el análisis. La variable `rotacion` será nuestra variable principal,
    ya que indica si el empleado se retiró o permaneció en la empresa.
    """
)


# Valores faltantes

st.markdown("**Valores faltantes:**")

valores_faltantes = (
    df.isnull()
    .sum()
    .sort_values(ascending=False)
)

st.dataframe(
    valores_faltantes.to_frame("Valores faltantes"),
    use_container_width=True
)


# Registros duplicados

duplicados = df.duplicated().sum()

st.metric(
    "Registros duplicados",
    duplicados
)



# ============================================================
# 5.5 ANÁLISIS DE VARIABLES NUMÉRICAS
# ============================================================

st.subheader("5.5 Análisis de variables numéricas")

variables_numericas = df.select_dtypes(include="number")

st.markdown("**Variables numéricas identificadas:**")

st.write(
    list(variables_numericas.columns)
)


st.markdown("**Resumen estadístico de las variables numéricas:**")

st.dataframe(
    variables_numericas.describe().T,
    use_container_width=True
)


# ============================================================
# HISTOGRAMAS
# ============================================================

st.markdown("**Distribución de variables numéricas:**")

cantidad_variables = len(variables_numericas.columns)

columnas = 4

filas = math.ceil(cantidad_variables / columnas)

fig, axes = plt.subplots(
    filas,
    columnas,
    figsize=(18, filas * 4)
)

axes = axes.flatten()

fig.patch.set_facecolor("#1E293B")

for i, variable in enumerate(variables_numericas.columns):

    axes[i].hist(
        df[variable],
        bins=15,
        color="#9CC3E6",
        edgecolor="#E2E8F0"
    )

    axes[i].set_facecolor("#1E293B")

    axes[i].set_title(
        variable,
        color="white",
        fontsize=11
    )

    axes[i].set_ylabel(
        "Frecuencia",
        color="white"
    )

    axes[i].tick_params(
        colors="white"
    )

    axes[i].grid(
        alpha=0.15,
        color="white"
    )


for j in range(cantidad_variables, len(axes)):
    axes[j].set_visible(False)


plt.tight_layout()

st.pyplot(fig)


# ============================================================
# 5.6 ANÁLISIS DE VARIABLES CATEGÓRICAS
# ============================================================

st.subheader("5.6 Análisis de variables categóricas")


variables_categoricas = [
    "viaje_negocio",
    "departamento",
    "nivel_educativo",
    "area_estudio",
    "satisfaccion_ambiente",
    "genero",
    "compromiso_trabajo",
    "nivel_cargo",
    "cargo",
    "satisfaccion_trabajo",
    "estado_civil",
    "horas_extras",
    "evaluacion_desempeno",
    "satisfaccion_relaciones",
    "equilibrio_vida_trabajo"
]


st.write(
    "Las variables categóricas seleccionadas para el análisis son:"
)

st.write(
    variables_categoricas
)





st.subheader("5.7 Variable objetivo")


st.write(
    """
    La variable `rotacion` será utilizada como variable objetivo.
    Esta variable indica si el empleado se retiró de la empresa (`Yes`)
    o permaneció (`No`).
    """
)

col1, col2 = st.columns(2)

rotacion = df["rotacion"].value_counts()

porcentaje_rotacion = (
    df["rotacion"]
    .value_counts(normalize=True) * 100
)

col1.metric(
    "Empleados que se fueron",
    rotacion.get("Yes", 0)
)

col2.metric(
    "Porcentaje de rotación",
    f"{porcentaje_rotacion.get('Yes', 0):.1f}%"
)


st.subheader("Distribución de la rotación")

fig, ax = plt.subplots()

df["rotacion"].value_counts().plot(
    kind="bar",
    ax=ax
)

ax.set_title("Distribución de la rotación de empleados")
ax.set_xlabel("Rotación")
ax.set_ylabel("Cantidad de empleados")
ax.tick_params(axis="x", rotation=0)


plt.tight_layout()

st.pyplot(fig)


# ============================================================
# VARIABLES CATEGÓRICAS
# ============================================================

variables_categoricas = [
    "viaje_negocio",
    "departamento",
    "nivel_educativo",
    "area_estudio",
    "satisfaccion_ambiente",
    "genero",
    "compromiso_trabajo",
    "nivel_cargo",
    "cargo",
    "satisfaccion_trabajo",
    "estado_civil",
    "horas_extras",
    "evaluacion_desempeno",
    "satisfaccion_relaciones",
    "equilibrio_vida_trabajo"
]


# ============================================================
# 5.8 RELACIÓN ENTRE VARIABLES Y ROTACIÓN
# ============================================================

st.subheader("5.8 Relación entre variables y rotación")


st.write(
    """
    A continuación se analiza la relación entre diferentes variables
    categóricas y la variable `rotacion`. Para cada variable se calcula
    el porcentaje de empleados que permanecieron o se retiraron.
    """
)

fig, axes = plt.subplots(
    4,
    4,
    figsize=(18, 16)
)

fig.patch.set_facecolor("#1E293B")

axes = axes.flatten()

for i, variable in enumerate(variables_categoricas):

    tabla = pd.crosstab(
        df[variable],
        df["rotacion"],
        normalize="index"
    ) * 100

    tabla.plot(
        kind="bar",
        ax=axes[i],
        color=["#9CC3E6", "#E6A0A0"]
    )

    axes[i].set_facecolor("#1E293B")

    axes[i].set_title(
        f"Rotación según {variable}",
        color="white"
    )

    axes[i].set_xlabel("")

    axes[i].set_ylabel(
        "%",
        color="white"
    )

    axes[i].tick_params(
        axis="both",
        colors="white"
    )

    axes[i].grid(
        axis="y",
        alpha=0.15,
        color="white"
    )

    axes[i].legend(
        title="Rotación",
        facecolor="#1E293B",
        labelcolor="white",
        title_fontsize=9
    )

    for contenedor in axes[i].containers:

        axes[i].bar_label(
            contenedor,
            fmt="%.1f%%",
            padding=2,
            fontsize=8,
            color="white"
        )


for j in range(
    len(variables_categoricas),
    len(axes)
):
    axes[j].set_visible(False)


plt.tight_layout()

st.pyplot(fig)




# ============================================================ # 5.9 HALLAZGOS PRINCIPALES # ============================================================ 
st.subheader("5.9 Hallazgos principales") 
st.write( """ El análisis exploratorio permitió identificar algunas diferencias entre los empleados que presentan rotación y quienes permanecen en la empresa. """ ) 
st.markdown(""" - Las **horas extras** muestran una diferencia importante: la rotación es del **30,5%** entre quienes realizan horas extras, frente al **10,4%** entre quienes no las realizan. - Los empleados con **menor compromiso con el trabajo** presentan mayores porcentajes de rotación. En el nivel 1 la rotación alcanza el **33,7%**, mientras que en el nivel 4 es del **9,0%**. - La **satisfacción laboral y con el ambiente** también muestra diferencias. Los niveles más bajos presentan mayores porcentajes de rotación. - Los empleados **solteros** presentan una rotación del **25,5%**, superior a la de los empleados casados (**12,5%**). - Según el **nivel del cargo**, la rotación es mayor en los niveles más bajos. En el nivel 1 alcanza el **26,3%**, mientras que en el nivel 4 es del **4,7%**. - También se observan diferencias según el **cargo**, los **viajes de negocio** y otras características laborales. """) 
st.write( """ En general, los resultados muestran que factores relacionados con la **carga laboral, satisfacción, compromiso y características del cargo** presentan diferencias en los niveles de rotación. """ ) 
st.info( """ Estos resultados son exploratorios y no permiten afirmar que una variable sea la causa de la rotación. Sin embargo, sirven como punto de partida para identificar las variables que pueden ser importantes en el modelo de clasificación. """ )


# ------------------------------------------------------------
# 6.1 PREPARACIÓN DE LOS DATOS
# ------------------------------------------------------------

st.subheader("6.1 Preparación de los datos")

st.write(
    f"""
    El conjunto de datos contiene **{df.shape[0]:,} registros y
    **{df.shape[1]} variables**.
    """
)

st.markdown("**Variables disponibles:**")

st.write(list(df.columns))


st.write(
    """
    Para construir el modelo de clasificación, se define `rotacion` como
    la variable objetivo. Esta variable indica si el empleado presentó o
    no rotación. Se codifica como 0 para los empleados sin rotación y 1
    para aquellos que presentaron rotación.
    """
)


# Variable objetivo

y = df["rotacion"].map({
    "No": 0,
    "Yes": 1
})


col1, col2 = st.columns(2)

col1.metric(
    "Empleados sin rotación",
    int((y == 0).sum())
)

col2.metric(
    "Empleados con rotación",
    int((y == 1).sum())
)


# ------------------------------------------------------------
# 6.2 VARIABLES UTILIZADAS
# ------------------------------------------------------------

st.subheader("6.2 Selección de variables")

X = df.drop(
    columns=[
        "rotacion",
        "id_empleado",
        "total_empleados",
        "horas_estandar",
        "mayor_18"
    ]
)

st.write(
    f"Después de excluir la variable objetivo y algunas variables que no "
    f"se utilizarán en el modelo, se obtienen **{X.shape[0]:,} registros "
    f"y {X.shape[1]} variables predictoras.**"
)


# ------------------------------------------------------------
# 6.3 DIVISIÓN DE LOS DATOS
# ------------------------------------------------------------

st.subheader("6.3 División de los datos")

st.write(
    """
    Los datos se dividen en un conjunto de entrenamiento y otro de prueba.
    El 80 % de los registros se utiliza para entrenar el modelo y el 20 %
    restante se reserva para evaluar su desempeño con datos que no fueron
    utilizados durante el entrenamiento.
    """
)


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


col1, col2 = st.columns(2)

col1.metric(
    "Registros de entrenamiento",
    X_train.shape[0]
)

col2.metric(
    "Registros de prueba",
    X_test.shape[0]
)



# ------------------------------------------------------------
# 6.4 IDENTIFICACIÓN DE VARIABLES
# ------------------------------------------------------------

st.subheader("6.4 Identificación de variables numéricas y categóricas")

variables_numericas_modelo = X.select_dtypes(
    include=["int64", "float64"]
).columns

variables_categoricas_modelo = X.select_dtypes(
    include=["object"]
).columns


col1, col2 = st.columns(2)

with col1:

    st.markdown("**Variables numéricas:**")

    st.write(
        list(variables_numericas_modelo)
    )


with col2:

    st.markdown("**Variables categóricas:**")

    st.write(
        list(variables_categoricas_modelo)
    )


st.write(
    """
    El conjunto de datos contiene variables numéricas y categóricas.
    Para que puedan ser utilizadas por el modelo, las variables numéricas
    se estandarizan mediante `StandardScaler`, mientras que las variables
    categóricas se transforman mediante `One-Hot Encoding`.
    """
)


# ------------------------------------------------------------
# 6.5 PREPROCESAMIENTO
# ------------------------------------------------------------

st.subheader("6.5 Preprocesamiento de los datos")


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


preprocesamiento = ColumnTransformer(
    transformers=[
        (
            "numericas",
            StandardScaler(),
            variables_numericas_modelo
        ),
        (
            "categoricas",
            OneHotEncoder(handle_unknown="ignore"),
            variables_categoricas_modelo
        )
    ]
)


X_train_preparado = preprocesamiento.fit_transform(
    X_train
)

X_test_preparado = preprocesamiento.transform(
    X_test
)


col1, col2 = st.columns(2)

col1.metric(
    "Variables antes del preprocesamiento",
    X.shape[1]
)

col2.metric(
    "Variables después del preprocesamiento",
    X_train_preparado.shape[1]
)


st.write(
    f"""
    El conjunto de entrenamiento pasó de **{X_train.shape[1]} variables**
    a **{X_train_preparado.shape[1]} variables** después de aplicar
    la estandarización y la transformación One-Hot Encoding.
    """
)

# ============================================================
# 5.9 HALLAZGOS PRINCIPALES
# ============================================================

st.subheader("5.9 Hallazgos principales")

st.write(
    """
    El análisis exploratorio permitió identificar algunas diferencias
    entre los empleados que presentan rotación y quienes permanecen
    en la empresa.
    """
)

st.markdown("""
- Las **horas extras** muestran una diferencia importante: la rotación es del **30,5%** entre quienes realizan horas extras, frente al **10,4%** entre quienes no las realizan.

- Los empleados con **menor compromiso con el trabajo** presentan mayores porcentajes de rotación. En el nivel 1 la rotación alcanza el **33,7%**, mientras que en el nivel 4 es del **9,0%**.

- La **satisfacción laboral y con el ambiente** también muestra diferencias. Los niveles más bajos presentan mayores porcentajes de rotación.

- Los empleados **solteros** presentan una rotación del **25,5%**, superior a la de los empleados casados (**12,5%**).

- Según el **nivel del cargo**, la rotación es mayor en los niveles más bajos. En el nivel 1 alcanza el **26,3%**, mientras que en el nivel 4 es del **4,7%**.

- También se observan diferencias según el **cargo**, los **viajes de negocio** y otras características laborales.
""")

st.write(
    """
    En general, los resultados muestran que factores relacionados con la
    **carga laboral, satisfacción, compromiso y características del cargo**
    presentan diferencias en los niveles de rotación.
    """
)

st.info(
    """
    Estos resultados son exploratorios y no permiten afirmar que una variable
    sea la causa de la rotación. Sin embargo, sirven como punto de partida
    para identificar las variables que pueden ser importantes en el modelo
    de clasificación.
    """
)


# ============================================================
# 6. PROTOTIPO DE SOLUCIÓN CON IA GENERATIVA
# ============================================================

st.header("6. 🧠 Prototipo de solución con IA generativa")


# ------------------------------------------------------------
# 6.1 PREPARACIÓN DE LOS DATOS
# ------------------------------------------------------------

st.subheader("6.1 Preparación de los datos")

st.write(
    f"""
    El conjunto de datos contiene **{df.shape[0]:,} registros y
    **{df.shape[1]} variables**.
    """
)

st.markdown("**Variables disponibles:**")

st.write(list(df.columns))


st.write(
    """
    Para construir el modelo de clasificación, se define `rotacion` como
    la variable objetivo. Esta variable indica si el empleado presentó o
    no rotación. Se codifica como 0 para los empleados sin rotación y 1
    para aquellos que presentaron rotación.
    """
)


# Variable objetivo

y = df["rotacion"].map({
    "No": 0,
    "Yes": 1
})


col1, col2 = st.columns(2)

col1.metric(
    "Empleados sin rotación",
    int((y == 0).sum())
)

col2.metric(
    "Empleados con rotación",
    int((y == 1).sum())
)


# ------------------------------------------------------------
# 6.2 VARIABLES UTILIZADAS
# ------------------------------------------------------------

st.subheader("6.2 Selección de variables")

X = df.drop(
    columns=[
        "rotacion",
        "id_empleado",
        "total_empleados",
        "horas_estandar",
        "mayor_18"
    ]
)

st.write(
    f"Después de excluir la variable objetivo y algunas variables que no "
    f"se utilizarán en el modelo, se obtienen **{X.shape[0]:,} registros "
    f"y {X.shape[1]} variables predictoras.**"
)


# ------------------------------------------------------------
# 6.3 DIVISIÓN DE LOS DATOS
# ------------------------------------------------------------

st.subheader("6.3 División de los datos")

st.write(
    """
    Los datos se dividen en un conjunto de entrenamiento y otro de prueba.
    El 80 % de los registros se utiliza para entrenar el modelo y el 20 %
    restante se reserva para evaluar su desempeño con datos que no fueron
    utilizados durante el entrenamiento.
    """
)


from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)


col1, col2 = st.columns(2)

col1.metric(
    "Registros de entrenamiento",
    X_train.shape[0]
)

col2.metric(
    "Registros de prueba",
    X_test.shape[0]
)


# ------------------------------------------------------------
# 6.4 IDENTIFICACIÓN DE VARIABLES
# ------------------------------------------------------------

st.subheader("6.4 Identificación de variables numéricas y categóricas")

variables_numericas_modelo = X.select_dtypes(
    include=["int64", "float64"]
).columns

variables_categoricas_modelo = X.select_dtypes(
    include=["object"]
).columns


col1, col2 = st.columns(2)

with col1:

    st.markdown("**Variables numéricas:**")

    st.write(
        list(variables_numericas_modelo)
    )


with col2:

    st.markdown("**Variables categóricas:**")

    st.write(
        list(variables_categoricas_modelo)
    )


st.write(
    """
    El conjunto de datos contiene variables numéricas y categóricas.
    Para que puedan ser utilizadas por el modelo, las variables numéricas
    se estandarizan mediante `StandardScaler`, mientras que las variables
    categóricas se transforman mediante `One-Hot Encoding`.
    """
)


# ------------------------------------------------------------
# 6.5 PREPROCESAMIENTO
# ------------------------------------------------------------

st.subheader("6.5 Preprocesamiento de los datos")


from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


preprocesamiento = ColumnTransformer(
    transformers=[
        (
            "numericas",
            StandardScaler(),
            variables_numericas_modelo
        ),
        (
            "categoricas",
            OneHotEncoder(handle_unknown="ignore"),
            variables_categoricas_modelo
        )
    ]
)


X_train_preparado = preprocesamiento.fit_transform(
    X_train
)

X_test_preparado = preprocesamiento.transform(
    X_test
)


col1, col2 = st.columns(2)

col1.metric(
    "Variables antes del preprocesamiento",
    X.shape[1]
)

col2.metric(
    "Variables después del preprocesamiento",
    X_train_preparado.shape[1]
)


st.write(
    f"""
    El conjunto de entrenamiento pasó de **{X_train.shape[1]} variables**
    a **{X_train_preparado.shape[1]} variables** después de aplicar
    la estandarización y la transformación One-Hot Encoding.
    """
)


# ------------------------------------------------------------
# 6.6 MODELO DE REGRESIÓN LOGÍSTICA
# ------------------------------------------------------------

st.subheader("6.6 Modelo de regresión logística")


st.write(
    """
    Para realizar la clasificación se utiliza un modelo de
    **Regresión Logística**, debido a que la variable objetivo es binaria:
    el empleado puede presentar rotación o no presentar rotación.
    """
)


from sklearn.linear_model import LogisticRegression


modelo = LogisticRegression(
    max_iter=1000,
    random_state=42
)


modelo.fit(
    X_train_preparado,
    y_train
)


st.success("Modelo de Regresión Logística entrenado correctamente.")


# ------------------------------------------------------------
# 6.7 PREDICCIONES
# ------------------------------------------------------------

st.subheader("6.7 Predicciones del modelo")


y_pred = modelo.predict(
    X_test_preparado
)

y_prob = modelo.predict_proba(
    X_test_preparado
)[:, 1]


st.write(
    """
    El modelo permite realizar dos tipos de predicción. Primero, clasifica
    si el empleado presenta o no rotación. Segundo, permite obtener una
    probabilidad de rotación para cada empleado.
    """
)


col1, col2 = st.columns(2)

col1.metric(
    "Predicciones realizadas",
    len(y_pred)
)

col2.metric(
    "Probabilidad promedio de rotación",
    f"{y_prob.mean() * 100:.1f}%"
)


# ------------------------------------------------------------
# 6.8 EVALUACIÓN DEL MODELO
# ------------------------------------------------------------

st.subheader("6.8 Evaluación del modelo")


from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix
)


accuracy = accuracy_score(
    y_test,
    y_pred
)

precision = precision_score(
    y_test,
    y_pred,
    zero_division=0
)

recall = recall_score(
    y_test,
    y_pred,
    zero_division=0
)

f1 = f1_score(
    y_test,
    y_pred,
    zero_division=0
)

roc_auc = roc_auc_score(
    y_test,
    y_prob
)


col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Accuracy",
    f"{accuracy:.2%}"
)

col2.metric(
    "Precision",
    f"{precision:.2%}"
)

col3.metric(
    "Recall",
    f"{recall:.2%}"
)

col4.metric(
    "F1-Score",
    f"{f1:.2%}"
)

col5.metric(
    "ROC-AUC",
    f"{roc_auc:.2%}"
)


st.write(
    """
    Estas métricas permiten evaluar diferentes aspectos del desempeño
    del modelo. Accuracy representa la proporción de predicciones
    correctas, mientras que Precision, Recall y F1-Score permiten
    evaluar específicamente el comportamiento de la clasificación.
    ROC-AUC permite evaluar la capacidad del modelo para distinguir
    entre empleados con y sin rotación.
    """
)


# ------------------------------------------------------------
# 6.9 MATRIZ DE CONFUSIÓN
# ------------------------------------------------------------

st.subheader("6.9 Matriz de confusión")


matriz = confusion_matrix(
    y_test,
    y_pred
)


fig, ax = plt.subplots(
    figsize=(6, 5)
)

ax.imshow(matriz)

ax.set_title(
    "Matriz de confusión"
)

ax.set_xlabel(
    "Predicción"
)

ax.set_ylabel(
    "Valor real"
)

ax.set_xticks([0, 1])
ax.set_yticks([0, 1])

ax.set_xticklabels(
    ["No rotación", "Rotación"]
)

ax.set_yticklabels(
    ["No rotación", "Rotación"]
)


for i in range(matriz.shape[0]):

    for j in range(matriz.shape[1]):

        ax.text(
            j,
            i,
            matriz[i, j],
            ha="center",
            va="center",
            fontsize=14
        )


plt.tight_layout()

st.pyplot(fig)


# ------------------------------------------------------------
# 6.10 PROBABILIDADES DE ROTACIÓN
# ------------------------------------------------------------

st.subheader("6.10 Probabilidad de rotación")


resultados = X_test.copy()

resultados["rotacion_real"] = y_test.values

resultados["probabilidad_rotacion"] = (
    y_prob * 100
)

resultados["prediccion"] = y_pred


resultados = resultados.sort_values(
    "probabilidad_rotacion",
    ascending=False
)


st.write(
    """
    A continuación se muestran los empleados del conjunto de prueba
    ordenados según la probabilidad estimada de rotación.
    """
)


st.dataframe(
    resultados[
        [
            "edad",
            "departamento",
            "cargo",
            "nivel_cargo",
            "horas_extras",
            "rotacion_real",
            "probabilidad_rotacion",
            "prediccion"
        ]
    ].head(20),
    use_container_width=True
)


# ============================================================
# 7. CONCLUSIONES
# ============================================================

st.header("7. 📌 Conclusiones")


st.markdown("""
- El análisis exploratorio permitió identificar diferencias en la rotación
  asociadas a factores como las horas extras, el compromiso con el trabajo,
  la satisfacción laboral, el estado civil y el nivel del cargo.

- Las variables analizadas presentan diferentes comportamientos entre los
  empleados que permanecen y aquellos que presentan rotación.

- El modelo de clasificación permite complementar el análisis exploratorio
  mediante la estimación de una probabilidad de rotación para cada empleado.

- La Regresión Logística permite construir un primer prototipo para identificar
  empleados que podrían presentar un mayor riesgo de rotación.

- Los resultados del modelo deben interpretarse como una herramienta de apoyo
  para Gestión Humana y no como una determinación definitiva sobre la decisión
  de un empleado de retirarse.

- El análisis puede servir como punto de partida para desarrollar estrategias
  de retención y realizar análisis posteriores con otros modelos de clasificación.
""")


st.success(
    "✅ Aplicación ejecutada correctamente."
)