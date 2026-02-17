# Invoice Analysis

Aplicación web para validación automática de facturas chilenas con dashboard interactivo.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-red)
![License](https://img.shields.io/badge/License-MIT-green)

## Qué hace

- Valida IVA (19% Chile) automáticamente
- Verifica que los totales coincidan (neto + IVA = total)
- Detecta fechas fuera de período contable
- Dashboard dark mode con métricas y gráficos
- Exporta reportes a CSV

## Requisitos

- Python 3.10+
- pip

## Instalación

```bash
# Clonar repositorio
git clone https://github.com/nyu-bit/data-invoice-analysis.git
cd data-invoice-analysis

# Instalar dependencias
pip install -r requirements.txt
```

## Dependencias

| Paquete | Uso |
|---------|-----|
| streamlit | Framework web |
| pandas | Procesamiento de datos |
| plotly | Gráficos interactivos |
| openpyxl | Lectura de archivos Excel |
| scikit-learn | Modelo ML de clasificación |

## Ejecutar la aplicación

```bash
streamlit run app.py
```

La app se abrirá en `http://localhost:8501`

## Uso

1. **Subir archivo**: Arrastra un CSV o Excel con facturas
2. **O usar datos de ejemplo**: Marca "Use sample data"
3. **Ver resultados**: El dashboard muestra:
   - Total de facturas válidas/con errores
   - Nivel de riesgo
   - Detalle de cada error
4. **Exportar**: Descarga el reporte completo o solo errores

## Formato del archivo

El archivo debe contener estas columnas:

| Columna | Descripción | Ejemplo |
|---------|-------------|---------|
| `invoice_id` | ID único de factura | INV-001 |
| `provider` | Nombre del proveedor | Empresa ABC |
| `net_amount` | Monto neto (sin IVA) | 100000 |
| `tax` | IVA (19%) | 19000 |
| `total` | Total con IVA | 119000 |
| `issue_date` | Fecha de emisión | 2024-01-15 |
| `period` | Período contable | 2024-01 |

## Estructura del proyecto

```
├── app.py              # Aplicación Streamlit
├── requirements.txt    # Dependencias
├── data/
│   └── sample_invoices.csv
├── models/
│   └── invoice_classifier.joblib
├── notebooks/
│   └── analysis.ipynb
└── src/
    └── data_cleaning.py
```

## Validaciones

La app verifica automáticamente:

| Validación | Regla |
|------------|-------|
| IVA correcto | `tax == net_amount * 0.19` |
| Total correcto | `total == net_amount + tax` |
| Fecha en período | La fecha de emisión debe coincidir con el período declarado |

## Notas

- Los datos de ejemplo son simulados (proyecto académico)
- Configurado para IVA chileno (19%)
- No reemplaza software contable certificado

