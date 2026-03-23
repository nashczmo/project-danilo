import streamlit as st
import os

if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write(
        '[theme]\nbase="light"\nprimaryColor="#007aff"\n'
        'backgroundColor="#f2f2f7"\nsecondaryBackgroundColor="#ffffff"\n'
        'textColor="#1d1d1f"\nfont="sans serif"\n'
    )

st.set_page_config(
    page_title="DANILO Learning",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────────────────────
#  GLOBAL CSS  ·  Apple-inspired design system
# ─────────────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=DM+Serif+Display&display=swap');

:root {
    --bg:            #f2f2f7;
    --surface:       #ffffff;
    --surface2:      #f8f8fa;
    --border:        rgba(0,0,0,0.08);
    --text-primary:  #1d1d1f;
    --text-secondary:#6e6e73;
    --text-tertiary: #aeaeb2;
    --blue:          #007aff;
    --green:         #34c759;
    --orange:        #ff9500;
    --red:           #ff3b30;
    --purple:        #af52de;
    --indigo:        #5856d6;
    --radius-sm:     10px;
    --radius-md:     16px;
    --radius-lg:     22px;
    --shadow-sm:     0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
    --shadow-md:     0 4px 24px rgba(0,0,0,0.08), 0 1px 3px rgba(0,0,0,0.05);
    --shadow-lg:     0 12px 40px rgba(0,0,0,0.12), 0 4px 12px rgba(0,0,0,0.06);
    --t:             0.25s cubic-bezier(0.4,0,0.2,1);
}

html, body, [class*="css"] {
    font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, 'SF Pro Text', sans-serif !important;
    -webkit-font-smoothing: antialiased;
    letter-spacing: -0.01em;
}
.stApp { background: var(--bg) !important; }
#MainMenu, footer { visibility: hidden; }

.block-container {
    padding: 1.5rem 1.75rem 6rem !important;
    max-width: 960px !important;
}

/* ── Sidebar glass ───────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: rgba(255,255,255,0.88) !important;
    backdrop-filter: blur(40px) saturate(1.8) !important;
    -webkit-backdrop-filter: blur(40px) saturate(1.8) !important;
    border-right: 1px solid var(--border) !important;
}
section[data-testid="stSidebar"] > div { padding-top: 0 !important; }

/* Always-visible sidebar toggle */
[data-testid="collapsedControl"] {
    visibility: visible !important;
    display: flex !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 14px !important;
    left: 14px !important;
    z-index: 99999 !important;
    width: 40px !important;
    height: 40px !important;
    background: rgba(255,255,255,0.92) !important;
    backdrop-filter: blur(20px) !important;
    border-radius: var(--radius-sm) !important;
    box-shadow: var(--shadow-md) !important;
    border: 1px solid var(--border) !important;
    transition: box-shadow var(--t) !important;
    cursor: pointer !important;
}
[data-testid="collapsedControl"]:hover {
    box-shadow: var(--shadow-lg) !important;
}

/* ── Sidebar content ─────────────────────────────────── */
.sb-brand {
    padding: 1.6rem 1.3rem 1.2rem;
    border-bottom: 1px solid var(--border);
    margin-bottom: 0.4rem;
    animation: fadeInDown 0.4s ease both;
}
.sb-wordmark {
    font-family: 'DM Serif Display', Georgia, serif !important;
    font-size: 1.5rem;
    font-weight: 400;
    color: var(--text-primary);
    letter-spacing: -0.03em;
    line-height: 1;
    margin-bottom: 3px;
}
.sb-sub {
    font-size: 0.67rem;
    font-weight: 700;
    color: var(--text-tertiary);
    text-transform: uppercase;
    letter-spacing: 0.1em;
}
.sb-section {
    display: block;
    font-size: 0.67rem !important;
    font-weight: 700 !important;
    color: var(--text-tertiary) !important;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    padding: 0.85rem 1.3rem 0.25rem !important;
}

/* ── Buttons ──────────────────────────────────────────── */
div[data-testid="stButton"] > button {
    font-family: 'DM Sans', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.88rem !important;
    border: none !important;
    border-radius: var(--radius-sm) !important;
    padding: 0.55rem 1rem !important;
    transition: all var(--t) !important;
    letter-spacing: -0.01em !important;
    background: transparent !important;
    color: var(--text-primary) !important;
    text-align: left !important;
    cursor: pointer !important;
}
div[data-testid="stButton"] > button:hover {
    background: rgba(0,122,255,0.08) !important;
    color: var(--blue) !important;
    transform: translateX(2px) !important;
}
div[data-testid="stButton"] > button:active {
    transform: scale(0.97) translateX(0) !important;
}
div[data-testid="stForm"] div[data-testid="stButton"] > button {
    background: var(--blue) !important;
    color: #fff !important;
    border-radius: var(--radius-md) !important;
    padding: 0.75rem 2rem !important;
    font-weight: 600 !important;
    font-size: 0.92rem !important;
    box-shadow: 0 2px 12px rgba(0,122,255,0.3) !important;
    text-align: center !important;
    width: auto !important;
}
div[data-testid="stForm"] div[data-testid="stButton"] > button:hover {
    background: #0062cc !important;
    box-shadow: 0 6px 20px rgba(0,122,255,0.4) !important;
    transform: translateY(-1px) !important;
}

/* ── Radios ───────────────────────────────────────────── */
div[role="radiogroup"] {
    background: var(--surface2) !important;
    border: 1px solid var(--border) !important;
    border-radius: var(--radius-md) !important;
    padding: 1.1rem 1.3rem !important;
    margin-bottom: 0.75rem !important;
    box-shadow: none !important;
    transition: border-color var(--t), box-shadow var(--t) !important;
}
div[role="radiogroup"]:focus-within {
    border-color: rgba(0,122,255,0.35) !important;
    box-shadow: 0 0 0 3px rgba(0,122,255,0.1) !important;
}

/* ── Keyframes ────────────────────────────────────────── */
@keyframes fadeInUp {
    from { opacity:0; transform:translateY(18px); }
    to   { opacity:1; transform:translateY(0); }
}
@keyframes fadeInDown {
    from { opacity:0; transform:translateY(-10px); }
    to   { opacity:1; transform:translateY(0); }
}
@keyframes scaleIn {
    from { opacity:0; transform:scale(0.95); }
    to   { opacity:1; transform:scale(1); }
}
@keyframes popIn {
    from { opacity:0; transform:scale(0.85); }
    to   { opacity:1; transform:scale(1); }
}
.au  { animation: fadeInUp 0.5s cubic-bezier(0.4,0,0.2,1) both; }
.asi { animation: scaleIn  0.4s cubic-bezier(0.4,0,0.2,1) both; }
.api { animation: popIn    0.45s cubic-bezier(0.34,1.56,0.64,1) both; }
.d1  { animation-delay: 0.04s; }
.d2  { animation-delay: 0.09s; }
.d3  { animation-delay: 0.14s; }
.d4  { animation-delay: 0.19s; }
.d5  { animation-delay: 0.24s; }
.d6  { animation-delay: 0.29s; }
.d7  { animation-delay: 0.34s; }
.d8  { animation-delay: 0.39s; }

/* ── Sticky page-header bar ──────────────────────────── */
.ph {
    background: rgba(255,255,255,0.78);
    backdrop-filter: blur(30px) saturate(1.6);
    border-bottom: 1px solid var(--border);
    padding: 0.85rem 1.75rem;
    margin: -1.5rem -1.75rem 1.75rem;
    display: flex;
    align-items: center;
    gap: 0.75rem;
    position: sticky;
    top: 0;
    z-index: 100;
    animation: fadeInDown 0.3s ease both;
}
.ph-title {
    font-family: 'DM Serif Display', serif !important;
    font-size: 1.12rem;
    font-weight: 400;
    color: var(--text-primary);
    letter-spacing: -0.02em;
    margin: 0;
}
.ph-avatar {
    margin-left: auto;
    width: 33px; height: 33px;
    background: linear-gradient(135deg, var(--blue), var(--indigo));
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.82rem; color: #fff; font-weight: 700;
    flex-shrink: 0;
}

/* ── Hero strip ──────────────────────────────────────── */
.hero {
    background: linear-gradient(135deg,#1d1d1f 0%,#3a3a3c 100%);
    border-radius: var(--radius-lg);
    padding: 2rem 2.5rem;
    margin-bottom: 1.75rem;
    position: relative;
    overflow: hidden;
    animation: fadeInUp 0.5s ease both;
}
.hero::before {
    content:'';
    position:absolute; inset:0;
    background: radial-gradient(ellipse at 85% -15%, rgba(0,122,255,0.38) 0%,transparent 55%),
                radial-gradient(ellipse at -10% 110%, rgba(88,86,214,0.28) 0%,transparent 50%);
}
.hero-eyebrow {
    font-size:0.68rem; font-weight:700;
    color:rgba(255,255,255,0.45);
    text-transform:uppercase; letter-spacing:0.12em;
    margin-bottom:0.35rem; position:relative;
}
.hero-title {
    font-family:'DM Serif Display',serif;
    font-size: clamp(1.55rem,3vw,2.3rem);
    font-weight:400; color:#fff;
    letter-spacing:-0.03em; line-height:1.15;
    margin-bottom:0.45rem; position:relative;
}
.hero-sub { font-size:0.88rem; color:rgba(255,255,255,0.55); position:relative; }

/* ── Stat card ───────────────────────────────────────── */
.stat-card {
    background: var(--surface);
    border-radius: var(--radius-md);
    padding: 1.15rem 1rem;
    text-align: center;
    border: 1px solid var(--border);
    box-shadow: var(--shadow-sm);
    animation: fadeInUp 0.5s ease both;
    transition: box-shadow var(--t), transform var(--t);
}
.stat-card:hover { box-shadow: var(--shadow-md); transform: translateY(-2px); }
.stat-val {
    font-family:'DM Serif Display',serif;
    font-size:2rem; font-weight:400;
    letter-spacing:-0.03em; line-height:1;
    margin-bottom:0.25rem;
}
.stat-lbl {
    font-size:0.67rem; font-weight:700;
    color:var(--text-tertiary);
    text-transform:uppercase; letter-spacing:0.09em;
}
.prog-track {
    height:4px; background:rgba(0,0,0,0.06);
    border-radius:99px; overflow:hidden; margin-top:0.7rem;
}
.prog-fill {
    height:100%; border-radius:99px;
    transition: width 0.9s cubic-bezier(0.4,0,0.2,1);
}

/* ── Section eyebrow ─────────────────────────────────── */
.eyebrow {
    font-size:0.67rem; font-weight:700;
    color:var(--text-tertiary);
    text-transform:uppercase; letter-spacing:0.1em;
    margin-bottom:0.75rem; margin-top:0.25rem;
}

/* ── Course card (dashboard) ─────────────────────────── */
.cc {
    background: var(--surface);
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    border: 1px solid var(--border);
    transition: box-shadow var(--t), transform var(--t);
    margin-bottom: 1rem;
    animation: fadeInUp 0.5s cubic-bezier(0.4,0,0.2,1) both;
}
.cc:hover { box-shadow: var(--shadow-lg); transform: translateY(-3px); }
.cc-thumb {
    height: 108px;
    position: relative;
    display: flex; align-items: flex-end;
    padding: 1rem 1.2rem;
    overflow: hidden;
}
.cc-thumb::after {
    content:'';
    position:absolute; inset:0;
    background: linear-gradient(to top, rgba(0,0,0,0.3) 0%, transparent 55%);
}
.cc-dots {
    position:absolute; inset:0;
    background-image: radial-gradient(circle, rgba(255,255,255,0.16) 1.5px, transparent 1.5px);
    background-size: 20px 20px;
}
.cc-icon {
    position:absolute; top:14px; right:16px;
    font-size:2rem; opacity:0.88; z-index:1;
    transition: transform var(--t);
}
.cc:hover .cc-icon { transform: scale(1.12) rotate(-5deg); }
.cc-name {
    font-family:'DM Serif Display',serif;
    font-size:1.05rem; color:#fff;
    letter-spacing:-0.02em;
    position:relative; z-index:1;
    text-shadow:0 1px 8px rgba(0,0,0,0.25);
}
.cc-body { padding:0.85rem 1.2rem; }
.cc-desc {
    font-size:0.78rem; color:var(--text-secondary);
    line-height:1.5; margin-bottom:0.65rem;
}
.cc-foot {
    display:flex; align-items:center;
    justify-content:space-between;
}

/* ── Chips ───────────────────────────────────────────── */
.chip {
    display:inline-flex; align-items:center; gap:0.28rem;
    font-size:0.7rem; font-weight:600;
    padding:0.22rem 0.65rem; border-radius:100px;
}
.cb { background:rgba(0,122,255,0.1);  color:#007aff; }
.cg { background:rgba(52,199,89,0.12); color:#1e8e3e; }
.co { background:rgba(255,149,0,0.12); color:#a86000; }
.cp { background:rgba(175,82,222,0.12);color:#7e22ce; }
.cr { background:rgba(255,59,48,0.1);  color:#ff3b30; }
.cz { background:rgba(0,0,0,0.06);     color:var(--text-tertiary); }
.glass-chip {
    background:rgba(255,255,255,0.18);
    backdrop-filter:blur(8px);
    border:1px solid rgba(255,255,255,0.28);
    color:#fff; font-size:0.73rem; font-weight:600;
    padding:0.26rem 0.78rem; border-radius:100px;
}

/* ── Module hero banner ──────────────────────────────── */
.mhero {
    border-radius: var(--radius-lg);
    padding: 2.1rem 2rem;
    margin-bottom: 1.4rem;
    position: relative; overflow: hidden;
    animation: scaleIn 0.4s cubic-bezier(0.4,0,0.2,1) both;
}
.mhero::before {
    content:'';
    position:absolute; inset:0;
    background-image: radial-gradient(circle,rgba(255,255,255,0.12) 2px,transparent 2px);
    background-size:24px 24px;
}
.mhero-emoji {
    font-size:2.6rem; margin-bottom:0.65rem;
    display:block; position:relative;
    animation: fadeInDown 0.5s ease 0.1s both;
}
.mhero h1 {
    font-family:'DM Serif Display',serif !important;
    font-size:clamp(1.45rem,3vw,1.95rem) !important;
    font-weight:400 !important; color:#fff !important;
    border:none !important; padding:0 !important;
    margin:0 0 0.35rem !important;
    letter-spacing:-0.03em !important; line-height:1.2 !important;
    position:relative;
}
.mhero p {
    color:rgba(255,255,255,0.7) !important;
    font-size:0.87rem !important; margin:0 !important;
    position:relative;
}
.mhero-chips {
    display:flex; gap:0.45rem;
    flex-wrap:wrap; margin-top:1rem;
    position:relative;
}

/* ── Topic card ──────────────────────────────────────── */
.tc {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 1.35rem 1.5rem;
    margin-bottom: 0.85rem;
    box-shadow: var(--shadow-sm);
    animation: fadeInUp 0.5s ease both;
    transition: box-shadow var(--t), border-color var(--t);
}
.tc:hover {
    box-shadow: var(--shadow-md);
    border-color: rgba(0,122,255,0.14);
}
.tc-head {
    display:flex; align-items:center; gap:0.65rem;
    margin-bottom:0.75rem;
}
.tc-icon {
    width:36px; height:36px; border-radius:9px;
    display:flex; align-items:center; justify-content:center;
    font-size:1.15rem; flex-shrink:0;
}
.tc-title {
    font-size:0.93rem; font-weight:700;
    color:var(--text-primary); letter-spacing:-0.02em;
}
.tc p {
    font-size:0.855rem !important;
    color:var(--text-secondary) !important;
    line-height:1.8 !important; margin:0 !important;
}

/* ── Quiz header card ────────────────────────────────── */
.qhc {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-md);
    padding: 1.15rem 1.5rem;
    margin: 1.25rem 0 1rem;
    display: flex; align-items: center; gap: 1rem;
    box-shadow: var(--shadow-sm);
    animation: fadeInUp 0.5s ease both;
}
.qhc-icon {
    width:44px; height:44px; border-radius:var(--radius-sm);
    background:rgba(0,122,255,0.1);
    display:flex; align-items:center; justify-content:center;
    font-size:1.35rem; flex-shrink:0;
}
.qhc-title {
    font-size:0.93rem; font-weight:700;
    color:var(--text-primary); margin:0;
}
.qhc-sub {
    font-size:0.75rem; color:var(--text-tertiary); margin:0.1rem 0 0;
}
.q-qlabel {
    font-size:0.68rem; font-weight:700;
    color:var(--text-tertiary);
    text-transform:uppercase; letter-spacing:0.09em;
    margin-bottom:0.18rem;
}

/* ── Result card ─────────────────────────────────────── */
.rc {
    border-radius: var(--radius-lg);
    padding: 1.75rem 2rem;
    margin: 1rem 0;
    display: flex; align-items: center; gap: 1.5rem;
    animation: popIn 0.45s cubic-bezier(0.34,1.56,0.64,1) both;
    flex-wrap: wrap;
}
.rc-pass { background:rgba(52,199,89,0.1);  border:1px solid rgba(52,199,89,0.3); }
.rc-fail { background:rgba(255,59,48,0.07); border:1px solid rgba(255,59,48,0.25); }
.rc-score {
    font-family:'DM Serif Display',serif;
    font-size:3.4rem; font-weight:400;
    letter-spacing:-0.04em; line-height:1; flex-shrink:0;
}
.rc-pass .rc-score { color:var(--green); }
.rc-fail .rc-score { color:var(--red); }
.rc-badge {
    font-size:0.72rem; font-weight:700;
    text-transform:uppercase; letter-spacing:0.07em; margin-top:0.3rem;
}
.rc-pass .rc-badge { color:#1e8e3e; }
.rc-fail .rc-badge { color:#c5221f; }
.rc-msg { font-size:0.87rem; color:var(--text-secondary); line-height:1.65; }
.rc-msg strong { color:var(--text-primary); }

/* ── Grade table ─────────────────────────────────────── */
.gt {
    background: var(--surface);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: var(--shadow-sm);
    width: 100%; border-collapse: collapse;
    animation: fadeInUp 0.5s ease both;
}
.gt th {
    background: var(--surface2);
    padding: 0.8rem 1.35rem;
    text-align: left;
    font-size:0.68rem; font-weight:700;
    color:var(--text-tertiary);
    text-transform:uppercase; letter-spacing:0.08em;
    border-bottom:1px solid var(--border);
}
.gt td {
    padding: 0.95rem 1.35rem;
    border-bottom: 1px solid rgba(0,0,0,0.04);
    font-size: 0.87rem; vertical-align:middle;
}
.gt tr:last-child td { border-bottom:none; }
.gt tr:hover td { background: var(--surface2); }
.gm {
    font-family:'SF Mono','Fira Code','Roboto Mono',monospace;
    font-size:0.9rem; font-weight:600;
}

/* ── Mobile ──────────────────────────────────────────── */
@media (max-width:768px) {
    .block-container { padding:0.75rem 0.9rem 5rem !important; }
    .ph { padding:0.7rem 0.9rem; margin:-0.75rem -0.9rem 1.2rem; }
    .hero { padding:1.5rem 1.4rem; border-radius:var(--radius-md); }
    .hero-title { font-size:1.45rem; }
    .mhero { padding:1.4rem 1.3rem; }
    .mhero h1 { font-size:1.35rem !important; }
    .rc { padding:1.3rem; gap:0.9rem; }
    .rc-score { font-size:2.6rem; }
    .gt th, .gt td { padding:0.65rem 0.85rem; font-size:0.78rem; }
    .tc { padding:1.05rem 1.15rem; }
    .stat-val { font-size:1.65rem; }
    .cc-thumb { height:88px; }
}
@media (max-width:480px) {
    .hero-title { font-size:1.25rem; }
    .gt { display:block; overflow-x:auto; }
    .mhero-chips { gap:0.35rem; }
}
</style>
""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'dashboard'
if 'unlocked_modules' not in st.session_state:
    st.session_state.unlocked_modules = ['module_1']

for m in ['1', '2', '3', '4']:
    for key, default in [('quiz_started', False), ('quiz_submitted', False), ('quiz_score', 0)]:
        if f'm{m}_{key}' not in st.session_state:
            st.session_state[f'm{m}_{key}'] = default


def navigate(view):
    st.session_state.current_view = view


# ─────────────────────────────────────────────────────────────────────────────
#  QUIZ DATA
# ─────────────────────────────────────────────────────────────────────────────
M1_QUIZ = [
    {"q": "What do we call the specific time and place in which a story unfolds?",
     "o": ["The Plot", "The Characters", "The Setting", "The Theme"], "a": "The Setting"},
    {"q": "Where is the main idea of a paragraph most commonly found?",
     "o": ["In a footnote", "At the very end", "In the topic sentence", "Between the lines"], "a": "In the topic sentence"},
    {"q": "What are surrounding clues that help a reader figure out the meaning of an unfamiliar word?",
     "o": ["Context clues", "Phonics hints", "Story settings", "Grammar rules"], "a": "Context clues"},
    {"q": "Who are the people, animals, or creatures that participate in a story's events?",
     "o": ["The Authors", "The Narrators", "The Characters", "The Themes"], "a": "The Characters"},
    {"q": "What is the term for the sequence of events that drives a story from beginning to end?",
     "o": ["The Plot", "The Cover Page", "The Vocabulary", "The Epilogue"], "a": "The Plot"},
]

M2_QUIZ = [
    {"q": "What does reading fluency primarily refer to?",
     "o": ["Reading as fast as possible", "Reading accurately, smoothly, and with natural expression",
           "Memorising every vocabulary word", "Reading silently without lip movement"],
     "a": "Reading accurately, smoothly, and with natural expression"},
    {"q": "Which technique involves reading the same short passage multiple times until it flows effortlessly?",
     "o": ["Skimming", "Scanning", "Repeated reading", "Speed reading"], "a": "Repeated reading"},
    {"q": "What is a 'sight word'?",
     "o": ["A word with silent letters", "A word instantly recognised without sounding it out",
           "A very long and complicated word", "A word borrowed from another language"],
     "a": "A word instantly recognised without sounding it out"},
    {"q": "What does reading with 'expression' mean?",
     "o": ["Speaking as loudly as possible",
           "Changing your voice to match the emotion and meaning of the text",
           "Reading every word at the same monotone pace",
           "Pausing for three seconds after every sentence"],
     "a": "Changing your voice to match the emotion and meaning of the text"},
    {"q": "Which habit best strengthens reading comprehension over time?",
     "o": ["Reading only one type of book",
           "Asking thoughtful questions before, during, and after reading",
           "Skipping all words that seem too difficult",
           "Reading only very short sentences"],
     "a": "Asking thoughtful questions before, during, and after reading"},
]

M3_QUIZ = [
    {"q": "What is the total sum when you add 145 and 278 together?",
     "o": ["423", "413", "433", "323"], "a": "423"},
    {"q": "What is the perimeter of a square whose one side measures 9 units?",
     "o": ["18 units", "27 units", "36 units", "81 units"], "a": "36 units"},
    {"q": "In the fraction 3/4, what does the bottom number 4 represent?",
     "o": ["The number of parts we currently have",
           "The total equal parts that make up the whole",
           "The sum of the numerator and denominator",
           "The difference between two numbers"],
     "a": "The total equal parts that make up the whole"},
    {"q": "What is the product when you multiply 15 by 8?",
     "o": ["100", "110", "120", "130"], "a": "120"},
    {"q": "What is the correct term for any flat, closed shape bounded entirely by straight sides?",
     "o": ["Circle", "Sphere", "Polygon", "Cylinder"], "a": "Polygon"},
]

M4_QUIZ = [
    {"q": "What process transforms liquid water from rivers and oceans into invisible water vapour?",
     "o": ["Condensation", "Evaporation", "Precipitation", "Sublimation"], "a": "Evaporation"},
    {"q": "Which source of energy is the primary driver of the entire water cycle on Earth?",
     "o": ["The Moon's gravity", "Geothermal vents", "The Sun", "Ocean currents"], "a": "The Sun"},
    {"q": "What atmospheric phenomenon forms when rising water vapour cools and condenses?",
     "o": ["Raindrops on a window", "Clouds", "Underground rivers", "Aquifers"], "a": "Clouds"},
    {"q": "Which of the following is a correct example of precipitation?",
     "o": ["A puddle drying in the sun", "Snow falling from the sky",
           "Steam rising from boiling water", "Ice slowly melting in a glass"],
     "a": "Snow falling from the sky"},
    {"q": "What is the name for an underground layer of permeable rock that holds large amounts of freshwater?",
     "o": ["A cloud layer", "An aquifer", "The stratosphere", "A water table valve"],
     "a": "An aquifer"},
]


# ─────────────────────────────────────────────────────────────────────────────
#  MODULE CONFIG
# ─────────────────────────────────────────────────────────────────────────────
MODULES = {
    'module_1': {
        'key': '1', 'label': 'Reading', 'icon': '📖',
        'subtitle': 'Understanding Stories and Words',
        'teacher': 'Ms. Santos · Grade 4 English',
        'bg': 'linear-gradient(135deg,#1a56db 0%,#007aff 60%,#34aadc 100%)',
        'icon_bg': 'rgba(0,122,255,0.1)', 'chip': 'cb',
        'quiz': M1_QUIZ, 'unlock_next': 'module_2',
        'unlock_msg': '🗣️  Reading Fluency is now unlocked!',
        'topics': [
            ('📚','rgba(0,122,255,0.1)','1.0 — Elements of a Story',
             'Every story is built from essential building blocks that work together to create meaning. '
             'The <strong>setting</strong> establishes the world of the story — not only the physical location '
             'but also the time period, culture, and atmosphere in which events take place. A story set in a rainy '
             'medieval castle feels completely different from one set on a sunny modern beach, even if the plot is similar. '
             'The <strong>characters</strong> are the living hearts of any narrative — they can be people, animals, '
             'mythical creatures, or even objects brought to life. Their personalities, desires, fears, and relationships '
             'create the emotional depth that keeps readers engaged. The <strong>plot</strong> is the engine of the story: '
             'the carefully ordered chain of events that creates tension, conflict, and resolution, propelling the reader '
             'from the opening sentence all the way to the final word. Understanding these three elements — setting, '
             'character, and plot — gives you a reliable framework for analysing any story you encounter.'),
            ('🔍','rgba(52,199,89,0.1)','1.1 — Finding the Main Idea',
             'Every well-written paragraph revolves around a single central point — the <strong>main idea</strong>. '
             'This is the author\'s primary message, the one thing they most want you to understand before moving on. '
             'Skilled readers train themselves to identify this idea quickly by looking for the <strong>topic sentence</strong>, '
             'which typically appears at or near the beginning of a paragraph and announces its subject. '
             'The sentences that follow — called <strong>supporting details</strong> — provide evidence, examples, '
             'statistics, or descriptions that back up and expand on the topic sentence. A helpful technique is to ask '
             'yourself after reading any paragraph: "If I had to summarise this in one sentence, what would it be?" '
             'That summary is almost always the main idea. Practising this skill on every paragraph you read — in '
             'textbooks, articles, even cereal boxes — will make complex texts feel far more manageable over time.'),
            ('💡','rgba(255,149,0,0.1)','1.2 — Using Context Clues',
             'Encountering an unfamiliar word mid-sentence doesn\'t have to break your reading momentum. '
             'Skilled readers use <strong>context clues</strong> — the words, phrases, and sentences surrounding '
             'the unknown term — to make an educated guess about its meaning. There are several types to watch for. '
             '<strong>Definition clues</strong> occur when the author directly explains a word right after using it, '
             'often signalled by phrases like "which means" or "that is." <strong>Synonym clues</strong> appear when '
             'a nearby word has a similar meaning. <strong>Antonym clues</strong> occur when contrast words like '
             '"but," "however," or "unlike" signal an opposite meaning. <strong>Example clues</strong> use specific '
             'instances to illustrate a word\'s meaning. The more widely you read, the richer your vocabulary becomes, '
             'which in turn makes context clues easier to spot and use — turning every unfamiliar word into an '
             'opportunity to learn rather than a reason to stop.'),
            ('✍️','rgba(175,82,222,0.1)','1.3 — Building Your Vocabulary',
             'A strong vocabulary is one of the most powerful tools a reader and writer can possess. Words are the '
             'precise instruments with which we both understand the world and express our thoughts. One proven strategy '
             'is keeping a <strong>vocabulary journal</strong> — a dedicated notebook where you record new words, '
             'their definitions, example sentences you write yourself, and drawings if they help you remember. '
             'Research in cognitive science shows that <strong>spaced repetition</strong> — reviewing new words at '
             'gradually increasing intervals — dramatically improves long-term retention compared to cramming. '
             'Another powerful technique is studying <strong>word roots, prefixes, and suffixes</strong>. '
             'Understanding that the Latin root <em>port</em> means "to carry" instantly helps you decode words like '
             'transport, import, export, portable, and portfolio. Knowing the prefix <em>un-</em> means "not" '
             'unlocks hundreds of English words at once. Vocabulary growth is cumulative and self-reinforcing — '
             'every new word you learn makes learning the next one slightly easier.'),
        ],
    },
    'module_2': {
        'key': '2', 'label': 'Reading Fluency', 'icon': '🗣️',
        'subtitle': 'Speed, Expression & Deep Comprehension',
        'teacher': 'Ms. Santos · Grade 4 English (Advanced)',
        'bg': 'linear-gradient(135deg,#6d28d9 0%,#af52de 60%,#ec4899 100%)',
        'icon_bg': 'rgba(175,82,222,0.1)', 'chip': 'cp',
        'quiz': M2_QUIZ, 'unlock_next': 'module_3',
        'unlock_msg': '🔢  Mathematics is now unlocked!',
        'topics': [
            ('🎯','rgba(175,82,222,0.1)','2.0 — What Is Reading Fluency?',
             'Reading fluency is the <strong>bridge between recognising individual words and truly understanding '
             'what you read</strong>. A fluent reader moves through text with accuracy (pronouncing words '
             'correctly), automaticity (recognising words instantly without effort), and prosody (reading with '
             'natural rhythm, pacing, and expression, just like spoken conversation). When reading is effortful '
             'and slow, most of your mental energy goes toward decoding individual words, leaving little capacity '
             'to think about meaning, make inferences, or enjoy the story. Fluency frees your brain to operate '
             'at a higher level — to question, visualise, connect, and analyse. Research consistently shows '
             'that fluency is one of the strongest predictors of overall reading comprehension. Building it is '
             'not a luxury; it is a foundation upon which all advanced literacy skills rest.'),
            ('🔄','rgba(0,122,255,0.1)','2.1 — The Power of Repeated Reading',
             '<strong>Repeated reading</strong> is a simple but remarkably effective technique: you read the '
             'same short, engaging passage multiple times — typically three to five — until it flows naturally '
             'and comfortably. On your first read, you decode. On your second, you begin to feel the shape of '
             'sentences. By the third and fourth reads, you are reading with genuine expression and comprehension. '
             'Think of a musician learning a piece of music: they do not play it once and move on. They rehearse, '
             'refine, and eventually perform it with confidence and feeling. Reading works the same way. '
             'Another powerful variation is <strong>paired reading</strong>, where a more skilled reader reads '
             'aloud alongside a developing reader, providing an immediate model of fluent expression and '
             'allowing the learner to adjust their own pace, intonation, and rhythm in real time.'),
            ('👁️','rgba(52,199,89,0.1)','2.2 — Sight Words and Automaticity',
             'In any piece of English text, a surprisingly small set of words accounts for a huge proportion '
             'of everything written. Words like "the," "and," "said," "because," "through," and "could" appear '
             'on virtually every page. When a reader must pause to decode these words every time, reading becomes '
             'painfully slow and exhausting. The goal is to recognise these words <strong>instantly and '
             'automatically</strong> — not by sounding them out, but by seeing them as complete, familiar units. '
             'Researchers call this process "orthographic mapping." Regular flashcard practice, word walls, '
             'and wide independent reading are all proven methods for building automatic sight-word recognition '
             'that dramatically increases both reading speed and enjoyment.'),
            ('🧠','rgba(255,149,0,0.1)','2.3 — Active Comprehension Strategies',
             'True reading comprehension is an active, ongoing conversation between reader and text. Expert '
             'readers do not passively absorb words — they continuously monitor their own understanding through '
             'deliberate mental strategies. <strong>Predicting</strong> means forming expectations about what '
             'will happen next, based on clues in the text and your own background knowledge. '
             '<strong>Questioning</strong> involves asking "Why?", "How?", and "What if?" as you read, '
             'turning passive reception into active inquiry. <strong>Visualising</strong> means constructing '
             'a vivid mental movie of events, characters, and settings — the clearer the image, the stronger '
             'the memory. <strong>Summarising</strong> requires you to identify what truly matters and restate '
             'it concisely in your own words. <strong>Making connections</strong> — linking new information to '
             'things you already know from life, other texts, or the world — is how deep, lasting understanding '
             'is built. Practise these strategies deliberately, and they will eventually become automatic.'),
        ],
    },
    'module_3': {
        'key': '3', 'label': 'Mathematics', 'icon': '🔢',
        'subtitle': 'Foundational Operations and Geometry',
        'teacher': 'Mr. Reyes · Grade 4 Mathematics',
        'bg': 'linear-gradient(135deg,#1e8e3e 0%,#34c759 60%,#a8e063 100%)',
        'icon_bg': 'rgba(52,199,89,0.1)', 'chip': 'cg',
        'quiz': M3_QUIZ, 'unlock_next': 'module_4',
        'unlock_msg': '🌍  Natural Sciences is now unlocked!',
        'topics': [
            ('➕','rgba(52,199,89,0.1)','3.0 — The Four Basic Operations',
             'Mathematics is built on four fundamental operations that together allow us to manipulate and '
             'understand numbers. <strong>Addition</strong> combines two or more quantities to find a total sum. '
             'When you add 47 and 58, you ask how many you have altogether. <strong>Subtraction</strong> is '
             'the inverse of addition — it finds the difference between two quantities and tells us how much '
             'remains. <strong>Multiplication</strong> is a powerful shortcut for repeated addition: instead '
             'of adding 9 seven separate times, we calculate 9 × 7 = 63. Understanding multiplication deeply — '
             'not just memorising times tables — opens the door to almost all advanced mathematics. '
             '<strong>Division</strong> is the inverse of multiplication, splitting a quantity into equal '
             'groups. Mastering all four operations fluently, so they require no conscious effort, is '
             'non-negotiable for mathematical success and lays the groundwork for algebra, geometry, and beyond.'),
            ('½','rgba(0,122,255,0.1)','3.1 — Understanding Fractions',
             'A fraction is a precise mathematical tool for representing a part of a whole. When we write ¾, '
             'the number on top — the <strong>numerator</strong> (3) — tells us how many parts we currently '
             'have. The number on the bottom — the <strong>denominator</strong> (4) — tells us how many equal '
             'parts the whole was divided into. Think of a pizza cut into four equal slices: eating three '
             'slices means you consumed ¾. The denominator can <strong>never be zero</strong>, because '
             'dividing something into zero parts has no mathematical meaning. Fractions can be '
             '<strong>proper</strong> (like ⅔), <strong>improper</strong> (like 7/4), or expressed as '
             '<strong>mixed numbers</strong> (like 1¾). Mastering fractions prepares you for decimals, '
             'percentages, ratios, probability, and algebraic thinking.'),
            ('📐','rgba(255,149,0,0.1)','3.2 — Shapes, Perimeter, and Area',
             'Geometry is the branch of mathematics concerned with the properties and relationships of '
             'points, lines, surfaces, and shapes. A <strong>polygon</strong> is any flat, closed figure '
             'bounded entirely by straight sides. Polygons are classified by their number of sides: '
             'triangle (3), quadrilateral (4), pentagon (5), hexagon (6), and so on. Two essential '
             'measurements of any flat shape are its <strong>perimeter</strong> — the total distance around '
             'the outside boundary — and its <strong>area</strong> — how much flat surface the shape covers. '
             'For a rectangle: perimeter = 2 × (length + width); area = length × width. Real-world '
             'applications are everywhere: perimeter tells a gardener how much fencing to buy; area tells '
             'a painter how much paint is needed. Understanding both measurements and when to use each is '
             'a vital practical and mathematical skill.'),
        ],
    },
    'module_4': {
        'key': '4', 'label': 'Natural Sciences', 'icon': '🌍',
        'subtitle': 'The Hydrological Cycle',
        'teacher': 'Ms. Cruz · Grade 4 Science',
        'bg': 'linear-gradient(135deg,#b45309 0%,#ff9500 60%,#fbbf24 100%)',
        'icon_bg': 'rgba(255,149,0,0.1)', 'chip': 'co',
        'quiz': M4_QUIZ, 'unlock_next': None,
        'unlock_msg': '🎉  Congratulations — you have completed all modules!',
        'topics': [
            ('🌊','rgba(0,122,255,0.1)','4.0 — Introduction to the Water Cycle',
             'The water cycle — scientifically known as the <strong>hydrological cycle</strong> — is one of '
             'the most important natural processes sustaining life on our planet. It describes the continuous, '
             'never-ending journey of water as it moves between Earth\'s surface, atmosphere, and underground '
             'systems. Water does not get used up or destroyed; it changes physical state and location, '
             'cycling through the same pathways it has for billions of years. The total volume of water '
             'on Earth has remained essentially constant since the planet formed. This means the water in '
             'your glass today may have filled a dinosaur\'s drinking pool, evaporated into an ancient cloud, '
             'frozen into a glacier during an ice age, and flowed down a mountain river before reaching '
             'your tap. Understanding the water cycle helps scientists predict weather, manage freshwater '
             'resources, and understand the impacts of climate change.'),
            ('☀️','rgba(255,149,0,0.1)','4.1 — Evaporation and Condensation',
             '<strong>Evaporation</strong> is the process by which the Sun\'s thermal energy converts '
             'liquid water — found in oceans, rivers, lakes, and puddles — into water vapour, an invisible '
             'gas that rises into the atmosphere. Approximately 90% of all atmospheric water vapour comes '
             'from ocean evaporation; the remaining 10% comes from plant transpiration (together called '
             '<strong>evapotranspiration</strong>). As water vapour rises higher into the atmosphere, '
             'temperatures decrease significantly. When vapour cools below its <strong>dew point</strong>, '
             'it undergoes <strong>condensation</strong> — reverting from a gas back into tiny liquid '
             'water droplets or ice crystals. These particles cluster around microscopic dust and sea salt '
             'to form the clouds we observe drifting across the sky, carrying enormous quantities of water '
             'thousands of kilometres from where it originally evaporated.'),
            ('🌧️','rgba(52,199,89,0.1)','4.2 — Precipitation and Collection',
             'As clouds grow heavier — accumulating more condensed droplets — gravity eventually overcomes '
             'the forces keeping them aloft, and water falls back to Earth as <strong>precipitation</strong>. '
             'The form it takes depends on atmospheric temperature: <strong>rain</strong> forms when '
             'temperatures stay above freezing; <strong>snow</strong> forms when below freezing; '
             '<strong>sleet</strong> forms when rain refreezes before reaching the ground; and '
             '<strong>hail</strong> forms when strong updrafts repeatedly lift ice pellets back up before '
             'they fall. Once precipitation reaches the surface, water is <strong>collected</strong> '
             'in several ways: it fills oceans, lakes, rivers, and reservoirs; it is absorbed by '
             'plant roots; it soaks into soil through <strong>infiltration</strong> and percolates down '
             'to replenish underground <strong>aquifers</strong> — vast stores of freshwater held within '
             'permeable rock and sediment, ready to sustain life long after rain stops falling.'),
        ],
    },
}


# ─────────────────────────────────────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-wordmark">Danilo</div>
        <div class="sb-sub">Learning Platform</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<span class="sb-section">Main</span>', unsafe_allow_html=True)
    st.button("🏠  Home",      on_click=navigate, args=('dashboard',), use_container_width=True)
    st.button("📊  My Grades", on_click=navigate, args=('profile',),   use_container_width=True)

    st.markdown('<span class="sb-section">Courses</span>', unsafe_allow_html=True)
    for mk, mod in MODULES.items():
        locked = mk not in st.session_state.unlocked_modules
        lbl = f"{'🔒' if locked else mod['icon']}  {mod['label']}"
        st.button(lbl, on_click=navigate, args=(mk,), disabled=locked, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<p style="font-size:0.67rem;color:var(--text-tertiary,#aaa);padding:0 1.1rem;line-height:1.7;">'
        '© 2025 Danilo Learning<br>All rights reserved.</p>',
        unsafe_allow_html=True,
    )


# ─────────────────────────────────────────────────────────────────────────────
#  HELPER
# ─────────────────────────────────────────────────────────────────────────────
def ph(icon, title):
    st.markdown(f"""
    <div class="ph">
        <span style="font-size:1.2rem;line-height:1;">{icon}</span>
        <h1 class="ph-title">{title}</h1>
        <div class="ph-avatar">D</div>
    </div>""", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
#  DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.current_view == 'dashboard':
    ph("🏠", "Home")

    st.markdown("""
    <div class="hero">
        <div class="hero-eyebrow">Welcome back</div>
        <div class="hero-title">Ready to learn<br>something new today?</div>
        <div class="hero-sub">Complete courses in sequence to unlock the next challenge.</div>
    </div>""", unsafe_allow_html=True)

    scores_taken = [st.session_state[f'm{m}_quiz_score']
                    for m in ['1','2','3','4'] if st.session_state[f'm{m}_quiz_submitted']]
    avg_acc  = (sum(scores_taken)/(len(scores_taken)*5)*100) if scores_taken else 0
    completed = sum(1 for m in ['1','2','3','4']
                    if st.session_state[f'm{m}_quiz_submitted']
                    and st.session_state[f'm{m}_quiz_score'] >= 4)
    unlocked = len(st.session_state.unlocked_modules)

    s1, s2, s3, s4 = st.columns(4, gap="small")
    for col, val, lbl, color, pct, di in [
        (s1, f"{unlocked}/4",           "Unlocked",  "#007aff", unlocked/4*100,    "d1"),
        (s2, f"{completed}/4",          "Passed",    "#34c759", completed/4*100,   "d2"),
        (s3, f"{avg_acc:.0f}%",         "Accuracy",  "#ff9500", avg_acc,           "d3"),
        (s4, f"{int(completed/4*100)}%","Progress",  "#af52de", completed/4*100,   "d4"),
    ]:
        with col:
            st.markdown(f"""
            <div class="stat-card {di}">
                <div class="stat-val" style="color:{color};">{val}</div>
                <div class="stat-lbl">{lbl}</div>
                <div class="prog-track">
                    <div class="prog-fill" style="width:{min(pct,100):.0f}%;background:{color};"></div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div style="height:1.4rem"></div>', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow au d5">Your Courses</div>', unsafe_allow_html=True)

    items = list(MODULES.items())
    for row in range(0, len(items), 2):
        cols = st.columns(2, gap="medium")
        for ci, (mk, mod) in enumerate(items[row: row + 2]):
            locked    = mk not in st.session_state.unlocked_modules
            m_key     = mod['key']
            submitted = st.session_state[f'm{m_key}_quiz_submitted']
            score     = st.session_state[f'm{m_key}_quiz_score']
            passed    = submitted and score >= 4
            badge = (
                f'<span class="chip cg">✓ Completed</span>' if passed
                else f'<span class="chip cz">🔒 Locked</span>' if locked
                else f'<span class="chip cb">● Open</span>'
            )
            delay_cls = f"d{min(row*2+ci+1, 8)}"
            with cols[ci]:
                st.markdown(f"""
                <div class="cc {delay_cls}">
                    <div class="cc-thumb" style="background:{mod['bg']};">
                        <div class="cc-dots"></div>
                        <div class="cc-icon">{mod['icon']}</div>
                        <div class="cc-name">{mod['label']}</div>
                    </div>
                    <div class="cc-body">
                        <div class="cc-desc">{mod['subtitle']}<br>
                            <span style="font-size:0.73rem;color:#aeaeb2;">{mod['teacher']}</span>
                        </div>
                        <div class="cc-foot">
                            {badge}
                            <span style="font-size:0.72rem;color:#aeaeb2;">{len(mod['quiz'])} questions</span>
                        </div>
                    </div>
                </div>""", unsafe_allow_html=True)
                st.button(
                    "Open →" if not locked else "Locked",
                    key=f"d_{mk}", on_click=navigate, args=(mk,),
                    disabled=locked, use_container_width=True,
                )


# ─────────────────────────────────────────────────────────────────────────────
#  MODULE VIEW
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.current_view in MODULES:
    mk  = st.session_state.current_view
    mod = MODULES[mk]
    m   = mod['key']
    qd  = mod['quiz']

    ph(mod['icon'], mod['label'])
    st.button("← Back", key=f"bk_{mk}", on_click=navigate, args=('dashboard',))
    st.markdown('<div style="height:0.4rem"></div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="mhero" style="background:{mod['bg']};">
        <span class="mhero-emoji">{mod['icon']}</span>
        <h1>{mod['label']}</h1>
        <p>{mod['subtitle']}</p>
        <div class="mhero-chips">
            <span class="glass-chip">👩‍🏫 {mod['teacher']}</span>
            <span class="glass-chip">📝 {len(qd)}-question quiz</span>
            <span class="glass-chip">📖 {len(mod['topics'])} lessons</span>
            <span class="glass-chip">⏱ ~15 min</span>
        </div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="eyebrow">Lesson Material</div>', unsafe_allow_html=True)
    for i, (icon, ibg, title, body) in enumerate(mod['topics']):
        st.markdown(f"""
        <div class="tc d{i+1}">
            <div class="tc-head">
                <div class="tc-icon" style="background:{ibg};">{icon}</div>
                <div class="tc-title">{title}</div>
            </div>
            <p>{body}</p>
        </div>""", unsafe_allow_html=True)

    pass_mark = len(qd) - 1
    st.markdown(f"""
    <div class="qhc">
        <div class="qhc-icon">📋</div>
        <div>
            <p class="qhc-title">Formative Assessment</p>
            <p class="qhc-sub">{len(qd)} questions · Pass mark: {pass_mark}/{len(qd)} · Unlimited retries</p>
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
                st.markdown(f'<div class="q-qlabel">Question {i+1} of {len(qd)}</div>',
                             unsafe_allow_html=True)
                st.markdown(f"**{q['q']}**")
                a = st.radio("", q['o'], key=f"{mk}_q{i}",
                             label_visibility="collapsed", index=None)
                answers.append(a)
                if i < len(qd) - 1:
                    st.markdown(
                        '<hr style="border:none;border-top:1px solid rgba(0,0,0,0.06);margin:0.85rem 0;">',
                        unsafe_allow_html=True)
            st.markdown("<br>", unsafe_allow_html=True)
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
            passed = score >= pass_mark
            pct    = int(score / len(qd) * 100)

            if passed:
                st.markdown(f"""
                <div class="rc rc-pass">
                    <div>
                        <div class="rc-score">{score}/{len(qd)}</div>
                        <div class="rc-badge">✓ Competency Verified</div>
                    </div>
                    <div class="rc-msg">
                        <strong>Outstanding work.</strong> You scored {pct}% and have demonstrated
                        solid mastery of this topic.<br>
                        <span style="color:#34c759;font-weight:600;">{mod['unlock_msg']}</span>
                    </div>
                </div>""", unsafe_allow_html=True)
                nxt = mod.get('unlock_next')
                if nxt and nxt not in st.session_state.unlocked_modules:
                    st.session_state.unlocked_modules.append(nxt)
            else:
                st.markdown(f"""
                <div class="rc rc-fail">
                    <div>
                        <div class="rc-score">{score}/{len(qd)}</div>
                        <div class="rc-badge">✗ Below Pass Mark</div>
                    </div>
                    <div class="rc-msg">
                        <strong>Keep going.</strong> You scored {pct}%.
                        Review the lesson material above carefully and try again —
                        you need at least {pass_mark}/{len(qd)} to pass.
                    </div>
                </div>""", unsafe_allow_html=True)
                if st.button("🔄  Retry", key=f"rt_{mk}"):
                    st.session_state[uk] = False
                    st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
#  GRADES
# ─────────────────────────────────────────────────────────────────────────────
elif st.session_state.current_view == 'profile':
    ph("📊", "My Grades")
    st.button("← Back", key="bk_g", on_click=navigate, args=('dashboard',))
    st.markdown('<div style="height:0.8rem"></div>', unsafe_allow_html=True)

    subs   = {m: st.session_state[f'm{m}_quiz_submitted'] for m in ['1','2','3','4']}
    scores = {m: st.session_state[f'm{m}_quiz_score']     for m in ['1','2','3','4']}
    taken  = [scores[m] for m in ['1','2','3','4'] if subs[m]]
    avg_a  = (sum(taken)/(len(taken)*5)*100) if taken else 0
    comp   = sum(1 for m in ['1','2','3','4'] if subs[m] and scores[m] >= 4)
    unl    = len(st.session_state.unlocked_modules)

    g1, g2, g3 = st.columns(3, gap="medium")
    for col, val, lbl, color, pct in [
        (g1, f"{unl}/4",          "Courses Unlocked", "#007aff", unl/4*100),
        (g2, f"{avg_a:.0f}%",     "Mean Accuracy",    "#34c759", avg_a),
        (g3, f"{int(comp/4*100)}%","Progress",        "#af52de", comp/4*100),
    ]:
        with col:
            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-val" style="color:{color};">{val}</div>
                <div class="stat-lbl">{lbl}</div>
                <div class="prog-track">
                    <div class="prog-fill" style="width:{min(pct,100):.0f}%;background:{color};"></div>
                </div>
            </div>""", unsafe_allow_html=True)

    st.markdown('<div style="height:1.25rem"></div>', unsafe_allow_html=True)
    st.markdown('<div class="eyebrow">Gradebook</div>', unsafe_allow_html=True)

    rows = ""
    for mk, mod in MODULES.items():
        m  = mod['key']
        total = len(mod['quiz'])
        locked = mk not in st.session_state.unlocked_modules
        sub    = subs[m]
        sc     = scores[m]
        passed = sub and sc >= 4

        if locked:
            sh = '<span class="chip cz">🔒 Locked</span>'
            sd = gd = '<span style="color:#aeaeb2;">—</span>'
        elif passed:
            sh = '<span class="chip cg">✓ Passed</span>'
            sd = f'<span class="gm" style="color:#1e8e3e;">{sc}/{total}</span>'
            gd = f'<span class="gm" style="color:#1e8e3e;">{int(sc/total*100)}%</span>'
        elif sub:
            sh = '<span class="chip cr">✗ Below Pass</span>'
            sd = f'<span class="gm" style="color:#ff3b30;">{sc}/{total}</span>'
            gd = f'<span class="gm" style="color:#ff3b30;">{int(sc/total*100)}%</span>'
        else:
            sh = '<span class="chip cz">○ Not Started</span>'
            sd = gd = '<span style="color:#aeaeb2;">—</span>'

        rows += f"""
        <tr>
            <td style="font-size:1.15rem;width:36px;">{mod['icon']}</td>
            <td style="font-weight:600;color:#1d1d1f;">{mod['label']}</td>
            <td style="color:#6e6e73;font-size:0.82rem;">{mod['subtitle']}</td>
            <td>{sh}</td>
            <td>{sd}</td>
            <td>{gd}</td>
        </tr>"""

    st.markdown(f"""
    <table class="gt">
        <thead>
            <tr>
                <th></th><th>Course</th><th>Topic</th>
                <th>Status</th><th>Score</th><th>Grade</th>
            </tr>
        </thead>
        <tbody>{rows}</tbody>
    </table>""", unsafe_allow_html=True)
