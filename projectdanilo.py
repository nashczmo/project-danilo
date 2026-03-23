import streamlit as st
import os

if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write('[theme]\nbase="light"\nprimaryColor="#18181b"\nbackgroundColor="#fafafa"\nsecondaryBackgroundColor="#ffffff"\ntextColor="#18181b"\nfont="sans serif"\n')

st.set_page_config(
    page_title="DANILO",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Session state ─────────────────────────────────────────────────
if 'dark'         not in st.session_state: st.session_state.dark         = False
if 'view'         not in st.session_state: st.session_state.view         = 'dashboard'
if 'unlocked_cls' not in st.session_state: st.session_state.unlocked_cls = ['reading']

for _c in ['reading', 'math', 'science']:
    for _k, _d in [('started', False), ('submitted', False), ('score', 0)]:
        if f'{_c}_q_{_k}' not in st.session_state:
            st.session_state[f'{_c}_q_{_k}'] = _d

def go(view):           st.session_state.view = view
def flip_theme():       st.session_state.dark = not st.session_state.dark

DM = st.session_state.dark

# ── CSS ───────────────────────────────────────────────────────────
DARK = """
:root {
  --bg:       #0a0a0a;
  --s0:       #111111;
  --s1:       #1a1a1a;
  --s2:       #222222;
  --border:   rgba(255,255,255,0.08);
  --border2:  rgba(255,255,255,0.14);
  --text:     #fafafa;
  --sub:      #a1a1aa;
  --muted:    #71717a;
  --accent:   #e4e4e7;
}
.stApp { background: var(--bg) !important; }
section[data-testid="stSidebar"] { background: var(--s0) !important; }
div[role="radiogroup"] label p { color: var(--sub) !important; }
"""
LIGHT = """
:root {
  --bg:       #fafafa;
  --s0:       #ffffff;
  --s1:       #f4f4f5;
  --s2:       #e4e4e7;
  --border:   rgba(0,0,0,0.07);
  --border2:  rgba(0,0,0,0.13);
  --text:     #18181b;
  --sub:      #52525b;
  --muted:    #a1a1aa;
  --accent:   #18181b;
}
.stApp { background: var(--bg) !important; }
section[data-testid="stSidebar"] { background: var(--s0) !important; }
"""

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

html,body,[class*="css"],p,div,span,h1,h2,h3,h4,
label,button,input,li,td,th { font-family:'Inter',sans-serif !important; }

.block-container { padding:2.25rem 2.5rem 6rem !important; max-width:880px !important; }
#MainMenu,footer,header { visibility:hidden; }
button[data-testid="collapsedControl"] { display:none !important; }

@keyframes up   { from{opacity:0;transform:translateY(10px)} to{opacity:1;transform:none} }
@keyframes fade { from{opacity:0} to{opacity:1} }
@keyframes grow { from{width:0} to{width:var(--w)} }
@keyframes dot  { 0%,100%{opacity:.4} 50%{opacity:1} }

/* ── SIDEBAR ───────────────────────────── */
section[data-testid="stSidebar"] {
  border-right:1px solid var(--border) !important;
  min-width:230px !important; max-width:230px !important;
}
section[data-testid="stSidebar"] > div,
section[data-testid="stSidebar"] .block-container {
  padding:0 !important; max-width:none !important;
}

.sb-top {
  padding:1.3rem 1.1rem 1rem;
  border-bottom:1px solid var(--border);
  animation:fade .3s ease;
}
.sb-logo {
  font-size:1.05rem; font-weight:800; letter-spacing:-.035em;
  color:var(--text); margin-bottom:.12rem;
}
.sb-tag { font-size:.65rem; color:var(--muted); font-weight:400; letter-spacing:.01em; }

.sb-label {
  padding:.85rem 1.1rem .2rem;
  font-size:.58rem; font-weight:700; letter-spacing:.13em;
  text-transform:uppercase; color:var(--muted);
}

/* Override sidebar buttons → plain nav links */
section[data-testid="stSidebar"] div[data-testid="stButton"] > button {
  display:block !important; width:100% !important; text-align:left !important;
  background:transparent !important; border:none !important;
  border-radius:7px !important;
  padding:.38rem 1.1rem !important; margin:.05rem 0 !important;
  color:var(--sub) !important; font-size:.82rem !important;
  font-weight:500 !important; box-shadow:none !important;
  letter-spacing:-.01em !important; transition:all .15s !important;
}
section[data-testid="stSidebar"] div[data-testid="stButton"] > button:hover {
  background:var(--s1) !important; color:var(--text) !important;
  transform:none !important;
}

.sb-row-active {
  display:flex; align-items:center; gap:.55rem;
  padding:.38rem 1.1rem; margin:.05rem 0; border-radius:7px;
  background:var(--s1); animation:fade .2s ease;
}
.sb-row-locked {
  display:flex; align-items:center; gap:.55rem;
  padding:.38rem 1.1rem; margin:.05rem 0; opacity:.32;
}
.sb-row-icon  { font-size:.82rem; width:18px; text-align:center; }
.sb-row-text  { font-size:.82rem; font-weight:500; color:var(--sub); flex-grow:1; }
.sb-row-active .sb-row-text { color:var(--text); font-weight:600; }
.sb-dot { width:5px; height:5px; border-radius:50%; flex-shrink:0; }
.d-green { background:#22c55e; }
.d-blue  { background:#6366f1; animation:dot 2s infinite; }
.d-grey  { background:var(--muted); opacity:.4; }

/* theme / footer */
.sb-foot {
  padding:.9rem 1.1rem 1.1rem;
  border-top:1px solid var(--border);
  margin-top:.4rem;
  animation:fade .4s ease .2s both;
}
.sb-foot-head { display:flex; justify-content:space-between; margin-bottom:.45rem; }
.sb-foot-lbl  { font-size:.65rem; font-weight:600; color:var(--muted); }
.sb-foot-pct  { font-size:.65rem; font-weight:700; color:var(--text); }
.sb-track { height:3px; background:var(--s2); border-radius:99px; overflow:hidden; }
.sb-bar   { height:3px; background:var(--text); border-radius:99px; animation:grow .8s ease .3s both; }
.sb-foot-sub { font-size:.62rem; color:var(--muted); margin-top:.35rem; }

.theme-wrap div[data-testid="stButton"] > button {
  margin:.35rem 1.1rem .1rem !important;
  width:calc(100% - 2.2rem) !important;
  background:var(--s1) !important;
  border:1px solid var(--border) !important;
  color:var(--sub) !important;
  font-size:.72rem !important; font-weight:600 !important;
  border-radius:7px !important; text-align:center !important;
  letter-spacing:.01em !important; padding:.38rem !important;
}
.theme-wrap div[data-testid="stButton"] > button:hover {
  background:var(--s2) !important; color:var(--text) !important;
}

/* ── PAGE HEADER ───────────────────────── */
.pg-head { padding:.75rem 0 2rem; animation:up .4s ease both; }
.pg-crumb {
  font-size:.65rem; font-weight:500; color:var(--muted);
  letter-spacing:.01em; margin-bottom:.55rem;
  display:flex; align-items:center; gap:.35rem;
}
.pg-title { font-size:2.2rem; font-weight:800; letter-spacing:-.05em;
            color:var(--text); line-height:1.06; }
.pg-sub   { font-size:.9rem; color:var(--sub); margin-top:.45rem;
            line-height:1.6; max-width:420px; font-weight:400; }

/* ── CLASS CARDS (dashboard) ──────────── */
.cls-card {
  background:var(--s0); border:1px solid var(--border);
  border-radius:12px; padding:1.4rem 1.5rem;
  position:relative; overflow:hidden;
  transition:border-color .2s, box-shadow .25s, transform .25s;
  cursor:default; margin-bottom:.65rem; height:190px;
  display:flex; flex-direction:column;
  animation:up .38s ease both;
}
.cls-card:not(.cls-locked):hover {
  border-color:var(--border2);
  box-shadow:0 8px 28px rgba(0,0,0,.08);
  transform:translateY(-3px);
}
.cls-locked { opacity:.4; pointer-events:none; }

.cls-card-a1 { animation-delay:.04s; }
.cls-card-a2 { animation-delay:.1s;  }
.cls-card-a3 { animation-delay:.16s; }

.cls-num {
  position:absolute; top:1rem; right:1.1rem;
  font-size:.58rem; font-weight:700; letter-spacing:.08em;
  color:var(--muted); background:var(--s1); border:1px solid var(--border);
  border-radius:5px; padding:.12rem .4rem;
}
.cls-icon {
  font-size:.95rem; width:34px; height:34px; border-radius:8px;
  background:var(--s1); border:1px solid var(--border);
  display:flex; align-items:center; justify-content:center;
  margin-bottom:.75rem; flex-shrink:0;
}
.cls-name { font-size:.95rem; font-weight:700; color:var(--text);
            letter-spacing:-.02em; margin-bottom:.25rem; }
.cls-desc { font-size:.78rem; color:var(--sub); line-height:1.5; flex-grow:1; }
.cls-pill {
  display:inline-flex; align-items:center; gap:.25rem;
  font-size:.65rem; font-weight:600; padding:.15rem .45rem;
  border-radius:99px; margin-top:.55rem; width:fit-content;
}
.pill-on  { background:rgba(34,197,94,.1); color:#16a34a; }
.pill-off { background:var(--s1); color:var(--muted); border:1px solid var(--border); }

/* Info panel */
.info-panel {
  background:var(--s0); border:1px solid var(--border);
  border-radius:12px; padding:1.4rem 1.5rem; height:auto;
  animation:up .38s ease .22s both;
}
.info-title { font-size:.58rem; font-weight:700; letter-spacing:.13em;
              text-transform:uppercase; color:var(--muted); margin-bottom:.85rem; }
.info-step  { display:flex; align-items:flex-start; gap:.6rem; margin-bottom:.65rem; }
.info-step:last-child { margin-bottom:0; }
.info-n {
  font-size:.62rem; font-weight:700; min-width:20px; height:20px;
  background:var(--s1); border:1px solid var(--border);
  border-radius:6px; display:flex; align-items:center; justify-content:center;
  flex-shrink:0; color:var(--sub); margin-top:1px;
}
.info-txt { font-size:.82rem; color:var(--sub); line-height:1.55; }
.info-txt strong { color:var(--text); font-weight:600; }

/* ── TOPIC PICKER ──────────────────────── */
.tp-card {
  background:var(--s0); border:1px solid var(--border);
  border-radius:10px; padding:1.1rem 1.35rem;
  display:flex; align-items:center; gap:1rem;
  cursor:default; transition:border-color .18s, box-shadow .2s, transform .2s;
  margin-bottom:.5rem; animation:up .35s ease both;
}
.tp-card:hover { border-color:var(--border2); box-shadow:0 4px 14px rgba(0,0,0,.06); transform:translateX(3px); }
.tp-card-a1 { animation-delay:.04s; }
.tp-card-a2 { animation-delay:.1s;  }
.tp-card-a3 { animation-delay:.16s; }

.tp-num {
  font-size:.62rem; font-weight:700; letter-spacing:.06em;
  color:var(--muted); min-width:24px; flex-shrink:0;
}
.tp-info { flex-grow:1; }
.tp-label { font-size:.6rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase;
            color:var(--muted); margin-bottom:.18rem; }
.tp-name  { font-size:.94rem; font-weight:700; color:var(--text); letter-spacing:-.02em; }
.tp-meta  { font-size:.73rem; color:var(--muted); margin-top:.12rem; }
.tp-arrow { font-size:.85rem; color:var(--muted); flex-shrink:0; transition:transform .2s; }
.tp-card:hover .tp-arrow { transform:translateX(3px); }

/* ── LESSON PAGE ───────────────────────── */
.les-head { padding:.5rem 0 1.5rem; animation:up .35s ease both; }
.les-crumb { font-size:.65rem; color:var(--muted); margin-bottom:.5rem;
             display:flex; align-items:center; gap:.3rem; }
.les-title { font-size:1.85rem; font-weight:800; letter-spacing:-.04em;
             color:var(--text); line-height:1.1; }

/* Content blocks */
.blk {
  border-radius:8px; padding:.85rem 1.05rem; margin:.45rem 0;
  border-left:2px solid; font-size:.865rem; line-height:1.72;
  animation:fade .35s ease both;
}
.blk-text { border-left:none; padding-left:0; border-radius:0;
            background:none; margin:.3rem 0; }
.blk-text p { font-size:.9rem; color:var(--sub) !important;
              line-height:1.75 !important; margin:0 !important; }
.blk-def  { background:rgba(99,102,241,.06); border-color:#6366f1; }
.blk-key  { background:rgba(168,85,247,.06); border-color:#a855f7; }
.blk-ex   { background:rgba(16,185,129,.06); border-color:#10b981; }
.blk-tip  { background:rgba(245,158,11,.06); border-color:#f59e0b; }

.blk-lbl {
  font-size:.55rem; font-weight:800; letter-spacing:.14em; text-transform:uppercase;
  margin-bottom:.28rem; display:flex; align-items:center; gap:.3rem;
}
.blk-def .blk-lbl  { color:#6366f1; }
.blk-key .blk-lbl  { color:#a855f7; }
.blk-ex  .blk-lbl  { color:#10b981; }
.blk-tip .blk-lbl  { color:#f59e0b; }

.blk-term { font-size:.88rem; font-weight:700; color:var(--text); margin-bottom:.15rem; }
.blk-body { color:var(--sub); font-size:.865rem; line-height:1.72; }
.blk-body strong { color:var(--text); font-weight:600; }

/* separator */
.sep {
  display:flex; align-items:center; gap:.6rem;
  margin:1.65rem 0 1rem; animation:fade .4s ease .1s both;
}
.sep-t { font-size:.58rem; font-weight:700; letter-spacing:.13em;
         text-transform:uppercase; color:var(--muted); white-space:nowrap; }
.sep-l { flex-grow:1; height:1px; background:var(--border); }

/* ── QUIZ ──────────────────────────────── */
.quiz-bar {
  background:var(--s1); border:1px solid var(--border);
  border-radius:10px; padding:1.25rem 1.5rem; margin-bottom:1rem;
  animation:up .35s ease .05s both;
}
.quiz-bar-lbl { font-size:.58rem; font-weight:700; letter-spacing:.13em;
                text-transform:uppercase; color:var(--muted); margin-bottom:.25rem; }
.quiz-bar-ttl { font-size:1.15rem; font-weight:800; letter-spacing:-.03em;
                color:var(--text); margin-bottom:.12rem; }
.quiz-bar-sub { font-size:.77rem; color:var(--muted); }

div[role="radiogroup"] {
  background:var(--s0) !important; border:1px solid var(--border) !important;
  border-radius:9px !important; padding:1.1rem 1.4rem !important;
  margin-bottom:.4rem !important;
  transition:border-color .15s !important;
}
div[role="radiogroup"]:hover { border-color:var(--border2) !important; }

/* ── RESULT ────────────────────────────── */
.result {
  border-radius:10px; padding:1.6rem 1.75rem; margin-top:1rem;
  animation:up .35s ease both;
}
.r-pass { background:rgba(34,197,94,.06);  border:1px solid rgba(34,197,94,.18); }
.r-fail { background:rgba(239,68,68,.05);  border:1px solid rgba(239,68,68,.15); }
.r-lbl  { font-size:.58rem; font-weight:700; letter-spacing:.13em;
          text-transform:uppercase; margin-bottom:.4rem; }
.r-pass .r-lbl { color:#16a34a; }
.r-fail .r-lbl { color:#dc2626; }
.r-score { font-size:3.2rem; font-weight:900; letter-spacing:-.06em; line-height:1; }
.r-pass .r-score { color:#22c55e; }
.r-fail .r-score { color:#ef4444; }
.r-denom { font-size:1.2rem; color:var(--muted); font-weight:400; }
.r-msg   { font-size:.84rem; color:var(--sub); margin-top:.4rem; line-height:1.6; }

/* ── METRICS ───────────────────────────── */
.stat {
  background:var(--s0); border:1px solid var(--border); border-radius:10px;
  padding:1.4rem 1.25rem; text-align:center; animation:up .38s ease both;
  transition:box-shadow .2s, transform .2s;
}
.stat:hover { box-shadow:0 6px 20px rgba(0,0,0,.07); transform:translateY(-2px); }
.stat-a1 { animation-delay:.04s; } .stat-a2 { animation-delay:.1s; } .stat-a3 { animation-delay:.16s; }
.stat-v { font-size:2.6rem; font-weight:800; letter-spacing:-.055em;
          line-height:1; margin-bottom:.3rem; color:var(--text); }
.stat-l { font-size:.6rem; font-weight:700; letter-spacing:.11em;
          text-transform:uppercase; color:var(--muted); }

.prog-box {
  background:var(--s0); border:1px solid var(--border); border-radius:10px;
  padding:1.25rem 1.6rem; margin-bottom:1.1rem; animation:up .38s ease .18s both;
}
.pb-row { display:flex; justify-content:space-between; margin-bottom:.55rem; }
.pb-t   { font-size:.84rem; font-weight:700; color:var(--text); }
.pb-s   { font-size:.75rem; color:var(--muted); }
.pb-tr  { height:5px; background:var(--s2); border-radius:99px; overflow:hidden; }
.pb-bar { height:5px; background:var(--text); border-radius:99px; animation:grow .8s ease .35s both; }

.dtable { width:100%; border-collapse:collapse; background:var(--s0);
          border:1px solid var(--border); border-radius:10px; overflow:hidden;
          animation:up .38s ease .22s both; }
.dtable th { background:var(--s1); padding:.7rem 1.35rem; font-size:.58rem;
             font-weight:700; letter-spacing:.11em; text-transform:uppercase;
             color:var(--muted); border-bottom:1px solid var(--border); text-align:left; }
.dtable td { padding:.85rem 1.35rem; border-bottom:1px solid var(--border);
             font-size:.84rem; color:var(--text); }
.dtable tr:last-child td { border-bottom:none; }
.dtable tr:hover td { background:var(--s1); }

/* ── GLOBAL OVERRIDES ──────────────────── */
hr { border:none !important; border-top:1px solid var(--border) !important; margin:1.75rem 0 !important; }
p  { color:var(--sub) !important; line-height:1.7 !important; }
h1,h2,h3 { color:var(--text) !important; font-weight:800 !important; letter-spacing:-.03em !important; }
div[data-testid="stAlert"] { border-radius:8px !important; }

/* Main action button */
div[data-testid="stButton"] > button {
  font-family:'Inter',sans-serif !important; font-weight:600 !important;
  font-size:.84rem !important; letter-spacing:-.01em !important;
  border-radius:7px !important; padding:.5rem 1.25rem !important;
  background:var(--text) !important; color:var(--bg) !important;
  border:none !important; box-shadow:none !important;
  transition:opacity .18s, transform .18s !important;
}
div[data-testid="stButton"] > button:hover {
  opacity:.8 !important; transform:translateY(-1px) !important;
}
div[data-testid="stButton"] > button:disabled {
  background:var(--s2) !important; color:var(--muted) !important;
  transform:none !important; opacity:.6 !important;
}
div[data-testid="stFormSubmitButton"] > button {
  font-family:'Inter',sans-serif !important;
  background:var(--text) !important; color:var(--bg) !important;
  border:none !important; border-radius:7px !important;
  font-weight:700 !important; font-size:.88rem !important;
  padding:.55rem 1.75rem !important; letter-spacing:-.01em !important;
  transition:opacity .18s, transform .18s !important;
}
div[data-testid="stFormSubmitButton"] > button:hover {
  opacity:.78 !important; transform:translateY(-1px) !important;
}
"""

st.markdown(f"<style>{DARK if DM else LIGHT}{CSS}</style>", unsafe_allow_html=True)

# ═══════════════════════════════════════════════════════════════════════
#  DATA
# ═══════════════════════════════════════════════════════════════════════
TOPICS = {
    'reading': [
        {'id':'reading_0','label':'Lesson 1.1','name':'Elements of a Story',
         'meta':'Setting · Characters · Plot'},
        {'id':'reading_1','label':'Lesson 1.2','name':'Finding the Main Idea',
         'meta':'Topic Sentence · Supporting Details'},
        {'id':'reading_2','label':'Lesson 1.3','name':'Using Context Clues',
         'meta':'Inference · Vocabulary Strategies'},
    ],
    'math': [
        {'id':'math_0','label':'Lesson 2.1','name':'Basic Operations',
         'meta':'Addition · Subtraction · Multiplication'},
        {'id':'math_1','label':'Lesson 2.2','name':'Understanding Fractions',
         'meta':'Numerator · Denominator · Equivalence'},
        {'id':'math_2','label':'Lesson 2.3','name':'Basic Geometry',
         'meta':'Polygons · Perimeter · Area'},
    ],
    'science': [
        {'id':'science_0','label':'Lesson 3.1','name':'The Water Cycle',
         'meta':'Hydrological Cycle · States of Water'},
        {'id':'science_1','label':'Lesson 3.2','name':'Evaporation & Condensation',
         'meta':'Phase Change · Cloud Formation'},
        {'id':'science_2','label':'Lesson 3.3','name':'Precipitation & Collection',
         'meta':'Rain · Snow · Aquifers'},
    ],
}

LESSONS = {
    'reading_0': {
        'class':'reading','class_name':'Reading','title':'Elements of a Story',
        'blocks':[
            {'t':'text','body':'Every story is built on three essential foundations. Recognising them helps you analyse and enjoy any narrative.'},
            {'t':'def','term':'Setting','body':'The <strong>time and place</strong> where a story takes place — a medieval castle, a future city, a small town in summer.'},
            {'t':'def','term':'Characters','body':'The <strong>people, animals, or creatures</strong> in the story. The <em>protagonist</em> drives the story; the <em>antagonist</em> creates conflict.'},
            {'t':'def','term':'Plot','body':'The <strong>sequence of events</strong> from start to finish. Plots follow an arc: introduction → rising action → climax → resolution.'},
            {'t':'key','body':'Ask three questions when starting a story: <em>Who is here?</em> &nbsp;<em>Where and when?</em> &nbsp;<em>What happens?</em> — those are your three elements.'},
            {'t':'ex','body':'In <em>Charlotte\'s Web</em>: Setting = a farm in summer; Characters = Wilbur the pig, Charlotte the spider; Plot = Charlotte saves Wilbur from slaughter by writing in her web.'},
        ],
    },
    'reading_1': {
        'class':'reading','class_name':'Reading','title':'Finding the Main Idea',
        'blocks':[
            {'t':'text','body':'Every paragraph has one central point. Finding it quickly is a core reading skill used in every subject.'},
            {'t':'def','term':'Main Idea','body':'The <strong>primary point</strong> an author wants to communicate. Everything else in the paragraph supports or elaborates on it.'},
            {'t':'def','term':'Topic Sentence','body':'Usually the <strong>first sentence</strong> of a paragraph. It states the main idea and tells you what the rest of the paragraph will explain.'},
            {'t':'ex','body':'<em>"Dogs make excellent family pets."</em> — This sentence signals the paragraph will explain <em>why</em> dogs are good family pets. Every sentence that follows should support it.'},
            {'t':'tip','body':'If the main idea isn\'t in the first sentence, check the last — authors sometimes place it there as a conclusion or summary.'},
        ],
    },
    'reading_2': {
        'class':'reading','class_name':'Reading','title':'Using Context Clues',
        'blocks':[
            {'t':'text','body':'An unfamiliar word doesn\'t have to stop you. The words around it almost always contain enough information to work out its meaning.'},
            {'t':'def','term':'Context Clues','body':'Hints found in the <strong>surrounding words and sentences</strong> that help you infer the meaning of an unknown word.'},
            {'t':'key','body':'Four clue types: <strong>Definition</strong> ("X, which means…"), <strong>Synonym</strong> ("tired, or <em>fatigued</em>"), <strong>Antonym</strong> ("unlike shy Ana, Marco was <em>gregarious</em>"), <strong>Example</strong> ("citrus fruits, like lemons and limes…").'},
            {'t':'ex','body':'<em>"The ravenous wolf hadn\'t eaten in days and devoured the entire carcass."</em> — <em>hadn\'t eaten</em> and <em>devoured</em> tell us ravenous means extremely hungry.'},
            {'t':'tip','body':'Strategy: substitute a word you know, re-read the sentence, and check if it still makes sense.'},
        ],
    },
    'math_0': {
        'class':'math','class_name':'Mathematics','title':'Basic Operations',
        'blocks':[
            {'t':'text','body':'The four fundamental operations underpin all of mathematics. Mastering them makes every topic that follows easier.'},
            {'t':'def','term':'Addition (+)','body':'<strong>Combining</strong> numbers to find a total sum. Example: 145 + 278 = <strong>423</strong>.'},
            {'t':'def','term':'Subtraction (−)','body':'<strong>Finding the difference</strong> between two numbers. Example: 500 − 278 = <strong>222</strong>.'},
            {'t':'def','term':'Multiplication (×)','body':'A <strong>shortcut for repeated addition</strong>. The result is called the product. Example: 15 × 8 = <strong>120</strong>.'},
            {'t':'tip','body':'Memorising the times tables up to 12 × 12 will speed up every calculation you do — it\'s worth the effort early on.'},
        ],
    },
    'math_1': {
        'class':'math','class_name':'Mathematics','title':'Understanding Fractions',
        'blocks':[
            {'t':'text','body':'Fractions express parts of a whole. They appear in cooking, measurements, probability, and almost every practical situation.'},
            {'t':'def','term':'Numerator','body':'The <strong>top number</strong> — tells you how many parts you have. In ¾, the numerator is 3.'},
            {'t':'def','term':'Denominator','body':'The <strong>bottom number</strong> — tells you how many equal parts make the whole. In ¾, the denominator is 4. <strong>It can never be zero.</strong>'},
            {'t':'ex','body':'A pizza cut into 8 slices. You eat 3. You ate <strong>3/8</strong> of the pizza — 3 parts out of 8 total equal parts.'},
            {'t':'key','body':'<strong>Equivalent fractions</strong> have the same value: ½ = 2/4 = 4/8. Simplify by dividing both numbers by their greatest common factor.'},
        ],
    },
    'math_2': {
        'class':'math','class_name':'Mathematics','title':'Basic Geometry',
        'blocks':[
            {'t':'text','body':'Geometry is the study of shapes, sizes, and spatial relationships. Even basic geometry has constant real-world applications.'},
            {'t':'def','term':'Polygon','body':'A <strong>flat, closed shape with straight sides</strong>. Named by side count: triangle (3), quadrilateral (4), pentagon (5), hexagon (6).'},
            {'t':'def','term':'Perimeter','body':'The <strong>total distance around the outside</strong> of a shape. For a square with side 9: P = 4 × 9 = <strong>36 units</strong>.'},
            {'t':'ex','body':'Fencing a 20 m × 15 m yard: P = 2 × (20 + 15) = <strong>70 m</strong> of fencing needed.'},
            {'t':'tip','body':'Remember the difference: <strong>perimeter</strong> = distance around the edge. <strong>Area</strong> = space inside. Don\'t mix them up.'},
        ],
    },
    'science_0': {
        'class':'science','class_name':'Natural Sciences','title':'The Water Cycle',
        'blocks':[
            {'t':'text','body':'Earth\'s water has been cycling continuously for billions of years. The water in your glass may have once been part of an ancient ocean.'},
            {'t':'def','term':'Water Cycle','body':'The <strong>continuous movement of water</strong> through Earth\'s systems — oceans, atmosphere, land, and underground. Also called the hydrological cycle.'},
            {'t':'key','body':'Water exists in three states: <strong>liquid</strong> (rivers, oceans), <strong>gas</strong> (water vapour), and <strong>solid</strong> (ice, snow). The cycle moves water between all three.'},
            {'t':'tip','body':'Earth\'s total water supply is constant — it never gets created or destroyed, only changes location and state.'},
        ],
    },
    'science_1': {
        'class':'science','class_name':'Natural Sciences','title':'Evaporation & Condensation',
        'blocks':[
            {'t':'text','body':'These two processes are what lift water from the surface into the sky and bring it back down again.'},
            {'t':'def','term':'Evaporation','body':'The sun\'s energy converts <strong>liquid water to water vapour</strong> (gas). Happens from oceans, lakes, rivers, and puddles.'},
            {'t':'def','term':'Condensation','body':'Water vapour <strong>cools and becomes liquid droplets</strong>, forming clouds — billions of tiny droplets suspended in air.'},
            {'t':'ex','body':'A cold glass on a warm day gets wet on the outside. That\'s condensation — air-moisture cools on the glass surface and turns back to liquid.'},
            {'t':'key','body':'The higher water vapour rises, the cooler it gets. At the <em>dew point</em> temperature, condensation begins and clouds form.'},
        ],
    },
    'science_2': {
        'class':'science','class_name':'Natural Sciences','title':'Precipitation & Collection',
        'blocks':[
            {'t':'text','body':'Once clouds hold too much water, gravity returns it to the surface. This water then collects, ready to begin the cycle again.'},
            {'t':'def','term':'Precipitation','body':'Any water that <strong>falls from clouds to the surface</strong> — rain, snow, sleet, or hail. The type depends on temperature.'},
            {'t':'def','term':'Aquifer','body':'An <strong>underground rock layer</strong> that stores and transmits groundwater. A critical source of fresh water worldwide.'},
            {'t':'ex','body':'Precipitation type by temperature: <strong>Rain</strong> (above 0°C), <strong>Snow</strong> (below 0°C), <strong>Sleet</strong> (rain that freezes mid-fall), <strong>Hail</strong> (ice balls formed by updrafts).'},
            {'t':'tip','body':'The full cycle in order: <strong>Evaporation → Condensation → Precipitation → Collection → repeat</strong>. The sun drives every step.'},
        ],
    },
}

QUIZZES = {
    'reading': [
        {"q":"What do we call the specific time and place where a story happens?",
         "o":["The Plot","The Characters","The Setting","The Title"],"a":"The Setting"},
        {"q":"Where is the main idea of a paragraph usually located?",
         "o":["In the middle","At the very end","In the topic sentence","In the dictionary"],"a":"In the topic sentence"},
        {"q":"What are hints around a new word that help you understand its meaning?",
         "o":["Context clues","Story settings","Hidden numbers","Spelling words"],"a":"Context clues"},
        {"q":"Who are the people or animals that take part in a story?",
         "o":["The Authors","The Readers","The Characters","The Settings"],"a":"The Characters"},
        {"q":"What is the sequence of events from beginning to end of a story called?",
         "o":["The Plot","The Cover","The Vocabulary","The Conclusion"],"a":"The Plot"},
    ],
    'math': [
        {"q":"What is the total sum when you combine 145 and 278?",
         "o":["423","413","433","323"],"a":"423"},
        {"q":"What is the perimeter of a square if one side measures 9 units?",
         "o":["18 units","27 units","36 units","81 units"],"a":"36 units"},
        {"q":"In the fraction 3/4, what does the number 4 represent?",
         "o":["The part we have","The total equal parts in the whole","The sum","The difference"],
         "a":"The total equal parts in the whole"},
        {"q":"What is the product of 15 multiplied by 8?",
         "o":["100","110","120","130"],"a":"120"},
        {"q":"What is the mathematical term for a flat shape with straight sides?",
         "o":["Circle","Sphere","Polygon","Line"],"a":"Polygon"},
    ],
    'science': [
        {"q":"What process changes liquid water into an invisible gas?",
         "o":["Condensation","Evaporation","Precipitation","Freezing"],"a":"Evaporation"},
        {"q":"What provides the main energy that powers the water cycle?",
         "o":["The Moon","The Wind","The Sun","The Ocean"],"a":"The Sun"},
        {"q":"What forms in the sky when water vapor cools and condenses?",
         "o":["Raindrops","Clouds","Rivers","Groundwater"],"a":"Clouds"},
        {"q":"Which of the following is an example of precipitation?",
         "o":["Snow falling","A puddle drying","Water boiling","Ice melting"],"a":"Snow falling"},
        {"q":"Where does a large amount of water collect underground?",
         "o":["Aquifer","Cloud","Atmosphere","Evaporator"],"a":"Aquifer"},
    ],
}

CLASS_META = {
    'reading': {'name':'Reading',         'icon':'📖','num':'01','next':'math',
                'sub':'Language Arts',    'topics':TOPICS['reading']},
    'math':    {'name':'Mathematics',      'icon':'📐','num':'02','next':'science',
                'sub':'Quantitative Reasoning','topics':TOPICS['math']},
    'science': {'name':'Natural Sciences', 'icon':'🌊','num':'03','next':None,
                'sub':'Earth Science',    'topics':TOPICS['science']},
}

# ═══════════════════════════════════════════════════════════════════════
#  HELPERS  — defined before the if/elif chain
# ═══════════════════════════════════════════════════════════════════════
def render_block(b):
    t = b['t']
    if t == 'text':
        st.markdown(f"<div class='blk blk-text'><p>{b['body']}</p></div>",
                    unsafe_allow_html=True)
    elif t == 'def':
        st.markdown(f"""
        <div class='blk blk-def'>
            <div class='blk-lbl'>📘 Definition</div>
            <div class='blk-term'>{b['term']}</div>
            <div class='blk-body'>{b['body']}</div>
        </div>""", unsafe_allow_html=True)
    elif t == 'key':
        st.markdown(f"""
        <div class='blk blk-key'>
            <div class='blk-lbl'>💡 Key Concept</div>
            <div class='blk-body'>{b['body']}</div>
        </div>""", unsafe_allow_html=True)
    elif t == 'ex':
        st.markdown(f"""
        <div class='blk blk-ex'>
            <div class='blk-lbl'>📝 Example</div>
            <div class='blk-body'>{b['body']}</div>
        </div>""", unsafe_allow_html=True)
    elif t == 'tip':
        st.markdown(f"""
        <div class='blk blk-tip'>
            <div class='blk-lbl'>✏️ Study Tip</div>
            <div class='blk-body'>{b['body']}</div>
        </div>""", unsafe_allow_html=True)


def render_quiz(cls_id, lesson_data):
    """Renders the end-of-class assessment (shown only on last topic)."""
    quiz  = QUIZZES[cls_id]
    meta  = CLASS_META[cls_id]
    sk_s  = f'{cls_id}_q_started'
    sk_sb = f'{cls_id}_q_submitted'
    sk_sc = f'{cls_id}_q_score'
    next_ = meta['next']

    st.markdown("""
    <div class='sep'>
        <span class='sep-t'>Class Assessment</span>
        <span class='sep-l'></span>
    </div>""", unsafe_allow_html=True)

    if not st.session_state[sk_s]:
        st.markdown("""
        <p style='font-size:.84rem;margin-bottom:.6rem!important;'>
            You've reviewed all three topics. Take the class quiz to unlock the next subject.
        </p>""", unsafe_allow_html=True)
        c1, c2, c3 = st.columns([2, 1.1, 2])
        with c2:
            st.button("Start Quiz →", key=f"start_{cls_id}", use_container_width=True)
        if st.session_state.get(f"start_{cls_id}"):
            st.session_state[sk_s] = True
            st.rerun()

    if st.session_state[sk_s]:
        st.markdown(f"""
        <div class='quiz-bar'>
            <div class='quiz-bar-lbl'>Formative Assessment · {meta['name']}</div>
            <div class='quiz-bar-ttl'>Knowledge Check</div>
            <div class='quiz-bar-sub'>5 questions &nbsp;·&nbsp; One correct answer each</div>
        </div>""", unsafe_allow_html=True)

        with st.form(key=f'quiz_{cls_id}', clear_on_submit=False):
            ans = []
            for i, q in enumerate(quiz):
                st.markdown(f"**{i+1}.&nbsp; {q['q']}**")
                a = st.radio("", q['o'], key=f"qa_{cls_id}_{i}",
                             label_visibility="collapsed", index=None)
                ans.append(a)
                if i < len(quiz) - 1:
                    st.markdown("<div style='height:.05rem'></div>", unsafe_allow_html=True)
            st.markdown("<div style='height:.35rem'></div>", unsafe_allow_html=True)
            sub = st.form_submit_button("Submit Answers")

        if sub:
            if None in ans:
                st.error("Answer all 5 questions before submitting.")
            else:
                score = sum(1 for i, q in enumerate(quiz) if ans[i] == q['a'])
                st.session_state[sk_sc] = score
                st.session_state[sk_sb] = True

        if st.session_state[sk_sb]:
            sc     = st.session_state[sk_sc]
            passed = sc >= 4
            rc  = "r-pass" if passed else "r-fail"
            tag = "✓ Competency Verified" if passed else "✗ Below Threshold"
            msg = ("Well done — the next class is now unlocked." if passed
                   else "Review the three topics above, then try again.")
            st.markdown(f"""
            <div class='result {rc}'>
                <div class='r-lbl'>{tag}</div>
                <div>
                    <span class='r-score'>{sc}</span>
                    <span class='r-denom'>&nbsp;/ {len(quiz)}</span>
                </div>
                <div class='r-msg'>{msg}</div>
            </div>""", unsafe_allow_html=True)

            if passed and next_ and next_ not in st.session_state.unlocked_cls:
                st.session_state.unlocked_cls.append(next_)

            if not passed:
                st.markdown("<div style='height:.4rem'></div>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns([2, 1.1, 2])
                with c2:
                    st.button("Retry", key=f"retry_{cls_id}", use_container_width=True)
                if st.session_state.get(f"retry_{cls_id}"):
                    st.session_state[sk_sb] = False
                    st.rerun()


# ═══════════════════════════════════════════════════════════════════════
#  SIDEBAR
# ═══════════════════════════════════════════════════════════════════════
view     = st.session_state.view
unlocked = st.session_state.unlocked_cls
done = sum([
    st.session_state.reading_q_submitted and st.session_state.reading_q_score >= 4,
    st.session_state.math_q_submitted    and st.session_state.math_q_score    >= 4,
    st.session_state.science_q_submitted and st.session_state.science_q_score >= 4,
])
pct = int(done / 3 * 100)

def sdot(cls_id):
    if st.session_state[f'{cls_id}_q_submitted'] and st.session_state[f'{cls_id}_q_score'] >= 4:
        return 'd-green'
    return 'd-blue' if cls_id in unlocked else 'd-grey'

def sb_active_row(icon, txt, dcls):
    st.markdown(f"""
    <div class='sb-row-active'>
        <span class='sb-row-icon'>{icon}</span>
        <span class='sb-row-text'>{txt}</span>
        <span class='sb-dot {dcls}'></span>
    </div>""", unsafe_allow_html=True)

def sb_locked_row(icon, txt):
    st.markdown(f"""
    <div class='sb-row-locked'>
        <span class='sb-row-icon'>🔒</span>
        <span class='sb-row-text'>{txt}</span>
    </div>""", unsafe_allow_html=True)

with st.sidebar:
    mode_lbl = ("☀️  Light Mode" if DM else "🌙  Dark Mode")
    st.markdown("""
    <div class='sb-top'>
        <div class='sb-logo'>DANILO</div>
        <div class='sb-tag'>Academic Platform</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div class="theme-wrap">', unsafe_allow_html=True)
    st.button(mode_lbl, key="theme_btn", on_click=flip_theme,
              use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb-label">Menu</div>', unsafe_allow_html=True)

    if view == 'dashboard':
        sb_active_row("⊞", "Dashboard", "d-blue")
    else:
        st.button("⊞  Dashboard", key="nav_home", on_click=go,
                  args=('dashboard',), use_container_width=True)

    st.markdown('<div class="sb-label">Classes</div>', unsafe_allow_html=True)
    for cid, icon, name in [('reading','📖','Reading'),
                              ('math','📐','Mathematics'),
                              ('science','🌊','Natural Sciences')]:
        vk = f'class_{cid}'
        is_active = view == vk or view.startswith(f'lesson_{cid}')
        if is_active:
            sb_active_row(icon, name, sdot(cid))
        elif cid in unlocked:
            st.button(f"{icon}  {name}", key=f"nav_{cid}", on_click=go,
                      args=(vk,), use_container_width=True)
        else:
            sb_locked_row(icon, name)

    st.markdown('<div class="sb-label">Records</div>', unsafe_allow_html=True)
    if view == 'metrics':
        sb_active_row("📊", "Metrics", "d-grey")
    else:
        st.button("📊  Metrics", key="nav_metrics", on_click=go,
                  args=('metrics',), use_container_width=True)

    st.markdown(f"""
    <div class='sb-foot'>
        <div class='sb-foot-head'>
            <span class='sb-foot-lbl'>Progress</span>
            <span class='sb-foot-pct'>{pct}%</span>
        </div>
        <div class='sb-track'>
            <div class='sb-bar' style='--w:{pct}%; width:{pct}%;'></div>
        </div>
        <div class='sb-foot-sub'>{done} of 3 classes completed</div>
    </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════
#  DASHBOARD
# ═══════════════════════════════════════════════════════════════════════
if view == 'dashboard':
    st.markdown("""
    <div class='pg-head'>
        <div class='pg-title'>DANILO</div>
        <div class='pg-sub'>
            Pick a class, choose a topic, and work through the lesson.
            Pass the quiz to unlock the next class.
        </div>
    </div>""", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3, gap="medium")
    order = [('reading', c1, 'cls-card-a1'),
             ('math',    c2, 'cls-card-a2'),
             ('science', c3, 'cls-card-a3')]

    for cid, col, anim in order:
        m      = CLASS_META[cid]
        locked = cid not in unlocked
        pill   = ('<span class="cls-pill pill-off">🔒 Locked</span>'
                  if locked else
                  '<span class="cls-pill pill-on">● Available</span>')
        dim    = " cls-locked" if locked else ""
        with col:
            st.markdown(f"""
            <div class='cls-card{dim} {anim}'>
                <span class='cls-num'>{m['num']}</span>
                <div class='cls-icon'>{m['icon']}</div>
                <div class='cls-name'>{m['name']}</div>
                <div class='cls-desc'>{m['sub']} &nbsp;·&nbsp; 3 topics</div>
                {pill}
            </div>""", unsafe_allow_html=True)
            st.button("Open Class", key=f"db_{cid}", on_click=go,
                      args=(f'class_{cid}',), disabled=locked,
                      use_container_width=True)

    st.markdown("<div style='height:.5rem'></div>", unsafe_allow_html=True)
    col4, col5 = st.columns([1, 1.65], gap="medium")

    with col4:
        st.markdown(f"""
        <div class='cls-card cc-a4' style='height:auto;min-height:160px;'>
            <div class='cls-icon'>📊</div>
            <div class='cls-name'>Metrics</div>
            <div class='cls-desc'>Scores and progress records</div>
            <div style='margin-top:.7rem;'>
                <div style='display:flex;justify-content:space-between;
                            font-size:.65rem;font-weight:600;color:var(--muted);margin-bottom:.3rem;'>
                    <span>Completed</span><span>{pct}%</span>
                </div>
                <div class='pb-tr'><div class='pb-bar' style='--w:{pct}%;width:{pct}%;'></div></div>
            </div>
        </div>""", unsafe_allow_html=True)
        st.button("View Metrics", key="db_metrics", on_click=go,
                  args=('metrics',), use_container_width=True)

    with col5:
        st.markdown("""
        <div class='info-panel'>
            <div class='info-title'>How it works</div>
            <div class='info-step'>
                <div class='info-n'>1</div>
                <div class='info-txt'>
                    <strong>Open a Class</strong> — choose Reading, Mathematics, or Natural Sciences.
                </div>
            </div>
            <div class='info-step'>
                <div class='info-n'>2</div>
                <div class='info-txt'>
                    <strong>Pick a Topic</strong> — select any of the three lessons inside the class.
                </div>
            </div>
            <div class='info-step'>
                <div class='info-n'>3</div>
                <div class='info-txt'>
                    <strong>Study & Quiz</strong> — read through the lesson, then take the class
                    assessment from the last topic page. Score 4/5 to unlock the next class.
                </div>
            </div>
        </div>""", unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════════
#  CLASS PAGES  (topic picker)
# ═══════════════════════════════════════════════════════════════════════
elif view.startswith('class_'):
    cid  = view.split('class_')[1]
    meta = CLASS_META[cid]

    st.button("← Back", key=f"back_cls_{cid}", on_click=go, args=('dashboard',))
    st.markdown("<div style='height:.25rem'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='pg-head' style='padding-bottom:1.5rem;'>
        <div class='pg-crumb'>Dashboard &rsaquo; {meta['name']}</div>
        <div class='pg-title'>{meta['icon']} {meta['name']}</div>
        <div class='pg-sub'>{meta['sub']} &nbsp;·&nbsp; Quarter 1 &nbsp;·&nbsp; 3 Topics</div>
    </div>""", unsafe_allow_html=True)

    st.markdown("<div style='font-size:.72rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:var(--muted);margin-bottom:.65rem;'>Topics</div>", unsafe_allow_html=True)

    anim_map = ['tp-card-a1', 'tp-card-a2', 'tp-card-a3']
    for i, topic in enumerate(meta['topics']):
        st.markdown(f"""
        <div class='tp-card {anim_map[i]}'>
            <span class='tp-num'>0{i+1}</span>
            <div class='tp-info'>
                <div class='tp-label'>{topic['label']}</div>
                <div class='tp-name'>{topic['name']}</div>
                <div class='tp-meta'>{topic['meta']}</div>
            </div>
            <span class='tp-arrow'>›</span>
        </div>""", unsafe_allow_html=True)
        st.button(f"Open →", key=f"tp_{topic['id']}", on_click=go,
                  args=(f"lesson_{topic['id']}",), use_container_width=False)


# ═══════════════════════════════════════════════════════════════════════
#  LESSON PAGES
# ═══════════════════════════════════════════════════════════════════════
elif view.startswith('lesson_'):
    lesson_id = view.split('lesson_')[1]
    les       = LESSONS[lesson_id]
    cid       = les['class']
    meta      = CLASS_META[cid]

    # Figure out which topic index this is
    topic_ids = [t['id'] for t in meta['topics']]
    t_idx     = topic_ids.index(lesson_id)
    is_last   = (t_idx == len(topic_ids) - 1)

    st.button("← Back to Topics", key=f"back_les_{lesson_id}", on_click=go,
              args=(f'class_{cid}',))
    st.markdown("<div style='height:.25rem'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='les-head'>
        <div class='les-crumb'>
            Dashboard &rsaquo; {meta['name']} &rsaquo; {les['title']}
        </div>
        <div class='les-title'>{les['title']}</div>
    </div>""", unsafe_allow_html=True)

    # Content blocks
    for blk in les['blocks']:
        render_block(blk)

    # Navigation between topics
    st.markdown("<div style='height:.75rem'></div>", unsafe_allow_html=True)
    nav_col1, nav_col2, nav_col3 = st.columns([1, 1, 1])

    with nav_col1:
        if t_idx > 0:
            prev_id = topic_ids[t_idx - 1]
            prev_name = meta['topics'][t_idx - 1]['name']
            st.button(f"← {prev_name}", key=f"prev_{lesson_id}",
                      on_click=go, args=(f'lesson_{prev_id}',))

    with nav_col3:
        if not is_last:
            next_id   = topic_ids[t_idx + 1]
            next_name = meta['topics'][t_idx + 1]['name']
            st.button(f"{next_name} →", key=f"next_{lesson_id}",
                      on_click=go, args=(f'lesson_{next_id}',))

    # Show quiz only on the last topic
    if is_last:
        render_quiz(cid, les)


# ═══════════════════════════════════════════════════════════════════════
#  METRICS
# ═══════════════════════════════════════════════════════════════════════
elif view == 'metrics':
    st.markdown("""
    <div class='pg-head' style='padding-bottom:1.5rem;'>
        <div class='pg-crumb'>Dashboard &rsaquo; Metrics</div>
        <div class='pg-title'>Academic Metrics</div>
    </div>""", unsafe_allow_html=True)

    sc_sum, sc_cnt = 0, 0
    for cid2 in ['reading', 'math', 'science']:
        if st.session_state[f'{cid2}_q_submitted']:
            sc_sum += st.session_state[f'{cid2}_q_score']
            sc_cnt += 1
    avg_pct  = int(sc_sum / (sc_cnt * 5) * 100) if sc_cnt else 0
    prog_pct = int(done / 3 * 100)

    c1, c2, c3 = st.columns(3, gap="medium")
    with c1:
        st.markdown(f"<div class='stat stat-a1'><div class='stat-v'>{done}</div><div class='stat-l'>Classes Passed</div></div>", unsafe_allow_html=True)
    with c2:
        st.markdown(f"<div class='stat stat-a2'><div class='stat-v'>{avg_pct}%</div><div class='stat-l'>Mean Accuracy</div></div>", unsafe_allow_html=True)
    with c3:
        st.markdown(f"<div class='stat stat-a3'><div class='stat-v'>{prog_pct}%</div><div class='stat-l'>Curriculum Done</div></div>", unsafe_allow_html=True)

    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class='prog-box'>
        <div class='pb-row'>
            <span class='pb-t'>Overall Progress</span>
            <span class='pb-s'>{done} of 3 classes completed</span>
        </div>
        <div class='pb-tr'><div class='pb-bar' style='--w:{prog_pct}%;width:{prog_pct}%;'></div></div>
    </div>""", unsafe_allow_html=True)

    def cell(cid2):
        sub  = st.session_state[f'{cid2}_q_submitted']
        sc   = st.session_state[f'{cid2}_q_score']
        lock = cid2 not in unlocked
        if lock: return '<span style="color:var(--muted);font-weight:500;">Locked</span>',      "—"
        if sub and sc >= 4: return '<span style="color:#16a34a;font-weight:700;">✓ Passed</span>',   f"{sc}/5"
        if sub:             return '<span style="color:#dc2626;font-weight:700;">✗ Retry</span>',    f"{sc}/5"
        return '<span style="color:var(--sub);font-weight:500;">In Progress</span>', "—"

    s1,d1=cell('reading'); s2,d2=cell('math'); s3,d3=cell('science')
    st.markdown(f"""
    <table class='dtable'>
        <thead><tr><th>#</th><th>Class</th><th>Status</th><th>Score</th></tr></thead>
        <tbody>
            <tr>
                <td style='color:var(--muted);font-size:.7rem;font-weight:700;'>01</td>
                <td style='font-weight:600;'>📖 Reading</td><td>{s1}</td>
                <td style='font-family:monospace;color:var(--muted);'>{d1}</td>
            </tr>
            <tr>
                <td style='color:var(--muted);font-size:.7rem;font-weight:700;'>02</td>
                <td style='font-weight:600;'>📐 Mathematics</td><td>{s2}</td>
                <td style='font-family:monospace;color:var(--muted);'>{d2}</td>
            </tr>
            <tr>
                <td style='color:var(--muted);font-size:.7rem;font-weight:700;'>03</td>
                <td style='font-weight:600;'>🌊 Natural Sciences</td><td>{s3}</td>
                <td style='font-family:monospace;color:var(--muted);'>{d3}</td>
            </tr>
        </tbody>
    </table>""", unsafe_allow_html=True)
