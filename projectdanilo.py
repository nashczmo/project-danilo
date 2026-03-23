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
    page_title="DANILO Learning",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
/* ─── Fonts ─────────────────────────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ─── Design tokens ──────────────────────────────────────────────────────── */
:root {
    --bg:        #f5f5f7;
    --card:      #ffffff;
    --card2:     #fafafa;
    --border:    rgba(0,0,0,0.07);
    --text:      #1d1d1f;
    --sub:       #6e6e73;
    --muted:     #aeaeb2;
    --blue:      #0071e3;
    --green:     #28cd41;
    --orange:    #ff9f0a;
    --red:       #ff3b30;
    --purple:    #bf5af2;
    --indigo:    #5e5ce6;
    --s1: 0 1px 3px rgba(0,0,0,0.07), 0 1px 2px rgba(0,0,0,0.04);
    --s2: 0 4px 20px rgba(0,0,0,0.09), 0 1px 4px rgba(0,0,0,0.05);
    --s3: 0 16px 48px rgba(0,0,0,0.13), 0 4px 12px rgba(0,0,0,0.07);
    --r1: 10px;
    --r2: 14px;
    --r3: 20px;
    --ease: cubic-bezier(0.4,0,0.2,1);
}

/* ─── Base reset ──────────────────────────────────────────────────────────── */
*, html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    -webkit-font-smoothing: antialiased !important;
    box-sizing: border-box;
}
.stApp { background: var(--bg) !important; }
#MainMenu, footer, header { visibility: hidden; }

/* ─── FULL WIDTH – remove all Streamlit padding caps ─────────────────────── */
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
    width: 100% !important;
}
/* inner scroll wrapper */
.main > div { padding: 0 !important; }

/* ─── Sidebar ─────────────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid var(--border) !important;
    width: 220px !important;
    min-width: 220px !important;
}
section[data-testid="stSidebar"] > div {
    padding: 0 !important;
    width: 220px !important;
}
/* Always show the open-sidebar toggle button */
[data-testid="collapsedControl"] {
    visibility: visible !important;
    display: flex !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 12px !important;
    left: 12px !important;
    z-index: 99999 !important;
    width: 38px !important;
    height: 38px !important;
    background: #ffffff !important;
    border-radius: var(--r1) !important;
    box-shadow: var(--s2) !important;
    border: 1px solid var(--border) !important;
    cursor: pointer !important;
    transition: box-shadow 0.2s var(--ease) !important;
    align-items: center !important;
    justify-content: center !important;
}
[data-testid="collapsedControl"]:hover { box-shadow: var(--s3) !important; }

/* ─── Sidebar brand ───────────────────────────────────────────────────────── */
.sb-brand {
    padding: 22px 18px 16px;
    border-bottom: 1px solid var(--border);
}
.sb-logo {
    font-size: 1.3rem;
    font-weight: 800;
    color: var(--text);
    letter-spacing: -0.04em;
    line-height: 1;
    margin-bottom: 2px;
}
.sb-tagline {
    font-size: 0.62rem;
    font-weight: 600;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.12em;
}
.sb-section {
    display: block;
    font-size: 0.62rem !important;
    font-weight: 700 !important;
    color: var(--muted) !important;
    text-transform: uppercase;
    letter-spacing: 0.12em;
    padding: 18px 18px 6px !important;
}
.sb-footer {
    padding: 16px 18px;
    font-size: 0.64rem;
    color: var(--muted);
    line-height: 1.6;
    border-top: 1px solid var(--border);
    margin-top: 8px;
}

/* ─── Sidebar buttons ─────────────────────────────────────────────────────── */
div[data-testid="stButton"] > button {
    font-family: 'Inter', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    color: var(--sub) !important;
    background: transparent !important;
    border: none !important;
    border-radius: var(--r1) !important;
    padding: 7px 14px !important;
    text-align: left !important;
    width: 100% !important;
    letter-spacing: -0.01em !important;
    transition: background 0.15s var(--ease), color 0.15s var(--ease), transform 0.15s var(--ease) !important;
    cursor: pointer !important;
}
div[data-testid="stButton"] > button:hover {
    background: rgba(0,113,227,0.07) !important;
    color: var(--blue) !important;
}
div[data-testid="stButton"] > button:active {
    transform: scale(0.97) !important;
}

/* ─── Form submit buttons ─────────────────────────────────────────────────── */
div[data-testid="stForm"] div[data-testid="stButton"] > button {
    background: var(--blue) !important;
    color: #fff !important;
    border-radius: var(--r2) !important;
    padding: 10px 28px !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    box-shadow: 0 2px 10px rgba(0,113,227,0.28) !important;
    width: auto !important;
    text-align: center !important;
    letter-spacing: -0.01em !important;
}
div[data-testid="stForm"] div[data-testid="stButton"] > button:hover {
    background: #0064c8 !important;
    box-shadow: 0 6px 18px rgba(0,113,227,0.38) !important;
    transform: translateY(-1px) !important;
}

/* ─── Radio groups ────────────────────────────────────────────────────────── */
div[role="radiogroup"] {
    background: var(--card2) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--r2) !important;
    padding: 14px 18px !important;
    margin-bottom: 10px !important;
    box-shadow: none !important;
    transition: border-color 0.18s var(--ease), box-shadow 0.18s var(--ease) !important;
}
div[role="radiogroup"]:focus-within {
    border-color: rgba(0,113,227,0.3) !important;
    box-shadow: 0 0 0 3px rgba(0,113,227,0.08) !important;
}

/* ─── Keyframes ───────────────────────────────────────────────────────────── */
@keyframes up   { from{opacity:0;transform:translateY(16px)} to{opacity:1;transform:translateY(0)} }
@keyframes down { from{opacity:0;transform:translateY(-10px)} to{opacity:1;transform:translateY(0)} }
@keyframes pop  { from{opacity:0;transform:scale(0.88)} to{opacity:1;transform:scale(1)} }
@keyframes fade { from{opacity:0} to{opacity:1} }
.au { animation: up   0.42s cubic-bezier(0.4,0,0.2,1) both; }
.ad { animation: down 0.32s cubic-bezier(0.4,0,0.2,1) both; }
.ap { animation: pop  0.4s  cubic-bezier(0.34,1.56,0.64,1) both; }
.af { animation: fade 0.3s ease both; }
.e1{animation-delay:.04s} .e2{animation-delay:.09s} .e3{animation-delay:.14s}
.e4{animation-delay:.19s} .e5{animation-delay:.24s} .e6{animation-delay:.29s}
.e7{animation-delay:.34s} .e8{animation-delay:.39s}

/* ─── Main content wrapper ───────────────────────────────────────────────── */
.main-wrap {
    padding: 28px 36px 80px;
    width: 100%;
}

