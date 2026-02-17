import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.data_cleaning import validate_tax

# ========================================
# CONFIGURACIÓN
# ========================================
st.set_page_config(
    page_title="Invoice Analysis",
    page_icon="◉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ========================================
# ESTILOS CSS - DARK MODE ENTERPRISE
# ========================================
st.markdown("""
<style>
    /* Fuentes y base */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }
    
    /* Dark mode base */
    .stApp {
        background-color: #0f1117;
    }
    
    /* Ocultar elementos de Streamlit */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Container principal */
    .block-container {
        padding: 2rem 3rem;
        max-width: 1200px;
    }
    
    /* Título principal */
    .main-header {
        font-size: 1.75rem;
        font-weight: 600;
        color: #FFFFFF;
        margin-bottom: 0.25rem;
    }
    
    .sub-header {
        font-size: 0.95rem;
        color: #B0B8C1;
        font-weight: 400;
        margin-bottom: 2rem;
    }
    
    /* Cards - Dark */
    .metric-card {
        background: #1a1d24;
        border: 1px solid #2d3139;
        border-radius: 12px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 1rem;
    }
    
    .metric-label {
        font-size: 0.75rem;
        color: #B0B8C1;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        font-size: 2rem;
        font-weight: 600;
        color: #FFFFFF;
        line-height: 1.2;
    }
    
    .metric-delta {
        font-size: 0.85rem;
        color: #B0B8C1;
        margin-top: 0.25rem;
    }
    
    /* Status badges - Dark */
    .status-ok {
        background: #0d2818;
        color: #4ade80;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        display: inline-block;
        border: 1px solid #166534;
    }
    
    .status-warning {
        background: #1c1a0d;
        color: #fbbf24;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        display: inline-block;
        border: 1px solid #854d0e;
    }
    
    .status-error {
        background: #1f0d0d;
        color: #f87171;
        padding: 0.5rem 1rem;
        border-radius: 8px;
        font-weight: 600;
        display: inline-block;
        border: 1px solid #991b1b;
    }
    
    /* Sección */
    .section-title {
        font-size: 0.85rem;
        font-weight: 600;
        color: #FFFFFF;
        margin: 2.5rem 0 1rem 0;
        padding-bottom: 0.75rem;
        border-bottom: 1px solid #2d3139;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Expander - Dark */
    .streamlit-expanderHeader {
        font-size: 0.9rem;
        font-weight: 500;
        color: #FFFFFF !important;
        background: #1a1d24 !important;
    }
    
    [data-testid="stExpander"] {
        background: #1a1d24;
        border: 1px solid #2d3139;
        border-radius: 8px;
    }
    
    /* Dataframe - Dark */
    .dataframe {
        font-size: 0.85rem;
    }
    
    /* Buttons - Dark */
    .stButton > button {
        background: #3b82f6;
        color: #FFFFFF;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        font-weight: 500;
        transition: all 0.2s;
    }
    
    .stButton > button:hover {
        background: #2563eb;
        transform: translateY(-1px);
    }
    
    /* Download buttons - Dark */
    .stDownloadButton > button {
        background: #1a1d24;
        color: #FFFFFF;
        border: 1px solid #2d3139;
        border-radius: 8px;
        font-weight: 500;
    }
    
    .stDownloadButton > button:hover {
        background: #252830;
        border-color: #3d4149;
    }
    
    /* Alerts - Dark with high contrast */
    .stAlert {
        border-radius: 8px;
    }
    
    [data-testid="stAlert"] {
        color: #FFFFFF !important;
    }
    
    /* Success alert */
    .stAlert[data-testid="stAlert"]:has([data-testid="stMarkdownContainer"]) {
        color: #FFFFFF;
    }
    
    /* Divider */
    hr {
        border: none;
        border-top: 1px solid #2d3139;
        margin: 1.5rem 0;
    }
    
    /* File uploader - Dark */
    [data-testid="stFileUploader"] {
        background: #1a1d24;
        border: 2px dashed #3d4149;
        border-radius: 12px;
        padding: 1rem;
    }
    
    [data-testid="stFileUploader"] label {
        color: #FFFFFF !important;
    }
    
    /* Checkbox - Dark */
    .stCheckbox label span {
        color: #FFFFFF !important;
    }
    
    /* Caption text */
    .stCaption, [data-testid="stCaptionContainer"] {
        color: #B0B8C1 !important;
    }
    
    /* Metrics nativas de Streamlit - Dark */
    [data-testid="stMetricValue"] {
        font-size: 1.75rem;
        font-weight: 600;
        color: #FFFFFF !important;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 0.75rem;
        color: #B0B8C1 !important;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }
    
    [data-testid="stMetricDelta"] {
        color: #B0B8C1 !important;
    }
    
    /* Selectbox - Dark */
    .stSelectbox label {
        color: #FFFFFF !important;
    }
    
    /* Radio - Dark */
    .stRadio label {
        color: #FFFFFF !important;
    }
    
    .stRadio > div {
        color: #FFFFFF !important;
    }
    
    /* Text elements */
    p, span, div {
        color: #E2E8F0;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #FFFFFF !important;
    }
    
    /* Strong/Bold text */
    strong, b {
        color: #FFFFFF;
    }
    
    /* Links */
    a {
        color: #60a5fa;
    }
    
    /* Info/Help text */
    .stTooltipIcon {
        color: #B0B8C1;
    }
    
    /* Empty state */
    .empty-state {
        text-align: center;
        padding: 4rem 2rem;
        background: #1a1d24;
        border: 2px dashed #2d3139;
        border-radius: 16px;
        margin: 2rem 0;
    }
    
    .empty-state h3 {
        color: #FFFFFF;
        margin-bottom: 0.5rem;
    }
    
    .empty-state p {
        color: #B0B8C1;
    }
</style>
""", unsafe_allow_html=True)

# ========================================
# HEADER
# ========================================
col_logo, col_title = st.columns([0.08, 0.92])

with col_logo:
    st.markdown("<div style='font-size: 2.5rem; margin-top: -0.25rem; color: #3b82f6;'>◉</div>", unsafe_allow_html=True)

with col_title:
    st.markdown('<p class="main-header">Invoice Analysis</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Automated accounting validation for Chilean invoices</p>', unsafe_allow_html=True)

# ========================================
# CARGA DE DATOS
# ========================================
st.markdown('<p class="section-title">Upload Data</p>', unsafe_allow_html=True)

col1, col2 = st.columns([2.5, 1])

with col1:
    uploaded_file = st.file_uploader(
        "Drop your invoice file here",
        type=["csv", "xlsx"],
        help="Supported formats: CSV, Excel (.xlsx)",
        label_visibility="collapsed"
    )
    st.caption("Supported: CSV, Excel • Required columns: invoice_id, net_amount, tax, total")

with col2:
    use_sample = st.checkbox("Use sample data", help="Load example invoices to test the system")

# Cargar datos
df = None

if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
    except Exception as e:
        st.error(f"Could not read file: {e}")

elif use_sample:
    df = pd.read_csv("data/sample_invoices.csv")

# ========================================
# ANÁLISIS
# ========================================
if df is not None:
    
    # --- VALIDACIONES ---
    if 'net_amount' in df.columns and 'tax' in df.columns:
        df['iva_correcto'] = df.apply(
            lambda row: validate_tax(row['net_amount'], row['tax']), axis=1
        )
        df['iva_esperado'] = df['net_amount'] * 0.19
        df['diferencia_iva'] = df['tax'] - df['iva_esperado']
    else:
        df['iva_correcto'] = True
        df['iva_esperado'] = 0
        df['diferencia_iva'] = 0
    
    if all(col in df.columns for col in ['net_amount', 'tax', 'total']):
        df['total_esperado'] = df['net_amount'] + df['tax']
        df['total_correcto'] = abs(df['total'] - df['total_esperado']) < 1
        df['diferencia_total'] = df['total'] - df['total_esperado']
    else:
        df['total_correcto'] = True
        df['total_esperado'] = 0
        df['diferencia_total'] = 0
    
    if 'issue_date' in df.columns and 'period' in df.columns:
        df['issue_date'] = pd.to_datetime(df['issue_date'], errors='coerce')
        df['periodo_fecha'] = df['issue_date'].dt.to_period('M').astype(str)
        df['fecha_en_periodo'] = df.apply(
            lambda row: row['periodo_fecha'] == row['period'] if pd.notna(row['issue_date']) else False,
            axis=1
        )
    else:
        df['fecha_en_periodo'] = True
    
    df['es_valida'] = df['iva_correcto'] & df['total_correcto'] & df['fecha_en_periodo']
    df['estado'] = df['es_valida'].apply(lambda x: 'OK' if x else 'Error')
    
    def explicar_error(row):
        errores = []
        if not row.get('iva_correcto', True):
            diff = row.get('diferencia_iva', 0)
            errores.append(f"VAT mismatch (${abs(diff):,.0f})")
        if not row.get('total_correcto', True):
            errores.append("Total doesn't match")
        if not row.get('fecha_en_periodo', True):
            errores.append("Date outside period")
        return ' • '.join(errores) if errores else '—'
    
    df['motivo_error'] = df.apply(explicar_error, axis=1)
    
    # Métricas
    total = len(df)
    ok = int(df['es_valida'].sum())
    errors = total - ok
    pct_ok = (ok / total * 100) if total > 0 else 0
    pct_error = (errors / total * 100) if total > 0 else 0
    
    if pct_error == 0:
        risk = "low"
    elif pct_error <= 5:
        risk = "medium"
    else:
        risk = "high"
    
    # ========================================
    # RESUMEN EJECUTIVO
    # ========================================
    st.markdown('<p class="section-title">Summary</p>', unsafe_allow_html=True)
    
    c1, c2, c3, c4 = st.columns(4)
    
    with c1:
        st.metric("Total Invoices", f"{total:,}")
    
    with c2:
        st.metric("Valid", f"{ok:,}", f"{pct_ok:.0f}%")
    
    with c3:
        st.metric("Issues Found", f"{errors:,}", f"{pct_error:.1f}%" if errors > 0 else None, delta_color="inverse")
    
    with c4:
        if risk == "high":
            st.markdown('<div class="status-error">● High Risk</div>', unsafe_allow_html=True)
        elif risk == "medium":
            st.markdown('<div class="status-warning">● Medium Risk</div>', unsafe_allow_html=True)
        else:
            st.markdown('<div class="status-ok">● Low Risk</div>', unsafe_allow_html=True)
    
    # Mensaje contextual
    st.markdown("")
    if risk == "high":
        st.error("⚠️ Multiple inconsistencies detected. Review required before processing.")
    elif risk == "medium":
        st.warning("Some invoices need manual review.")
    else:
        st.success("All validations passed. Data looks good.")
    
    # ========================================
    # GRÁFICOS
    # ========================================
    st.markdown('<p class="section-title">Overview</p>', unsafe_allow_html=True)
    
    col_g1, col_g2 = st.columns([1, 1.5])
    
    with col_g1:
        # Donut chart minimalista
        fig = go.Figure(data=[go.Pie(
            values=[ok, errors],
            labels=['Valid', 'Issues'],
            hole=0.7,
            marker_colors=['#4ade80', '#f87171'],
            textinfo='none',
            hovertemplate='%{label}: %{value}<extra></extra>'
        )])
        
        fig.update_layout(
            showlegend=True,
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.15,
                xanchor="center",
                x=0.5,
                font=dict(size=12, color="#B0B8C1")
            ),
            margin=dict(t=20, b=40, l=20, r=20),
            height=220,
            paper_bgcolor='rgba(0,0,0,0)',
            plot_bgcolor='rgba(0,0,0,0)',
            annotations=[dict(
                text=f'{pct_ok:.0f}%',
                x=0.5, y=0.5,
                font_size=28,
                font_color='#FFFFFF',
                font_weight=600,
                showarrow=False
            )]
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col_g2:
        # Métricas financieras en cards
        if 'total' in df.columns:
            st.markdown("""
            <div class="metric-card">
                <div class="metric-label">Net Amount</div>
                <div class="metric-value">$""" + f"{df['net_amount'].sum():,.0f}" + """</div>
            </div>
            """, unsafe_allow_html=True)
            
            fc1, fc2 = st.columns(2)
            with fc1:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-label">VAT (19%)</div>
                    <div class="metric-value" style="font-size: 1.5rem;">$""" + f"{df['tax'].sum():,.0f}" + """</div>
                </div>
                """, unsafe_allow_html=True)
            with fc2:
                st.markdown("""
                <div class="metric-card">
                    <div class="metric-label">Total</div>
                    <div class="metric-value" style="font-size: 1.5rem;">$""" + f"{df['total'].sum():,.0f}" + """</div>
                </div>
                """, unsafe_allow_html=True)
    
    # ========================================
    # DETALLE
    # ========================================
    st.markdown('<p class="section-title">Details</p>', unsafe_allow_html=True)
    
    # Facturas con error
    if errors > 0:
        with st.expander(f"⚠️ {errors} invoice{'s' if errors > 1 else ''} with issues", expanded=True):
            df_error = df[~df['es_valida']][['invoice_id', 'provider', 'net_amount', 'tax', 'total', 'motivo_error']].copy()
            df_error.columns = ['Invoice ID', 'Provider', 'Net', 'VAT', 'Total', 'Issue']
            
            st.dataframe(
                df_error.style.format({
                    'Net': '${:,.0f}',
                    'VAT': '${:,.0f}',
                    'Total': '${:,.0f}'
                }),
                use_container_width=True,
                hide_index=True,
                height=min(len(df_error) * 40 + 40, 300)
            )
    
    # Explicación detallada
    if errors > 0:
        with st.expander("🔍 Understand specific issue"):
            factura_sel = st.selectbox(
                "Select invoice:",
                df[~df['es_valida']]['invoice_id'].tolist(),
                label_visibility="collapsed"
            )
            
            fac = df[df['invoice_id'] == factura_sel].iloc[0]
            
            col_i, col_e = st.columns([1, 2])
            
            with col_i:
                st.markdown("**Invoice Details**")
                st.caption(f"ID: {fac['invoice_id']}")
                st.caption(f"Provider: {fac.get('provider', '—')}")
                st.caption(f"Net: ${fac.get('net_amount', 0):,.0f}")
                st.caption(f"VAT: ${fac.get('tax', 0):,.0f}")
                st.caption(f"Total: ${fac.get('total', 0):,.0f}")
            
            with col_e:
                st.markdown("**Issue Explanation**")
                
                if not fac.get('iva_correcto', True):
                    st.error(f"""
                    **VAT Mismatch**  
                    Expected (19%): ${fac['iva_esperado']:,.0f}  
                    Declared: ${fac['tax']:,.0f}  
                    Difference: ${fac['diferencia_iva']:,.0f}
                    """)
                
                if not fac.get('total_correcto', True):
                    st.error(f"""
                    **Total Mismatch**  
                    Should be: ${fac['total_esperado']:,.0f}  
                    Declared: ${fac['total']:,.0f}
                    """)
                
                if not fac.get('fecha_en_periodo', True):
                    st.error(f"""
                    **Date Outside Period**  
                    Declared period: {fac.get('period', '—')}  
                    Actual date: {fac.get('periodo_fecha', '—')}
                    """)
    
    # Todas las facturas
    with st.expander("📋 All invoices"):
        filtro = st.radio("Filter:", ["All", "Valid only", "Issues only"], horizontal=True, label_visibility="collapsed")
        
        if filtro == "Valid only":
            df_mostrar = df[df['es_valida']]
        elif filtro == "Issues only":
            df_mostrar = df[~df['es_valida']]
        else:
            df_mostrar = df
        
        cols_mostrar = ['invoice_id', 'provider', 'net_amount', 'tax', 'total', 'estado']
        cols_disponibles = [c for c in cols_mostrar if c in df_mostrar.columns]
        
        st.dataframe(
            df_mostrar[cols_disponibles].rename(columns={
                'invoice_id': 'ID',
                'provider': 'Provider', 
                'net_amount': 'Net',
                'tax': 'VAT',
                'total': 'Total',
                'estado': 'Status'
            }),
            use_container_width=True,
            hide_index=True
        )
    
    # ========================================
    # DESCARGAS
    # ========================================
    st.markdown('<p class="section-title">Export</p>', unsafe_allow_html=True)
    
    col_d1, col_d2, col_d3 = st.columns([1, 1, 2])
    
    with col_d1:
        st.download_button(
            "📄 Full Report (CSV)",
            df.to_csv(index=False),
            "invoice_analysis.csv",
            "text/csv"
        )
    
    with col_d2:
        if errors > 0:
            st.download_button(
                "⚠️ Issues Only (CSV)",
                df[~df['es_valida']].to_csv(index=False),
                "invoices_with_issues.csv",
                "text/csv"
            )

else:
    # Estado vacío
    st.markdown("")
    st.markdown("")
    st.markdown("""
    <div style="
        text-align: center; 
        padding: 4rem 2rem; 
        background: #1a1d24; 
        border: 2px dashed #2d3139;
        border-radius: 16px;
        margin: 2rem 0;
    ">
        <div style="font-size: 3rem; margin-bottom: 1rem;">📄</div>
        <h3 style="color: #FFFFFF; margin-bottom: 0.5rem;">No data loaded</h3>
        <p style="color: #B0B8C1;">Upload an invoice file or use sample data to get started</p>
    </div>
    """, unsafe_allow_html=True)
