#Informe primera parte del trabajo

##1. Dataset elegido: Centros Sanitarios de Valencia

| Fichero | Dominio Smart CIty | Entidades Clave para Linkeo |
| :--- | :--- | :--- |
| **'hospitales.csv'** | **Servicios Sociales y Salud/ Infraestructura Sanitaria** | **Latitud/Longitud**, **Barrio**, **Tipo** (Hospital, Centro de Salud) |

###Cumplimiento de los requisitos (R1 - R6)

Hemos seleccionado el dataset de **Centros Sanitarios de Valencia** ('hospitales.csv').

| Requisito | Cumplimiento | Justificación |
| :--- | :--- | :--- |
| **R1. Dominio Smart City** | **SÍ** | La gestión y ubicación de la **infraestructura de salud pública** es esencial para la calidad de vida en una Smart City. |
| **R2. Disponible como CSV** | **SÍ** | El fichero base para la transformación es el archivo **`hospitales.csv`**. |
| **R3. Licencia Abierta** | **SÍ** | El origen público del dato garantiza una licencia que permite su publicación y reutilización. |
| **R4. Fácilmente Enlazable (Entidades Reales)** | **SÍ** | Contiene **Latitud/Longitud** (`geo_point_2d`), la clave más robusta para enlazar con LOD geográfico (GeoNames, DBpedia). |
| **R5. Documentación Existe (Opcional)**| **SÍ** | Las cabeceras de las columnas (`Nombre`, `Tipo`, `Camas`, `Direccion`) sirven como documentación directa. |
| **R6. Múltiples Fuentes (Opcional)** | **SÍ** | Se propone enlazar con datasets de **Movilidad (paradas de transporte)** y **Demografía (población por barrio)**. |

