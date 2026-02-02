# Invoice Data Processing for Accounting Support

Este proyecto tiene como objetivo apoyar procesos contables mediante el análisis, limpieza y estructuración de información proveniente de facturas.

## Descripción
El sistema procesa datos de facturas en formato estructurado (CSV), normalizando la información, validando campos clave y generando datos limpios que faciliten el registro contable y la revisión por parte de profesionales del área.

El proyecto no reemplaza el trabajo del contador, sino que busca reducir tareas manuales repetitivas y minimizar errores en la gestión de facturas.

## Tecnologías utilizadas
- Python
- Pandas
- Jupyter Notebook
- Scikit-learn (Machine Learning)

## Funcionalidades principales
- Limpieza y normalización de datos de facturas
- Validación básica de montos, fechas e impuestos (IVA 19% Chile)
- Identificación de registros incompletos o inconsistentes
- Generación de datasets listos para su uso contable
- **Machine Learning**: Clasificación automática de errores en facturas

## Machine Learning
El proyecto incluye un modelo de clasificación (Decision Tree) para detectar automáticamente errores en facturas:
- Validación de IVA
- Validación de totales
- Validación de períodos contables

El modelo entrenado se guarda en `models/invoice_classifier.joblib`.

## Enfoque
Proyecto académico con enfoque en Ingeniería de Datos e IA aplicada como apoyo a procesos empresariales.

## Limitations
- This project does not replace accounting software.
- Advanced tax rules are not implemented.
- Data is simulated for academic purposes.

## Estado del proyecto
Completado - Versión 1.0

