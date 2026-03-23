import streamlit as st
import os

if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write(
        '[theme]\nbase="light"\nprimaryColor="#0071e3"\n'
        'backgroundColor="#f5f5f7"\nsecondaryBackgroundColor="#ffffff"\n'
        'textColor="#1d1d1f"\nfont="sans serif"\n'
    )

st.set_page_config(
    page_title="DANILO Academic Platform",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══════════════════════════════════════════════════════════════════
#  CSS — Linear × Apple × Notion
# ═══════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ── Variables ─────────────────────────── */
:root {
    --bg:           #f5f5f7;
    --surface:      #ffffff;
    --surface2:     #fafafa;
    --border:       rgba(0,0,0,0.08);
    --border2:      rgba(0,0,0,0.13);
    --text:         #1d1d1f;
    --muted:        #6e6e73;
    --muted2:       #86868b;
    --blue:         #0071e3;
    --blue-mid:     rgba(0,113,227,0.14);
    --blue-soft:    rgba(0,113,227,0.07);
    --green:        #34c759;
    --green-soft:   rgba(52,199,89,0.09);
    --purple:       #af52de;
    --purple-soft:  rgba(175,82,222,0.09);
    --amber:        #ff9f0a;
    --amber-soft:   rgba(255,159,10,0.09);
    --red:          #ff3b30;
    --sh1: 0 1px 3px rgba(0,0,0,0.05), 0 1px 2px rgba(0,0,0,0.03);
    --sh2: 0 4px 16px rgba(0,0,0,0.07), 0 2px 6px rgba(0,0,0,0.04);
    --sh3: 0 12px 36px rgba(0,0,0,0.1), 0 4px 12px rgba(0,0,0,0.05);
    --r:   16px;
    --r-sm:10px;
}

/* ── Global ────────────────────────────── */
html, body, [class*="css"],
p, div, span, h1, h2, h3, h4, h5,
label, button, input, li, td, th, textarea {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}
.stApp { background: var(--bg) !important; }
.block-container {
    padding: 2.75rem 2.5rem 6rem !important;
    max-width: 940px !important;
}
#MainMenu, footer, header { visibility: hidden; }

/* ── Keyframes ─────────────────────────── */
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(18px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes slideRight {
    from { opacity: 0; transform: translateX(-10px); }
    to   { opacity: 1; transform: translateX(0); }
}
@keyframes scalePop {
    0%   { transform: scale(0.94); opacity: 0; }
    100% { transform: scale(1);    opacity: 1; }
}
@keyframes barGrow {
    from { width: 0%; }
    to   { width: var(--bar-w); }
}
@keyframes glowPulse {
    0%, 100% { opacity: 0.6; }
    50%       { opacity: 1; }
}

/* ═══ SIDEBAR ══════════════════════════ */
section[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
    min-width: 258px !important;
    max-width: 258px !important;
}
section[data-testid="stSidebar"] > div { padding: 0 !important; }
section[data-testid="stSidebar"] .block-container {
    padding: 0 !important;
    max-width: none !important;
}
button[data-testid="collapsedControl"] { display: none !important; }

/* Sidebar brand */
.sb-brand {
    padding: 1.4rem 1.25rem 1.1rem;
    border-bottom: 1px solid var(--border);
    animation: fadeIn 0.4s ease both;
}
.sb-logo {
    font-size: 1.25rem;
    font-weight: 800;
    letter-spacing: -0.04em;
    color: var(--text);
    line-height: 1.1;
    margin-bottom: 0.15rem;
}
.sb-logo .grd {
    background: linear-gradient(120deg, var(--blue) 0%, var(--purple) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.sb-tagline {
    font-size: 0.7rem;
    color: var(--muted2);
    font-weight: 400;
    letter-spacing: 0.01em;
}

/* Sidebar section label */
.sb-section {
    padding: 1rem 1.25rem 0.3rem;
    font-size: 0.6rem;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--muted2);
}

/* Nav rows */
.nav-row {
    display: flex;
    align-items: center;
    gap: 0.55rem;
    padding: 0.5rem 0.75rem;
    margin: 0.1rem 0.5rem;
    border-radius: var(--r-sm);
    cursor: default;
    animation: slideRight 0.3s ease both;
}
.nav-active {
    background: var(--blue-soft);
}
.nav-locked {
    opacity: 0.38;
}
.nav-icon {
    font-size: 0.9rem;
    width: 20px;
    text-align: center;
    flex-shrink: 0;
}
.nav-label {
    font-size: 0.855rem;
    font-weight: 500;
    color: var(--muted);
    flex-grow: 1;
    letter-spacing: -0.01em;
}
.nav-active .nav-label {
    color: var(--blue);
    font-weight: 600;
}
.nav-dot {
    width: 7px; height: 7px;
    border-radius: 50%;
    flex-shrink: 0;
}
.dot-done   { background: var(--green); }
.dot-active { background: var(--blue); animation: glowPulse 2s ease infinite; }
.dot-none   { background: rgba(0,0,0,0.12); }

/* Sidebar buttons (styled as nav links) */
section[data-testid="stSidebar"] div[data-testid="stButton"] > button {
    display: flex !important;
    align-items: center !important;
    width: 100% !important;
    text-align: left !important;
    background: transparent !important;
    border: none !important;
    border-radius: var(--r-sm) !important;
    padding: 0.5rem 1.25rem !important;
    margin: 0.1rem 0 !important;
    color: var(--muted) !important;
    font-size: 0.855rem !important;
    font-weight: 500 !important;
    box-shadow: none !important;
    transition: background 0.15s, color 0.15s !important;
    letter-spacing: -0.01em !important;
}
section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
    background: rgba(0,0,0,0.04) !important;
    color: var(--text) !important;
    transform: none !important;
}

/* Sidebar progress */
.sb-progress {
    padding: 1.1rem 1.25rem;
    border-top: 1px solid var(--border);
    margin-top: 0.5rem;
    animation: fadeIn 0.5s ease 0.4s both;
}
.sb-prog-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.55rem;
}
.sb-prog-label {
    font-size: 0.72rem;
    font-weight: 600;
    color: var(--muted);
    letter-spacing: -0.01em;
}
.sb-prog-pct {
    font-size: 0.72rem;
    font-weight: 700;
    color: var(--blue);
}
.sb-track {
    height: 4px;
    background: rgba(0,0,0,0.07);
    border-radius: 99px;
    overflow: hidden;
}
.sb-fill {
    height: 4px;
    border-radius: 99px;
    background: linear-gradient(90deg, var(--blue), var(--purple));
    animation: barGrow 0.8s ease 0.5s both;
}
.sb-modules-done {
    font-size: 0.68rem;
    color: var(--muted2);
    margin-top: 0.4rem;
    font-weight: 400;
}

/* ═══ HERO ══════════════════════════════ */
.hero {
    padding: 1.5rem 0 2.5rem;
    position: relative;
    animation: fadeUp 0.5s ease both;
}
.hero::before {
    content: '';
    position: absolute;
    top: -80px; left: -120px;
    width: 460px; height: 460px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0,113,227,0.055) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
}
.hero::after {
    content: '';
    position: absolute;
    top: -40px; right: -80px;
    width: 340px; height: 340px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(175,82,222,0.045) 0%, transparent 60%);
    pointer-events: none;
    z-index: 0;
}
.hero-eyebrow {
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--blue);
    margin-bottom: 0.55rem;
    position: relative;
    z-index: 1;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    animation: fadeUp 0.5s ease 0.05s both;
}
.hero-eyebrow::before {
    content: '';
    width: 18px; height: 2px;
    background: var(--blue);
    border-radius: 2px;
    display: inline-block;
}
.hero-title {
    font-size: 3.1rem;
    font-weight: 800;
    letter-spacing: -0.045em;
    line-height: 1.05;
    color: var(--text);
    margin-bottom: 0.7rem;
    position: relative;
    z-index: 1;
    animation: fadeUp 0.5s ease 0.1s both;
}
.hero-title .grd {
    background: linear-gradient(120deg, var(--blue) 0%, #7b5ce7 60%, var(--purple) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-sub {
    font-size: 1rem;
    color: var(--muted);
    font-weight: 400;
    line-height: 1.65;
    max-width: 500px;
    position: relative;
    z-index: 1;
    animation: fadeUp 0.5s ease 0.15s both;
}

/* ═══ MODULE CARDS ══════════════════════ */
.mc {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r);
    padding: 1.65rem;
    height: 218px;
    display: flex;
    flex-direction: column;
    position: relative;
    overflow: hidden;
    box-shadow: var(--sh1);
    transition: box-shadow 0.3s ease, transform 0.3s ease, border-color 0.2s;
    margin-bottom: 0.75rem;
}
.mc:hover {
    box-shadow: var(--sh3);
    transform: translateY(-4px);
    border-color: rgba(0,0,0,0.13);
}
.mc.mc-locked {
    opacity: 0.5;
    pointer-events: none;
}
.mc.mc-locked:hover {
    transform: none;
    box-shadow: var(--sh1);
}
/* Top gradient stripe */
.mc::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    border-radius: var(--r) var(--r) 0 0;
}
.mc-blue::before   { background: linear-gradient(90deg, #0071e3, #38bdf8); }
.mc-green::before  { background: linear-gradient(90deg, #34c759, #86efac); }
.mc-purple::before { background: linear-gradient(90deg, #af52de, #e879f9); }
.mc-amber::before  { background: linear-gradient(90deg, #ff9f0a, #fcd34d); }
/* Ghost number watermark */
.mc-ghost {
    position: absolute;
    bottom: -10px; right: 8px;
    font-size: 6rem;
    font-weight: 900;
    letter-spacing: -0.06em;
    color: var(--text);
    opacity: 0.028;
    pointer-events: none;
    line-height: 1;
    user-select: none;
}
/* Card icon pill */
.mc-icon {
    width: 40px; height: 40px;
    border-radius: 11px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
    margin-bottom: 0.85rem;
    flex-shrink: 0;
}
.i-blue   { background: var(--blue-soft); }
.i-green  { background: var(--green-soft); }
.i-purple { background: var(--purple-soft); }
.i-amber  { background: var(--amber-soft); }
.mc-num {
    position: absolute;
    top: 1.15rem; right: 1.15rem;
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.06em;
    color: var(--muted2);
    background: rgba(0,0,0,0.04);
    border: 1px solid var(--border);
    border-radius: 6px;
    padding: 0.15rem 0.45rem;
}
.mc-title {
    font-size: 1rem;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.02em;
    margin-bottom: 0.3rem;
}
.mc-desc {
    font-size: 0.82rem;
    color: var(--muted);
    line-height: 1.5;
    flex-grow: 1;
}
.mc-status {
    display: inline-flex;
    align-items: center;
    gap: 0.3rem;
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.03em;
    padding: 0.2rem 0.55rem;
    border-radius: 99px;
    width: fit-content;
    margin-top: 0.65rem;
}
.ms-on  { background: var(--green-soft);  color: #166534; }
.ms-off { background: rgba(0,0,0,0.05);   color: var(--muted2); }

/* Card animations with stagger */
.mc-anim-1 { animation: scalePop 0.45s ease 0.08s both; }
.mc-anim-2 { animation: scalePop 0.45s ease 0.16s both; }
.mc-anim-3 { animation: scalePop 0.45s ease 0.24s both; }
.mc-anim-4 { animation: scalePop 0.45s ease 0.32s both; }

/* ═══ HOW IT WORKS PANEL ════════════════ */
.how-panel {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r);
    padding: 1.65rem;
    box-shadow: var(--sh1);
    animation: scalePop 0.45s ease 0.36s both;
    position: relative;
    overflow: hidden;
}
.how-panel::after {
    content: '';
    position: absolute;
    bottom: -40px; right: -40px;
    width: 160px; height: 160px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(0,113,227,0.055), transparent 70%);
    pointer-events: none;
}
.how-title {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--muted2);
    margin-bottom: 1rem;
}
.how-step {
    display: flex;
    align-items: flex-start;
    gap: 0.7rem;
    margin-bottom: 0.75rem;
}
.how-step:last-child { margin-bottom: 0; }
.how-num {
    font-size: 0.7rem;
    font-weight: 700;
    min-width: 22px; height: 22px;
    border-radius: 7px;
    display: flex; align-items: center; justify-content: center;
    flex-shrink: 0;
    margin-top: 1px;
}
.hn-blue   { background: var(--blue-soft);   color: var(--blue); }
.hn-green  { background: var(--green-soft);  color: #166534; }
.hn-purple { background: var(--purple-soft); color: #6b21a8; }
.how-text {
    font-size: 0.845rem;
    color: var(--muted);
    line-height: 1.5;
}

/* ═══ MAIN BUTTONS ══════════════════════ */
div[data-testid="stButton"] > button {
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.875rem !important;
    letter-spacing: -0.01em !important;
    border-radius: 980px !important;
    padding: 0.58rem 1.3rem !important;
    background: var(--text) !important;
    color: #fff !important;
    border: none !important;
    box-shadow: none !important;
    transition: all 0.2s ease !important;
}
div[data-testid="stButton"] > button:hover {
    background: #2d2d2d !important;
    transform: scale(1.025) !important;
}
div[data-testid="stButton"] > button:disabled {
    background: rgba(0,0,0,0.06) !important;
    color: rgba(0,0,0,0.22) !important;
    transform: none !important;
}
div[data-testid="stFormSubmitButton"] > button {
    font-family: 'Inter', sans-serif !important;
    background: var(--blue) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 980px !important;
    font-weight: 700 !important;
    font-size: 0.9rem !important;
    padding: 0.65rem 2rem !important;
    box-shadow: 0 4px 18px rgba(0,113,227,0.28) !important;
    transition: all 0.2s ease !important;
    letter-spacing: -0.01em !important;
}
div[data-testid="stFormSubmitButton"] > button:hover {
    background: #0077ed !important;
    box-shadow: 0 8px 28px rgba(0,113,227,0.38) !important;
    transform: translateY(-1px) !important;
}

/* ═══ MODULE PAGE ═══════════════════════ */
.mod-header {
    padding: 1rem 0 2rem;
    animation: fadeUp 0.4s ease both;
}
.mod-eyebrow {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    margin-bottom: 0.45rem;
    display: flex;
    align-items: center;
    gap: 0.45rem;
}
.mod-eyebrow-line {
    width: 14px; height: 2px;
    border-radius: 2px;
    display: inline-block;
}
.mod-title {
    font-size: 2.5rem;
    font-weight: 800;
    letter-spacing: -0.045em;
    color: var(--text);
    line-height: 1.05;
}

/* Lesson cards */
.lc {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r-sm);
    padding: 1.5rem 1.7rem;
    margin-bottom: 0.6rem;
    position: relative;
    overflow: hidden;
    box-shadow: var(--sh1);
    transition: box-shadow 0.2s, border-color 0.2s, transform 0.2s;
}
.lc:hover {
    box-shadow: var(--sh2);
    transform: translateX(2px);
    border-color: rgba(0,0,0,0.12);
}
.lc::before {
    content: '';
    position: absolute;
    left: 0; top: 0; bottom: 0;
    width: 3px;
}
.lc-blue::before   { background: var(--blue); }
.lc-green::before  { background: var(--green); }
.lc-purple::before { background: var(--purple); }
.lc-anim-1 { animation: fadeUp 0.4s ease 0.05s both; }
.lc-anim-2 { animation: fadeUp 0.4s ease 0.12s both; }
.lc-anim-3 { animation: fadeUp 0.4s ease 0.19s both; }
.lc-label {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--muted2);
    margin-bottom: 0.3rem;
}
.lc-heading {
    font-size: 1.05rem;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.02em;
    margin-bottom: 0.55rem;
}
.lc-body {
    font-size: 0.905rem;
    color: var(--muted);
    line-height: 1.78;
}
.lc-body strong { color: var(--text); font-weight: 600; }

/* Section separator */
.sep {
    display: flex;
    align-items: center;
    gap: 0.7rem;
    margin: 2rem 0 1.25rem;
    animation: fadeIn 0.4s ease 0.25s both;
}
.sep-text {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    color: var(--muted2);
    white-space: nowrap;
}
.sep-line {
    flex-grow: 1;
    height: 1px;
    background: var(--border);
}

/* ═══ QUIZ ══════════════════════════════ */
.quiz-banner {
    border-radius: var(--r);
    padding: 1.75rem 2rem;
    margin-bottom: 1.25rem;
    position: relative;
    overflow: hidden;
    animation: fadeUp 0.4s ease 0.1s both;
}
.qb-blue {
    background: linear-gradient(135deg, #eff6ff, #dbeafe 80%);
    border: 1px solid rgba(0,113,227,0.15);
}
.qb-green {
    background: linear-gradient(135deg, #f0fdf4, #dcfce7 80%);
    border: 1px solid rgba(52,199,89,0.18);
}
.qb-purple {
    background: linear-gradient(135deg, #faf5ff, #ede9fe 80%);
    border: 1px solid rgba(175,82,222,0.18);
}
.quiz-banner::after {
    content: '?';
    position: absolute;
    right: 1.5rem; top: 50%;
    transform: translateY(-50%);
    font-size: 7rem;
    font-weight: 900;
    opacity: 0.06;
    line-height: 1;
    pointer-events: none;
}
.qb-tag {
    font-size: 0.62rem;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--muted2);
    margin-bottom: 0.3rem;
}
.qb-title {
    font-size: 1.5rem;
    font-weight: 800;
    letter-spacing: -0.03em;
    color: var(--text);
    margin-bottom: 0.2rem;
}
.qb-sub {
    font-size: 0.84rem;
    font-weight: 500;
    color: var(--muted);
}

div[role="radiogroup"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 12px !important;
    padding: 1.35rem 1.7rem !important;
    margin-bottom: 0.55rem !important;
    box-shadow: var(--sh1) !important;
    animation: fadeUp 0.35s ease both !important;
    transition: border-color 0.15s, box-shadow 0.15s !important;
}
div[role="radiogroup"]:hover {
    border-color: rgba(0,0,0,0.13) !important;
    box-shadow: var(--sh2) !important;
}

/* ═══ RESULT CARD ═══════════════════════ */
.result-card {
    border-radius: var(--r);
    padding: 2rem 2.25rem;
    margin-top: 1.25rem;
    animation: scalePop 0.4s ease both;
    position: relative;
    overflow: hidden;
}
.rc-pass {
    background: linear-gradient(135deg, #f0fdf4, #dcfce7);
    border: 1px solid rgba(52,199,89,0.22);
}
.rc-fail {
    background: linear-gradient(135deg, #fff5f5, #fee2e2);
    border: 1px solid rgba(255,59,48,0.18);
}
.rc-tag {
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
    margin-bottom: 0.45rem;
}
.rt-pass { color: #166534; }
.rt-fail { color: #991b1b; }
.rc-score {
    font-size: 4rem;
    font-weight: 900;
    letter-spacing: -0.06em;
    line-height: 1;
    margin-bottom: 0.2rem;
}
.rs-pass { color: var(--green); }
.rs-fail { color: var(--red); }
.rc-denom { font-size: 1.5rem; color: var(--muted2); font-weight: 500; }
.rc-msg {
    font-size: 0.895rem;
    color: var(--muted);
    margin-top: 0.5rem;
    line-height: 1.6;
}

/* ═══ METRICS PAGE ══════════════════════ */
.stat-card {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r);
    padding: 1.75rem 1.5rem 1.5rem;
    text-align: center;
    box-shadow: var(--sh1);
    position: relative;
    overflow: hidden;
    transition: box-shadow 0.25s, transform 0.25s;
}
.stat-card:hover { box-shadow: var(--sh3); transform: translateY(-3px); }
.stat-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
}
.sc-b::before { background: linear-gradient(90deg, var(--blue), #38bdf8); }
.sc-g::before { background: linear-gradient(90deg, var(--green), #86efac); }
.sc-p::before { background: linear-gradient(90deg, var(--purple), #e879f9); }
.stat-card-anim-1 { animation: scalePop 0.45s ease 0.08s both; }
.stat-card-anim-2 { animation: scalePop 0.45s ease 0.16s both; }
.stat-card-anim-3 { animation: scalePop 0.45s ease 0.24s both; }
.sv {
    font-size: 2.9rem;
    font-weight: 800;
    letter-spacing: -0.05em;
    line-height: 1;
    margin-bottom: 0.35rem;
}
.sv-b { color: var(--blue); }
.sv-g { color: var(--green); }
.sv-p { color: var(--purple); }
.sl {
    font-size: 0.68rem;
    font-weight: 700;
    letter-spacing: 0.11em;
    text-transform: uppercase;
    color: var(--muted2);
}

/* Progress section */
.prog-section {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r);
    padding: 1.5rem 2rem;
    box-shadow: var(--sh1);
    margin-bottom: 1.25rem;
    animation: fadeUp 0.4s ease 0.3s both;
}
.prog-head {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 0.7rem;
}
.prog-title { font-size: 0.88rem; font-weight: 700; color: var(--text); letter-spacing: -0.01em; }
.prog-sub   { font-size: 0.78rem; color: var(--muted2); font-weight: 400; }
.prog-track {
    height: 7px;
    background: rgba(0,0,0,0.07);
    border-radius: 99px;
    overflow: hidden;
}
.prog-fill {
    height: 7px;
    border-radius: 99px;
    background: linear-gradient(90deg, var(--blue), var(--purple));
    animation: barGrow 0.9s ease 0.5s both;
}

/* Data table */
.dtable {
    width: 100%;
    border-collapse: collapse;
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--r);
    overflow: hidden;
    box-shadow: var(--sh1);
    animation: fadeUp 0.4s ease 0.38s both;
}
.dtable th {
    background: #fafafa;
    padding: 0.8rem 1.5rem;
    font-size: 0.65rem;
    font-weight: 700;
    letter-spacing: 0.11em;
    text-transform: uppercase;
    color: var(--muted2);
    border-bottom: 1px solid var(--border);
    text-align: left;
}
.dtable td {
    padding: 1rem 1.5rem;
    border-bottom: 1px solid var(--border);
    font-size: 0.9rem;
    color: var(--text);
}
.dtable tr:last-child td { border-bottom: none; }
.dtable tr:hover td { background: rgba(0,113,227,0.02); }

/* ═══ MISC ══════════════════════════════ */
hr { border: none !important; border-top: 1px solid var(--border) !important; margin: 2rem 0 !important; }
p { color: var(--muted) !important; line-height: 1.7 !important; }
h1, h2, h3 { color: var(--text) !important; font-weight: 800 !important; letter-spacing: -0.03em !important; }
div[data-testid="stAlert"] { border-radius: 12px !important; }
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'dashboard'
if 'unlocked_modules' not in st.session_state:
    st.session_state.unlocked_modules = ['module_1']
for _m in ['1', '2', '3']:
    for _k, _d in [('quiz_started', False), ('quiz_submitted', False), ('quiz_score', 0)]:
        if f'm{_m}_{_k}' not in st.session_state:
            st.session_state[f'm{_m}_{_k}'] = _d

def navigate(view):
    st.session_state.current_view = view

# ── Quiz data ─────────────────────────────────────────────────────────────
M1 = [
    {"q": "What do we call the specific time and place where a story happens?",       "o": ["The Plot","The Characters","The Setting","The Title"],                  "a": "The Setting"},
    {"q": "Where is the main idea of a paragraph usually located?",                   "o": ["In the middle","At the very end","In the topic sentence","In the dictionary"], "a": "In the topic sentence"},
    {"q": "What are hints around a new word that help you understand its meaning?",   "o": ["Context clues","Story settings","Hidden numbers","Spelling words"],    "a": "Context clues"},
    {"q": "Who are the people or animals that take part in a story?",                 "o": ["The Authors","The Readers","The Characters","The Settings"],           "a": "The Characters"},
    {"q": "What is the sequence of events from beginning to end of a story called?",  "o": ["The Plot","The Cover","The Vocabulary","The Conclusion"],              "a": "The Plot"},
]
M2 = [
    {"q": "What is the total sum when you combine 145 and 278?",               "o": ["423","413","433","323"],                                                               "a": "423"},
    {"q": "What is the perimeter of a square if one side measures 9 units?",   "o": ["18 units","27 units","36 units","81 units"],                                           "a": "36 units"},
    {"q": "In the fraction 3/4, what does the number 4 represent?",            "o": ["The part we have","The total equal parts in the whole","The sum","The difference"],   "a": "The total equal parts in the whole"},
    {"q": "What is the product of 15 multiplied by 8?",                        "o": ["100","110","120","130"],                                                               "a": "120"},
    {"q": "What is the mathematical term for a flat shape with straight sides?","o": ["Circle","Sphere","Polygon","Line"],                                                   "a": "Polygon"},
]
M3 = [
    {"q": "What process changes liquid water into an invisible gas?",         "o": ["Condensation","Evaporation","Precipitation","Freezing"],  "a": "Evaporation"},
    {"q": "What provides the main energy that powers the water cycle?",       "o": ["The Moon","The Wind","The Sun","The Ocean"],              "a": "The Sun"},
    {"q": "What forms in the sky when water vapor cools and condenses?",      "o": ["Raindrops","Clouds","Rivers","Groundwater"],              "a": "Clouds"},
    {"q": "Which of the following is an example of precipitation?",           "o": ["Snow falling","A puddle drying","Water boiling","Ice melting"], "a": "Snow falling"},
    {"q": "Where does a large amount of water collect underground?",          "o": ["Aquifer","Cloud","Atmosphere","Evaporator"],              "a": "Aquifer"},
]


# ═══════════════════════════════════════════════════════════════════
#  HELPER — must live above the if/elif chain
# ═══════════════════════════════════════════════════════════════════
def render_module(m_num, title, eyebrow, icon, accent, lc_cls, qb_cls, sections, quiz_data):
    """Renders a full module page: header → lessons → assessment."""

    st.button("← Dashboard", key=f"back_{m_num}", on_click=navigate, args=('dashboard',))
    st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="mod-header">
        <div class="mod-eyebrow" style="color:{accent};">
            <span class="mod-eyebrow-line" style="background:{accent};"></span>
            {eyebrow}
        </div>
        <div class="mod-title">{icon} {title}</div>
    </div>
    """, unsafe_allow_html=True)

    anim_cls = ["lc-anim-1", "lc-anim-2", "lc-anim-3"]
    for i, (lbl, heading, body) in enumerate(sections):
        st.markdown(f"""
        <div class="lc {lc_cls} {anim_cls[i]}">
            <div class="lc-label">{lbl}</div>
            <div class="lc-heading">{heading}</div>
            <div class="lc-body">{body}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="sep">
        <span class="sep-text">Assessment</span>
        <span class="sep-line"></span>
    </div>
    """, unsafe_allow_html=True)

    sk_started   = f'm{m_num}_quiz_started'
    sk_submitted = f'm{m_num}_quiz_submitted'
    sk_score     = f'm{m_num}_quiz_score'
    btn_start    = f'start_{m_num}'
    btn_retry    = f'retry_{m_num}'
    next_mod     = f'module_{int(m_num) + 1}'

    if not st.session_state[sk_started]:
        st.markdown("""
        <p style="text-align:center; font-size:0.875rem; margin-bottom:0.75rem !important;">
            Finished reading? Test your understanding with 5 questions.
        </p>
        """, unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1.8, 1, 1.8])
        with c2:
            st.button("Begin Quiz →", key=btn_start, use_container_width=True)
        if st.session_state.get(btn_start):
            st.session_state[sk_started] = True
            st.rerun()

    if st.session_state[sk_started]:
        st.markdown(f"""
        <div class="quiz-banner {qb_cls}">
            <div class="qb-tag">Formative Evaluation</div>
            <div class="qb-title">Knowledge Check</div>
            <div class="qb-sub">5 questions &nbsp;·&nbsp; Select the best answer for each</div>
        </div>
        """, unsafe_allow_html=True)

        with st.form(key=f'form_{m_num}', clear_on_submit=False):
            answers = []
            for i, q in enumerate(quiz_data):
                st.markdown(f"**{i+1}.&nbsp; {q['q']}**")
                a = st.radio("", q['o'], key=f"q_{m_num}_{i}",
                             label_visibility="collapsed", index=None)
                answers.append(a)
                if i < len(quiz_data) - 1:
                    st.markdown("<div style='height:0.15rem'></div>", unsafe_allow_html=True)
            st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Submit Answers")

        if submitted:
            if None in answers:
                st.error("Please answer every question before submitting.")
            else:
                score = sum(1 for i, q in enumerate(quiz_data) if answers[i] == q['a'])
                st.session_state[sk_score] = score
                st.session_state[sk_submitted] = True

        if st.session_state[sk_submitted]:
            sc = st.session_state[sk_score]
            passed = sc >= 4
            rc  = "rc-pass" if passed else "rc-fail"
            rt  = "rt-pass" if passed else "rt-fail"
            rs  = "rs-pass" if passed else "rs-fail"
            tag = "✓ Competency Verified" if passed else "✗ Below Threshold"
            msg = "Well done — the next module has been unlocked." if passed else "Review the lesson material above and try again."

            st.markdown(f"""
            <div class="result-card {rc}">
                <div class="rc-tag {rt}">{tag}</div>
                <div>
                    <span class="rc-score {rs}">{sc}</span>
                    <span class="rc-denom"> / {len(quiz_data)}</span>
                </div>
                <div class="rc-msg">{msg}</div>
            </div>
            """, unsafe_allow_html=True)

            if passed and int(m_num) < 3 and next_mod not in st.session_state.unlocked_modules:
                st.session_state.unlocked_modules.append(next_mod)

            if not passed:
                st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns([1.8, 1, 1.8])
                with c2:
                    st.button("Retry Quiz", key=btn_retry, use_container_width=True)
                if st.session_state.get(btn_retry):
                    st.session_state[sk_submitted] = False
                    st.rerun()


# ═══════════════════════════════════════════════════════════════════
#  SIDEBAR
# ═══════════════════════════════════════════════════════════════════
_cur = st.session_state.current_view
_m2_ok = 'module_2' in st.session_state.unlocked_modules
_m3_ok = 'module_3' in st.session_state.unlocked_modules
_done = sum([
    st.session_state.m1_quiz_submitted and st.session_state.m1_quiz_score >= 4,
    st.session_state.m2_quiz_submitted and st.session_state.m2_quiz_score >= 4,
    st.session_state.m3_quiz_submitted and st.session_state.m3_quiz_score >= 4,
])
_pct = int(_done / 3 * 100)

def _dot(mn):
    if st.session_state[f'm{mn}_quiz_submitted'] and st.session_state[f'm{mn}_quiz_score'] >= 4:
        return "dot-done"
    if f'module_{mn}' in st.session_state.unlocked_modules:
        return "dot-active"
    return "dot-none"

def _active_row(icon, label, dot_cls):
    st.markdown(f"""
    <div class="nav-row nav-active">
        <span class="nav-icon">{icon}</span>
        <span class="nav-label">{label}</span>
        <span class="nav-dot {dot_cls}"></span>
    </div>
    """, unsafe_allow_html=True)

def _locked_row(icon, label):
    st.markdown(f"""
    <div class="nav-row nav-locked">
        <span class="nav-icon">🔒</span>
        <span class="nav-label">{label}</span>
        <span class="nav-dot dot-none"></span>
    </div>
    """, unsafe_allow_html=True)

with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-logo"><span class="grd">DANILO</span></div>
        <div class="sb-tagline">Academic Platform</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section">Navigation</div>', unsafe_allow_html=True)

    # Dashboard
    if _cur == 'dashboard':
        _active_row("⊞", "Dashboard", "dot-active")
    else:
        st.button("⊞  Dashboard", key="nav_dash", on_click=navigate,
                  args=('dashboard',), use_container_width=True)

    st.markdown('<div class="sb-section" style="padding-top:0.6rem;">Curriculum</div>', unsafe_allow_html=True)

    # Reading
    if _cur == 'module_1':
        _active_row("📖", "Reading", _dot('1'))
    else:
        st.button("📖  Reading", key="nav_m1", on_click=navigate,
                  args=('module_1',), use_container_width=True)

    # Mathematics
    if _cur == 'module_2':
        _active_row("📐", "Mathematics", _dot('2'))
    elif _m2_ok:
        st.button("📐  Mathematics", key="nav_m2", on_click=navigate,
                  args=('module_2',), use_container_width=True)
    else:
        _locked_row("📐", "Mathematics")

    # Natural Sciences
    if _cur == 'module_3':
        _active_row("🌊", "Natural Sciences", _dot('3'))
    elif _m3_ok:
        st.button("🌊  Natural Sciences", key="nav_m3", on_click=navigate,
                  args=('module_3',), use_container_width=True)
    else:
        _locked_row("🌊", "Natural Sciences")

    st.markdown('<div class="sb-section" style="padding-top:0.6rem;">Records</div>', unsafe_allow_html=True)

    # Metrics
    if _cur == 'profile':
        _active_row("📊", "Metrics", "dot-none")
    else:
        st.button("📊  Metrics", key="nav_prof", on_click=navigate,
                  args=('profile',), use_container_width=True)

    # Progress footer
    st.markdown(f"""
    <div class="sb-progress">
        <div class="sb-prog-head">
            <span class="sb-prog-label">Progress</span>
            <span class="sb-prog-pct">{_pct}%</span>
        </div>
        <div class="sb-track">
            <div class="sb-fill" style="--bar-w:{_pct}%; width:{_pct}%;"></div>
        </div>
        <div class="sb-modules-done">{_done} of 3 modules completed</div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  DASHBOARD
# ═══════════════════════════════════════════════════════════════════
if st.session_state.current_view == 'dashboard':

    st.markdown("""
    <div class="hero">
        <div class="hero-eyebrow">Academic Platform</div>
        <div class="hero-title">
            Learn, Test &amp; <span class="grd">Unlock.</span>
        </div>
        <div class="hero-sub">
            A sequential curriculum that rewards mastery.
            Pass each module's assessment to advance to the next.
        </div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("""
        <div class="mc mc-blue mc-anim-1">
            <span class="mc-num">01</span>
            <span class="mc-ghost">01</span>
            <div class="mc-icon i-blue">📖</div>
            <div class="mc-title">Reading</div>
            <div class="mc-desc">Story elements, main ideas &amp; context clues.</div>
            <div class="mc-status ms-on">● Unlocked</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Open →", key="db_m1", on_click=navigate,
                  args=('module_1',), use_container_width=True)

    with col2:
        locked2 = 'module_2' not in st.session_state.unlocked_modules
        tag2 = '<div class="mc-status ms-off">🔒 Requires Reading</div>' if locked2 \
               else '<div class="mc-status ms-on">● Unlocked</div>'
        extra2 = "mc-locked" if locked2 else ""
        st.markdown(f"""
        <div class="mc mc-green mc-anim-2 {extra2}">
            <span class="mc-num">02</span>
            <span class="mc-ghost">02</span>
            <div class="mc-icon i-green">📐</div>
            <div class="mc-title">Mathematics</div>
            <div class="mc-desc">Operations, fractions &amp; geometry.</div>
            {tag2}
        </div>
        """, unsafe_allow_html=True)
        st.button("Open →", key="db_m2", on_click=navigate,
                  args=('module_2',), disabled=locked2, use_container_width=True)

    with col3:
        locked3 = 'module_3' not in st.session_state.unlocked_modules
        tag3 = '<div class="mc-status ms-off">🔒 Requires Mathematics</div>' if locked3 \
               else '<div class="mc-status ms-on">● Unlocked</div>'
        extra3 = "mc-locked" if locked3 else ""
        st.markdown(f"""
        <div class="mc mc-purple mc-anim-3 {extra3}">
            <span class="mc-num">03</span>
            <span class="mc-ghost">03</span>
            <div class="mc-icon i-purple">🌊</div>
            <div class="mc-title">Natural Sciences</div>
            <div class="mc-desc">The water cycle &amp; Earth's hydrosphere.</div>
            {tag3}
        </div>
        """, unsafe_allow_html=True)
        st.button("Open →", key="db_m3", on_click=navigate,
                  args=('module_3',), disabled=locked3, use_container_width=True)

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    col4, col5 = st.columns([1, 1.65], gap="medium")

    with col4:
        st.markdown(f"""
        <div class="mc mc-amber mc-anim-4" style="height:auto; min-height:160px;">
            <span class="mc-ghost"></span>
            <div class="mc-icon i-amber">📊</div>
            <div class="mc-title">Academic Metrics</div>
            <div class="mc-desc">Performance records &amp; curriculum logs.</div>
            <div style="margin-top:0.7rem;">
                <div style="display:flex;justify-content:space-between;
                            font-size:0.7rem;font-weight:600;color:var(--muted2);margin-bottom:0.4rem;">
                    <span>Progress</span><span>{_pct}%</span>
                </div>
                <div class="prog-track">
                    <div class="prog-fill" style="--bar-w:{_pct}%; width:{_pct}%;"></div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("View Metrics →", key="db_prof", on_click=navigate,
                  args=('profile',), use_container_width=True)

    with col5:
        st.markdown("""
        <div class="how-panel">
            <div class="how-title">How it works</div>
            <div class="how-step">
                <div class="how-num hn-blue">01</div>
                <div class="how-text">
                    <strong style="color:var(--text);font-weight:600;">Read</strong> —
                    Work through the lesson material inside each module.
                </div>
            </div>
            <div class="how-step">
                <div class="how-num hn-green">02</div>
                <div class="how-text">
                    <strong style="color:var(--text);font-weight:600;">Test</strong> —
                    Score 4 out of 5 on the formative quiz to pass.
                </div>
            </div>
            <div class="how-step">
                <div class="how-num hn-purple">03</div>
                <div class="how-text">
                    <strong style="color:var(--text);font-weight:600;">Unlock</strong> —
                    Passing a module opens the next subject automatically.
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  MODULE 1 — READING
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'module_1':
    render_module(
        m_num='1', title='Reading',
        eyebrow='Module 01 · Language Arts', icon='📖',
        accent='#0071e3', lc_cls='lc-blue', qb_cls='qb-blue',
        sections=[
            ("Section 1.0", "Elements of a Story",
             "Every story has essential parts. The <strong>setting</strong> tells us when and where the story takes place. "
             "The <strong>characters</strong> are the people, animals, or creatures in the story. "
             "The <strong>plot</strong> is the sequence of events from beginning to end."),
            ("Section 1.1", "Finding the Main Idea",
             "The <strong>main idea</strong> is the primary point an author wants to communicate. "
             "It is often found in the <strong>topic sentence</strong> — usually the first sentence of a paragraph."),
            ("Section 1.2", "Using Context Clues",
             "When you encounter an unfamiliar word, examine the surrounding words for hints about its meaning. "
             "These helpful hints are called <strong>context clues</strong>."),
        ],
        quiz_data=M1
    )


# ═══════════════════════════════════════════════════════════════════
#  MODULE 2 — MATHEMATICS
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'module_2':
    render_module(
        m_num='2', title='Mathematics',
        eyebrow='Module 02 · Quantitative Reasoning', icon='📐',
        accent='#34c759', lc_cls='lc-green', qb_cls='qb-green',
        sections=[
            ("Section 2.0", "Basic Operations",
             "<strong>Addition</strong> combines two numbers into a sum. "
             "<strong>Subtraction</strong> finds the difference. "
             "<strong>Multiplication</strong> is a faster form of repeated addition."),
            ("Section 2.1", "Understanding Fractions",
             "A fraction represents part of a whole. The <strong>numerator</strong> (top) shows parts we have; "
             "the <strong>denominator</strong> (bottom) shows total equal parts. The denominator can never be zero."),
            ("Section 2.2", "Basic Geometry",
             "A <strong>polygon</strong> is any flat, closed shape with straight sides — triangles, squares, rectangles. "
             "The total distance around the outside edge of a shape is its <strong>perimeter</strong>."),
        ],
        quiz_data=M2
    )


# ═══════════════════════════════════════════════════════════════════
#  MODULE 3 — NATURAL SCIENCES
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'module_3':
    render_module(
        m_num='3', title='Natural Sciences',
        eyebrow='Module 03 · Earth Science', icon='🌊',
        accent='#af52de', lc_cls='lc-purple', qb_cls='qb-purple',
        sections=[
            ("Section 3.0", "The Water Cycle",
             "Water continuously moves between the ground, oceans, and sky. "
             "The total amount of water on Earth stays roughly constant — it simply changes location and state."),
            ("Section 3.1", "Evaporation & Condensation",
             "The sun heats liquid water, turning it into invisible <strong>water vapor</strong> — this is <strong>evaporation</strong>. "
             "As vapor rises and cools, it forms clouds through <strong>condensation</strong>."),
            ("Section 3.2", "Precipitation & Collection",
             "When clouds hold too much water, it falls as <strong>precipitation</strong> (rain, snow, hail). "
             "Water collects in oceans, lakes, and underground <strong>aquifers</strong>, restarting the cycle."),
        ],
        quiz_data=M3
    )


# ═══════════════════════════════════════════════════════════════════
#  METRICS PAGE
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'profile':
    st.markdown("""
    <div style="padding:1rem 0 1.75rem; animation: fadeUp 0.4s ease both;">
        <div class="hero-eyebrow">Performance Records</div>
        <div class="hero-title" style="font-size:2.4rem; margin-bottom:0;">Academic Metrics</div>
    </div>
    """, unsafe_allow_html=True)

    _sc_sum, _sc_cnt = 0, 0
    for _mn in ['1', '2', '3']:
        if st.session_state[f'm{_mn}_quiz_submitted']:
            _sc_sum += st.session_state[f'm{_mn}_quiz_score']
            _sc_cnt += 1
    _avg = int(_sc_sum / (_sc_cnt * 5) * 100) if _sc_cnt else 0
    _prog = int(_done / 3 * 100)

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown(f"""
        <div class="stat-card sc-b stat-card-anim-1">
            <div class="sv sv-b">{_done}</div>
            <div class="sl">Modules Passed</div>
        </div>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown(f"""
        <div class="stat-card sc-g stat-card-anim-2">
            <div class="sv sv-g">{_avg}%</div>
            <div class="sl">Mean Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    with c3:
        st.markdown(f"""
        <div class="stat-card sc-p stat-card-anim-3">
            <div class="sv sv-p">{_prog}%</div>
            <div class="sl">Curriculum Done</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:1.25rem'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="prog-section">
        <div class="prog-head">
            <span class="prog-title">Overall Progress</span>
            <span class="prog-sub">{_done} of 3 modules completed</span>
        </div>
        <div class="prog-track">
            <div class="prog-fill" style="--bar-w:{_prog}%; width:{_prog}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    def _status_cell(mn):
        sub = st.session_state[f'm{mn}_quiz_submitted']
        sc  = st.session_state[f'm{mn}_quiz_score']
        locked = f'module_{mn}' not in st.session_state.unlocked_modules
        if locked:
            return '<span style="color:var(--muted2);font-weight:500;">🔒 Locked</span>', "—"
        if sub and sc >= 4:
            return '<span style="color:#166534;font-weight:700;">✓ Verified</span>', f"{sc}/5"
        if sub:
            return '<span style="color:#991b1b;font-weight:700;">✗ Needs Retry</span>', f"{sc}/5"
        return '<span style="color:#92400e;font-weight:600;">◷ In Progress</span>', "—"

    s1, d1 = _status_cell('1')
    s2, d2 = _status_cell('2')
    s3, d3 = _status_cell('3')

    st.markdown(f"""
    <table class="dtable">
        <thead>
            <tr>
                <th>#</th><th>Module</th><th>Status</th><th>Score</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="color:var(--muted2);font-size:0.75rem;font-weight:700;">01</td>
                <td style="font-weight:600;">📖 Reading</td>
                <td>{s1}</td>
                <td style="font-family:monospace;color:var(--muted2);letter-spacing:0.05em;">{d1}</td>
            </tr>
            <tr>
                <td style="color:var(--muted2);font-size:0.75rem;font-weight:700;">02</td>
                <td style="font-weight:600;">📐 Mathematics</td>
                <td>{s2}</td>
                <td style="font-family:monospace;color:var(--muted2);letter-spacing:0.05em;">{d2}</td>
            </tr>
            <tr>
                <td style="color:var(--muted2);font-size:0.75rem;font-weight:700;">03</td>
                <td style="font-weight:600;">🌊 Natural Sciences</td>
                <td>{s3}</td>
                <td style="font-family:monospace;color:var(--muted2);letter-spacing:0.05em;">{d3}</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)
