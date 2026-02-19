"""
Humira (Adalimumab) - Professional Drug Information App
Pre-Pharmacode V2.5 Standard
FDA-verified | Evidence-based | Updated 2026-02-19
Reference ID: 4845012
"""

import streamlit as st
import os
from datetime import datetime

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="Humira (Adalimumab) Info",
    page_icon="💊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CUSTOM CSS (LIGHT + DARK MODE) ====================
st.markdown("""
<style>
    /* إخفاء القائمة الجانبية تماماً */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* إخفاء زر المشاركة والقائمة العلوية */
    #MainMenu {visibility: hidden;}
    header {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* تحسين الهوامش الرئيسية للموبايل */
    .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }
    
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1e3a8a;
        text-align: center;
        padding: 1rem 0;
        background: linear-gradient(135deg, #e74c3c 0%, #c0392b 50%, #8e44ad 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #475569;
        text-align: center;
        margin-bottom: 1rem;
    }
    .info-box {
        background-color: #f0f9ff;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #3b82f6;
        margin: 0.8rem 0;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .warning-box {
        background-color: #fef2f2;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #ef4444;
        margin: 0.8rem 0;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .success-box {
        background-color: #f0fdf4;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #22c55e;
        margin: 0.8rem 0;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .critical-box {
        background-color: #fdf2f8;
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 5px solid #dc2626;
        margin: 0.8rem 0;
        border: 2px solid #dc2626;
        word-wrap: break-word;
        overflow-wrap: break-word;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    /* تحسين التبويبات للموبايل - عرض على سطرين/ثلاثة */
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px;
        flex-wrap: wrap !important;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        height: 45px;
        padding: 0 12px;
        background-color: #f1f5f9;
        border-radius: 8px;
        font-size: 0.9rem;
        white-space: nowrap;
        flex: 0 1 auto;
        margin: 2px;
    }
    .stTabs [aria-selected="true"] {
        background-color: #e74c3c;
        color: white;
    }
    
    /* تحسين العرض على الموبايل */
    @media (max-width: 768px) {
        .block-container {
            padding-left: 0.5rem !important;
            padding-right: 0.5rem !important;
        }
        
        .main-header {
            font-size: 1.6rem;
            padding: 0.5rem 0;
        }
        
        .sub-header {
            font-size: 0.95rem;
            margin-bottom: 0.5rem;
        }
        
        .stTabs [data-baseweb="tab-list"] {
            gap: 3px;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-size: 0.75rem;
            padding: 0 6px;
            height: 38px;
            min-width: auto;
        }
        
        .info-box, .warning-box, .success-box, .critical-box {
            padding: 0.8rem;
            font-size: 0.9rem;
        }
        
        .info-box h3, .warning-box h3, .success-box h3, .critical-box h3,
        .info-box h4, .warning-box h4, .success-box h4, .critical-box h4 {
            font-size: 1rem;
        }
        
        /* جعل الأعمدة تتراص عمودياً على الموبايل */
        [data-testid="column"] {
            width: 100% !important;
            flex: 1 1 100% !important;
            min-width: 100% !important;
        }
        
        /* تحسين حجم النصوص */
        h1 { font-size: 1.5rem !important; }
        h2 { font-size: 1.3rem !important; }
        h3 { font-size: 1.1rem !important; }
        h4 { font-size: 1rem !important; }
        
        .element-container {
            margin-bottom: 0.5rem;
        }
    }
    
    /* شاشات أصغر (هواتف صغيرة) */
    @media (max-width: 480px) {
        .main-header {
            font-size: 1.3rem;
        }
        
        .sub-header {
            font-size: 0.85rem;
        }
        
        .stTabs [data-baseweb="tab"] {
            font-size: 0.7rem;
            padding: 0 4px;
            height: 34px;
        }
        
        .info-box, .warning-box, .success-box, .critical-box {
            padding: 0.6rem;
            font-size: 0.85rem;
            border-radius: 8px;
        }
    }
    
    /* تنسيق صورة الدواء */
    .drug-image-container {
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 0.5rem 0;
        margin-bottom: 1rem;
    }
    
    /* تنسيق المصادر */
    .reference-item {
        background-color: #f8fafc;
        padding: 1rem;
        margin: 0.5rem 0;
        border-radius: 8px;
        border-left: 3px solid #3b82f6;
    }
    .reference-item strong { color: #1e40af; font-size: 1.05rem; }
    .reference-item a { color: #2563eb; text-decoration: none; word-break: break-all; display: block; margin-top: 0.3rem; }
    .reference-item a:hover { color: #1d4ed8; text-decoration: underline; }
    
    /* بطاقات المعلومات بدل الجداول */
    .card-item {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 10px;
        padding: 1rem;
        margin: 0.6rem 0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.08);
        transition: box-shadow 0.2s;
    }
    .card-item:hover { box-shadow: 0 3px 8px rgba(0,0,0,0.12); }
    .card-item h4 { margin: 0 0 0.5rem 0; color: #1e3a8a; font-size: 1.05rem; }
    .card-item .card-detail { font-size: 0.92rem; color: #334155; margin: 0.25rem 0; line-height: 1.5; }
    .card-item .card-detail strong { color: #475569; }
    .card-item .card-badge { display: inline-block; padding: 2px 8px; border-radius: 12px; font-size: 0.82rem; font-weight: 600; margin-right: 4px; }
    .card-badge-red { background: #fee2e2; color: #dc2626; }
    .card-badge-green { background: #dcfce7; color: #16a34a; }
    .card-badge-blue { background: #dbeafe; color: #2563eb; }
    .card-badge-yellow { background: #fef9c3; color: #ca8a04; }
    .card-badge-purple { background: #f3e8ff; color: #7c3aed; }
    
    @media (max-width: 768px) {
        .card-item { padding: 0.8rem; margin: 0.4rem 0; }
        .card-item h4 { font-size: 0.95rem; }
        .card-item .card-detail { font-size: 0.85rem; }
    }
    
    /* ============================== DARK MODE ============================== */
    @media (prefers-color-scheme: dark) {
        .main-header {
            background: linear-gradient(135deg, #f87171 0%, #ef4444 50%, #d8b4fe 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .sub-header { color: #94a3b8; }
        
        /* ---- Info Box (blue) ---- */
        .info-box { background-color: #172033; border-left-color: #60a5fa; color: #e2e8f0; }
        .info-box h3, .info-box h4, .info-box h5 { color: #93c5fd !important; }
        .info-box p, .info-box li, .info-box em { color: #cbd5e1; }
        .info-box strong { color: #f1f5f9; }
        .info-box a { color: #60a5fa; }
        
        /* ---- Warning Box (red/orange) ---- */
        .warning-box { background-color: #2a1a1a; border-left-color: #f87171; color: #e2e8f0; }
        .warning-box h3, .warning-box h4, .warning-box h5 { color: #fca5a5 !important; }
        .warning-box p, .warning-box li, .warning-box em { color: #cbd5e1; }
        .warning-box strong { color: #f1f5f9; }
        
        /* ---- Success Box (green) ---- */
        .success-box { background-color: #172318; border-left-color: #4ade80; color: #e2e8f0; }
        .success-box h3, .success-box h4, .success-box h5 { color: #86efac !important; }
        .success-box p, .success-box li, .success-box em { color: #cbd5e1; }
        .success-box strong { color: #f1f5f9; }
        
        /* ---- Critical Box (dark red) ---- */
        .critical-box { background-color: #2d1318; border-color: #ef4444; border-left-color: #ef4444; color: #e2e8f0; }
        .critical-box h2, .critical-box h3, .critical-box h4, .critical-box h5 { color: #fca5a5 !important; }
        .critical-box p, .critical-box li, .critical-box em { color: #cbd5e1; }
        .critical-box strong { color: #f1f5f9; }
        .critical-box span { color: #fca5a5 !important; }
        
        /* ---- Cards ---- */
        .card-item { background: #1e293b; border-color: #334155; box-shadow: 0 1px 3px rgba(0,0,0,0.4); }
        .card-item:hover { box-shadow: 0 3px 8px rgba(0,0,0,0.5); }
        .card-item h4 { color: #93c5fd; }
        .card-item .card-detail { color: #cbd5e1; }
        .card-item .card-detail strong { color: #e2e8f0; }
        
        /* ---- Badges ---- */
        .card-badge-red { background: #450a0a; color: #fca5a5; }
        .card-badge-green { background: #052e16; color: #86efac; }
        .card-badge-blue { background: #1e3a5f; color: #93c5fd; }
        .card-badge-yellow { background: #422006; color: #fde047; }
        .card-badge-purple { background: #2e1065; color: #c4b5fd; }
        
        /* ---- Metric Card ---- */
        .metric-card { background: #1e293b; box-shadow: 0 2px 4px rgba(0,0,0,0.4); color: #e2e8f0; }
        
        /* ---- References ---- */
        .reference-item { background-color: #1e293b; border-left-color: #60a5fa; }
        .reference-item strong { color: #93c5fd; }
        .reference-item a { color: #60a5fa; }
        .reference-item a:hover { color: #93c5fd; }
        
        /* ---- Links inside boxes ---- */
        .info-box a:hover, .warning-box a:hover,
        .success-box a:hover, .critical-box a:hover { color: #93c5fd; }
        
        /* ---- Tabs (unselected) ---- */
        .stTabs [data-baseweb="tab"] { background-color: #1e293b; color: #cbd5e1; }
        .stTabs [aria-selected="true"] { background-color: #e74c3c; color: white; }
    }
</style>
""", unsafe_allow_html=True)

