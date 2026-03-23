import streamlit as st
import os

if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write(
        '[theme]\nbase="light"\nprimaryColor="#1a73e8"\n'
        'backgroundColor="#f0f4f9"\nsecondaryBackgroundColor="#ffffff"\n'
        'textColor="#202124"\nfont="sans serif"\n'
    )

st.set_page_config(
    page_title="DANILO Classroom",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Global CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Roboto:wght@300;400;500;700&family=Roboto+Mono&display=swap');

/* reset */
html, body, [class*="css"] { font-family: 'Roboto', sans-serif !important; }

/* page background */
.stApp { background-color: #f0f4f9 !important; }

/* sidebar */
section[data-testid="stSidebar"] {
    background: #ffffff !important;
    border-right: 1px solid #e0e0e0 !important;
    padding-top: 0 !important;
}
section[data-testid="stSidebar"] > div { padding-top: 0 !important; }

/* hide hamburger & default header */
#MainMenu, footer, header { visibility: hidden; }

/* block container */
.block-container {
    padding: 2rem 2.5rem 5rem !important;
    max-width: 1100px !important;
}

/* ── Sidebar branding ── */
.sidebar-brand {
    background: linear-gradient(135deg, #1e8e3e 0%, #34a853 100%);
    padding: 1.4rem 1.2rem 1.2rem;
    margin-bottom: 0.5rem;
    display: flex;
    align-items: center;
    gap: 10px;
}
.sidebar-brand-icon { font-size: 1.8rem; }
.sidebar-brand-text {
    font-family: 'Google Sans', sans-serif !important;
    font-size: 1.2rem;
    font-weight: 700;
    color: #ffffff !important;
    line-height: 1.2;
}
.sidebar-brand-sub {
    font-size: 0.72rem;
    color: rgba(255,255,255,0.8) !important;
    font-weight: 400;
    letter-spacing: 0.04em;
}

/* ── Sidebar nav items ── */
.nav-section-label {
    font-size: 0.7rem !important;
    font-weight: 700 !important;
    color: #5f6368 !important;
    text-transform: uppercase;
    letter-spacing: 0.08em;
    padding: 0.8rem 1.2rem 0.3rem !important;
}
div[data-testid="stButton"] > button {
    border-radius: 0 24px 24px 0 !important;
    font-family: 'Roboto', sans-serif !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    padding: 0.55rem 1rem !important;
    width: 100% !important;
    text-align: left !important;
    border: none !important;
    transition: background 0.15s ease !important;
    background: transparent !important;
    color: #3c4043 !important;
}
div[data-testid="stButton"] > button:hover {
    background: #e8f5e9 !important;
    color: #1e8e3e !important;
}

/* ── Top page header bar ── */
.page-header {
    background: #ffffff;
    border-bottom: 1px solid #e0e0e0;
    padding: 1rem 2rem;
    margin: -2rem -2.5rem 2rem;
    display: flex;
    align-items: center;
    gap: 1rem;
}
.page-header-title {
    font-family: 'Google Sans', sans-serif !important;
    font-size: 1.35rem;
    font-weight: 700;
    color: #202124;
    margin: 0;
}
.page-header-avatar {
    margin-left: auto;
    width: 36px; height: 36px;
    background: linear-gradient(135deg, #1e8e3e, #34a853);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem; color: white; font-weight: 700;
}

/* ── Class banner cards (dashboard) ── */
.class-card {
    border-radius: 8px;
    overflow: hidden;
    background: #ffffff;
    box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.08);
    transition: box-shadow 0.2s ease, transform 0.15s ease;
    margin-bottom: 1rem;
    cursor: pointer;
    position: relative;
}
.class-card:hover {
    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
    transform: translateY(-2px);
}
.class-banner {
    height: 96px;
    padding: 1rem 1.2rem;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
}
.class-banner-pattern {
    position: absolute; inset: 0;
    opacity: 0.18;
    background-image: repeating-linear-gradient(
        45deg, rgba(255,255,255,0.4) 0px, rgba(255,255,255,0.4) 1px,
        transparent 1px, transparent 12px
    );
}
.class-banner-icon {
    font-size: 2.2rem;
    position: absolute;
    top: 12px; right: 16px;
    opacity: 0.9;
}
.class-name {
    font-family: 'Google Sans', sans-serif !important;
    font-size: 1.15rem;
    font-weight: 700;
    color: #ffffff;
    text-shadow: 0 1px 3px rgba(0,0,0,0.2);
    position: relative;
}
.class-section {
    font-size: 0.75rem;
    color: rgba(255,255,255,0.88);
    font-weight: 400;
    position: relative;
}
.class-card-body {
    padding: 0.75rem 1.2rem 0.6rem;
    border-top: 1px solid #f1f3f4;
    display: flex;
    align-items: center;
    justify-content: space-between;
}
.class-teacher { font-size: 0.78rem; color: #5f6368; }
.class-badge-locked {
    font-size: 0.7rem; font-weight: 600;
    background: #fce8e6; color: #c5221f;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
}
.class-badge-open {
    font-size: 0.7rem; font-weight: 600;
    background: #e6f4ea; color: #1e8e3e;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
}
.class-badge-done {
    font-size: 0.7rem; font-weight: 600;
    background: #e8f0fe; color: #1a73e8;
    padding: 0.2rem 0.6rem;
    border-radius: 12px;
}

/* ── Module lesson page ── */
.module-banner {
    border-radius: 12px;
    padding: 2rem 2.5rem;
    margin-bottom: 2rem;
    position: relative;
    overflow: hidden;
    color: white;
}
.module-banner-overlay {
    position: absolute; inset: 0;
    background-image: repeating-linear-gradient(
        -45deg, rgba(255,255,255,0.05) 0px, rgba(255,255,255,0.05) 2px,
        transparent 2px, transparent 16px
    );
}
.module-banner h1 {
    font-family: 'Google Sans', sans-serif !important;
    font-size: 1.8rem !important;
    font-weight: 700 !important;
    color: white !important;
    border: none !important;
    margin: 0 0 0.3rem !important;
    padding: 0 !important;
    position: relative;
}
.module-banner p {
    color: rgba(255,255,255,0.88) !important;
    font-size: 0.95rem !important;
    margin: 0 !important;
    position: relative;
}
.module-banner-meta {
    position: relative;
    display: flex; gap: 1rem;
    margin-top: 1rem;
}
.module-meta-chip {
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(4px);
    padding: 0.3rem 0.9rem;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 500;
    color: white;
    border: 1px solid rgba(255,255,255,0.3);
}

/* ── Lesson topic cards ── */
.topic-card {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    padding: 1.4rem 1.6rem;
    margin-bottom: 1rem;
    box-shadow: 0 1px 2px rgba(0,0,0,0.06);
}
.topic-card h3 {
    font-family: 'Google Sans', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    color: #202124 !important;
    margin: 0 0 0.6rem !important;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}
.topic-card p {
    color: #5f6368 !important;
    font-size: 0.9rem !important;
    line-height: 1.65 !important;
    margin: 0 !important;
}

/* ── Quiz / Assessment section ── */
.quiz-header {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-left: 4px solid #1a73e8;
    border-radius: 8px;
    padding: 1.2rem 1.6rem;
    margin: 1.5rem 0 1rem;
    display: flex;
    align-items: center;
    gap: 0.8rem;
}
.quiz-header-icon { font-size: 1.5rem; }
.quiz-header-title {
    font-family: 'Google Sans', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #202124;
    margin: 0;
}
.quiz-header-sub { font-size: 0.78rem; color: #5f6368; margin: 0; }

div[role="radiogroup"] {
    background-color: #fafafa !important;
    border: 1px solid #e8eaed !important;
    border-radius: 8px !important;
    padding: 1rem 1.2rem !important;
    margin-bottom: 0.8rem !important;
    box-shadow: none !important;
}

/* ── Score / result cards ── */
.score-banner {
    border-radius: 10px;
    padding: 1.5rem 2rem;
    margin: 1rem 0;
    display: flex;
    align-items: center;
    gap: 1.2rem;
}
.score-pass { background: #e6f4ea; border: 1px solid #34a853; }
.score-fail { background: #fce8e6; border: 1px solid #ea4335; }
.score-value {
    font-family: 'Google Sans', sans-serif;
    font-size: 3rem;
    font-weight: 700;
    line-height: 1;
}
.score-pass .score-value { color: #1e8e3e; }
.score-fail .score-value { color: #c5221f; }
.score-label { font-size: 0.88rem; font-weight: 500; margin-top: 0.2rem; }
.score-pass .score-label { color: #1e8e3e; }
.score-fail .score-label { color: #c5221f; }
.score-message { font-size: 0.9rem; color: #3c4043; }

/* ── Analytics cards ── */
.analytics-card {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 12px;
    padding: 1.6rem;
    text-align: center;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
}
.analytics-value {
    font-family: 'Google Sans', sans-serif;
    font-size: 2.6rem;
    font-weight: 700;
    line-height: 1;
    margin-bottom: 0.4rem;
}
.analytics-label {
    font-size: 0.78rem;
    font-weight: 700;
    color: #5f6368;
    text-transform: uppercase;
    letter-spacing: 0.06em;
}

/* ── Progress bar ── */
.progress-track {
    background: #e8eaed;
    border-radius: 99px;
    height: 8px;
    overflow: hidden;
    margin-top: 0.5rem;
}
.progress-fill {
    height: 100%;
    border-radius: 99px;
    background: linear-gradient(90deg, #1e8e3e, #34a853);
    transition: width 0.5s ease;
}

/* ── Gradebook table ── */
.gradebook {
    background: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 8px;
    overflow: hidden;
    box-shadow: 0 1px 3px rgba(0,0,0,0.08);
    width: 100%;
    border-collapse: collapse;
}
.gradebook th {
    background: #f8f9fa;
    padding: 0.85rem 1.4rem;
    text-align: left;
    font-size: 0.78rem;
    font-weight: 700;
    color: #5f6368;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    border-bottom: 1px solid #e0e0e0;
}
.gradebook td {
    padding: 0.9rem 1.4rem;
    border-bottom: 1px solid #f1f3f4;
    font-size: 0.9rem;
    color: #3c4043;
}
.gradebook tr:last-child td { border-bottom: none; }
.gradebook tr:hover td { background: #f8f9fa; }
.chip-verified {
    background: #e6f4ea; color: #1e8e3e;
    padding: 0.2rem 0.65rem; border-radius: 12px;
    font-size: 0.75rem; font-weight: 700;
    display: inline-flex; align-items: center; gap: 0.3rem;
}
.chip-pending {
    background: #fef7e0; color: #b06000;
    padding: 0.2rem 0.65rem; border-radius: 12px;
    font-size: 0.75rem; font-weight: 700;
    display: inline-flex; align-items: center; gap: 0.3rem;
}
.chip-locked {
    background: #f1f3f4; color: #5f6368;
    padding: 0.2rem 0.65rem; border-radius: 12px;
    font-size: 0.75rem; font-weight: 700;
    display: inline-flex; align-items: center; gap: 0.3rem;
}
.score-mono {
    font-family: 'Roboto Mono', monospace;
    font-weight: 600; font-size: 0.95rem;
}

/* streamlit form submit buttons */
div[data-testid="stForm"] div[data-testid="stButton"] > button {
    background: #1a73e8 !important;
    color: white !important;
    border-radius: 4px !important;
    padding: 0.6rem 1.5rem !important;
    font-weight: 500 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.02em !important;
    box-shadow: 0 1px 2px rgba(60,64,67,0.3) !important;
    width: auto !important;
}
div[data-testid="stForm"] div[data-testid="stButton"] > button:hover {
    background: #1557b0 !important;
    box-shadow: 0 2px 6px rgba(60,64,67,0.25) !important;
}
</style>
""", unsafe_allow_html=True)

# ── Session state ─────────────────────────────────────────────────────────────
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'dashboard'
if 'unlocked_modules' not in st.session_state:
    st.session_state.unlocked_modules = ['module_1']
for m in ['1', '2', '3']:
    for key in ['quiz_started', 'quiz_submitted', 'quiz_score']:
        if f'm{m}_{key}' not in st.session_state:
            st.session_state[f'm{m}_{key}'] = False if key != 'quiz_score' else 0

def navigate(view):
    st.session_state.current_view = view

# ── Quiz data ─────────────────────────────────────────────────────────────────
M1_QUIZ_DATA = [
    {"question": "What do we call the specific time and place where a story happens?",
     "options": ["The Plot", "The Characters", "The Setting", "The Title"], "answer": "The Setting"},
    {"question": "Where is the main idea of a paragraph usually located?",
     "options": ["In the middle", "At the very end", "In the topic sentence", "In the dictionary"], "answer": "In the topic sentence"},
    {"question": "What are hints around a new word called that help you understand its meaning?",
     "options": ["Context clues", "Story settings", "Hidden numbers", "Spelling words"], "answer": "Context clues"},
    {"question": "Who are the people or animals that take part in a story?",
     "options": ["The Authors", "The Readers", "The Characters", "The Settings"], "answer": "The Characters"},
    {"question": "What is the sequence of events from beginning to end of a story called?",
     "options": ["The Plot", "The Cover", "The Vocabulary", "The Conclusion"], "answer": "The Plot"},
]

M2_QUIZ_DATA = [
    {"question": "What is the total sum when you combine 145 and 278?",
     "options": ["423", "413", "433", "323"], "answer": "423"},
    {"question": "What is the perimeter of a square if one side measures 9 units?",
     "options": ["18 units", "27 units", "36 units", "81 units"], "answer": "36 units"},
    {"question": "In the fraction 3/4, what does the number 4 represent?",
     "options": ["The part we have", "The total equal parts in the whole", "The sum", "The difference"], "answer": "The total equal parts in the whole"},
    {"question": "What is the product of 15 multiplied by 8?",
     "options": ["100", "110", "120", "130"], "answer": "120"},
    {"question": "What is the mathematical term for a flat shape with straight sides?",
     "options": ["Circle", "Sphere", "Polygon", "Line"], "answer": "Polygon"},
]

M3_QUIZ_DATA = [
    {"question": "What process changes liquid water into an invisible gas called water vapor?",
     "options": ["Condensation", "Evaporation", "Precipitation", "Freezing"], "answer": "Evaporation"},
    {"question": "What provides the main energy that powers the entire water cycle?",
     "options": ["The Moon", "The Wind", "The Sun", "The Ocean"], "answer": "The Sun"},
    {"question": "What forms in the sky when water vapor cools and condenses?",
     "options": ["Raindrops", "Clouds", "Rivers", "Groundwater"], "answer": "Clouds"},
    {"question": "Which of the following is an example of precipitation?",
     "options": ["Snow falling", "A puddle drying", "Water boiling", "Ice melting"], "answer": "Snow falling"},
    {"question": "Where does a large amount of water collect underground?",
     "options": ["Aquifer", "Cloud", "Atmosphere", "Evaporator"], "answer": "Aquifer"},
]

# ── Module config ─────────────────────────────────────────────────────────────
MODULES = {
    'module_1': {
        'key': '1', 'label': 'Reading', 'icon': '📖',
        'subtitle': 'Understanding Stories and Words',
        'teacher': 'Ms. Santos',
        'color': '#1a73e8',
        'gradient': 'linear-gradient(135deg, #1a73e8 0%, #4285f4 100%)',
        'unlock_msg': 'Mathematics is now unlocked!',
        'quiz_data': M1_QUIZ_DATA,
        'topics': [
            ('📚', '1.0 Elements of a Story',
             'Every story has essential parts. The <b>setting</b> tells us when and where the story takes place. '
             'The <b>characters</b> are the people, animals, or creatures in the story. '
             'The <b>plot</b> is the sequence of events from the beginning to the end.'),
            ('🔍', '1.1 Finding the Main Idea',
             'When reading a paragraph, find the main idea — the primary point the author wants to communicate. '
             'It is often found in the <b>topic sentence</b>, usually the first sentence of the paragraph.'),
            ('💡', '1.2 Using Context Clues',
             'When you encounter an unfamiliar word, look at the surrounding words for hints about its meaning. '
             'These helpful hints are called <b>context clues</b> — no dictionary needed!'),
        ],
    },
    'module_2': {
        'key': '2', 'label': 'Mathematics', 'icon': '🔢',
        'subtitle': 'Foundational Operations and Shapes',
        'teacher': 'Mr. Reyes',
        'color': '#1e8e3e',
        'gradient': 'linear-gradient(135deg, #1e8e3e 0%, #34a853 100%)',
        'unlock_msg': 'Natural Sciences is now unlocked!',
        'quiz_data': M2_QUIZ_DATA,
        'topics': [
            ('➕', '2.0 Basic Operations',
             '<b>Addition</b> combines two numbers to find a total sum. <b>Subtraction</b> finds the difference '
             'between numbers. <b>Multiplication</b> is a faster way to perform repeated addition.'),
            ('½', '2.1 Fractions',
             'A fraction represents a part of a whole. The top number (<b>numerator</b>) shows how many parts '
             'we have. The bottom number (<b>denominator</b>) shows how many equal parts make up the whole. '
             'The denominator can never be zero.'),
            ('📐', '2.2 Basic Geometry',
             'Geometry is the study of shapes and spaces. A <b>polygon</b> is a flat shape with straight sides — '
             'like a triangle, square, or rectangle. The distance around the outside edge is the <b>perimeter</b>.'),
        ],
    },
    'module_3': {
        'key': '3', 'label': 'Natural Sciences', 'icon': '🌍',
        'subtitle': 'The Water Cycle',
        'teacher': 'Ms. Cruz',
        'color': '#e37400',
        'gradient': 'linear-gradient(135deg, #e37400 0%, #f29900 100%)',
        'unlock_msg': 'All modules complete!',
        'quiz_data': M3_QUIZ_DATA,
        'topics': [
            ('🌊', '3.0 Introduction to the Cycle',
             'The water cycle is the <b>continuous movement</b> of water on Earth. Water changes state as it '
             'moves between the ground, oceans, and sky. The total amount of water on our planet stays the '
             'same — it simply travels to different places.'),
            ('☁️', '3.1 Evaporation & Condensation',
             '<b>Evaporation</b> happens when the sun heats liquid water in rivers and oceans, turning it into '
             'water vapor. When vapor rises and cools, it undergoes <b>condensation</b>, forming the clouds we see.'),
            ('🌧️', '3.2 Precipitation & Collection',
             'When clouds become too heavy, water falls back to Earth as <b>precipitation</b> — rain, snow, or '
             'hail. It then collects in oceans, lakes, and underground <b>aquifers</b>, ready to start the cycle again.'),
        ],
    },
}

UNLOCK_CHAIN = {'module_1': 'module_2', 'module_2': 'module_3'}

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-brand-icon">🎓</div>
        <div>
            <div class="sidebar-brand-text">DANILO</div>
            <div class="sidebar-brand-sub">ACADEMIC PLATFORM</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="nav-section-label">Navigation</div>', unsafe_allow_html=True)
    st.button("🏠  Home", on_click=navigate, args=('dashboard',), use_container_width=True)
    st.button("📊  My Grades", on_click=navigate, args=('profile',), use_container_width=True)

    st.markdown('<div class="nav-section-label">Enrolled Classes</div>', unsafe_allow_html=True)
    for mod_key, mod in MODULES.items():
        locked = mod_key not in st.session_state.unlocked_modules
        icon = mod['icon']
        label = f"{'🔒' if locked else icon}  {mod['label']}"
        st.button(label, on_click=navigate, args=(mod_key,),
                  disabled=locked, use_container_width=True)

    st.markdown("---")
    st.markdown(
        '<p style="font-size:0.72rem;color:#9aa0a6;padding:0 1rem;line-height:1.5;">'
        '© 2025 DANILO Academic Platform<br>Powered by Streamlit</p>',
        unsafe_allow_html=True
    )

# ── DASHBOARD ─────────────────────────────────────────────────────────────────
if st.session_state.current_view == 'dashboard':
    st.markdown("""
    <div class="page-header">
        <span style="font-size:1.5rem;">🏠</span>
        <h1 class="page-header-title">Home</h1>
        <div class="page-header-avatar">D</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<p style="font-size:0.95rem;color:#5f6368;margin-bottom:1.5rem;">'
        'Welcome back! Continue where you left off.</p>',
        unsafe_allow_html=True
    )

    # ── Class cards ──────────────────────────────────────────────────────────
    cols = st.columns(3, gap="medium")
    for i, (mod_key, mod) in enumerate(MODULES.items()):
        locked = mod_key not in st.session_state.unlocked_modules
        m_key = mod['key']
        submitted = st.session_state[f'm{m_key}_quiz_submitted']
        score = st.session_state[f'm{m_key}_quiz_score']
        passed = submitted and score >= 4

        if passed:
            badge_html = '<span class="class-badge-done">✓ Completed</span>'
        elif locked:
            badge_html = '<span class="class-badge-locked">🔒 Locked</span>'
        else:
            badge_html = '<span class="class-badge-open">● Open</span>'

        next_mod = UNLOCK_CHAIN.get(mod_key, '')
        if locked and i > 0:
            prev_labels = list(MODULES.values())[i - 1]['label']
            teacher_text = f'Requires {prev_labels}'
        else:
            teacher_text = mod['teacher']

        with cols[i]:
            st.markdown(f"""
            <div class="class-card">
                <div class="class-banner" style="background: {mod['gradient']};">
                    <div class="class-banner-pattern"></div>
                    <div class="class-banner-icon">{mod['icon']}</div>
                    <div class="class-name">{mod['label']}</div>
                    <div class="class-section">{mod['subtitle']}</div>
                </div>
                <div class="class-card-body">
                    <span class="class-teacher">{teacher_text}</span>
                    {badge_html}
                </div>
            </div>
            """, unsafe_allow_html=True)
            st.button("Open Class →", key=f"dash_btn_{mod_key}",
                      on_click=navigate, args=(mod_key,),
                      disabled=locked, use_container_width=True)

    # ── Quick stats strip ─────────────────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    unlocked_count = len(st.session_state.unlocked_modules)
    submitted_list = [
        st.session_state[f'm{m}_quiz_submitted']
        for m in ['1', '2', '3']
    ]
    scores_list = [
        st.session_state[f'm{m}_quiz_score']
        for m in ['1', '2', '3']
        if st.session_state[f'm{m}_quiz_submitted']
    ]
    avg_acc = (sum(scores_list) / (len(scores_list) * 5) * 100) if scores_list else 0
    completed = sum(1 for m in ['1', '2', '3']
                    if st.session_state[f'm{m}_quiz_submitted']
                    and st.session_state[f'm{m}_quiz_score'] >= 4)

    c1, c2, c3, c4 = st.columns(4)
    for col, val, label, color in [
        (c1, f"{unlocked_count}/3", "Classes Unlocked", "#1a73e8"),
        (c2, f"{completed}/3", "Assessments Passed", "#1e8e3e"),
        (c3, f"{avg_acc:.0f}%", "Mean Accuracy", "#e37400"),
        (c4, f"{int(completed/3*100)}%", "Overall Progress", "#8430ce"),
    ]:
        with col:
            st.markdown(f"""
            <div class="analytics-card">
                <div class="analytics-value" style="color:{color};">{val}</div>
                <div class="analytics-label">{label}</div>
                <div class="progress-track" style="margin-top:0.8rem;">
                    <div class="progress-fill" style="width:{min(float(val.replace('%','').replace('/3','').split('/')[0]) / (3 if '/' in val and '%' not in val else 1) * (100 if '%' not in val else 1), 100):.0f}%; background:{color};"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

# ── MODULE VIEWS ──────────────────────────────────────────────────────────────
elif st.session_state.current_view in MODULES:
    mod_key = st.session_state.current_view
    mod = MODULES[mod_key]
    m_key = mod['key']

    st.markdown(f"""
    <div class="page-header">
        <span style="font-size:1.3rem;">{mod['icon']}</span>
        <h1 class="page-header-title">{mod['label']}</h1>
        <div class="page-header-avatar">D</div>
    </div>
    """, unsafe_allow_html=True)

    st.button("← Back to Home", key=f"back_{mod_key}", on_click=navigate, args=('dashboard',))
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    # Banner
    st.markdown(f"""
    <div class="module-banner" style="background: {mod['gradient']};">
        <div class="module-banner-overlay"></div>
        <h1>{mod['icon']} {mod['label']}</h1>
        <p>{mod['subtitle']}</p>
        <div class="module-banner-meta">
            <span class="module-meta-chip">👩‍🏫 {mod['teacher']}</span>
            <span class="module-meta-chip">📝 5-question quiz</span>
            <span class="module-meta-chip">⏱ ~10 min</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Topic cards
    st.markdown(
        '<p style="font-size:0.78rem;font-weight:700;color:#5f6368;'
        'text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.8rem;">'
        'LESSON MATERIAL</p>',
        unsafe_allow_html=True
    )
    for icon, title, body in mod['topics']:
        st.markdown(f"""
        <div class="topic-card">
            <h3>{icon} {title}</h3>
            <p>{body}</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="quiz-header">
        <span class="quiz-header-icon">📋</span>
        <div>
            <p class="quiz-header-title">Formative Assessment</p>
            <p class="quiz-header-sub">5 questions · Pass mark: 4/5 · Unlimited attempts</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    quiz_data = mod['quiz_data']
    submitted_key = f'm{m_key}_quiz_submitted'
    started_key = f'm{m_key}_quiz_started'
    score_key = f'm{m_key}_quiz_score'

    if not st.session_state[started_key]:
        st.button("▶  Begin Assessment", key=f"start_{mod_key}_quiz")
        if st.session_state.get(f'start_{mod_key}_quiz'):
            st.session_state[started_key] = True
            st.rerun()

    if st.session_state[started_key]:
        with st.form(key=f'{mod_key}_quiz_form', clear_on_submit=False):
            user_answers = []
            for i, q in enumerate(quiz_data):
                st.markdown(f"**Question {i+1} of {len(quiz_data)}**")
                st.markdown(f"*{q['question']}*")
                ans = st.radio("", q['options'], key=f"{mod_key}_q_{i}",
                               label_visibility="collapsed", index=None)
                user_answers.append(ans)
                if i < len(quiz_data) - 1:
                    st.markdown("---")
            st.markdown("<br>", unsafe_allow_html=True)
            submitted = st.form_submit_button("Submit Assessment")

        if submitted:
            if None in user_answers:
                st.error("⚠️ Please answer all questions before submitting.")
            else:
                score = sum(1 for i, q in enumerate(quiz_data)
                            if user_answers[i] == q['answer'])
                st.session_state[score_key] = score
                st.session_state[submitted_key] = True

        if st.session_state[submitted_key]:
            score = st.session_state[score_key]
            passed = score >= 4
            pct = int(score / len(quiz_data) * 100)

            if passed:
                st.markdown(f"""
                <div class="score-banner score-pass">
                    <div>
                        <div class="score-value">{score}/{len(quiz_data)}</div>
                        <div class="score-label">✓ Competency Verified</div>
                    </div>
                    <div class="score-message">
                        <b>Excellent work!</b> You scored {pct}% and have demonstrated mastery of this topic.<br>
                        {mod['unlock_msg']}
                    </div>
                </div>
                """, unsafe_allow_html=True)
                next_mod = UNLOCK_CHAIN.get(mod_key)
                if next_mod and next_mod not in st.session_state.unlocked_modules:
                    st.session_state.unlocked_modules.append(next_mod)
            else:
                st.markdown(f"""
                <div class="score-banner score-fail">
                    <div>
                        <div class="score-value">{score}/{len(quiz_data)}</div>
                        <div class="score-label">✗ Below Pass Mark</div>
                    </div>
                    <div class="score-message">
                        <b>Keep going!</b> You scored {pct}%. Review the lesson material above and try again.<br>
                        You need at least 4/5 to unlock the next module.
                    </div>
                </div>
                """, unsafe_allow_html=True)
                if st.button("🔄  Retry Assessment", key=f"retry_{mod_key}"):
                    st.session_state[submitted_key] = False
                    st.rerun()

# ── GRADES / ANALYTICS ────────────────────────────────────────────────────────
elif st.session_state.current_view == 'profile':
    st.markdown("""
    <div class="page-header">
        <span style="font-size:1.3rem;">📊</span>
        <h1 class="page-header-title">My Grades</h1>
        <div class="page-header-avatar">D</div>
    </div>
    """, unsafe_allow_html=True)

    st.button("← Back to Home", key="back_grades", on_click=navigate, args=('dashboard',))
    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)

    scores = {m: st.session_state[f'm{m}_quiz_score'] for m in ['1', '2', '3']}
    subs = {m: st.session_state[f'm{m}_quiz_submitted'] for m in ['1', '2', '3']}
    submitted_scores = [scores[m] for m in ['1', '2', '3'] if subs[m]]
    avg_acc = (sum(submitted_scores) / (len(submitted_scores) * 5) * 100) if submitted_scores else 0
    completed = sum(1 for m in ['1', '2', '3'] if subs[m] and scores[m] >= 4)
    unlocked = len(st.session_state.unlocked_modules)
    progress_pct = int(completed / 3 * 100)

    c1, c2, c3 = st.columns(3, gap="large")
    for col, val, label, color in [
        (c1, f"{unlocked}/3", "Modules Unlocked", "#1a73e8"),
        (c2, f"{avg_acc:.0f}%", "Mean Accuracy", "#1e8e3e"),
        (c3, f"{progress_pct}%", "Curriculum Progress", "#e37400"),
    ]:
        with col:
            st.markdown(f"""
            <div class="analytics-card">
                <div class="analytics-value" style="color:{color};">{val}</div>
                <div class="analytics-label">{label}</div>
                <div class="progress-track">
                    <div class="progress-fill" style="width:{min(float(val.replace('%','').replace('/3','').split('/')[0]) / (3 if '/' in val and '%' not in val else 1) * (100 if '%' not in val else 1), 100):.0f}%; background:{color};"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown(
        '<br><p style="font-size:0.78rem;font-weight:700;color:#5f6368;'
        'text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.8rem;">'
        'GRADEBOOK</p>',
        unsafe_allow_html=True
    )

    rows = ""
    for mod_key, mod in MODULES.items():
        m = mod['key']
        locked = mod_key not in st.session_state.unlocked_modules
        sub = subs[m]
        sc = scores[m]
        passed = sub and sc >= 4

        if locked:
            status_html = '<span class="chip-locked">🔒 Locked</span>'
            score_disp = '<span style="color:#9aa0a6;">—</span>'
            grade_disp = '<span style="color:#9aa0a6;">—</span>'
        elif passed:
            status_html = '<span class="chip-verified">✓ Verified</span>'
            score_disp = f'<span class="score-mono">{sc}/5</span>'
            grade_pct = int(sc / 5 * 100)
            grade_disp = f'<span class="score-mono" style="color:#1e8e3e;">{grade_pct}%</span>'
        elif sub:
            status_html = '<span class="chip-pending">⚠ Below Pass</span>'
            score_disp = f'<span class="score-mono">{sc}/5</span>'
            grade_pct = int(sc / 5 * 100)
            grade_disp = f'<span class="score-mono" style="color:#c5221f;">{grade_pct}%</span>'
        else:
            status_html = '<span class="chip-pending">○ Not Attempted</span>'
            score_disp = '<span style="color:#9aa0a6;">—</span>'
            grade_disp = '<span style="color:#9aa0a6;">—</span>'

        rows += f"""
        <tr>
            <td><span style="font-size:1.1rem;">{mod['icon']}</span></td>
            <td style="font-weight:500;">{mod['label']}</td>
            <td style="color:#5f6368;font-size:0.85rem;">{mod['subtitle']}</td>
            <td>{status_html}</td>
            <td>{score_disp}</td>
            <td>{grade_disp}</td>
        </tr>
        """

    st.markdown(f"""
    <table class="gradebook">
        <thead>
            <tr>
                <th></th>
                <th>Class</th>
                <th>Topic</th>
                <th>Status</th>
                <th>Score</th>
                <th>Grade</th>
            </tr>
        </thead>
        <tbody>
            {rows}
        </tbody>
    </table>
    """, unsafe_allow_html=True)
