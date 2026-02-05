# Análisis de Facturas

Procesamiento y validación de datos de facturas para apoyo contable.

## Qué hace

- Limpia y normaliza datos de facturas (CSV)
- Valida montos, fechas e IVA (19% Chile)
- Detecta registros inconsistentes
- Clasifica errores automáticamente usando ML (Decision Tree)

## Estructura

```
data/           # Datasets de facturas
models/         # Modelo entrenado (.joblib)
notebooks/      # Análisis exploratorio
src/            # Scripts de limpieza
```

## Stack

Python, Pandas, Scikit-learn, Jupyter

## Uso

```bash
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```

## Notas

- Los datos son simulados (proyecto académico)
- No reemplaza software contable ni reglas fiscales avanzadas