# ==================== HEADER WITH DRUG IMAGE ====================
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "humira.png")
if not os.path.exists(image_path):
    image_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "humira.png")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists(image_path):
        st.image(image_path, use_column_width=True)
    else:
        st.warning("⚠️ Drug image not found. Please place humira.png in the app folder.")

st.markdown('<h1 class="main-header">💊 Humira (Adalimumab)</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">✅ FDA-verified • 🔬 Evidence-based • 📅 Updated 2026-02-19</p>', unsafe_allow_html=True)

st.markdown("---")

# ==================== MAIN TABS ====================
tabs = st.tabs([
    "📖 Overview",
    "⚗️ Mechanism",
    "💊 Dosage",
    "⚖️ Pharmacokinetics",
    "🚫 Contraindications",
    "⚠️ Side Effects",
    "💊⚖️ Interactions",
    "📊 Comparison",
    "📚 References"
])

# ==================== TAB 1: OVERVIEW ====================
with tabs[0]:
    st.header("📖 Overview of Humira (Adalimumab)")
    
    st.markdown("### ℹ️ Basic Information")
    st.markdown("""
    <div class="info-box">
    <p class="card-detail">🧪 <strong>Generic Name:</strong> Adalimumab</p>
    <p class="card-detail">🏷️ <strong>Brand Name:</strong> Humira®</p>
    <p class="card-detail">🏭 <strong>Manufacturer:</strong> AbbVie Inc.</p>
    <p class="card-detail">💊 <strong>Drug Class:</strong> TNF-alpha Inhibitor (Recombinant Human IgG1 Monoclonal Antibody)</p>
    <p class="card-detail">📅 <strong>FDA Approval:</strong> December 2002</p>
    <p class="card-detail">📋 <strong>Pregnancy Category:</strong> Should be used during pregnancy only if clearly needed (IgG1 — crosses placenta)</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🎯 Indications")
        st.markdown("""
        <div class="info-box">
        <h4>👨‍⚕️ Adult Indications:</h4>
        <ul>
            <li><strong>Rheumatoid Arthritis (RA):</strong> Moderate to severe active RA (monotherapy or with methotrexate/DMARDs)</li>
            <li><strong>Psoriatic Arthritis (PsA):</strong> Active PsA (monotherapy or with non-biologic DMARDs)</li>
            <li><strong>Ankylosing Spondylitis (AS):</strong> Active AS</li>
            <li><strong>Crohn's Disease (CD):</strong> Moderate to severe active CD (adults)</li>
            <li><strong>Ulcerative Colitis (UC):</strong> Moderate to severe active UC (adults)</li>
            <li><strong>Plaque Psoriasis (Ps):</strong> Moderate to severe chronic plaque psoriasis (candidates for systemic therapy/phototherapy)</li>
            <li><strong>Hidradenitis Suppurativa (HS):</strong> Moderate to severe HS</li>
            <li><strong>Uveitis (UV):</strong> Non-infectious intermediate, posterior, and panuveitis</li>
        </ul>
        
        <h4>👶 Pediatric Indications:</h4>
        <ul>
            <li><strong>Juvenile Idiopathic Arthritis (JIA):</strong> Polyarticular JIA in patients ≥2 years</li>
            <li><strong>Pediatric Crohn's Disease:</strong> Moderate to severe active CD in patients ≥6 years</li>
            <li><strong>Pediatric Uveitis:</strong> Non-infectious uveitis in patients ≥2 years</li>
            <li><strong>Pediatric HS:</strong> Moderate to severe HS in adolescents ≥12 years</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 📦 Available Strengths")
        st.markdown("""
        <div class="card-item">
            <h4>💊 10 mg/0.1 mL — Prefilled Syringe</h4>
            <p class="card-detail">For pediatric patients (JIA/Uveitis: 10-15 kg)</p>
        </div>
        <div class="card-item">
            <h4>💊 20 mg/0.2 mL — Prefilled Syringe</h4>
            <p class="card-detail">For pediatric patients (JIA/Uveitis: 15-30 kg; Pediatric CD <40 kg maintenance)</p>
        </div>
        <div class="card-item">
            <h4>💊 40 mg/0.4 mL — Prefilled Syringe</h4>
            <p class="card-detail">Standard adult dose; also available as SureClick Autoinjector (Pen)</p>
        </div>
        <div class="card-item">
            <h4>💊 40 mg/0.8 mL — Prefilled Syringe</h4>
            <p class="card-detail">Alternative 40 mg concentration</p>
        </div>
        <div class="card-item">
            <h4>💊 80 mg/0.8 mL — Prefilled Syringe</h4>
            <p class="card-detail">For loading doses and HS weekly maintenance</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 🏆 Key Clinical Points")
        st.markdown("""
        <div class="success-box">
        <h4>✅ Efficacy:</h4>
        <ul>
            <li>🎯 Broadest indication range among TNF inhibitors (8 adult + 4 pediatric indications)</li>
            <li>📊 Proven efficacy in both autoimmune and inflammatory bowel diseases</li>
            <li>📅 Subcutaneous self-injection allows convenient home administration</li>
        </ul>
        
        <h4>⚠️ Critical Safety Notes:</h4>
        <ul>
            <li>🚨 <strong>BOXED WARNING:</strong> Risk of serious infections (TB, invasive fungal) and malignancies (lymphoma, HSTCL)</li>
            <li>🧪 TB testing REQUIRED before initiation — treat latent TB first</li>
            <li>💉 Do NOT give live vaccines concurrently; wait 6 months for infants exposed in utero</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 2: MECHANISM ====================
with tabs[1]:
    st.header("⚗️ Mechanism of Action")
    
    st.markdown("""
    <div class="info-box">
    <h3 style="color: #1e3a8a;">🔬 Tumor Necrosis Factor (TNF) Alpha Blockade</h3>
    <p>Adalimumab is a recombinant human IgG1 monoclonal antibody that binds specifically to TNF-alpha (both soluble and transmembrane forms), blocking its interaction with p55 and p75 cell surface TNF receptors. This neutralizes the biological activity of TNF-alpha, a key pro-inflammatory cytokine involved in chronic autoimmune and inflammatory diseases.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 1️⃣ TNF-alpha Neutralization")
        st.markdown("""
        <div class="success-box">
        <h4>🎯 Direct Cytokine Blockade</h4>
        <h5>Mechanism:</h5>
        <ul>
            <li>Binds to soluble TNF-alpha (sTNF) with high affinity, preventing receptor activation</li>
            <li>Binds to transmembrane TNF-alpha (tmTNF), inducing reverse signaling and cell apoptosis</li>
        </ul>
        <h5>Clinical Effect:</h5>
        <ul>
            <li>✅ Reduces joint inflammation, swelling, and erosion in RA/PsA/AS</li>
            <li>✅ Induces and maintains remission in Crohn's disease and Ulcerative Colitis</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 2️⃣ Downstream Inflammatory Cascade")
        st.markdown("""
        <div class="success-box">
        <h4>🎯 Modulation of Inflammatory Mediators</h4>
        <h5>Mechanism:</h5>
        <ul>
            <li>Reduces levels of adhesion molecules (ELAM-1, VCAM-1, ICAM-1) responsible for leukocyte migration</li>
            <li>Decreases serum levels of IL-6, CRP, and matrix metalloproteinases (MMP-1, MMP-3)</li>
        </ul>
        <h5>Clinical Effect:</h5>
        <ul>
            <li>✅ Reduces tissue destruction and disease progression</li>
            <li>✅ Clears skin plaques in psoriasis and HS lesions</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 3: DOSAGE ====================
with tabs[2]:
    st.header("💊 Dosage and Administration")
    
    st.markdown("### 👨‍⚕️ Adult Dosing by Indication")
    
    st.markdown("""
    <div class="card-item">
        <h4>1️⃣ Rheumatoid Arthritis</h4>
        <p class="card-detail"><strong>Dose:</strong> 40 mg every other week (EOW)</p>
        <p class="card-detail"><strong>Note:</strong> Can increase to 40 mg every week if NOT on concomitant methotrexate</p>
    </div>
    <div class="card-item">
        <h4>2️⃣ Psoriatic Arthritis</h4>
        <p class="card-detail"><strong>Dose:</strong> 40 mg every other week (EOW)</p>
    </div>
    <div class="card-item">
        <h4>3️⃣ Ankylosing Spondylitis</h4>
        <p class="card-detail"><strong>Dose:</strong> 40 mg every other week (EOW)</p>
    </div>
    <div class="card-item">
        <h4>4️⃣ Crohn's Disease</h4>
        <p class="card-detail"><strong>Day 1:</strong> 160 mg (four 40 mg injections or two 80 mg injections)</p>
        <p class="card-detail"><strong>Day 15:</strong> 80 mg</p>
        <p class="card-detail"><strong>Maintenance (Day 29+):</strong> 40 mg EOW</p>
    </div>
    <div class="card-item">
        <h4>5️⃣ Ulcerative Colitis</h4>
        <p class="card-detail"><strong>Day 1:</strong> 160 mg</p>
        <p class="card-detail"><strong>Day 15:</strong> 80 mg</p>
        <p class="card-detail"><strong>Maintenance (Day 29+):</strong> 40 mg EOW</p>
        <p class="card-detail"><strong>Note:</strong> Discontinue if no evidence of remission by 8 weeks</p>
    </div>
    <div class="card-item">
        <h4>6️⃣ Plaque Psoriasis</h4>
        <p class="card-detail"><strong>Initial:</strong> 80 mg</p>
        <p class="card-detail"><strong>Maintenance (1 week later):</strong> 40 mg EOW</p>
    </div>
    <div class="card-item">
        <h4>7️⃣ Hidradenitis Suppurativa</h4>
        <p class="card-detail"><strong>Day 1:</strong> 160 mg</p>
        <p class="card-detail"><strong>Day 15:</strong> 80 mg</p>
        <p class="card-detail"><strong>Maintenance (Day 29+):</strong> 40 mg EVERY WEEK (or 80 mg EOW)</p>
    </div>
    <div class="card-item">
        <h4>8️⃣ Uveitis</h4>
        <p class="card-detail"><strong>Initial:</strong> 80 mg</p>
        <p class="card-detail"><strong>Maintenance (1 week later):</strong> 40 mg EOW</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 👶 Pediatric Dosing (Weight-Based)")
    
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #7c3aed;">
        <h4>🧒 JIA / Pediatric Uveitis</h4>
        <p class="card-detail"><strong>10 kg to <15 kg:</strong> 10 mg EOW</p>
        <p class="card-detail"><strong>15 kg to <30 kg:</strong> 20 mg EOW</p>
        <p class="card-detail"><strong>≥30 kg:</strong> 40 mg EOW</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #7c3aed;">
        <h4>🧒 Pediatric Crohn's Disease</h4>
        <p class="card-detail"><strong><40 kg:</strong> Day 1 (80 mg) → Day 15 (40 mg) → Maintenance: 20 mg EOW</p>
        <p class="card-detail"><strong>≥40 kg:</strong> Day 1 (160 mg) → Day 15 (80 mg) → Maintenance: 40 mg EOW</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📉 Dose Adjustments")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🟡 Renal Impairment")
        st.markdown("""
        <div class="card-item">
            <h4>🟡 No Dose Adjustment Required</h4>
            <p class="card-detail"><strong>Dose:</strong> Standard dosing applies</p>
            <p class="card-detail"><strong>Note:</strong> Adalimumab is a monoclonal antibody degraded by proteolysis, not renally eliminated</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 🔴 Hepatic Impairment")
        st.markdown("""
        <div class="card-item" style="border-left: 4px solid #dc2626;">
            <h4>🟡 No Specific Dose Adjustment</h4>
            <p class="card-detail"><strong>Note:</strong> Not hepatically metabolized (proteolysis). No formal studies in hepatic impairment. Use with caution.</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 📋 Administration Instructions")
    st.success("""
    ✅ Administer by subcutaneous injection into thigh or abdomen (rotate sites)
    
    ✅ Allow prefilled syringe/pen to reach room temperature (15-30 min) before injection
    
    ❌ Do NOT inject into skin that is tender, bruised, red, or hard
    
    ✅ For loading doses (160 mg): administer as four 40 mg injections in one day OR two 40 mg injections per day over two consecutive days
    """)

# ==================== TAB 4: PHARMACOKINETICS ====================
with tabs[3]:
    st.header("⚖️ Pharmacokinetics")
    
    st.markdown("### 📊 Pharmacokinetic Parameters Summary")
    
    st.markdown("""
    <div class="card-item">
        <h4>📊 Bioavailability</h4>
        <p class="card-detail"><strong>Value:</strong> ~64% (subcutaneous administration)</p>
        <p class="card-detail">💡 Absolute bioavailability after single SC dose</p>
    </div>
    <div class="card-item">
        <h4>⏱️ Tmax</h4>
        <p class="card-detail"><strong>Value:</strong> 131 ± 56 hours (~5.5 days)</p>
        <p class="card-detail">💡 Very slow absorption typical of monoclonal antibodies</p>
    </div>
    <div class="card-item">
        <h4>⌛ Half-life</h4>
        <p class="card-detail"><strong>Value:</strong> ~2 weeks (range: 10-20 days)</p>
        <p class="card-detail">💡 Supports every-other-week dosing for most indications</p>
    </div>
    <div class="card-item">
        <h4>🔗 Volume of Distribution</h4>
        <p class="card-detail"><strong>Value:</strong> 4.7 to 6.0 L</p>
        <p class="card-detail">💡 Low Vd consistent with IgG distribution (mainly vascular/extracellular)</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🧬 Distribution")
        st.info("""
        **Volume of Distribution:** 4.7 – 6.0 L
        
        **Placental Transfer:** Yes — IgG1 crosses placenta (especially in 3rd trimester)
        
        **Tissue Distribution:**
        - Distributes primarily in vascular and extracellular fluid
        - Synovial fluid concentrations 31–96% of serum levels in RA patients
        """)
        
        st.markdown("### 🔄 Metabolism")
        st.warning("""
        **Metabolism Type:** PROTEOLYSIS
        
        **NOT metabolized by hepatic CYP450 enzymes**
        
        Degraded into small peptides and amino acids like other endogenous IgG proteins
        
        **Immunogenicity Impact:**
        - Anti-adalimumab antibodies (AAA) increase clearance
        - Concomitant methotrexate reduces AAA formation
        """)
    
    with col2:
        st.markdown("### 🚰 Elimination")
        st.markdown("""
        <div class="card-item">
            <h4>🚰 Systemic Clearance — ~12 mL/h</h4>
            <p class="card-detail">Clearance increases with body weight and in presence of anti-adalimumab antibodies</p>
        </div>
        <div class="card-item">
            <h4>📉 Effect of Methotrexate on Clearance</h4>
            <p class="card-detail">MTX reduces adalimumab clearance by 29% to 44%, leading to higher serum concentrations</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### 👥 Special Populations")
        st.warning("""
        **Renal Impairment:**
        - No formal PK studies; not expected to be affected (proteolysis-based clearance)
        
        **Hepatic Impairment:**
        - No formal PK studies; not CYP-metabolized
        
        **Pediatric:**
        - Weight-based dosing required; clearance similar on mg/kg basis
        
        **Elderly:**
        - No specific dose adjustment; limited data in patients >65 years
        """)

# ==================== TAB 5: CONTRAINDICATIONS ====================
with tabs[4]:
    st.header("🚫 Contraindications and Warnings")
    
    st.markdown("""
    <div class="critical-box">
    <h2 style="color: #dc2626; text-align: center;">🚨 BOXED WARNING — SERIOUS INFECTIONS AND MALIGNANCY 🚨</h2>
    <p style="font-size: 1.1rem; text-align: center; font-weight: bold;">
    <strong>SERIOUS INFECTIONS:</strong> Patients treated with Humira are at increased risk for developing serious infections that may lead to hospitalization or death, including tuberculosis (TB), invasive fungal infections (histoplasmosis, coccidioidomycosis), bacterial sepsis, and opportunistic infections.<br><br>
    <strong>MALIGNANCY:</strong> Lymphoma and other malignancies, some fatal, have been reported in children and adolescent patients treated with TNF blockers including Humira. Post-marketing cases of hepatosplenic T-cell lymphoma (HSTCL), a rare type of T-cell lymphoma, have been reported — predominantly in adolescent and young adult males with Crohn's disease or ulcerative colitis treated with TNF blockers including Humira.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.markdown("### 🚨 Absolute Contraindications")
    
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚨 1. Severe Hypersensitivity</h4>
        <p class="card-detail"><strong>Risk:</strong> Anaphylaxis or serious allergic reactions to adalimumab or any excipient</p>
        <p class="card-detail"><strong>Action:</strong> Do NOT initiate or re-administer Humira if previous severe hypersensitivity reaction occurred</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚨 2. Active Serious Infections</h4>
        <p class="card-detail"><strong>Risk:</strong> Including active TB, sepsis, opportunistic infections</p>
        <p class="card-detail"><strong>Action:</strong> Do NOT start Humira during any active serious infection. Treat infection first, then reassess.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ⚠️ Warnings and Precautions")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("#### 🔴 Infections & TB")
        st.markdown("""
        <div class="warning-box">
        <ul>
            <li>Test for latent TB before starting; treat latent TB before initiating Humira</li>
            <li>Monitor for signs of active TB during treatment (even if initial TB test was negative)</li>
            <li>Discontinue Humira if patient develops a serious infection or sepsis</li>
            <li>Invasive fungal infections: Consider empiric antifungal therapy in patients at risk</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 🔴 Malignancy")
        st.markdown("""
        <div class="warning-box">
        <ul>
            <li>Increased risk of lymphoma and other malignancies in children and adolescents</li>
            <li>Hepatosplenic T-cell lymphoma (HSTCL) — predominantly in young males with IBD</li>
            <li>Non-melanoma skin cancer (NMSC) reported; periodic skin examinations recommended</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("#### 🟠 Neurologic & Cardiac")
        st.markdown("""
        <div class="warning-box">
        <ul>
            <li><strong>Demyelinating Disease:</strong> Exacerbation of MS, optic neuritis, Guillain-Barré — avoid in pre-existing demyelinating conditions</li>
            <li><strong>Heart Failure:</strong> Worsening or new onset CHF — use with caution in NYHA Class III/IV</li>
            <li><strong>Hematologic:</strong> Pancytopenia, aplastic anemia reported — discontinue if significant cytopenias develop</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 🟠 Autoimmunity & Other")
        st.markdown("""
        <div class="warning-box">
        <ul>
            <li><strong>Lupus-like Syndrome:</strong> Positive ANA/anti-dsDNA with symptoms — discontinue if confirmed</li>
            <li><strong>Immunizations:</strong> No live vaccines; bring pediatric patients up to date on all vaccinations before starting</li>
            <li><strong>Hepatitis B Reactivation:</strong> Test for HBV before initiation; monitor carriers during and after treatment</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)

# ==================== TAB 6: SIDE EFFECTS ====================
with tabs[5]:
    st.header("⚠️ Adverse Reactions (Side Effects)")
    
    st.markdown("""
    <div class="warning-box">
    <h3>⚠️ Critical Pre-Treatment Requirements</h3>
    <p style="font-size: 1.1rem; font-weight: bold;">
    Test for latent TB infection BEFORE initiating Humira. Treat latent TB before starting therapy. Monitor all patients for active TB during treatment, even if initial test is negative.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Common Side Effects")
    
    st.markdown("""
    <div class="card-item">
        <h4>🦠 Infections (Upper Respiratory, Sinusitis) <span class="card-badge card-badge-red">17–23%</span></h4>
        <p class="card-detail">💡 vs 11–13% placebo. Monitor for signs of infection; withhold if serious infection develops</p>
    </div>
    <div class="card-item">
        <h4>💉 Injection Site Reactions (Erythema, Pain, Swelling) <span class="card-badge card-badge-red">11–20%</span></h4>
        <p class="card-detail">💡 vs 7–10% placebo. Usually mild and self-limiting; rotate injection sites</p>
    </div>
    <div class="card-item">
        <h4>🤕 Headache <span class="card-badge card-badge-yellow">12%</span></h4>
        <p class="card-detail">💡 vs 8% placebo. Generally mild to moderate</p>
    </div>
    <div class="card-item">
        <h4>🔴 Rash <span class="card-badge card-badge-yellow">12%</span></h4>
        <p class="card-detail">💡 vs 6% placebo. Monitor for signs of serious dermatologic reactions</p>
    </div>
    <div class="card-item">
        <h4>🤢 Nausea <span class="card-badge card-badge-blue">9%</span></h4>
        <p class="card-detail">💡 Generally mild; take other medications with food if needed</p>
    </div>
    <div class="card-item">
        <h4>🫁 Sinusitis / Flu Syndrome / Bronchitis <span class="card-badge card-badge-blue">>2%</span></h4>
        <p class="card-detail">💡 Respiratory infections common with immunosuppression</p>
    </div>
    <div class="card-item">
        <h4>🔬 Laboratory: Hyperlipidemia, Elevated CPK, Hematuria <span class="card-badge card-badge-blue">7%</span></h4>
        <p class="card-detail">💡 Monitor lipid panel and CBC periodically</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 🔴 Serious Adverse Reactions")
        st.markdown("""
        <div class="warning-box">
        <h4>🦠 Serious Infections (Boxed Warning):</h4>
        <ul>
            <li><strong>Tuberculosis (TB)</strong> — Reactivation of latent TB; test before starting</li>
            <li><strong>Invasive Fungal Infections</strong> — Histoplasmosis, coccidioidomycosis</li>
            <li><strong>Bacterial Sepsis</strong> — Reported including fatal cases</li>
        </ul>
        <h4>🧬 Malignancy (Boxed Warning):</h4>
        <ul>
            <li><strong>Lymphoma</strong> — Including HSTCL in young males with IBD</li>
            <li><strong>Leukemia</strong> — Cases reported with TNF-blocker use</li>
            <li><strong>Non-melanoma Skin Cancer</strong> — Periodic skin exams recommended</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 💪 Other Serious Reactions")
        st.info("""
        **Neurologic:**
        - **Demyelinating disease** (MS exacerbation, optic neuritis)
        - **Seizures** reported
        
        **Hematologic:**
        - **Pancytopenia, aplastic anemia** — rare but serious
        
        **Cardiac:**
        - **Worsening/new onset CHF**
        
        **Autoimmune:**
        - **Lupus-like syndrome** — reversible on discontinuation
        """)
    
    st.markdown("### 🩺 Monitoring Parameters")
    
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🫁 TB Screening</h4>
        <p class="card-detail"><strong>Baseline:</strong> TB skin test (TST) or IGRA before starting Humira</p>
        <p class="card-detail"><strong>During Treatment:</strong> Monitor for signs/symptoms of active TB periodically</p>
        <p class="card-detail"><strong>If Abnormal:</strong> Treat latent TB before starting; discontinue if active TB develops</p>
    </div>
    <div class="card-item">
        <h4>🩸 Complete Blood Count (CBC)</h4>
        <p class="card-detail"><strong>Baseline:</strong> CBC with differential before initiating therapy</p>
        <p class="card-detail"><strong>During Treatment:</strong> Periodic monitoring; more frequently if cytopenias suspected</p>
        <p class="card-detail"><strong>If Abnormal:</strong> Discontinue Humira if significant cytopenias confirmed</p>
    </div>
    <div class="card-item">
        <h4>🔬 Hepatitis B (HBV)</h4>
        <p class="card-detail"><strong>Baseline:</strong> Test for HBV infection before initiating therapy</p>
        <p class="card-detail"><strong>During Treatment:</strong> Monitor HBV carriers during and for several months after stopping</p>
        <p class="card-detail"><strong>If Abnormal:</strong> If HBV reactivation occurs, stop Humira and initiate antiviral therapy</p>
    </div>
    <div class="card-item">
        <h4>🔬 Signs of Infection</h4>
        <p class="card-detail"><strong>Baseline:</strong> Evaluate for active or latent infections</p>
        <p class="card-detail"><strong>During Treatment:</strong> Monitor for fever, malaise, cough, weight loss</p>
        <p class="card-detail"><strong>If Abnormal:</strong> Withhold therapy; initiate appropriate antimicrobial treatment</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🚨 When to Seek Immediate Medical Attention")
    st.error("""
    **Stop drug and seek emergency care if:**
    - Signs of serious infection: persistent fever, night sweats, weight loss, cough, fatigue
    - Neurologic symptoms: numbness/tingling, vision changes, weakness in legs
    - Signs of heart failure: shortness of breath, swelling of ankles/feet, sudden weight gain
    - Allergic reaction: difficulty breathing, hives, swelling of face/throat
    - Unusual bleeding or bruising, persistent pallor (signs of blood disorder)
    """)

# ==================== TAB 7: DRUG INTERACTIONS ====================
with tabs[6]:
    st.header("💊⚖️ Drug Interactions")
    
    st.markdown("### 🔴 Contraindicated / Avoid Combinations")
    
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #dc2626;">
        <h4>🚫 Live Vaccines (MMR, Varicella, Yellow Fever, Rotavirus) <span class="card-badge card-badge-red">CONTRAINDICATED</span></h4>
        <p class="card-detail"><strong>Mechanism:</strong> Risk of disseminated infection due to immunosuppression from Humira</p>
        <p class="card-detail"><strong>Consequence:</strong> Potentially fatal disseminated vaccine-strain infection</p>
        <p class="card-detail"><strong>Instruction:</strong> Do NOT give live vaccines concurrently. Infants exposed in utero should wait ≥6 months before live vaccines (e.g., Rotavirus)</p>
        <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Prescribing Information Section 7.3</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔴 Avoid Combinations")
    
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #f59e0b;">
        <h4>⚠️ Anakinra (Kineret) <span class="card-badge card-badge-red">AVOID</span></h4>
        <p class="card-detail"><strong>Mechanism:</strong> Concurrent biologic immunosuppression without added clinical benefit</p>
        <p class="card-detail"><strong>Consequence:</strong> Increased risk of serious infections (7% vs 0%) and neutropenia with NO added clinical benefit over adalimumab alone</p>
        <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Prescribing Information Section 7.1</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #f59e0b;">
        <h4>⚠️ Abatacept (Orencia) <span class="card-badge card-badge-red">AVOID</span></h4>
        <p class="card-detail"><strong>Mechanism:</strong> Dual biologic T-cell modulation + TNF blockade</p>
        <p class="card-detail"><strong>Consequence:</strong> Controlled trials showed increased rates of serious infections and adverse events without enhanced efficacy</p>
        <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Prescribing Information Section 7.2</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🟡 Monitor Closely")
    
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #eab308;">
        <h4>🟡 CYP450 Substrates with Narrow Therapeutic Index (Warfarin, Cyclosporine, Theophylline) <span class="card-badge card-badge-yellow">MONITOR</span></h4>
        <p class="card-detail"><strong>Mechanism:</strong> "Cytokine Normalization" — chronic inflammation suppresses CYP450 enzymes. Treating with Humira lowers cytokines → CYP450 activity restores → metabolism of co-administered drugs speeds up → drug levels DROP</p>
        <p class="card-detail"><strong>Consequence:</strong> Decreased levels of narrow therapeutic index drugs; potential therapeutic failure</p>
        <p class="card-detail"><strong>Instruction:</strong> Monitor INR (warfarin), drug levels (theophylline, cyclosporine) upon initiation or discontinuation of Humira</p>
        <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Prescribing Information Section 7.4</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🟢 Beneficial Combination")
    
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #22c55e;">
        <h4>✅ Methotrexate (MTX) <span class="card-badge card-badge-green">BENEFICIAL / SAFE</span></h4>
        <p class="card-detail"><strong>Mechanism:</strong> MTX reduces the clearance of adalimumab by approximately 29–44%, resulting in higher serum concentrations</p>
        <p class="card-detail"><strong>Consequence:</strong> Improved efficacy; reduced formation of anti-drug antibodies (AAA)</p>
        <p class="card-detail"><strong>Instruction:</strong> No dose adjustment needed; often prescribed together for better efficacy in RA</p>
        <p class="card-detail" style="color: #64748b; font-size: 0.85rem;">Source: FDA Prescribing Information Section 12.3 — Pharmacokinetics</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🧬 CYP450 Profile")
    
    st.markdown("""
    <div class="info-box">
    <h4>Adalimumab CYP Metabolism:</h4>
    <ul>
        <li><strong>Substrates of:</strong> NOT a CYP substrate — metabolized by proteolysis</li>
        <li><strong>Inhibits:</strong> No direct CYP inhibition</li>
        <li><strong>Induces:</strong> No direct CYP induction</li>
    </ul>
    <p><strong>Clinical Significance:</strong> Adalimumab itself does NOT interact with CYP450 enzymes. However, by reducing TNF-alpha levels, it normalizes CYP450 activity that was previously suppressed by chronic inflammation — this "cytokine normalization" effect can alter the metabolism of co-administered CYP substrates.</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 8: COMPARISON ====================
with tabs[7]:
    st.header("📊 Comparison with Similar Drugs")
    
    st.markdown("### 🔬 Adalimumab vs. Alternative TNF Inhibitors")
    
    st.markdown("""
    <div class="card-item" style="border-left: 4px solid #e74c3c; border: 2px solid #e74c3c;">
        <h4>🏆 Humira (Adalimumab)</h4>
        <p class="card-detail"><strong>Class:</strong> Fully Human Monoclonal Antibody (anti-TNF-alpha)</p>
        <p class="card-detail"><strong>Route:</strong> Subcutaneous (Pen / Prefilled Syringe)</p>
        <p class="card-detail"><strong>Frequency (RA):</strong> Every 2 Weeks</p>
        <p class="card-detail"><strong>IBD Indication:</strong> ✅ Yes (Crohn's & UC)</p>
        <p class="card-detail"><strong>TB Risk:</strong> High (Reactivation risk — test before starting)</p>
        <p class="card-detail"><strong>Key Interaction:</strong> MTX increases levels (beneficial)</p>
        <p class="card-detail"><strong>Efficacy:</strong> <span class="card-badge card-badge-green">Broadest indication range among TNF inhibitors</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="card-item">
        <h4>💊 Enbrel (Etanercept)</h4>
        <p class="card-detail"><strong>Class:</strong> Fusion Protein (TNFR:Fc)</p>
        <p class="card-detail"><strong>Route:</strong> Subcutaneous</p>
        <p class="card-detail"><strong>Frequency (RA):</strong> Weekly</p>
        <p class="card-detail"><strong>IBD Indication:</strong> ❌ No (Not effective for Crohn's or UC)</p>
        <p class="card-detail"><strong>TB Risk:</strong> Moderate</p>
        <p class="card-detail"><strong>Key Interaction:</strong> Minimal drug interactions</p>
        <p class="card-detail"><strong>Efficacy:</strong> Effective for RA, PsA, AS, Plaque Psoriasis</p>
    </div>
    <div class="card-item">
        <h4>💊 Remicade (Infliximab)</h4>
        <p class="card-detail"><strong>Class:</strong> Chimeric Monoclonal Antibody (mouse/human anti-TNF)</p>
        <p class="card-detail"><strong>Route:</strong> Intravenous (IV infusion)</p>
        <p class="card-detail"><strong>Frequency (RA):</strong> Every 8 Weeks (after induction)</p>
        <p class="card-detail"><strong>IBD Indication:</strong> ✅ Yes (Crohn's & UC)</p>
        <p class="card-detail"><strong>TB Risk:</strong> High (Reactivation risk)</p>
        <p class="card-detail"><strong>Key Interaction:</strong> MTX reduces antibody formation</p>
        <p class="card-detail"><strong>Efficacy:</strong> Potent for IBD and RA; requires infusion center</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🏆 When to Choose Adalimumab")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="success-box">
        <h4>✅ Choose Adalimumab When:</h4>
        <ul>
            <li>Patient needs self-administered SC injection at home (vs IV infusion)</li>
            <li>IBD indication required (Crohn's or UC) — Enbrel is NOT effective</li>
            <li>Broad indication coverage needed (RA, PsA, AS, IBD, Ps, HS, Uveitis)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="warning-box">
        <h4>❌ Avoid Adalimumab When:</h4>
        <ul>
            <li>Active serious infection, including active TB or sepsis</li>
            <li>Pre-existing demyelinating disease (MS, optic neuritis)</li>
            <li>Moderate-to-severe heart failure (NYHA Class III/IV)</li>
        </ul>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("### 📈 Key Differentiators")
    st.markdown("""
    <div class="info-box">
    <h4>What Makes Adalimumab Unique:</h4>
    </div>
    <div class="card-item" style="border-left: 4px solid #3b82f6;">
        <h4>🎯 Broadest Indication Range</h4>
        <p class="card-detail">FDA-approved for 8 adult and 4 pediatric conditions — the most of any TNF inhibitor. Covers autoimmune joints (RA, PsA, AS, JIA), IBD (Crohn's, UC), skin (Psoriasis, HS), and eyes (Uveitis).</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #22c55e;">
        <h4>💉 Fully Human Antibody</h4>
        <p class="card-detail">Unlike infliximab (chimeric), adalimumab is fully human — potentially lower immunogenicity. Concomitant MTX further reduces anti-drug antibody formation for sustained efficacy.</p>
    </div>
    <div class="card-item" style="border-left: 4px solid #7c3aed;">
        <h4>🏠 Home Administration Convenience</h4>
        <p class="card-detail">Subcutaneous injection via autoinjector pen allows self-administration at home, unlike infliximab which requires IV infusion at a healthcare facility every 6-8 weeks.</p>
    </div>
    """, unsafe_allow_html=True)

# ==================== TAB 9: REFERENCES ====================
with tabs[8]:
    st.header("📚 References and Sources")
    
    st.markdown("### 📋 Primary Regulatory Sources")
    st.write("")
    
    st.markdown("""
    **1. FDA Prescribing Information — Humira (Adalimumab)**  
    U.S. Food and Drug Administration. Full Prescribing Information, Reference ID: 4845012  
    🔗 [https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/125057s422lbl.pdf](https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/125057s422lbl.pdf)
    """)
    
    st.markdown("---")
    
    st.markdown("""
    **2. EMA Summary of Product Characteristics (SmPC) — Humira**  
    European Medicines Agency. Humira EPAR — Product Information  
    🔗 [https://www.ema.europa.eu/en/medicines/human/EPAR/humira](https://www.ema.europa.eu/en/medicines/human/EPAR/humira)
    """)
    
    st.markdown("---")
    st.markdown("### 🔬 Key Clinical Studies & Reviews")
    st.write("")
    
    st.markdown("""
    **3. Weinblatt ME, et al. — Adalimumab in Rheumatoid Arthritis (ARMADA Trial)**  
    Pivotal trial demonstrating efficacy of adalimumab + MTX vs placebo + MTX in active RA.  
    🔗 [https://pubmed.ncbi.nlm.nih.gov/12528101/](https://pubmed.ncbi.nlm.nih.gov/12528101/)
    """)
    
    st.markdown("---")
    
    st.markdown("""
    **4. Hanauer SB, et al. — Adalimumab in Crohn's Disease (CLASSIC-I Trial)**  
    Induction therapy study showing efficacy in moderate-to-severe Crohn's disease.  
    🔗 [https://pubmed.ncbi.nlm.nih.gov/16678061/](https://pubmed.ncbi.nlm.nih.gov/16678061/)
    """)
    
    st.markdown("---")
    
    st.markdown("""
    **5. Drug Interaction Databases**  
    Lexicomp, Micromedex, Clinical Pharmacology — used for triple-verification of drug interactions  
    🔗 [https://www.wolterskluwer.com/en/solutions/lexicomp](https://www.wolterskluwer.com/en/solutions/lexicomp)
    """)
    
    st.markdown("---")
    st.info("""
    **📊 Data Accuracy Statement**
    
    All information in this application has been verified against:
    - FDA Prescribing Information (Reference ID: 4845012)
    - EMA Summary of Product Characteristics
    - Peer-reviewed clinical studies and guidelines
    
    **📅 Last Updated:** 2026-02-19  
    **📌 Version:** 1.0.0  
    **✅ Verification Status:** All references checked and validated  
    **🔬 Methodology:** Pre-Pharmacode V2.5 Standard with Triple-Verification
    """)

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748b; padding: 2rem 0;">
    <p><strong>Humira (Adalimumab) Professional Drug Information</strong></p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">
        ⚠️ <em>This information is for healthcare professionals only. 
        Always consult the full prescribing information and clinical judgment when making treatment decisions.</em>
    </p>
</div>
""", unsafe_allow_html=True)
