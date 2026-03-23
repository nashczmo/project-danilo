import streamlit as st
import os

if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write('[theme]\nbase="light"\nprimaryColor="#6366f1"\nbackgroundColor="#f8f9fa"\nsecondaryBackgroundColor="#ffffff"\ntextColor="#1d1d1f"\nfont="sans serif"\n')

st.set_page_config(
    page_title="DANILO Academic Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════
#  SESSION STATE
# ═══════════════════════════════════════════════════════════════════
if 'dark_mode'      not in st.session_state: st.session_state.dark_mode      = True
if 'current_view'   not in st.session_state: st.session_state.current_view   = 'dashboard'
if 'unlocked'       not in st.session_state: st.session_state.unlocked        = ['reading']

for _c in ['reading', 'math', 'science']:
    for _k, _d in [('quiz_started', False), ('quiz_submitted', False), ('quiz_score', 0)]:
        if f'{_c}_{_k}' not in st.session_state:
            st.session_state[f'{_c}_{_k}'] = _d

def navigate(view):    st.session_state.current_view = view
def toggle_theme():    st.session_state.dark_mode = not st.session_state.dark_mode

DM = st.session_state.dark_mode

# ═══════════════════════════════════════════════════════════════════
#  THEME CSS  (light vars = default; dark vars = injected override)
# ═══════════════════════════════════════════════════════════════════
LIGHT_VARS = """
:root {
    --bg:          #f5f5f7;
    --surface:     #ffffff;
    --surface2:    #fafafa;
    --surface3:    #f0f0f5;
    --border:      rgba(0,0,0,0.08);
    --border2:     rgba(0,0,0,0.13);
    --text:        #1d1d1f;
    --muted:       #6e6e73;
    --muted2:      #86868b;
    --shadow1: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
    --shadow2: 0 4px 16px rgba(0,0,0,0.08), 0 2px 6px rgba(0,0,0,0.04);
    --shadow3: 0 12px 36px rgba(0,0,0,0.11), 0 4px 12px rgba(0,0,0,0.05);
    --def-bg:      rgba(99,102,241,0.07);
    --def-border:  rgba(99,102,241,0.25);
    --key-bg:      rgba(168,85,247,0.07);
    --key-border:  rgba(168,85,247,0.22);
    --ex-bg:       rgba(16,185,129,0.07);
    --ex-border:   rgba(16,185,129,0.22);
    --tip-bg:      rgba(245,158,11,0.07);
    --tip-border:  rgba(245,158,11,0.22);
    --q-banner-bg: linear-gradient(135deg,#eff6ff,#dbeafe 80%);
    --q-banner-br: rgba(99,102,241,0.18);
}
"""

DARK_VARS = """
:root {
    --bg:          #09090f;
    --surface:     #111118;
    --surface2:    #16161f;
    --surface3:    #1c1c27;
    --border:      rgba(255,255,255,0.07);
    --border2:     rgba(255,255,255,0.13);
    --text:        #e2e8f0;
    --muted:       #64748b;
    --muted2:      #94a3b8;
    --shadow1: 0 1px 3px rgba(0,0,0,0.35);
    --shadow2: 0 4px 16px rgba(0,0,0,0.45);
    --shadow3: 0 12px 36px rgba(0,0,0,0.55);
    --def-bg:      rgba(99,102,241,0.13);
    --def-border:  rgba(99,102,241,0.32);
    --key-bg:      rgba(168,85,247,0.13);
    --key-border:  rgba(168,85,247,0.28);
    --ex-bg:       rgba(16,185,129,0.1);
    --ex-border:   rgba(16,185,129,0.28);
    --tip-bg:      rgba(245,158,11,0.1);
    --tip-border:  rgba(245,158,11,0.28);
    --q-banner-bg: linear-gradient(135deg,#1e1b4b,#1a1033 80%);
    --q-banner-br: rgba(99,102,241,0.22);
}
.stApp { background: var(--bg) !important; }
section[data-testid="stSidebar"] { background: var(--surface) !important; }
p, label, .stMarkdown, div[data-testid="stText"] { color: var(--muted2) !important; }
div[role="radiogroup"] label { color: var(--text) !important; }
div[data-testid="stForm"] { background: transparent !important; }
div[data-baseweb="radio"] > div { background: transparent !important; }
.stAlert > div { background: var(--surface2) !important; color: var(--text) !important; }
"""

THEME_VARS = DARK_VARS if DM else LIGHT_VARS

# ═══════════════════════════════════════════════════════════════════
#  BASE CSS  (components, animations – uses CSS vars)
# ═══════════════════════════════════════════════════════════════════
BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

html,body,[class*="css"],p,div,span,h1,h2,h3,h4,h5,
label,button,input,li,td,th,textarea {
    font-family:'Inter',-apple-system,BlinkMacSystemFont,sans-serif !important;
}
.block-container { padding:2.5rem 2.5rem 6rem !important; max-width:960px !important; }
#MainMenu,footer,header { visibility:hidden; }

/* ── Keyframes ──────────────────────────── */
@keyframes fadeIn  { from{opacity:0}              to{opacity:1} }
@keyframes fadeUp  { from{opacity:0;transform:translateY(14px)} to{opacity:1;transform:translateY(0)} }
@keyframes slideIn { from{opacity:0;transform:translateX(-8px)} to{opacity:1;transform:translateX(0)} }
@keyframes pop     { 0%{opacity:0;transform:scale(.95)} 100%{opacity:1;transform:scale(1)} }
@keyframes barGrow { from{width:0} to{width:var(--bw)} }
@keyframes pulse   { 0%,100%{opacity:.55} 50%{opacity:1} }
@keyframes shimmer {
    0%  { background-position:-400px 0 }
    100%{ background-position: 400px 0 }
}

/* ── Accent palette ─────────────────────── */
:root {
    --indigo:       #6366f1;
    --indigo-s:     rgba(99,102,241,.12);
    --indigo-g:     rgba(99,102,241,.28);
    --emerald:      #10b981;
    --emerald-s:    rgba(16,185,129,.11);
    --violet:       #a855f7;
    --violet-s:     rgba(168,85,247,.11);
    --amber:        #f59e0b;
    --amber-s:      rgba(245,158,11,.11);
    --red:          #ef4444;
    --green:        #22c55e;
}

/* ── SIDEBAR ────────────────────────────── */
section[data-testid="stSidebar"] {
    border-right:1px solid var(--border) !important;
    min-width:260px !important; max-width:260px !important;
}
section[data-testid="stSidebar"] > div   { padding:0 !important; }
section[data-testid="stSidebar"] .block-container { padding:0 !important; max-width:none !important; }
button[data-testid="collapsedControl"]   { display:none !important; }

.sb-brand {
    padding:1.4rem 1.25rem 1.1rem;
    border-bottom:1px solid var(--border);
    animation:fadeIn .35s ease both;
}
.sb-wordmark {
    font-size:1.3rem; font-weight:900; letter-spacing:-.04em;
    line-height:1.1; margin-bottom:.15rem; color:var(--text);
}
.sb-wordmark .grd {
    background:linear-gradient(120deg,var(--indigo) 0%,var(--violet) 100%);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.sb-sub { font-size:.68rem; color:var(--muted); font-weight:400; letter-spacing:.01em; }

.sb-sec  { padding:.9rem 1.25rem .25rem; font-size:.58rem; font-weight:700;
           letter-spacing:.14em; text-transform:uppercase; color:var(--muted); }

.sb-row  {
    display:flex; align-items:center; gap:.55rem;
    padding:.45rem .75rem; margin:.08rem .5rem;
    border-radius:9px; cursor:default;
    animation:slideIn .3s ease both;
}
.sb-active { background:var(--indigo-s); }
.sb-locked { opacity:.32; }

.sb-row-icon  { font-size:.88rem; width:20px; text-align:center; flex-shrink:0; }
.sb-row-label { font-size:.84rem; font-weight:500; color:var(--muted); flex-grow:1; letter-spacing:-.01em; }
.sb-active .sb-row-label { color:var(--indigo); font-weight:650; }

.sb-dot { width:6px; height:6px; border-radius:50%; flex-shrink:0; }
.d-done { background:var(--emerald); }
.d-live { background:var(--indigo); animation:pulse 2s ease infinite; }
.d-none { background:rgba(128,128,128,.25); }

/* Sidebar native buttons styled as nav rows */
section[data-testid="stSidebar"] div[data-testid="stButton"] > button {
    display:block !important; width:100% !important; text-align:left !important;
    background:transparent !important; border:none !important;
    border-radius:9px !important; padding:.45rem 1.25rem !important;
    margin:.08rem 0 !important; color:var(--muted) !important;
    font-size:.84rem !important; font-weight:500 !important;
    box-shadow:none !important; letter-spacing:-.01em !important;
    transition:background .15s,color .15s !important;
}
section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
    background:rgba(99,102,241,.07) !important;
    color:var(--text) !important; transform:none !important;
}

/* Progress footer */
.sb-footer {
    padding:1rem 1.25rem 1.2rem;
    border-top:1px solid var(--border);
    animation:fadeIn .5s ease .3s both;
}
.sb-phead { display:flex; justify-content:space-between; align-items:center; margin-bottom:.5rem; }
.sb-plabel{ font-size:.7rem; font-weight:600; color:var(--muted); }
.sb-ppct  { font-size:.7rem; font-weight:700; color:var(--indigo); }
.sb-track { height:4px; background:rgba(128,128,128,.15); border-radius:99px; overflow:hidden; }
.sb-fill  { height:4px; border-radius:99px;
            background:linear-gradient(90deg,var(--indigo),var(--violet));
            animation:barGrow .8s ease .4s both; }
.sb-done-label { font-size:.65rem; color:var(--muted); margin-top:.35rem; }

/* Theme toggle button */
.theme-btn-wrap div[data-testid="stButton"] > button {
    display:block !important; width:calc(100% - 2.5rem) !important;
    margin:.25rem 1.25rem !important; text-align:center !important;
    background:var(--surface2) !important; color:var(--muted) !important;
    border:1px solid var(--border) !important; border-radius:9px !important;
    font-size:.78rem !important; font-weight:600 !important;
    padding:.45rem 1rem !important; letter-spacing:.01em !important;
    transition:all .2s !important;
}
.theme-btn-wrap div[data-testid="stButton"] > button:hover {
    background:var(--indigo-s) !important; color:var(--indigo) !important;
    border-color:var(--indigo-g) !important; transform:none !important;
}

/* ── HERO ───────────────────────────────── */
.hero { padding:1.5rem 0 2.25rem; position:relative; animation:fadeUp .45s ease both; }
.hero::before {
    content:''; position:absolute; top:-80px; left:-100px;
    width:420px; height:420px; border-radius:50%;
    background:radial-gradient(circle,rgba(99,102,241,.07) 0%,transparent 60%);
    pointer-events:none; z-index:0;
}
.hero-eye  {
    font-size:.67rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase;
    color:var(--indigo); margin-bottom:.55rem; display:flex; align-items:center;
    gap:.45rem; position:relative; z-index:1; animation:fadeUp .4s ease .05s both;
}
.hero-eye::before { content:''; width:16px; height:2px; background:var(--indigo);
                    border-radius:2px; display:inline-block; }
.hero-title {
    font-size:3rem; font-weight:900; letter-spacing:-.05em; line-height:1.02;
    color:var(--text); margin-bottom:.65rem; position:relative; z-index:1;
    animation:fadeUp .4s ease .09s both;
}
.hero-title .grd {
    background:linear-gradient(120deg,var(--indigo) 0%,var(--violet) 55%,#ec4899 100%);
    -webkit-background-clip:text; -webkit-text-fill-color:transparent; background-clip:text;
}
.hero-sub {
    font-size:.985rem; color:var(--muted); font-weight:400; line-height:1.65;
    max-width:460px; position:relative; z-index:1;
    animation:fadeUp .4s ease .13s both;
}

/* ── CLASS CARDS ────────────────────────── */
.cc {
    background:var(--surface); border:1px solid var(--border);
    border-radius:18px; padding:1.65rem; height:224px;
    display:flex; flex-direction:column; position:relative; overflow:hidden;
    box-shadow:var(--shadow1);
    transition:box-shadow .3s ease,transform .28s ease,border-color .2s;
    margin-bottom:.75rem;
}
.cc:not(.cc-locked):hover { box-shadow:var(--shadow3); transform:translateY(-5px); border-color:var(--border2); }
.cc-locked { opacity:.42; pointer-events:none; }
.cc::before { content:''; position:absolute; top:0;left:0;right:0; height:3px; border-radius:18px 18px 0 0; }
.cc-i::before { background:linear-gradient(90deg,var(--indigo),#818cf8); }
.cc-e::before { background:linear-gradient(90deg,var(--emerald),#6ee7b7); }
.cc-v::before { background:linear-gradient(90deg,var(--violet),#e879f9); }
.cc-a::before { background:linear-gradient(90deg,var(--amber),#fcd34d); }

.cc-ghost {
    position:absolute; bottom:-8px; right:6px;
    font-size:6rem; font-weight:900; letter-spacing:-.06em;
    color:var(--text); opacity:.025; pointer-events:none; line-height:1; user-select:none;
}
.cc-num {
    position:absolute; top:1.1rem; right:1.1rem;
    font-size:.6rem; font-weight:700; letter-spacing:.07em;
    color:var(--muted); background:var(--surface3); border:1px solid var(--border);
    border-radius:6px; padding:.15rem .45rem;
}
.cc-icon { width:40px; height:40px; border-radius:11px; display:flex; align-items:center;
           justify-content:center; font-size:1rem; margin-bottom:.8rem; flex-shrink:0; }
.ci-i  { background:var(--indigo-s); }
.ci-e  { background:var(--emerald-s); }
.ci-v  { background:var(--violet-s); }
.ci-a  { background:var(--amber-s); }

.cc-title { font-size:1rem;    font-weight:700; color:var(--text); letter-spacing:-.02em; margin-bottom:.28rem; }
.cc-sub   { font-size:.78rem;  font-weight:500; color:var(--muted); letter-spacing:.01em;
            text-transform:uppercase; margin-bottom:.25rem; }
.cc-desc  { font-size:.81rem;  color:var(--muted); line-height:1.5; flex-grow:1; }

.cc-tag {
    display:inline-flex; align-items:center; gap:.28rem;
    font-size:.68rem; font-weight:600; letter-spacing:.02em;
    padding:.18rem .52rem; border-radius:99px; width:fit-content; margin-top:.6rem;
}
.t-on  { background:rgba(34,197,94,.1);  color:#16a34a; border:1px solid rgba(34,197,94,.2); }
.t-off { background:var(--surface3);     color:var(--muted);  border:1px solid var(--border); }

/* Card stagger animations */
.cc-a1 { animation:pop .4s ease .06s both; }
.cc-a2 { animation:pop .4s ease .13s both; }
.cc-a3 { animation:pop .4s ease .20s both; }
.cc-a4 { animation:pop .4s ease .27s both; }

/* ── HOW-IT-WORKS ────────────────────────── */
.how {
    background:var(--surface); border:1px solid var(--border);
    border-radius:18px; padding:1.6rem; box-shadow:var(--shadow1);
    animation:pop .4s ease .32s both; position:relative; overflow:hidden;
}
.how::after {
    content:''; position:absolute; bottom:-40px; right:-40px;
    width:150px; height:150px; border-radius:50%;
    background:radial-gradient(circle,var(--indigo-s),transparent 70%); pointer-events:none;
}
.how-ttl { font-size:.6rem; font-weight:700; letter-spacing:.13em; text-transform:uppercase;
           color:var(--muted); margin-bottom:.9rem; }
.how-row { display:flex; align-items:flex-start; gap:.65rem; margin-bottom:.7rem; }
.how-row:last-child { margin-bottom:0; }
.how-n {
    font-size:.68rem; font-weight:700; min-width:22px; height:22px;
    border-radius:7px; display:flex; align-items:center; justify-content:center; flex-shrink:0;
}
.hn-i { background:var(--indigo-s);  color:var(--indigo); }
.hn-e { background:var(--emerald-s); color:var(--emerald); }
.hn-v { background:var(--violet-s);  color:var(--violet); }
.how-txt { font-size:.84rem; color:var(--muted); line-height:1.5; }
.how-txt strong { color:var(--text); font-weight:600; }

/* ── MAIN BUTTONS ────────────────────────── */
div[data-testid="stButton"] > button {
    font-family:'Inter',sans-serif !important; font-weight:600 !important;
    font-size:.875rem !important; letter-spacing:-.01em !important;
    border-radius:980px !important; padding:.58rem 1.4rem !important;
    background:var(--text) !important; color:var(--bg) !important;
    border:none !important; box-shadow:none !important;
    transition:all .2s ease !important;
}
div[data-testid="stButton"] > button:hover { opacity:.85 !important; transform:scale(1.025) !important; }
div[data-testid="stButton"] > button:disabled {
    background:var(--surface3) !important; color:var(--muted) !important;
    transform:none !important; opacity:.55 !important;
}
div[data-testid="stFormSubmitButton"] > button {
    font-family:'Inter',sans-serif !important;
    background:linear-gradient(135deg,var(--indigo),var(--violet)) !important;
    color:#fff !important; border:none !important; border-radius:980px !important;
    font-weight:700 !important; font-size:.9rem !important;
    padding:.65rem 2rem !important; letter-spacing:-.01em !important;
    box-shadow:0 4px 18px var(--indigo-g) !important;
    transition:all .2s ease !important;
}
div[data-testid="stFormSubmitButton"] > button:hover {
    transform:translateY(-2px) !important; box-shadow:0 8px 28px var(--indigo-g) !important;
}

/* ── CLASS PAGE HEADER ───────────────────── */
.cl-header { padding:1rem 0 1.75rem; animation:fadeUp .4s ease both; }
.cl-eye {
    font-size:.67rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase;
    margin-bottom:.45rem; display:flex; align-items:center; gap:.4rem;
}
.cl-eye-bar { width:14px; height:2px; border-radius:2px; display:inline-block; }
.cl-title   { font-size:2.6rem; font-weight:900; letter-spacing:-.05em; color:var(--text); line-height:1.04; }

/* ── QUARTER SECTIONS ────────────────────── */
.q-section { margin-bottom:2rem; }
.q-head {
    display:flex; align-items:center; gap:.75rem;
    margin-bottom:1.1rem; animation:fadeIn .4s ease both;
}
.q-num {
    font-size:.65rem; font-weight:800; letter-spacing:.06em;
    padding:.22rem .6rem; border-radius:7px; flex-shrink:0;
}
.qn-active { background:var(--indigo-s); color:var(--indigo); }
.qn-locked { background:var(--surface3); color:var(--muted); }
.q-title   { font-size:1.05rem; font-weight:700; color:var(--text); letter-spacing:-.02em; }
.q-line    { flex-grow:1; height:1px; background:var(--border); }
.q-badge {
    font-size:.62rem; font-weight:700; letter-spacing:.05em;
    padding:.18rem .52rem; border-radius:6px;
}
.qb-active { background:rgba(34,197,94,.1);  color:#16a34a; border:1px solid rgba(34,197,94,.2); }
.qb-locked { background:var(--surface3);     color:var(--muted);  border:1px solid var(--border); }

/* ── LESSON CARDS ────────────────────────── */
.lcard {
    background:var(--surface); border:1px solid var(--border);
    border-radius:14px; padding:1.6rem 1.8rem; margin-bottom:.6rem;
    box-shadow:var(--shadow1); position:relative; overflow:hidden;
    transition:box-shadow .2s,border-color .2s,transform .2s;
    animation:fadeUp .38s ease both;
}
.lcard:hover { box-shadow:var(--shadow2); transform:translateX(2px); border-color:var(--border2); }
.lcard::before { content:''; position:absolute; left:0;top:0;bottom:0; width:3px; border-radius:0 2px 2px 0; }
.lc-i::before { background:var(--indigo); }
.lc-e::before { background:var(--emerald); }
.lc-v::before { background:var(--violet); }
.lcard-a1 { animation-delay:.04s; }
.lcard-a2 { animation-delay:.10s; }
.lcard-a3 { animation-delay:.16s; }

.lcard-label   { font-size:.6rem;  font-weight:700; letter-spacing:.13em; text-transform:uppercase;
                 color:var(--muted); margin-bottom:.3rem; }
.lcard-heading { font-size:1.05rem; font-weight:700; color:var(--text);
                 letter-spacing:-.02em; margin-bottom:.65rem; }

/* ── CONTENT BLOCKS ──────────────────────── */
.blk {
    border-radius:10px; padding:1rem 1.15rem; margin:.55rem 0;
    border-left:3px solid; font-size:.875rem; line-height:1.72;
}
.blk-def  { background:var(--def-bg);  border-color:var(--indigo);  color:var(--text); }
.blk-key  { background:var(--key-bg);  border-color:var(--violet);  color:var(--text); }
.blk-ex   { background:var(--ex-bg);   border-color:var(--emerald); color:var(--text); }
.blk-tip  { background:var(--tip-bg);  border-color:var(--amber);   color:var(--text); }

.blk-label {
    font-size:.58rem; font-weight:800; letter-spacing:.13em; text-transform:uppercase;
    margin-bottom:.3rem; display:flex; align-items:center; gap:.35rem;
}
.blk-def .blk-label  { color:var(--indigo); }
.blk-key .blk-label  { color:var(--violet); }
.blk-ex  .blk-label  { color:var(--emerald); }
.blk-tip .blk-label  { color:var(--amber); }
.blk-body { color:var(--muted2); line-height:1.72; }
.blk-body strong { color:var(--text); font-weight:600; }
.blk-term { font-weight:700; color:var(--text); font-size:.92rem; margin-bottom:.18rem; }

/* ── LOCKED QUARTER ──────────────────────── */
.q-locked-card {
    background:var(--surface2); border:1px dashed var(--border2);
    border-radius:14px; padding:1.5rem 2rem;
    display:flex; align-items:center; gap:1rem;
    animation:fadeIn .4s ease both;
}
.qlc-icon { font-size:1.5rem; opacity:.4; }
.qlc-text { font-size:.88rem; color:var(--muted); }
.qlc-text strong { color:var(--muted2); font-weight:600; }
.qlc-badge {
    margin-left:auto; font-size:.65rem; font-weight:700; letter-spacing:.06em;
    background:var(--surface3); border:1px solid var(--border);
    color:var(--muted); padding:.2rem .55rem; border-radius:6px; white-space:nowrap;
}

/* ── ASSESSMENT BANNER ───────────────────── */
.asmnt-banner {
    background:var(--q-banner-bg); border:1px solid var(--q-banner-br);
    border-radius:16px; padding:1.65rem 2rem; margin-bottom:1.2rem;
    position:relative; overflow:hidden; animation:fadeUp .4s ease .1s both;
}
.asmnt-banner::after {
    content:'?'; position:absolute; right:1.5rem; top:50%; transform:translateY(-50%);
    font-size:7rem; font-weight:900; opacity:.06; line-height:1; pointer-events:none;
    color:var(--indigo);
}
.ab-tag   { font-size:.6rem; font-weight:700; letter-spacing:.14em; text-transform:uppercase;
            color:var(--indigo); margin-bottom:.28rem; }
.ab-title { font-size:1.45rem; font-weight:800; letter-spacing:-.03em; color:var(--text); margin-bottom:.2rem; }
.ab-sub   { font-size:.82rem; color:var(--muted); font-weight:500; }

div[role="radiogroup"] {
    background:var(--surface) !important; border:1px solid var(--border) !important;
    border-radius:12px !important; padding:1.25rem 1.65rem !important;
    margin-bottom:.5rem !important; box-shadow:var(--shadow1) !important;
    transition:border-color .15s,box-shadow .15s !important;
}
div[role="radiogroup"]:hover { border-color:var(--border2) !important; box-shadow:var(--shadow2) !important; }

/* ── RESULT CARD ─────────────────────────── */
.result { border-radius:16px; padding:1.85rem 2.1rem; margin-top:1.1rem;
          animation:pop .4s ease both; }
.r-pass { background:linear-gradient(135deg,rgba(34,197,94,.07),rgba(16,185,129,.05));
          border:1px solid rgba(34,197,94,.2); }
.r-fail { background:linear-gradient(135deg,rgba(239,68,68,.07),rgba(220,38,38,.04));
          border:1px solid rgba(239,68,68,.18); }
.r-tag  { font-size:.62rem; font-weight:700; letter-spacing:.13em; text-transform:uppercase; margin-bottom:.4rem; }
.rt-p { color:#16a34a; } .rt-f { color:#dc2626; }
.r-num  { font-size:3.8rem; font-weight:900; letter-spacing:-.06em; line-height:1; margin-bottom:.2rem; }
.rn-p { color:var(--green); } .rn-f { color:var(--red); }
.r-den  { font-size:1.4rem; color:var(--muted); font-weight:500; }
.r-msg  { font-size:.88rem; color:var(--muted); margin-top:.45rem; line-height:1.6; }

/* ── SEPARATOR ───────────────────────────── */
.sep { display:flex; align-items:center; gap:.65rem; margin:1.75rem 0 1.1rem;
       animation:fadeIn .4s ease .2s both; }
.sep-txt  { font-size:.62rem; font-weight:700; letter-spacing:.13em; text-transform:uppercase;
            color:var(--muted); white-space:nowrap; }
.sep-line { flex-grow:1; height:1px; background:var(--border); }

/* ── STAT CARDS ──────────────────────────── */
.stat {
    background:var(--surface); border:1px solid var(--border);
    border-radius:16px; padding:1.65rem 1.4rem; text-align:center;
    box-shadow:var(--shadow1); position:relative; overflow:hidden;
    transition:box-shadow .25s,transform .25s;
}
.stat:hover { box-shadow:var(--shadow3); transform:translateY(-3px); }
.stat::before { content:''; position:absolute; top:0;left:0;right:0; height:3px; }
.s-i::before  { background:linear-gradient(90deg,var(--indigo),#818cf8); }
.s-e::before  { background:linear-gradient(90deg,var(--emerald),#6ee7b7); }
.s-v::before  { background:linear-gradient(90deg,var(--violet),#e879f9); }
.stat-a1 { animation:pop .4s ease .06s both; }
.stat-a2 { animation:pop .4s ease .13s both; }
.stat-a3 { animation:pop .4s ease .20s both; }
.sv { font-size:2.9rem; font-weight:900; letter-spacing:-.055em; line-height:1; margin-bottom:.3rem; }
.sv-i { color:var(--indigo); } .sv-e { color:var(--emerald); } .sv-v { color:var(--violet); }
.sl { font-size:.65rem; font-weight:700; letter-spacing:.11em; text-transform:uppercase; color:var(--muted); }

.prog-box {
    background:var(--surface); border:1px solid var(--border); border-radius:14px;
    padding:1.4rem 1.8rem; box-shadow:var(--shadow1); margin-bottom:1.2rem;
    animation:fadeUp .4s ease .27s both;
}
.pb-head { display:flex; justify-content:space-between; align-items:center; margin-bottom:.65rem; }
.pb-t    { font-size:.88rem; font-weight:700; color:var(--text); letter-spacing:-.01em; }
.pb-s    { font-size:.76rem; color:var(--muted); }
.pb-track{ height:7px; background:rgba(128,128,128,.12); border-radius:99px; overflow:hidden; }
.pb-fill { height:7px; border-radius:99px;
           background:linear-gradient(90deg,var(--indigo),var(--violet));
           animation:barGrow .9s ease .4s both; }

.dtable { width:100%; border-collapse:collapse; background:var(--surface);
          border:1px solid var(--border); border-radius:14px; overflow:hidden;
          box-shadow:var(--shadow1); animation:fadeUp .4s ease .34s both; }
.dtable th { background:var(--surface2); padding:.75rem 1.4rem; font-size:.6rem;
             font-weight:700; letter-spacing:.11em; text-transform:uppercase;
             color:var(--muted); border-bottom:1px solid var(--border); text-align:left; }
.dtable td { padding:.95rem 1.4rem; border-bottom:1px solid var(--border);
             font-size:.88rem; color:var(--text); }
.dtable tr:last-child td { border-bottom:none; }
.dtable tr:hover td { background:rgba(99,102,241,.02); }

hr { border:none !important; border-top:1px solid var(--border) !important; margin:2rem 0 !important; }
p  { color:var(--muted) !important; line-height:1.7 !important; }
h1,h2,h3 { color:var(--text) !important; font-weight:800 !important; letter-spacing:-.03em !important; }
div[data-testid="stAlert"] { border-radius:12px !important; }
"""

st.markdown(f"<style>{THEME_VARS}{BASE_CSS}</style>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
#  CONTENT DATA
# ═══════════════════════════════════════════════════════════════════
QUIZZES = {
    'reading': [
        {"q":"What do we call the specific time and place where a story happens?",       "o":["The Plot","The Characters","The Setting","The Title"],                  "a":"The Setting"},
        {"q":"Where is the main idea of a paragraph usually located?",                   "o":["In the middle","At the very end","In the topic sentence","In the dictionary"],"a":"In the topic sentence"},
        {"q":"What are hints around a new word that help you understand its meaning?",   "o":["Context clues","Story settings","Hidden numbers","Spelling words"],    "a":"Context clues"},
        {"q":"Who are the people or animals that take part in a story?",                 "o":["The Authors","The Readers","The Characters","The Settings"],           "a":"The Characters"},
        {"q":"What is the sequence of events from beginning to end of a story called?",  "o":["The Plot","The Cover","The Vocabulary","The Conclusion"],              "a":"The Plot"},
    ],
    'math': [
        {"q":"What is the total sum when you combine 145 and 278?",                    "o":["423","413","433","323"],                                                               "a":"423"},
        {"q":"What is the perimeter of a square if one side measures 9 units?",        "o":["18 units","27 units","36 units","81 units"],                                           "a":"36 units"},
        {"q":"In the fraction 3/4, what does the number 4 represent?",                 "o":["The part we have","The total equal parts in the whole","The sum","The difference"],   "a":"The total equal parts in the whole"},
        {"q":"What is the product of 15 multiplied by 8?",                             "o":["100","110","120","130"],                                                               "a":"120"},
        {"q":"What is the mathematical term for a flat shape with straight sides?",    "o":["Circle","Sphere","Polygon","Line"],                                                   "a":"Polygon"},
    ],
    'science': [
        {"q":"What process changes liquid water into an invisible gas?",               "o":["Condensation","Evaporation","Precipitation","Freezing"],  "a":"Evaporation"},
        {"q":"What provides the main energy that powers the water cycle?",             "o":["The Moon","The Wind","The Sun","The Ocean"],              "a":"The Sun"},
        {"q":"What forms in the sky when water vapor cools and condenses?",            "o":["Raindrops","Clouds","Rivers","Groundwater"],              "a":"Clouds"},
        {"q":"Which of the following is an example of precipitation?",                "o":["Snow falling","A puddle drying","Water boiling","Ice melting"],"a":"Snow falling"},
        {"q":"Where does a large amount of water collect underground?",               "o":["Aquifer","Cloud","Atmosphere","Evaporator"],              "a":"Aquifer"},
    ],
}

# Lesson content blocks per class
# block types: text | def | key | ex | tip
LESSONS = {
    'reading': [
        {
            'label':'Lesson 1.1', 'title':'Elements of a Story',
            'blocks':[
                {'t':'text','body':'Every story is built on three essential foundations. Understanding these elements helps you analyze and enjoy any narrative you read.'},
                {'t':'def','term':'Setting','body':'The <strong>time and place</strong> where a story takes place. It establishes the world the characters inhabit — a medieval castle, a spaceship, a small town in the 1950s.'},
                {'t':'def','term':'Characters','body':'The <strong>people, animals, or creatures</strong> that take part in a story. The <em>protagonist</em> is the main character; the <em>antagonist</em> creates conflict.'},
                {'t':'def','term':'Plot','body':'The <strong>sequence of events</strong> from beginning to end. Most plots follow an arc: introduction → rising action → climax → falling action → resolution.'},
                {'t':'key','body':'<strong>Tip:</strong> When starting a new story, ask yourself — <em>Who</em> is here? <em>Where and when</em> are we? <em>What happens?</em> — to quickly identify all three elements.'},
            ]
        },
        {
            'label':'Lesson 1.2', 'title':'Finding the Main Idea',
            'blocks':[
                {'t':'text','body':'Every paragraph has one central point the author is trying to communicate. Finding it quickly is a foundational reading skill.'},
                {'t':'def','term':'Main Idea','body':'The <strong>primary point</strong> an author wants to communicate in a paragraph or passage. Everything else in the paragraph supports it.'},
                {'t':'def','term':'Topic Sentence','body':'Usually the <strong>first sentence</strong> of a paragraph. It introduces the main idea and tells the reader what the paragraph is about.'},
                {'t':'ex','body':'<strong>Example:</strong> "Dogs make excellent pets for families." — This topic sentence tells us the paragraph will explain <em>why</em> dogs are good family pets. Every sentence after it should support this claim.'},
                {'t':'tip','body':'<strong>Study Tip:</strong> If the main idea isn\'t in the first sentence, check the last sentence — authors sometimes place it there as a conclusion.'},
            ]
        },
        {
            'label':'Lesson 1.3', 'title':'Using Context Clues',
            'blocks':[
                {'t':'text','body':'Encountering an unfamiliar word while reading doesn\'t have to slow you down. The words and sentences around it often contain enough information to figure out its meaning.'},
                {'t':'def','term':'Context Clues','body':'Hints found in the <strong>surrounding words and sentences</strong> that help you infer the meaning of an unknown word without a dictionary.'},
                {'t':'ex','body':'<strong>Example:</strong> "The <em>ravenous</em> wolf hadn\'t eaten in three days and devoured the entire carcass." — The words <em>hadn\'t eaten</em> and <em>devoured</em> tell us ravenous means extremely hungry.'},
                {'t':'key','body':'<strong>Common clue types:</strong> Definitions ("X, which means..."), synonyms ("tired, or <em>fatigued</em>"), antonyms ("unlike the shy girl, she was <em>gregarious</em>"), and examples.'},
                {'t':'tip','body':'<strong>Strategy:</strong> Re-read the sentence, substitute a word you know, and check if it makes sense in context.'},
            ]
        },
    ],
    'math': [
        {
            'label':'Lesson 2.1', 'title':'Basic Operations',
            'blocks':[
                {'t':'text','body':'The four fundamental operations are the building blocks of all mathematics. Mastering them unlocks every more advanced topic.'},
                {'t':'def','term':'Addition','body':'<strong>Combining</strong> two or more numbers to find a total. Symbol: <strong>+</strong>. The result is called the <em>sum</em>. Example: 145 + 278 = 423'},
                {'t':'def','term':'Subtraction','body':'<strong>Finding the difference</strong> between two numbers by removing one from the other. Symbol: <strong>−</strong>. Example: 500 − 278 = 222'},
                {'t':'def','term':'Multiplication','body':'A <strong>faster way to add the same number repeatedly</strong>. Symbol: <strong>×</strong>. The result is the <em>product</em>. Example: 15 × 8 = 120'},
                {'t':'tip','body':'<strong>Shortcut:</strong> Memorizing multiplication tables up to 12×12 will dramatically speed up all your calculations.'},
            ]
        },
        {
            'label':'Lesson 2.2', 'title':'Understanding Fractions',
            'blocks':[
                {'t':'text','body':'Fractions let us express parts of a whole. They appear everywhere — in cooking recipes, measurements, and probability.'},
                {'t':'def','term':'Numerator','body':'The <strong>top number</strong> of a fraction. It tells you <em>how many parts you have</em>. In ¾, the numerator is 3.'},
                {'t':'def','term':'Denominator','body':'The <strong>bottom number</strong> of a fraction. It tells you <em>how many equal parts make up the whole</em>. In ¾, the denominator is 4. It <strong>can never be zero</strong>.'},
                {'t':'ex','body':'<strong>Visual Example:</strong> A pizza cut into 8 equal slices. If you eat 3 slices, you ate 3/8 of the pizza. The denominator (8) = total slices; numerator (3) = slices eaten.'},
                {'t':'key','body':'<strong>Equivalent fractions</strong> represent the same value: ½ = 2/4 = 4/8. You can simplify by dividing both numbers by their greatest common factor.'},
            ]
        },
        {
            'label':'Lesson 2.3', 'title':'Basic Geometry',
            'blocks':[
                {'t':'text','body':'Geometry is the branch of mathematics concerned with shapes, sizes, and the properties of figures. Even basic geometry has real-world applications everywhere.'},
                {'t':'def','term':'Polygon','body':'A <strong>flat, closed shape with straight sides</strong>. Named by the number of sides: triangle (3), quadrilateral (4), pentagon (5), hexagon (6).'},
                {'t':'def','term':'Perimeter','body':'The <strong>total distance around the outside</strong> of a shape. For a rectangle: P = 2(length + width). For a square with side 9: P = 4 × 9 = <strong>36 units</strong>.'},
                {'t':'ex','body':'<strong>Real world:</strong> A fence around a rectangular yard 20m × 15m requires: 2(20+15) = 70 metres of fencing material.'},
                {'t':'tip','body':'<strong>Remember:</strong> Perimeter = <em>distance around</em> (like walking the border). Area = <em>space inside</em> (like tiles on a floor).'},
            ]
        },
    ],
    'science': [
        {
            'label':'Lesson 3.1', 'title':'The Water Cycle',
            'blocks':[
                {'t':'text','body':'Earth\'s water has been cycling continuously for billions of years. The same water molecules that existed in ancient oceans may be in your glass today.'},
                {'t':'def','term':'Water Cycle','body':'The <strong>continuous movement of water</strong> through Earth\'s systems — oceans, atmosphere, land, and underground. Also called the <em>hydrological cycle</em>.'},
                {'t':'key','body':'Water can exist in three states: <strong>liquid</strong> (rivers, oceans), <strong>gas</strong> (water vapor, clouds), and <strong>solid</strong> (ice, snow). The water cycle involves all three.'},
                {'t':'tip','body':'<strong>Big picture:</strong> Earth\'s total water supply stays constant. It simply moves between different locations and changes state — it is never created or destroyed.'},
            ]
        },
        {
            'label':'Lesson 3.2', 'title':'Evaporation & Condensation',
            'blocks':[
                {'t':'text','body':'These two opposing processes are what lift water from the surface into the sky, where it forms clouds and eventually returns to Earth.'},
                {'t':'def','term':'Evaporation','body':'The process by which <strong>liquid water is converted to water vapor</strong> (gas) by the sun\'s energy. It occurs from oceans, lakes, rivers, and even puddles.'},
                {'t':'def','term':'Condensation','body':'The process by which <strong>water vapor cools and turns back into liquid droplets</strong>. This is what forms clouds — billions of tiny water droplets suspended in air.'},
                {'t':'ex','body':'<strong>Everyday example:</strong> A cold glass on a warm day gets wet on the outside — that\'s condensation. Water vapor in the air cools when it touches the cold glass and becomes liquid.'},
                {'t':'key','body':'The higher in the atmosphere water vapor rises, the cooler it gets. At a certain altitude (the <em>dew point</em>), condensation begins and clouds form.'},
            ]
        },
        {
            'label':'Lesson 3.3', 'title':'Precipitation & Collection',
            'blocks':[
                {'t':'text','body':'Once clouds accumulate enough water, gravity returns it to Earth\'s surface in various forms. This water then collects and begins the cycle again.'},
                {'t':'def','term':'Precipitation','body':'Any form of water that <strong>falls from clouds to Earth\'s surface</strong>. Types include rain, snow, sleet, and hail — determined by temperature.'},
                {'t':'def','term':'Aquifer','body':'An <strong>underground layer of rock or sediment</strong> that holds and transmits groundwater. Aquifers are a critical source of fresh drinking water worldwide.'},
                {'t':'ex','body':'<strong>Precipitation type depends on temperature:</strong> Rain (above 0°C all the way down), Snow (below 0°C), Sleet (rain that freezes mid-fall), Hail (updrafts freeze water into ice balls).'},
                {'t':'tip','body':'<strong>Remember the full cycle:</strong> Evaporation → Condensation → Precipitation → Collection → (repeat). Energy from the sun drives every step.'},
            ]
        },
    ],
}

CLASSES_META = {
    'reading': {
        'id':'reading','title':'Reading','sub':'Language Arts',
        'icon':'📖','acc':'#6366f1','cc_cls':'cc-i','ci_cls':'ci-i',
        'lc_cls':'lc-i','num':'01','next':'math',
        'q2_title':'Reading Comprehension','q3_title':'Literary Analysis',
    },
    'math': {
        'id':'math','title':'Mathematics','sub':'Quantitative Reasoning',
        'icon':'📐','acc':'#10b981','cc_cls':'cc-e','ci_cls':'ci-e',
        'lc_cls':'lc-e','num':'02','next':'science',
        'q2_title':'Advanced Operations','q3_title':'Problem Solving',
    },
    'science': {
        'id':'science','title':'Natural Sciences','sub':'Earth Science',
        'icon':'🌊','acc':'#a855f7','cc_cls':'cc-v','ci_cls':'ci-v',
        'lc_cls':'lc-v','num':'03','next':None,
        'q2_title':'Physical Science','q3_title':'Life Science',
    },
}

# ═══════════════════════════════════════════════════════════════════
#  BLOCK RENDERER
# ═══════════════════════════════════════════════════════════════════
def render_block(blk):
    t = blk['t']
    if t == 'text':
        st.markdown(f"<p style='font-size:.905rem;color:var(--muted2)!important;line-height:1.78;margin:.35rem 0 .55rem;'>{blk['body']}</p>", unsafe_allow_html=True)
    elif t == 'def':
        st.markdown(f"""
        <div class="blk blk-def">
            <div class="blk-label">📘 Definition</div>
            <div class="blk-term">{blk['term']}</div>
            <div class="blk-body">{blk['body']}</div>
        </div>""", unsafe_allow_html=True)
    elif t == 'key':
        st.markdown(f"""
        <div class="blk blk-key">
            <div class="blk-label">💡 Key Concept</div>
            <div class="blk-body">{blk['body']}</div>
        </div>""", unsafe_allow_html=True)
    elif t == 'ex':
        st.markdown(f"""
        <div class="blk blk-ex">
            <div class="blk-label">📝 Example</div>
            <div class="blk-body">{blk['body']}</div>
        </div>""", unsafe_allow_html=True)
    elif t == 'tip':
        st.markdown(f"""
        <div class="blk blk-tip">
            <div class="blk-label">✏️ Study Tip</div>
            <div class="blk-body">{blk['body']}</div>
        </div>""", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════
#  CLASS PAGE RENDERER  — must be before if/elif chain
# ═══════════════════════════════════════════════════════════════════
def render_class(cls_id):
    meta    = CLASSES_META[cls_id]
    lessons = LESSONS[cls_id]
    quiz    = QUIZZES[cls_id]
    acc     = meta['acc']
    lc_cls  = meta['lc_cls']
    next_cls = meta['next']

    # Back button
    st.button("← Back to Dashboard", key=f"back_{cls_id}", on_click=navigate, args=('dashboard',))
    st.markdown("<div style='height:.3rem'></div>", unsafe_allow_html=True)

    # Class header
    st.markdown(f"""
    <div class="cl-header">
        <div class="cl-eye" style="color:{acc};">
            <span class="cl-eye-bar" style="background:{acc};"></span>
            {meta['sub']} &nbsp;·&nbsp; Class {meta['num']}
        </div>
        <div class="cl-title">{meta['icon']} {meta['title']}</div>
    </div>
    """, unsafe_allow_html=True)

    # ── QUARTER 1 ──────────────────────────
    st.markdown(f"""
    <div class="q-head">
        <span class="q-num qn-active">Q1</span>
        <span class="q-title">Foundations of {meta['title']}</span>
        <span class="q-line"></span>
        <span class="q-badge qb-active">● Active</span>
    </div>
    """, unsafe_allow_html=True)

    anim_cls = ['lcard-a1', 'lcard-a2', 'lcard-a3']
    for i, lesson in enumerate(lessons):
        blocks_html = ""
        for blk in lesson['blocks']:
            t = blk['t']
            if t == 'text':
                blocks_html += f"<p style='font-size:.9rem;color:var(--muted2);line-height:1.78;margin:.35rem 0 .5rem;'>{blk['body']}</p>"
            elif t == 'def':
                blocks_html += f"<div class='blk blk-def'><div class='blk-label'>📘 Definition</div><div class='blk-term'>{blk['term']}</div><div class='blk-body'>{blk['body']}</div></div>"
            elif t == 'key':
                blocks_html += f"<div class='blk blk-key'><div class='blk-label'>💡 Key Concept</div><div class='blk-body'>{blk['body']}</div></div>"
            elif t == 'ex':
                blocks_html += f"<div class='blk blk-ex'><div class='blk-label'>📝 Example</div><div class='blk-body'>{blk['body']}</div></div>"
            elif t == 'tip':
                blocks_html += f"<div class='blk blk-tip'><div class='blk-label'>✏️ Study Tip</div><div class='blk-body'>{blk['body']}</div></div>"

        st.markdown(f"""
        <div class="lcard {lc_cls} {anim_cls[i]}">
            <div class="lcard-label">{lesson['label']}</div>
            <div class="lcard-heading">{lesson['title']}</div>
            {blocks_html}
        </div>
        """, unsafe_allow_html=True)

    # ── Assessment separator ──
    st.markdown("""
    <div class="sep">
        <span class="sep-txt">Q1 Assessment</span>
        <span class="sep-line"></span>
    </div>
    """, unsafe_allow_html=True)

    sk_started   = f'{cls_id}_quiz_started'
    sk_submitted = f'{cls_id}_quiz_submitted'
    sk_score     = f'{cls_id}_quiz_score'
    btn_start    = f'start_{cls_id}'
    btn_retry    = f'retry_{cls_id}'

    if not st.session_state[sk_started]:
        st.markdown("""
        <p style="text-align:center;font-size:.875rem;margin-bottom:.65rem!important;">
            Finished all three lessons? Take the Q1 assessment to advance.
        </p>
        """, unsafe_allow_html=True)
        c1, c2, c3 = st.columns([2, 1, 2])
        with c2:
            st.button("Begin Quiz →", key=btn_start, use_container_width=True)
        if st.session_state.get(btn_start):
            st.session_state[sk_started] = True
            st.rerun()

    if st.session_state[sk_started]:
        st.markdown(f"""
        <div class="asmnt-banner">
            <div class="ab-tag">Formative Evaluation · Quarter 1</div>
            <div class="ab-title">Knowledge Check</div>
            <div class="ab-sub">5 questions &nbsp;·&nbsp; Choose the best answer for each</div>
        </div>
        """, unsafe_allow_html=True)

        with st.form(key=f'form_{cls_id}', clear_on_submit=False):
            answers = []
            for i, q in enumerate(quiz):
                st.markdown(f"**{i+1}.&nbsp; {q['q']}**")
                a = st.radio("", q['o'], key=f"q_{cls_id}_{i}",
                             label_visibility="collapsed", index=None)
                answers.append(a)
                if i < len(quiz) - 1:
                    st.markdown("<div style='height:.1rem'></div>", unsafe_allow_html=True)
            st.markdown("<div style='height:.4rem'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Submit Answers")

        if submitted:
            if None in answers:
                st.error("Please answer all 5 questions before submitting.")
            else:
                score = sum(1 for i, q in enumerate(quiz) if answers[i] == q['a'])
                st.session_state[sk_score] = score
                st.session_state[sk_submitted] = True

        if st.session_state[sk_submitted]:
            sc     = st.session_state[sk_score]
            passed = sc >= 4
            rc  = "r-pass" if passed else "r-fail"
            rt  = "rt-p"   if passed else "rt-f"
            rn  = "rn-p"   if passed else "rn-f"
            tag = "✓ Competency Verified" if passed else "✗ Below Threshold"
            msg = ("Outstanding — the next class has been unlocked. Continue your journey." if passed
                   else "Review the lesson blocks above and try the assessment again.")

            st.markdown(f"""
            <div class="result {rc}">
                <div class="r-tag {rt}">{tag}</div>
                <div><span class="r-num {rn}">{sc}</span><span class="r-den"> / {len(quiz)}</span></div>
                <div class="r-msg">{msg}</div>
            </div>
            """, unsafe_allow_html=True)

            if passed and next_cls and next_cls not in st.session_state.unlocked:
                st.session_state.unlocked.append(next_cls)

            if not passed:
                st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns([2, 1, 2])
                with c2:
                    st.button("Retry Quiz", key=btn_retry, use_container_width=True)
                if st.session_state.get(btn_retry):
                    st.session_state[sk_submitted] = False
                    st.rerun()

    # ── Quarter 2 & 3 — locked ──
    st.markdown("<div style='height:.75rem'></div>", unsafe_allow_html=True)

    for q_num, q_title, q_release in [
        ('Q2', meta['q2_title'], 'Coming — 2nd Quarter'),
        ('Q3', meta['q3_title'], 'Coming — 3rd Quarter'),
    ]:
        st.markdown(f"""
        <div class="q-head">
            <span class="q-num qn-locked">{q_num}</span>
            <span class="q-title" style="color:var(--muted);">{q_title}</span>
            <span class="q-line"></span>
            <span class="q-badge qb-locked">Coming Soon</span>
        </div>
        <div class="q-locked-card" style="margin-bottom:1.25rem;">
            <span class="qlc-icon">🔒</span>
            <div class="qlc-text">
                <strong>{q_title}</strong><br>
                This quarter's modules are not yet available.
            </div>
            <span class="qlc-badge">{q_release}</span>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  SIDEBAR
# ═══════════════════════════════════════════════════════════════════
cur = st.session_state.current_view
unlocked = st.session_state.unlocked
done_count = sum([
    st.session_state.reading_quiz_submitted and st.session_state.reading_quiz_score >= 4,
    st.session_state.math_quiz_submitted    and st.session_state.math_quiz_score    >= 4,
    st.session_state.science_quiz_submitted and st.session_state.science_quiz_score >= 4,
])
pct = int(done_count / 3 * 100)

def dot_cls(cls_id):
    if st.session_state[f'{cls_id}_quiz_submitted'] and st.session_state[f'{cls_id}_quiz_score'] >= 4:
        return 'd-done'
    if cls_id in unlocked:
        return 'd-live'
    return 'd-none'

def sb_active(icon, label, dcls):
    st.markdown(f"""
    <div class="sb-row sb-active">
        <span class="sb-row-icon">{icon}</span>
        <span class="sb-row-label">{label}</span>
        <span class="sb-dot {dcls}"></span>
    </div>""", unsafe_allow_html=True)

def sb_locked(label):
    st.markdown(f"""
    <div class="sb-row sb-locked">
        <span class="sb-row-icon">🔒</span>
        <span class="sb-row-label">{label}</span>
        <span class="sb-dot d-none"></span>
    </div>""", unsafe_allow_html=True)

with st.sidebar:
    mode_icon = "☀️" if DM else "🌙"
    mode_lbl  = "Light Mode" if DM else "Dark Mode"

    st.markdown(f"""
    <div class="sb-brand">
        <div class="sb-wordmark"><span class="grd">DANILO</span></div>
        <div class="sb-sub">Academic Platform</div>
    </div>
    """, unsafe_allow_html=True)

    # Theme toggle
    st.markdown('<div class="theme-btn-wrap">', unsafe_allow_html=True)
    st.button(f"{mode_icon}  {mode_lbl}", key="theme_toggle",
              on_click=toggle_theme, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb-sec">Navigation</div>', unsafe_allow_html=True)
    if cur == 'dashboard':
        sb_active("⊞", "Dashboard", "d-live")
    else:
        st.button("⊞  Dashboard", key="nav_dash", on_click=navigate,
                  args=('dashboard',), use_container_width=True)

    st.markdown('<div class="sb-sec">Classes</div>', unsafe_allow_html=True)

    for cls_id, label, icon in [
        ('reading', 'Reading',          '📖'),
        ('math',    'Mathematics',       '📐'),
        ('science', 'Natural Sciences',  '🌊'),
    ]:
        view_key = f'class_{cls_id}'
        if cur == view_key:
            sb_active(icon, label, dot_cls(cls_id))
        elif cls_id in unlocked:
            st.button(f"{icon}  {label}", key=f"nav_{cls_id}", on_click=navigate,
                      args=(view_key,), use_container_width=True)
        else:
            sb_locked(label)

    st.markdown('<div class="sb-sec">Records</div>', unsafe_allow_html=True)
    if cur == 'profile':
        sb_active("📊", "Metrics", "d-none")
    else:
        st.button("📊  Metrics", key="nav_prof", on_click=navigate,
                  args=('profile',), use_container_width=True)

    # Progress footer
    st.markdown(f"""
    <div class="sb-footer">
        <div class="sb-phead">
            <span class="sb-plabel">Progress</span>
            <span class="sb-ppct">{pct}%</span>
        </div>
        <div class="sb-track">
            <div class="sb-fill" style="--bw:{pct}%; width:{pct}%;"></div>
        </div>
        <div class="sb-done-label">{done_count} of 3 classes completed</div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  DASHBOARD
# ═══════════════════════════════════════════════════════════════════
if st.session_state.current_view == 'dashboard':

    st.markdown("""
    <div class="hero">
        <div class="hero-eye">Academic Platform</div>
        <div class="hero-title">Learn. Test. <span class="grd">Advance.</span></div>
        <div class="hero-sub">
            Sequential classes unlock as you master each one.
            Complete Q1 of every class to progress through the full curriculum.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")

    class_order = [
        ('reading', 'col1', 'cc-a1'),
        ('math',    'col2', 'cc-a2'),
        ('science', 'col3', 'cc-a3'),
    ]
    cols = [col1, col2, col3]

    for i, (cls_id, _, anim) in enumerate(class_order):
        m = CLASSES_META[cls_id]
        locked  = cls_id not in unlocked
        tag_cls = "t-off" if locked else "t-on"
        tag_txt = f"🔒 Requires {'Reading' if cls_id=='math' else 'Mathematics' if cls_id=='science' else ''}" if locked else "● Unlocked"
        dim     = " cc-locked" if locked else ""

        with cols[i]:
            st.markdown(f"""
            <div class="cc {m['cc_cls']}{dim} {anim}">
                <span class="cc-num">{m['num']}</span>
                <span class="cc-ghost">{m['num']}</span>
                <div class="cc-icon {m['ci_cls']}">{m['icon']}</div>
                <div class="cc-sub">{m['sub']}</div>
                <div class="cc-title">{m['title']}</div>
                <div class="cc-desc">Quarter 1 · 3 Lessons · 1 Assessment</div>
                <div class="cc-tag {tag_cls}">{tag_txt}</div>
            </div>
            """, unsafe_allow_html=True)
            st.button("Open Class →", key=f"db_{cls_id}", on_click=navigate,
                      args=(f'class_{cls_id}',), disabled=locked, use_container_width=True)

    st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)
    col4, col5 = st.columns([1, 1.7], gap="medium")

    with col4:
        st.markdown(f"""
        <div class="cc cc-a cc-a4" style="height:auto;min-height:175px;">
            <span class="cc-num">Analytics</span>
            <div class="cc-icon ci-a">📊</div>
            <div class="cc-sub">Performance</div>
            <div class="cc-title">Academic Metrics</div>
            <div class="cc-desc">Scores, progress &amp; curriculum logs.</div>
            <div style="margin-top:.65rem;">
                <div style="display:flex;justify-content:space-between;
                            font-size:.68rem;font-weight:600;color:var(--muted);margin-bottom:.35rem;">
                    <span>Curriculum Progress</span><span>{pct}%</span>
                </div>
                <div class="pb-track"><div class="pb-fill" style="--bw:{pct}%;width:{pct}%;"></div></div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("View Metrics →", key="db_prof", on_click=navigate,
                  args=('profile',), use_container_width=True)

    with col5:
        st.markdown("""
        <div class="how">
            <div class="how-ttl">How it works</div>
            <div class="how-row">
                <div class="how-n hn-i">01</div>
                <div class="how-txt">
                    <strong>Open a Class</strong> — Work through all lessons in Quarter 1,
                    using the definition, key concept, and example blocks to guide you.
                </div>
            </div>
            <div class="how-row">
                <div class="how-n hn-e">02</div>
                <div class="how-txt">
                    <strong>Pass the Assessment</strong> — Score at least 4 out of 5
                    on the Q1 quiz to verify your competency.
                </div>
            </div>
            <div class="how-row">
                <div class="how-n hn-v">03</div>
                <div class="how-txt">
                    <strong>Unlock the Next Class</strong> — Completing each class
                    automatically opens the next subject in the curriculum.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  CLASS VIEWS
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'class_reading':
    render_class('reading')

elif st.session_state.current_view == 'class_math':
    render_class('math')

elif st.session_state.current_view == 'class_science':
    render_class('science')


# ═══════════════════════════════════════════════════════════════════
#  METRICS PAGE
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'profile':

    st.markdown("""
    <div style="padding:1rem 0 1.75rem; animation:fadeUp .4s ease both;">
        <div class="hero-eye">Performance Records</div>
        <div class="hero-title" style="font-size:2.45rem;">Academic Metrics</div>
    </div>
    """, unsafe_allow_html=True)

    sc_sum, sc_cnt = 0, 0
    for cid in ['reading', 'math', 'science']:
        if st.session_state[f'{cid}_quiz_submitted']:
            sc_sum += st.session_state[f'{cid}_quiz_score']; sc_cnt += 1
    avg_pct  = int(sc_sum / (sc_cnt * 5) * 100) if sc_cnt else 0
    prog_pct = int(done_count / 3 * 100)

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown(f"<div class='stat s-i stat-a1'><div class='sv sv-i'>{done_count}</div><div class='sl'>Classes Passed</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='stat s-e stat-a2'><div class='sv sv-e'>{avg_pct}%</div><div class='sl'>Mean Accuracy</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='stat s-v stat-a3'><div class='sv sv-v'>{prog_pct}%</div><div class='sl'>Curriculum Done</div></div>", unsafe_allow_html=True)

    st.markdown("<div style='height:1.1rem'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="prog-box">
        <div class="pb-head">
            <span class="pb-t">Overall Curriculum Progress</span>
            <span class="pb-s">{done_count} of 3 classes completed</span>
        </div>
        <div class="pb-track"><div class="pb-fill" style="--bw:{prog_pct}%;width:{prog_pct}%;"></div></div>
    </div>
    """, unsafe_allow_html=True)

    def cell(cid):
        sub  = st.session_state[f'{cid}_quiz_submitted']
        sc   = st.session_state[f'{cid}_quiz_score']
        lock = cid not in unlocked
        if lock: return '<span style="color:var(--muted);font-weight:500;">🔒 Locked</span>', "—"
        if sub and sc >= 4: return '<span style="color:#16a34a;font-weight:700;">✓ Verified</span>', f"{sc}/5"
        if sub:             return '<span style="color:#dc2626;font-weight:700;">✗ Retry</span>',    f"{sc}/5"
        return '<span style="color:#d97706;font-weight:600;">◷ In Progress</span>', "—"

    s1,d1 = cell('reading'); s2,d2 = cell('math'); s3,d3 = cell('science')

    st.markdown(f"""
    <table class="dtable">
        <thead><tr><th>#</th><th>Class</th><th>Quarter</th><th>Status</th><th>Score</th></tr></thead>
        <tbody>
            <tr>
                <td style="color:var(--muted);font-size:.72rem;font-weight:700;">01</td>
                <td style="font-weight:600;">📖 Reading</td>
                <td style="color:var(--muted);font-size:.82rem;">Q1 · Foundations</td>
                <td>{s1}</td>
                <td style="font-family:monospace;color:var(--muted2);letter-spacing:.05em;">{d1}</td>
            </tr>
            <tr>
                <td style="color:var(--muted);font-size:.72rem;font-weight:700;">02</td>
                <td style="font-weight:600;">📐 Mathematics</td>
                <td style="color:var(--muted);font-size:.82rem;">Q1 · Foundations</td>
                <td>{s2}</td>
                <td style="font-family:monospace;color:var(--muted2);letter-spacing:.05em;">{d2}</td>
            </tr>
            <tr>
                <td style="color:var(--muted);font-size:.72rem;font-weight:700;">03</td>
                <td style="font-weight:600;">🌊 Natural Sciences</td>
                <td style="color:var(--muted);font-size:.82rem;">Q1 · Foundations</td>
                <td>{s3}</td>
                <td style="font-family:monospace;color:var(--muted2);letter-spacing:.05em;">{d3}</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)
