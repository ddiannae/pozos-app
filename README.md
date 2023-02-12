# Estimación de riesgo en consumo de agua

Proyecto desarrollado en conjunto con la Dra. Mónica Imelda Martínez, investigadora del Laboratorio de Epidemiología Ambiental en la Unidad Académica de Ciencias Químicas de la Universidad Autónoma de Zacatecas.

Esta aplicación calcula el cociente de riesgo dados los contaminantes presentes en la fuente de abastecimiento de agua más cercana a la posición indicada por el usuario y la cantidad de vasos de agua consumidos al día. 

Fue construida en [Django](https://www.djangoproject.com/) con la base de datos implementada en [MySQL](https://www.mysql.com/).

## Descripción 

El proyecto se compone de dos aplicaciones:

**mapi:** Rest API para realizar consultas a la base de datos que alberga información de los pozos. Se construyó de esta forma para facilitar el posterior desarrollo de aplicaciones móviles nativas que hacen uso de los datos. Tiene implementados los siguientes endpoints:
  - `GET /pozo/`: obtiene todos los pozos de la base de datos.
  - `GET /pozo/<id>`: obtiene el pozo asociado al id correspondiente.
  - `GET /cercano/<lat>/<long>`: obtiene el pozo más cercano dados los valores de latitud y longitud especificados.
  
**encuesta**: Aplicación web que permite que el usuario conteste un formulario para conocer su ubicación y sus hábitos de consumo de agua y presenta como respuesta información asociada a los contaminantes medidos en el pozo más cercano, así como el resultado del cociente de riesgo calculado. La identificación de ubicación se implementó de dos formas: seleccionando un punto en el mapa desplegado utilizando [leaflet](https://leafletjs.com/) o compartiendo la ubicación del  dispositivo. 

## Fuente de datos

Los datos de los pozos se obtuvieron de CONAGUA con información de los contaminantes registrada en el año 2020. Las escalas de clasificación  asignadas a los valores de contaminantes medidos también se obtienen de su base de datos. Se cuenta con los siguientes valores en miligramos por litro: Alcalinidad Total, Arsénico Total, Cadmio Total, Cromo Total, Dureza Total, Hierro Total, Fluoruros Totales, Mercurio Total, Manganeso Total, Nitrógeno de Nitratos, Plomo Total y Sólidos Disueltos Totales-Medidos. Además, en número más probable por 100 mililitros se registran Coliformes Fecales y Conductividad en microsiemens por centímetro. Cada valor de contaminante tiene una clasificación de calidad asociada y a partir del valor de Sólidos Disueltos Totales, se derivan dos clasficiadores: indicador para Riego agrícola e indicador para Salinización.

## Datos almacenados

Para realizar futuros análisis sobre los hábitos de consumo de agua en la población mexicana, se almacenan los datos proporcionados por los usuarios al contestar el cuestionario. Estos datos incluyen: peso, edad, sexo, procedencia del agua para tomar, procedencia del agua para cocinar, cantidad de vasos de agua que se consumen al día, si el usuario es cuidador de menores de edad y la longitud y latitud indicadas en el mapa.  

## Cálculo del cociente de riesgo

Para obtener el cociente de riesgo se divide la dosis de exposición del usuario entre la dosis de referencia. Para el cálculo de la dosis de exposición se utiliza la siguiente fórmula: 

$$ Dosis_{exposición} = {concentración * ingesta * FE \over peso } $$

Donde:
  - $concentración$: se refiere a la concentración del contaminante para el cual se calcula la dosis
  - $ingesta$: es la cantidad de agua consumida al día por el usuario, tomando en cuenta que un vaso equivale a 250ml
  - $peso$: se refiere al peso corporal del usuario
  - $FE$: es un factor de exposición, con valor de 1
  
Las dosis de referencia utilizadas en la aplicación son las siguientes:
  - Arsénico, efectos dérmicos: 0.0003 mg/kg al día
  - Arsénico, riesgo cancerígeno: 1.5 mg/kg al día
  - Cadmio: 0.0005 mg/kg al día, sin efectos cancerígenos
  - Cromo: 0.003 mg/kg al día
  - Fluor: 0.06 mg/kg al día, sin efecto cancerígeno, fluorosis dental
  - Manganeso: 0.14 mg/kg al día, con afectaciones al sistema nervioso
  - Mercurio: 0.0003 mg/kg al día, con afectaciones al sistema nervioso