/* ─── Page header ─────────────────────────────────────────────────────────── */
.pheader {
    display: flex;
    align-items: center;
    gap: 10px;
    padding-bottom: 22px;
    margin-bottom: 24px;
    border-bottom: 1px solid var(--border);
    animation: down 0.3s ease both;
}
.pheader-title {
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.04em;
    line-height: 1;
}
.pheader-icon { font-size: 1.4rem; line-height: 1; }
.pheader-avatar {
    margin-left: auto;
    width: 34px; height: 34px;
    background: linear-gradient(135deg, var(--blue), var(--indigo));
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.78rem; font-weight: 700; color: #fff;
    flex-shrink: 0;
}

/* ─── Hero banner ─────────────────────────────────────────────────────────── */
.hero {
    background: linear-gradient(130deg, #1a1a2e 0%, #16213e 50%, #0f3460 100%);
    border-radius: var(--r3);
    padding: 36px 44px;
    margin-bottom: 24px;
    position: relative;
    overflow: hidden;
    animation: up 0.42s ease both;
}
.hero::before {
    content: '';
    position: absolute; inset: 0;
    background:
        radial-gradient(ellipse at 90% -10%, rgba(0,113,227,0.45) 0%, transparent 50%),
        radial-gradient(ellipse at -5% 110%, rgba(94,92,230,0.3) 0%, transparent 50%);
}
.hero-eyebrow {
    font-size: 0.65rem; font-weight: 600;
    color: rgba(255,255,255,0.4);
    text-transform: uppercase; letter-spacing: 0.14em;
    margin-bottom: 10px; position: relative;
}
.hero-headline {
    font-size: clamp(1.7rem, 2.5vw, 2.5rem);
    font-weight: 800;
    color: #fff;
    letter-spacing: -0.045em;
    line-height: 1.1;
    margin-bottom: 10px;
    position: relative;
}
.hero-sub {
    font-size: 0.88rem;
    color: rgba(255,255,255,0.5);
    font-weight: 400;
    position: relative;
}

/* ─── Stat cards ──────────────────────────────────────────────────────────── */
.sc {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--r2);
    padding: 18px 16px 14px;
    text-align: center;
    box-shadow: var(--s1);
    transition: box-shadow 0.2s var(--ease), transform 0.2s var(--ease);
    animation: up 0.42s ease both;
}
.sc:hover { box-shadow: var(--s2); transform: translateY(-2px); }
.sc-val {
    font-size: 1.9rem;
    font-weight: 800;
    letter-spacing: -0.05em;
    line-height: 1;
    margin-bottom: 4px;
}
.sc-lbl {
    font-size: 0.62rem;
    font-weight: 700;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
}
.sc-bar {
    height: 3px;
    background: rgba(0,0,0,0.06);
    border-radius: 99px;
    overflow: hidden;
    margin-top: 12px;
}
.sc-fill {
    height: 100%;
    border-radius: 99px;
    transition: width 1s cubic-bezier(0.4,0,0.2,1);
}

/* ─── Section label ───────────────────────────────────────────────────────── */
.sec-label {
    font-size: 0.62rem;
    font-weight: 700;
    color: var(--muted);
    text-transform: uppercase;
    letter-spacing: 0.12em;
    margin: 6px 0 12px;
}

/* ─── Course cards ────────────────────────────────────────────────────────── */
.ccard {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--r3);
    overflow: hidden;
    box-shadow: var(--s1);
    transition: box-shadow 0.22s var(--ease), transform 0.22s var(--ease);
    margin-bottom: 14px;
    animation: up 0.42s ease both;
}
.ccard:hover { box-shadow: var(--s3); transform: translateY(-4px); }
.cthumb {
    height: 116px;
    position: relative;
    display: flex;
    align-items: flex-end;
    padding: 14px 16px;
    overflow: hidden;
}
.cthumb::after {
    content: '';
    position: absolute; inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,0.32) 0%, transparent 55%);
}
.cthumb-dots {
    position: absolute; inset: 0;
    background-image: radial-gradient(circle, rgba(255,255,255,0.14) 1.5px, transparent 1.5px);
    background-size: 22px 22px;
}
.cthumb-icon {
    position: absolute;
    top: 14px; right: 16px;
    font-size: 2rem;
    z-index: 1;
    transition: transform 0.22s var(--ease);
}
.ccard:hover .cthumb-icon { transform: scale(1.15) rotate(-6deg); }
.cthumb-name {
    font-size: 1.05rem;
    font-weight: 700;
    color: #fff;
    letter-spacing: -0.03em;
    position: relative; z-index: 1;
    text-shadow: 0 1px 6px rgba(0,0,0,0.22);
}
.cbody { padding: 13px 16px 12px; }
.cdesc {
    font-size: 0.77rem;
    color: var(--sub);
    line-height: 1.5;
    margin-bottom: 10px;
}
.cfoot {
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.ccount { font-size: 0.7rem; color: var(--muted); }

/* ─── Chips ───────────────────────────────────────────────────────────────── */
.chip {
    display: inline-flex; align-items: center; gap: 3px;
    font-size: 0.68rem; font-weight: 600;
    padding: 3px 9px; border-radius: 100px;
}
.cb { background: rgba(0,113,227,0.1);  color: #0064c8; }
.cg { background: rgba(40,205,65,0.12); color: #1a9430; }
.co { background: rgba(255,159,10,0.12);color: #b86e00; }
.cp { background: rgba(191,90,242,0.12);color: #8b2fc9; }
.cr { background: rgba(255,59,48,0.1);  color: #c0392b; }
.cz { background: rgba(0,0,0,0.05);     color: var(--muted); }

/* ─── Module hero ─────────────────────────────────────────────────────────── */
.mhero {
    border-radius: var(--r3);
    padding: 32px 36px;
    margin-bottom: 22px;
    position: relative; overflow: hidden;
    animation: up 0.38s ease both;
}
.mhero::before {
    content: '';
    position: absolute; inset: 0;
    background-image: radial-gradient(circle, rgba(255,255,255,0.1) 1.5px, transparent 1.5px);
    background-size: 22px 22px;
}
.mhero-ico { font-size: 2.5rem; margin-bottom: 12px; display: block; position: relative; }
.mhero-title {
    font-size: clamp(1.4rem, 2.5vw, 1.9rem);
    font-weight: 800;
    color: #fff;
    letter-spacing: -0.045em;
    line-height: 1.15;
    margin: 0 0 6px;
    position: relative;
}
.mhero-sub {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.65);
    margin: 0;
    position: relative;
}
.mhero-chips {
    display: flex; gap: 6px; flex-wrap: wrap;
    margin-top: 16px; position: relative;
}
.gchip {
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.25);
    color: #fff;
    font-size: 0.7rem; font-weight: 600;
    padding: 4px 11px; border-radius: 100px;
}

/* ─── Topic card ──────────────────────────────────────────────────────────── */
.tcard {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--r2);
    padding: 18px 20px;
    margin-bottom: 10px;
    box-shadow: var(--s1);
    animation: up 0.42s ease both;
    transition: box-shadow 0.2s var(--ease), border-color 0.2s var(--ease);
}
.tcard:hover {
    box-shadow: var(--s2);
    border-color: rgba(0,113,227,0.15);
}
.thead {
    display: flex; align-items: center; gap: 10px;
    margin-bottom: 10px;
}
.ticon {
    width: 36px; height: 36px;
    border-radius: 9px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.1rem; flex-shrink: 0;
}
.ttitle {
    font-size: 0.9rem;
    font-weight: 700;
    color: var(--text);
    letter-spacing: -0.02em;
}
.tbody {
    font-size: 0.83rem !important;
    color: var(--sub) !important;
    line-height: 1.8 !important;
    margin: 0 !important;
}

/* ─── Quiz header ─────────────────────────────────────────────────────────── */
.qbar {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--r2);
    padding: 14px 18px;
    margin: 18px 0 12px;
    display: flex; align-items: center; gap: 12px;
    box-shadow: var(--s1);
    animation: up 0.42s ease both;
}
.qbar-ico {
    width: 42px; height: 42px;
    border-radius: var(--r1);
    background: rgba(0,113,227,0.09);
    display: flex; align-items: center; justify-content: center;
    font-size: 1.25rem; flex-shrink: 0;
}
.qbar-title { font-size: 0.9rem; font-weight: 700; color: var(--text); margin: 0; }
.qbar-sub   { font-size: 0.72rem; color: var(--muted); margin: 2px 0 0; }
.qlabel {
    font-size: 0.62rem; font-weight: 700;
    color: var(--muted);
    text-transform: uppercase; letter-spacing: 0.1em;
    margin-bottom: 3px;
}

/* ─── Result card ─────────────────────────────────────────────────────────── */
.rcard {
    border-radius: var(--r3);
    padding: 28px 32px;
    margin: 14px 0;
    display: flex; align-items: center; gap: 24px;
    animation: pop 0.4s cubic-bezier(0.34,1.56,0.64,1) both;
    flex-wrap: wrap;
}
.rpass { background: rgba(40,205,65,0.09);  border: 1px solid rgba(40,205,65,0.28); }
.rfail { background: rgba(255,59,48,0.07);  border: 1px solid rgba(255,59,48,0.24); }
.rscore {
    font-size: 3.8rem;
    font-weight: 800;
    letter-spacing: -0.06em;
    line-height: 1;
    flex-shrink: 0;
}
.rpass .rscore { color: var(--green); }
.rfail .rscore { color: var(--red); }
.rbadge {
    font-size: 0.65rem; font-weight: 700;
    text-transform: uppercase; letter-spacing: 0.08em;
    margin-top: 4px;
}
.rpass .rbadge { color: #1a9430; }
.rfail .rbadge { color: #c0392b; }
.rmsg { font-size: 0.85rem; color: var(--sub); line-height: 1.7; }
.rmsg strong { color: var(--text); }

/* ─── Grades table ────────────────────────────────────────────────────────── */
.gtable {
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: var(--r3);
    overflow: hidden;
    box-shadow: var(--s1);
    width: 100%; border-collapse: collapse;
    animation: up 0.42s ease both;
}
.gtable th {
    background: var(--card2);
    padding: 10px 18px;
    font-size: 0.62rem; font-weight: 700;
    color: var(--muted);
    text-transform: uppercase; letter-spacing: 0.1em;
    text-align: left;
    border-bottom: 1px solid var(--border);
}
.gtable td {
    padding: 13px 18px;
    border-bottom: 1px solid rgba(0,0,0,0.04);
    font-size: 0.84rem;
    vertical-align: middle;
}
.gtable tr:last-child td { border-bottom: none; }
.gtable tr:hover td { background: var(--card2); }
.gmono {
    font-variant-numeric: tabular-nums;
    font-weight: 700; font-size: 0.88rem;
}

/* ─── Divider ─────────────────────────────────────────────────────────────── */
.div-line {
    border: none;
    border-top: 1px solid rgba(0,0,0,0.06);
    margin: 12px 0;
}

/* ─── Mobile ──────────────────────────────────────────────────────────────── */
@media (max-width: 768px) {
    .main-wrap { padding: 16px 14px 72px; }
    .pheader-title { font-size: 1.2rem; }
    .hero { padding: 24px 22px; border-radius: var(--r2); }
    .hero-headline { font-size: 1.45rem; }
    .mhero { padding: 22px 18px; }
    .mhero-title { font-size: 1.3rem; }
    .rcard { padding: 20px 16px; gap: 14px; }
    .rscore { font-size: 2.8rem; }
    .gtable th, .gtable td { padding: 9px 12px; font-size: 0.78rem; }
    .sc-val { font-size: 1.5rem; }
    .cthumb { height: 90px; }
    .gtable { display: block; overflow-x: auto; }
}
</style>
""", unsafe_allow_html=True)

# ─── Session state ────────────────────────────────────────────────────────────
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'dashboard'
if 'unlocked_modules' not in st.session_state:
    st.session_state.unlocked_modules = ['module_1']
for m in ['1', '2', '3', '4']:
    for k, d in [('quiz_started', False), ('quiz_submitted', False), ('quiz_score', 0)]:
        if f'm{m}_{k}' not in st.session_state:
            st.session_state[f'm{m}_{k}'] = d

def nav(view):
    st.session_state.current_view = view

# ─── Quiz data ────────────────────────────────────────────────────────────────
M1 = [
    {"q": "What do we call the specific time and place in which a story unfolds?",
     "o": ["The Plot", "The Characters", "The Setting", "The Theme"], "a": "The Setting"},
    {"q": "Where is the main idea of a paragraph most commonly found?",
     "o": ["In a footnote", "At the very end", "In the topic sentence", "Between the lines"], "a": "In the topic sentence"},
    {"q": "What are surrounding clues that help a reader decode an unfamiliar word?",
     "o": ["Context clues", "Phonics hints", "Story settings", "Grammar rules"], "a": "Context clues"},
    {"q": "Who are the people, animals, or creatures that participate in a story's events?",
     "o": ["The Authors", "The Narrators", "The Characters", "The Themes"], "a": "The Characters"},
    {"q": "What is the term for the sequence of events that drives a story from beginning to end?",
     "o": ["The Plot", "The Cover Page", "The Vocabulary", "The Epilogue"], "a": "The Plot"},
]
M2 = [
    {"q": "What does reading fluency primarily involve?",
     "o": ["Reading as fast as possible", "Reading accurately, smoothly, and with natural expression",
           "Memorising every vocabulary word", "Reading silently without any lip movement"],
     "a": "Reading accurately, smoothly, and with natural expression"},
    {"q": "Which technique involves reading the same passage multiple times until it flows effortlessly?",
     "o": ["Skimming", "Scanning", "Repeated reading", "Speed reading"], "a": "Repeated reading"},
    {"q": "What is a 'sight word'?",
     "o": ["A word with silent letters", "A word instantly recognised without sounding it out",
           "A very long and complicated word", "A word borrowed from another language"],
     "a": "A word instantly recognised without sounding it out"},
    {"q": "What does reading with 'expression' mean?",
     "o": ["Speaking as loudly as possible", "Changing your voice to match the emotion and meaning of the text",
           "Reading every word at the same monotone pace", "Pausing three seconds after every sentence"],
     "a": "Changing your voice to match the emotion and meaning of the text"},
    {"q": "Which habit best strengthens reading comprehension over time?",
     "o": ["Reading only one type of book", "Asking thoughtful questions before, during, and after reading",
           "Skipping all words that seem too difficult", "Reading only very short sentences"],
     "a": "Asking thoughtful questions before, during, and after reading"},
]
M3 = [
    {"q": "What is the total sum when you add 145 and 278?",
     "o": ["423", "413", "433", "323"], "a": "423"},
    {"q": "What is the perimeter of a square with one side measuring 9 units?",
     "o": ["18 units", "27 units", "36 units", "81 units"], "a": "36 units"},
    {"q": "In the fraction 3/4, what does the bottom number 4 represent?",
     "o": ["The parts we have", "The total equal parts making up the whole",
           "The sum of both numbers", "The difference between two numbers"],
     "a": "The total equal parts making up the whole"},
    {"q": "What is the product of 15 multiplied by 8?",
     "o": ["100", "110", "120", "130"], "a": "120"},
    {"q": "What is the correct term for any flat, closed shape bounded by straight sides?",
     "o": ["Circle", "Sphere", "Polygon", "Cylinder"], "a": "Polygon"},
]
M4 = [
    {"q": "What process transforms liquid water from rivers and oceans into invisible water vapour?",
     "o": ["Condensation", "Evaporation", "Precipitation", "Sublimation"], "a": "Evaporation"},
    {"q": "Which energy source is the primary driver of the entire water cycle?",
     "o": ["The Moon's gravity", "Geothermal vents", "The Sun", "Ocean currents"], "a": "The Sun"},
    {"q": "What forms when rising water vapour cools and condenses in the atmosphere?",
     "o": ["Raindrops on a window", "Clouds", "Underground rivers", "Aquifers"], "a": "Clouds"},
    {"q": "Which of the following is an example of precipitation?",
     "o": ["A puddle drying in the sun", "Snow falling from the sky",
           "Steam rising from boiling water", "Ice melting in a glass"], "a": "Snow falling from the sky"},
    {"q": "What is the name for an underground layer of permeable rock holding large amounts of freshwater?",
     "o": ["A cloud layer", "An aquifer", "The stratosphere", "A water table valve"], "a": "An aquifer"},
]

# ─── Module config ────────────────────────────────────────────────────────────
MODS = {
    'module_1': {
        'k':'1','label':'Reading','icon':'📖',
        'sub':'Understanding Stories and Words',
        'teacher':'Ms. Santos · Grade 4 English',
        'bg':'linear-gradient(130deg,#1a56db 0%,#0071e3 55%,#32ade6 100%)',
        'ibg':'rgba(0,113,227,0.1)','chip':'cb',
        'quiz':M1,'next':'module_2',
        'umsg':'🗣️  Reading Fluency is now unlocked!',
        'topics':[
            ('📚','rgba(0,113,227,0.1)','1.0 — Elements of a Story',
             'Every story is built from essential building blocks that work together to create meaning and bring '
             'a narrative to life. The <strong>setting</strong> establishes the world of the story — not only '
             'the physical location but also the time period, culture, atmosphere, and mood in which events unfold. '
             'A story set in a rainy medieval castle creates an entirely different feeling from one set on a '
             'sun-drenched modern beach, even when the plot is nearly identical. The <strong>characters</strong> '
             'are the living hearts of any narrative — they can be people, animals, mythical creatures, or even '
             'everyday objects given a personality. Their hopes, fears, flaws, and relationships create the '
             'emotional texture that keeps readers turning pages long after bedtime. The <strong>plot</strong> '
             'is the engine: the carefully ordered chain of events — conflict, rising action, climax, falling '
             'action, resolution — that propels the reader from the opening sentence to the very last word. '
             'Mastering these three elements gives you a reliable lens through which to read, analyse, and '
             'enjoy any story you encounter, from picture books to classic literature.'),
            ('🔍','rgba(40,205,65,0.1)','1.1 — Finding the Main Idea',
             'Every well-written paragraph revolves around a single central point called the <strong>main '
             'idea</strong>. This is the author\'s primary message — the one thing they most want you to '
             'understand and remember. Skilled readers train themselves to locate this quickly by looking for '
             'the <strong>topic sentence</strong>, which typically appears at or near the beginning of a '
             'paragraph and announces its subject clearly. The sentences that follow — called '
             '<strong>supporting details</strong> — provide evidence, examples, statistics, anecdotes, or '
             'descriptions that expand on and reinforce the topic sentence. One reliable technique is to pause '
             'after reading any paragraph and ask yourself: "If I had to express this entire paragraph in a '
             'single sentence, what would it say?" That mental summary is almost always the main idea. '
             'Apply this skill consistently across every text you read — newspaper articles, science chapters, '
             'social media posts — and complex material will feel far more approachable and manageable.'),
            ('💡','rgba(255,159,10,0.1)','1.2 — Using Context Clues',
             'Encountering an unfamiliar word mid-sentence does not have to interrupt your reading flow. '
             'Skilled readers use <strong>context clues</strong> — the words, phrases, sentences, and even '
             'images surrounding the unknown term — to make an educated, confident guess about its meaning. '
             'There are several recognisable types. <strong>Definition clues</strong> occur when the author '
             'helpfully explains a word immediately after using it, often signalled by phrases like "which '
             'means," "that is," or "in other words." <strong>Synonym clues</strong> appear when a nearby '
             'word shares a similar meaning, allowing comparison. <strong>Antonym clues</strong> use contrast '
             'words like "but," "however," "unlike," or "instead" to hint at the opposite meaning. '
             '<strong>Example clues</strong> illustrate a word\'s meaning through specific, concrete instances. '
             'The wider and more varied your reading, the sharper your ability to use context clues '
             'becomes — turning every unfamiliar word into an exciting opportunity to expand your vocabulary.'),
            ('✍️','rgba(191,90,242,0.1)','1.3 — Building Your Vocabulary',
             'A rich vocabulary is among the most powerful tools any reader, writer, thinker, or communicator '
             'can possess. Words are the instruments of thought — the more precise and varied your vocabulary, '
             'the more accurately and vividly you can both understand the world and express your own ideas. '
             'One deeply effective strategy is keeping a <strong>personal vocabulary journal</strong>: a '
             'dedicated notebook or digital file where you record new words, their precise definitions, '
             'the original sentence in which you found them, and an original example sentence you craft '
             'yourself. Cognitive science research consistently shows that <strong>spaced repetition</strong> '
             '— revisiting new words at gradually increasing intervals (1 day, 3 days, 1 week, 1 month) — '
             'produces dramatically stronger long-term retention than last-minute cramming. Another proven '
             'strategy is studying <strong>Greek and Latin word roots, prefixes, and suffixes</strong>. '
             'For example, knowing that the Latin root <em>port</em> means "to carry" instantly unlocks '
             'transport, import, export, portable, portfolio, and deportation. Vocabulary knowledge is '
             'wonderfully cumulative — each new word you learn makes learning the next one marginally easier.'),
        ],
    },
    'module_2': {
        'k':'2','label':'Reading Fluency','icon':'🗣️',
        'sub':'Speed, Expression & Deep Comprehension',
        'teacher':'Ms. Santos · Grade 4 English (Advanced)',
        'bg':'linear-gradient(130deg,#6d28d9 0%,#bf5af2 55%,#e879a8 100%)',
        'ibg':'rgba(191,90,242,0.1)','chip':'cp',
        'quiz':M2,'next':'module_3',
        'umsg':'🔢  Mathematics is now unlocked!',
        'topics':[
            ('🎯','rgba(191,90,242,0.1)','2.0 — What Is Reading Fluency?',
             'Reading fluency is the essential <strong>bridge between recognising individual words on a page '
             'and truly comprehending what you read</strong>. A fluent reader moves through text with three '
             'interlocking qualities: <strong>accuracy</strong> (decoding words correctly without errors), '
             '<strong>automaticity</strong> (recognising words instantly without conscious, laborious effort), '
             'and <strong>prosody</strong> (reading with natural rhythm, appropriate pacing, meaningful pauses, '
             'and expressive intonation that mirrors natural speech). When reading is effortful and halting, '
             'virtually all of a reader\'s mental energy is consumed by simply decoding individual words, '
             'leaving little or no cognitive capacity remaining for higher-order thinking: inferring meaning, '
             'questioning the author, visualising scenes, or connecting ideas. Fluency liberates the brain '
             'to operate at a genuinely higher level. Decades of reading research have consistently identified '
             'fluency as one of the strongest individual predictors of overall reading comprehension — which '
             'means developing it is not optional; it is absolutely foundational.'),
            ('🔄','rgba(0,113,227,0.1)','2.1 — The Power of Repeated Reading',
             '<strong>Repeated reading</strong> is one of the most elegantly simple yet strikingly powerful '
             'techniques in all of reading instruction. The method is straightforward: select a short, '
             'engaging passage — typically 50 to 200 words — and read it aloud multiple times (usually '
             'three to five), tracking your own accuracy, expression, and fluency as you improve with each '
             'reading. On your very first encounter, you are largely decoding. By your second reading, you '
             'begin to feel the natural shape and rhythm of sentences. By the third and fourth, you are '
             'reading with genuine expression and a level of comprehension you could not access before. '
             'Think of how a musician learns a new piece: they do not play it once and declare mastery. '
             'They rehearse it, refine it, identify trouble spots, slow down for difficult passages, and '
             'gradually build toward a confident, expressive performance. Reading is the same kind of '
             'practised, deliberate skill. A powerful companion to this technique is <strong>paired '
             'reading</strong>, where a more skilled reader sits beside a developing reader, reading aloud '
             'together as a team — providing an immediate, real-time model of fluent, expressive reading '
             'while allowing the learner to gradually take more and more responsibility.'),
            ('👁️','rgba(40,205,65,0.1)','2.2 — Sight Words and Automaticity',
             'Research in reading science has revealed a remarkable fact: a relatively small set of '
             'high-frequency words — sometimes called <strong>sight words</strong> — accounts for an '
             'astonishing proportion of all written English text. Words like "the," "and," "said," '
             '"because," "through," "could," "would," and "there" appear on virtually every single page. '
             'When a reader must laboriously decode these extremely common words character by character '
             'on every encounter, reading becomes painfully slow and mentally exhausting, draining energy '
             'that should be directed toward comprehension. The goal is complete <strong>automaticity</strong> '
             '— recognising these words as whole, instant, effortless units, in the same way a fluent '
             'speaker recognises spoken words without consciously processing each individual phoneme. '
             'Reading scientists call this process <strong>orthographic mapping</strong> — the deep '
             'encoding of a word\'s spelling, pronunciation, and meaning into long-term memory as a '
             'single, retrievable unit. Proven methods include systematic flashcard practice, classroom '
             'word walls, word sorts, word games, and — most powerfully — wide, regular, and pleasurable '
             'independent reading, which provides the repeated, meaningful exposures necessary for '
             'words to become truly automatic.'),
            ('🧠','rgba(255,159,10,0.1)','2.3 — Active Comprehension Strategies',
             'Deep, lasting reading comprehension is not a passive activity — it is an active, ongoing, '
             'and intentional conversation between the reader and the text. Expert readers do not simply '
             'absorb words and hope meaning arrives; they deploy a toolkit of deliberate mental strategies '
             'that transform passive decoding into active sense-making. <strong>Predicting</strong> means '
             'forming expectations about what will happen next, based on evidence in the text and your '
             'own background knowledge, then confirming or revising those predictions as you read. '
             '<strong>Questioning</strong> involves generating your own genuine questions — "Why did the '
             'character do that?", "What will happen if...?", "Do I agree with this argument?" — '
             'transforming you from a recipient into a critical thinker. <strong>Visualising</strong> '
             'means constructing a vivid, detailed mental movie of settings, characters, actions, and '
             'emotions — research consistently shows that strong visualisation dramatically improves '
             'both comprehension and memory. <strong>Summarising</strong> requires you to identify '
             'what truly matters and restate it concisely in your own words — a skill that reveals '
             'whether you have genuinely understood or merely recognised words. <strong>Making '
             'connections</strong> — linking new information to your personal experience, to other '
             'texts, or to the wider world — is the mechanism by which truly deep and durable '
             'understanding is formed and retained.'),
        ],
    },
    'module_3': {
        'k':'3','label':'Mathematics','icon':'🔢',
        'sub':'Foundational Operations and Geometry',
        'teacher':'Mr. Reyes · Grade 4 Mathematics',
        'bg':'linear-gradient(130deg,#1a7a38 0%,#28cd41 55%,#a8e063 100%)',
        'ibg':'rgba(40,205,65,0.1)','chip':'cg',
        'quiz':M3,'next':'module_4',
        'umsg':'🌍  Natural Sciences is now unlocked!',
        'topics':[
            ('➕','rgba(40,205,65,0.1)','3.0 — The Four Basic Operations',
             'All of mathematics rests on four fundamental operations that allow us to manipulate, '
             'compare, and understand numbers in every conceivable context. <strong>Addition</strong> '
             'combines two or more quantities to find their total sum — asking, in essence, "how many '
             'altogether?" <strong>Subtraction</strong> is addition\'s inverse, finding the difference '
             'between quantities — asking "how many remain?" or "how much more?" <strong>Multiplication</strong> '
             'is a powerful and elegant shortcut for repeated addition: rather than laboriously adding '
             '9 together seven separate times, we express this instantly as 9 × 7 = 63. Understanding '
             'multiplication conceptually — not merely as a set of facts to memorise — is the gateway '
             'to virtually all advanced mathematics, from algebra to calculus. <strong>Division</strong> '
             'is multiplication\'s inverse, partitioning a quantity into equal groups. Mastering all four '
             'operations with genuine fluency — so they require no conscious effort, freeing mental '
             'resources for higher-level reasoning — is a non-negotiable foundation for mathematical '
             'success at every stage of education and life.'),
            ('½','rgba(0,113,227,0.1)','3.1 — Understanding Fractions',
             'A fraction is a precise, powerful mathematical tool for representing any part of a whole. '
             'When we write ¾, the number on top — the <strong>numerator</strong> (3) — tells us how '
             'many equal parts we currently possess or are considering. The number on the bottom — the '
             '<strong>denominator</strong> (4) — tells us into how many equal parts the whole has been '
             'divided. Imagine a rectangular chocolate bar divided into four equal pieces: eating three '
             'of those pieces means you have consumed ¾ of the bar. The denominator can '
             '<strong>never be zero</strong>, because dividing something into zero parts is a '
             'mathematical impossibility — it carries no coherent meaning whatsoever. Fractions can be '
             'classified as <strong>proper</strong> (numerator smaller than denominator, like ⅔, '
             'representing less than one whole), <strong>improper</strong> (numerator larger, like 7/4, '
             'representing more than one whole), or expressed as <strong>mixed numbers</strong> '
             '(combining a whole number and a proper fraction, like 1¾). A thorough understanding of '
             'fractions is the direct foundation for decimals, percentages, ratios, rates, and '
             'the algebraic thinking that defines secondary mathematics.'),
            ('📐','rgba(255,159,10,0.1)','3.2 — Shapes, Perimeter, and Area',
             'Geometry is the magnificent branch of mathematics devoted to understanding the properties, '
             'relationships, and measurements of points, lines, angles, surfaces, and solid figures. '
             'A <strong>polygon</strong> is any flat, closed, two-dimensional figure entirely bounded by '
             'straight sides. Polygons are classified by the number of their sides: triangle (3 sides), '
             'quadrilateral (4 sides), pentagon (5 sides), hexagon (6 sides), heptagon (7 sides), '
             'and octagon (8 sides). Two of the most essential measurements associated with any flat shape '
             'are its <strong>perimeter</strong> and its <strong>area</strong>. The perimeter is the total '
             'distance around the complete outer boundary of a shape — imagine an ant walking all the way '
             'around the edge without ever leaving it and measuring every millimetre of its journey. For a '
             'rectangle, perimeter = 2 × (length + width). The area, by contrast, measures how much flat '
             'surface the shape covers — how many unit squares fit perfectly inside it. For a rectangle, '
             'area = length × width. Real-world applications are everywhere: a builder uses perimeter to '
             'calculate how much baseboard to purchase; a painter uses area to determine how much paint '
             'to mix; a farmer uses both to plan fields and fencing simultaneously.'),
        ],
    },
    'module_4': {
        'k':'4','label':'Natural Sciences','icon':'🌍',
        'sub':'The Hydrological Cycle',
        'teacher':'Ms. Cruz · Grade 4 Science',
        'bg':'linear-gradient(130deg,#92400e 0%,#ff9f0a 55%,#fbbf24 100%)',
        'ibg':'rgba(255,159,10,0.1)','chip':'co',
        'quiz':M4,'next':None,
        'umsg':'🎉  Congratulations — you have completed all modules!',
        'topics':[
            ('🌊','rgba(0,113,227,0.1)','4.0 — Introduction to the Water Cycle',
             'The water cycle — known scientifically as the <strong>hydrological cycle</strong> — is '
             'one of Earth\'s most fundamental and life-sustaining natural processes. It describes the '
             'continuous, perpetual journey of water as it moves and transforms among Earth\'s surface '
             '(oceans, rivers, lakes, glaciers, soil), its atmosphere, and its underground systems. '
             'Water is never created or destroyed in this process; it simply changes its physical state '
             '(liquid, gas, or solid) and its location, cycling through the same pathways it has '
             'followed for approximately 4.5 billion years. The total volume of water on Earth has '
             'remained essentially constant since our planet formed. This extraordinary continuity '
             'means that the water flowing from your tap today has, at some earlier moment in deep '
             'geological history, filled a prehistoric ocean, nourished a dinosaur, been locked inside '
             'an Antarctic glacier, and fallen as rain over a distant mountain range. Understanding '
             'the water cycle is fundamental to meteorology, hydrology, ecology, agriculture, '
             'and the science of climate change.'),
            ('☀️','rgba(255,159,10,0.1)','4.1 — Evaporation and Condensation',
             '<strong>Evaporation</strong> is the process by which the Sun\'s tremendous thermal '
             'energy heats liquid water at Earth\'s surface — primarily in oceans, seas, rivers, '
             'and lakes — converting it into water vapour, an invisible gas that rises buoyantly '
             'into the atmosphere. Roughly 90% of all atmospheric water vapour originates from '
             'ocean evaporation; the remaining 10% comes from the transpiration of land plants '
             '(collectively called <strong>evapotranspiration</strong>). As water vapour rises '
             'higher into the troposphere, it encounters progressively colder temperatures. When '
             'the vapour cools below a critical threshold called the <strong>dew point</strong>, '
             'it undergoes <strong>condensation</strong> — reverting from an invisible gas back '
             'into microscopic liquid water droplets or tiny ice crystals. These minuscule particles '
             'cling to even tinier specks of dust, sea salt, pollen, and pollution particles '
             'suspended in the air (called condensation nuclei), clustering together to form the '
             'visible, billowing clouds we observe drifting across the sky — each one carrying '
             'enormous quantities of water across potentially thousands of kilometres.'),
            ('🌧️','rgba(40,205,65,0.1)','4.2 — Precipitation and Collection',
             'As clouds continue to grow — accumulating ever-greater quantities of condensed '
             'water droplets through ongoing condensation — gravity eventually overcomes the '
             'atmospheric forces that have been keeping the droplets suspended aloft. Water then '
             'falls back to Earth\'s surface as <strong>precipitation</strong>. The precise form '
             'precipitation takes is determined by the temperature of the atmosphere through which '
             'it falls: <strong>rain</strong> forms when temperatures remain above freezing '
             'throughout the atmosphere; <strong>snow</strong> forms when temperatures stay below '
             'freezing from cloud to ground; <strong>sleet</strong> forms when falling raindrops '
             'refreeze before reaching the ground; and <strong>hail</strong> forms when powerful '
             'updrafts inside intense thunderstorms repeatedly carry ice pellets back upward '
             'before they finally fall. Once precipitation reaches Earth\'s surface, collected '
             'water takes multiple pathways simultaneously: it replenishes oceans, seas, lakes, '
             'rivers, and reservoirs; it is drawn up by plant roots and eventually transpired '
             'back into the atmosphere; it seeps into soil through <strong>infiltration</strong> '
             'and percolates downward through layers of rock and sediment to recharge underground '
             '<strong>aquifers</strong> — vast, slow-moving reservoirs of freshwater capable of '
             'sustaining entire cities, ecosystems, and civilisations long after rainfall has ceased.'),
        ],
    },
}

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-logo">Danilo</div>
        <div class="sb-tagline">Learning Platform</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<span class="sb-section">Main</span>', unsafe_allow_html=True)
    st.button("🏠  Home",      on_click=nav, args=('dashboard',), use_container_width=True)
    st.button("📊  My Grades", on_click=nav, args=('profile',),   use_container_width=True)

    st.markdown('<span class="sb-section">Courses</span>', unsafe_allow_html=True)
    for mk, mod in MODS.items():
        locked = mk not in st.session_state.unlocked_modules
        lbl = f"{'🔒' if locked else mod['icon']}  {mod['label']}"
        st.button(lbl, on_click=nav, args=(mk,), disabled=locked, use_container_width=True)

    st.markdown("""
    <div class="sb-footer">© 2025 Danilo Learning<br>All rights reserved.</div>
    """, unsafe_allow_html=True)

# ─── Helper: header ───────────────────────────────────────────────────────────
def page_header(icon, title):
    st.markdown(f"""
    <div class="pheader">
        <span class="pheader-icon">{icon}</span>
        <span class="pheader-title">{title}</span>
        <div class="pheader-avatar">D</div>
    </div>""", unsafe_allow_html=True)

# ─── VIEWS ────────────────────────────────────────────────────────────────────
st.markdown('<div class="main-wrap">', unsafe_allow_html=True)

# ── DASHBOARD ─────────────────────────────────────────────────────────────────
if st.session_state.current_view == 'dashboard':
    page_header("🏠", "Home")

    # Hero
    st.markdown("""
    <div class="hero">
        <div class="hero-eyebrow">Welcome back, Danilo</div>
        <div class="hero-headline">Ready to learn<br>something new today?</div>
        <div class="hero-sub">Complete courses in order to unlock the next challenge.</div>
    </div>""", unsafe_allow_html=True)

    # Stats
    all_m = ['1','2','3','4']
    scores_taken = [st.session_state[f'm{m}_quiz_score']
                    for m in all_m if st.session_state[f'm{m}_quiz_submitted']]
    avg_acc  = (sum(scores_taken) / (len(scores_taken)*5) * 100) if scores_taken else 0
    passed   = sum(1 for m in all_m
                   if st.session_state[f'm{m}_quiz_submitted']
                   and st.session_state[f'm{m}_quiz_score'] >= 4)
    unlocked = len(st.session_state.unlocked_modules)

    s1, s2, s3, s4 = st.columns(4, gap="small")
    for col, val, lbl, color, pct, ei in [
        (s1, f"{unlocked}/4",         "Unlocked",  "#0071e3", unlocked/4*100,  "e1"),
        (s2, f"{passed}/4",           "Passed",    "#28cd41", passed/4*100,    "e2"),
        (s3, f"{avg_acc:.0f}%",       "Accuracy",  "#ff9f0a", avg_acc,         "e3"),
        (s4, f"{int(passed/4*100)}%", "Progress",  "#bf5af2", passed/4*100,    "e4"),
    ]:
        with col:
            st.markdown(f"""
            <div class="sc {ei}">
                <div class="sc-val" style="color:{color};">{val}</div>
                <div class="sc-lbl">{lbl}</div>
                <div class="sc-bar">
                    <div class="sc-fill" style="width:{min(pct,100):.0f}%;background:{color};"></div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-label au e5">Your Courses</div>', unsafe_allow_html=True)

    items = list(MODS.items())
    for row in range(0, len(items), 2):
        c1, c2 = st.columns(2, gap="medium")
        for ci, (mk, mod) in enumerate(items[row: row+2]):
            locked    = mk not in st.session_state.unlocked_modules
            m         = mod['k']
            submitted = st.session_state[f'm{m}_quiz_submitted']
            score     = st.session_state[f'm{m}_quiz_score']
            done      = submitted and score >= 4
            badge = (
                '<span class="chip cg">✓ Completed</span>' if done
                else '<span class="chip cz">🔒 Locked</span>' if locked
                else '<span class="chip cb">● Open</span>'
            )
            ei = f"e{min(row*2+ci+1,8)}"
            col = c1 if ci == 0 else c2
            with col:
                st.markdown(f"""
                <div class="ccard {ei}">
                    <div class="cthumb" style="background:{mod['bg']};">
                        <div class="cthumb-dots"></div>
                        <div class="cthumb-icon">{mod['icon']}</div>
                        <div class="cthumb-name">{mod['label']}</div>
                    </div>
                    <div class="cbody">
                        <div class="cdesc">
                            {mod['sub']}<br>
                            <span style="font-size:0.7rem;color:var(--muted);">{mod['teacher']}</span>
                        </div>
                        <div class="cfoot">
                            {badge}
                            <span class="ccount">{len(mod['quiz'])} questions</span>
                        </div>
                    </div>
                </div>""", unsafe_allow_html=True)
                st.button(
                    "Open →" if not locked else "Locked",
                    key=f"d_{mk}", on_click=nav, args=(mk,),
                    disabled=locked, use_container_width=True,
                )

# ── MODULE VIEW ───────────────────────────────────────────────────────────────
elif st.session_state.current_view in MODS:
    mk  = st.session_state.current_view
    mod = MODS[mk]
    m   = mod['k']
    qd  = mod['quiz']

    page_header(mod['icon'], mod['label'])
    st.button("← Back to Home", key=f"bk_{mk}", on_click=nav, args=('dashboard',))
    st.markdown('<div style="height:6px"></div>', unsafe_allow_html=True)

    # Module hero
    st.markdown(f"""
    <div class="mhero" style="background:{mod['bg']};">
        <span class="mhero-ico">{mod['icon']}</span>
        <div class="mhero-title">{mod['label']}</div>
        <div class="mhero-sub">{mod['sub']}</div>
        <div class="mhero-chips">
            <span class="gchip">👩‍🏫 {mod['teacher']}</span>
            <span class="gchip">📝 {len(qd)}-question quiz</span>
            <span class="gchip">📖 {len(mod['topics'])} lessons</span>
            <span class="gchip">⏱ ~15 min</span>
        </div>
    </div>""", unsafe_allow_html=True)

    # Lessons
    st.markdown('<div class="sec-label">Lesson Material</div>', unsafe_allow_html=True)
    for i, (ico, ibg, title, body) in enumerate(mod['topics']):
        st.markdown(f"""
        <div class="tcard e{i+1}">
            <div class="thead">
                <div class="ticon" style="background:{ibg};">{ico}</div>
                <div class="ttitle">{title}</div>
            </div>
            <p class="tbody">{body}</p>
        </div>""", unsafe_allow_html=True)

    # Quiz
    pm = len(qd) - 1
    st.markdown(f"""
    <div class="qbar">
        <div class="qbar-ico">📋</div>
        <div>
            <p class="qbar-title">Formative Assessment</p>
            <p class="qbar-sub">{len(qd)} questions · Pass mark: {pm}/{len(qd)} · Unlimited retries</p>
        </div>
    </div>""", unsafe_allow_html=True)

    sk = f'm{m}_quiz_started'
    uk = f'm{m}_quiz_submitted'
    ck = f'm{m}_quiz_score'

    if not st.session_state[sk]:
        st.button("▶  Start Assessment", key=f"st_{mk}")
        if st.session_state.get(f'st_{mk}'):
            st.session_state[sk] = True
            st.rerun()

    if st.session_state[sk]:
        with st.form(key=f'{mk}_form', clear_on_submit=False):
            answers = []
            for i, q in enumerate(qd):
                st.markdown(f'<div class="qlabel">Question {i+1} of {len(qd)}</div>',
                             unsafe_allow_html=True)
                st.markdown(f"**{q['q']}**")
                a = st.radio("", q['o'], key=f"{mk}_q{i}",
                             label_visibility="collapsed", index=None)
                answers.append(a)
                if i < len(qd) - 1:
                    st.markdown('<hr class="div-line">', unsafe_allow_html=True)
            st.markdown('<div style="height:6px"></div>', unsafe_allow_html=True)
            sub = st.form_submit_button("Submit Assessment")

        if sub:
            if None in answers:
                st.error("⚠️  Please answer every question before submitting.")
            else:
                score = sum(1 for i, q in enumerate(qd) if answers[i] == q['a'])
                st.session_state[ck] = score
                st.session_state[uk] = True

        if st.session_state[uk]:
            score  = st.session_state[ck]
            passed = score >= pm
            pct    = int(score / len(qd) * 100)

            if passed:
                st.markdown(f"""
                <div class="rcard rpass">
                    <div>
                        <div class="rscore">{score}/{len(qd)}</div>
                        <div class="rbadge">✓ Competency Verified</div>
                    </div>
                    <div class="rmsg">
                        <strong>Outstanding work.</strong> You scored {pct}% and have demonstrated
                        solid mastery of this topic. Your performance unlocks the next course in the sequence.<br><br>
                        <span style="color:#28cd41;font-weight:600;">{mod['umsg']}</span>
                    </div>
                </div>""", unsafe_allow_html=True)
                nxt = mod.get('next')
                if nxt and nxt not in st.session_state.unlocked_modules:
                    st.session_state.unlocked_modules.append(nxt)
            else:
                st.markdown(f"""
                <div class="rcard rfail">
                    <div>
                        <div class="rscore">{score}/{len(qd)}</div>
                        <div class="rbadge">✗ Below Pass Mark</div>
                    </div>
                    <div class="rmsg">
                        <strong>Keep going.</strong> You scored {pct}%.
                        Revisit the lesson material above — pay close attention to any sections
                        you found confusing — then try again. You need {pm}/{len(qd)} to pass.
                    </div>
                </div>""", unsafe_allow_html=True)
                if st.button("🔄  Retry Assessment", key=f"rt_{mk}"):
                    st.session_state[uk] = False
                    st.rerun()

# ── GRADES ────────────────────────────────────────────────────────────────────
elif st.session_state.current_view == 'profile':
    page_header("📊", "My Grades")
    st.button("← Back to Home", key="bk_g", on_click=nav, args=('dashboard',))
    st.markdown('<div style="height:10px"></div>', unsafe_allow_html=True)

    all_m  = ['1','2','3','4']
    subs   = {m: st.session_state[f'm{m}_quiz_submitted'] for m in all_m}
    scores = {m: st.session_state[f'm{m}_quiz_score']     for m in all_m}
    taken  = [scores[m] for m in all_m if subs[m]]
    avg_a  = (sum(taken) / (len(taken)*5) * 100) if taken else 0
    comp   = sum(1 for m in all_m if subs[m] and scores[m] >= 4)
    unl    = len(st.session_state.unlocked_modules)

    g1, g2, g3 = st.columns(3, gap="medium")
    for col, val, lbl, color, pct in [
        (g1, f"{unl}/4",          "Courses Unlocked", "#0071e3", unl/4*100),
        (g2, f"{avg_a:.0f}%",     "Mean Accuracy",    "#28cd41", avg_a),
        (g3, f"{int(comp/4*100)}%","Progress",        "#bf5af2", comp/4*100),
    ]:
        with col:
            st.markdown(f"""
            <div class="sc">
                <div class="sc-val" style="color:{color};">{val}</div>
                <div class="sc-lbl">{lbl}</div>
                <div class="sc-bar">
                    <div class="sc-fill" style="width:{min(pct,100):.0f}%;background:{color};"></div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div style="height:18px"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sec-label">Gradebook</div>', unsafe_allow_html=True)

    rows = ""
    for mk, mod in MODS.items():
        m     = mod['k']
        total = len(mod['quiz'])
        locked = mk not in st.session_state.unlocked_modules
        sub    = subs[m]; sc = scores[m]; done = sub and sc >= 4

        if locked:
            sh = '<span class="chip cz">🔒 Locked</span>'
            sd = gd = '<span style="color:var(--muted);">—</span>'
        elif done:
            sh = '<span class="chip cg">✓ Passed</span>'
            sd = f'<span class="gmono" style="color:#1a9430;">{sc}/{total}</span>'
            gd = f'<span class="gmono" style="color:#1a9430;">{int(sc/total*100)}%</span>'
        elif sub:
            sh = '<span class="chip cr">✗ Below Pass</span>'
            sd = f'<span class="gmono" style="color:#c0392b;">{sc}/{total}</span>'
            gd = f'<span class="gmono" style="color:#c0392b;">{int(sc/total*100)}%</span>'
        else:
            sh = '<span class="chip cz">○ Not Started</span>'
            sd = gd = '<span style="color:var(--muted);">—</span>'

        rows += f"""
        <tr>
            <td style="font-size:1.1rem;width:34px;">{mod['icon']}</td>
            <td style="font-weight:600;color:var(--text);">{mod['label']}</td>
            <td style="color:var(--sub);font-size:0.8rem;">{mod['sub']}</td>
            <td>{sh}</td>
            <td>{sd}</td>
            <td>{gd}</td>
        </tr>"""

    st.markdown(f"""
    <table class="gtable">
        <thead>
            <tr>
                <th></th><th>Course</th><th>Topic</th>
                <th>Status</th><th>Score</th><th>Grade</th>
            </tr>
        </thead>
        <tbody>{rows}</tbody>
    </table>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close main-wrap
