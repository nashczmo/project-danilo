import streamlit as st
import os

if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write('[theme]\nbase="dark"\nprimaryColor="#6366f1"\nbackgroundColor="#09090f"\nsecondaryBackgroundColor="#111118"\ntextColor="#e2e8f0"\nfont="sans serif"\n')

st.set_page_config(page_title="DANILO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

    :root {
        --bg:          #09090f;
        --surface:     #111118;
        --surface2:    #16161f;
        --border:      rgba(255,255,255,0.07);
        --border-glow: rgba(99,102,241,0.35);
        --text:        #e2e8f0;
        --muted:       #64748b;
        --muted2:      #94a3b8;

        --indigo:      #6366f1;
        --indigo-soft: rgba(99,102,241,0.12);
        --indigo-glow: rgba(99,102,241,0.25);

        --emerald:     #10b981;
        --emerald-soft:rgba(16,185,129,0.12);
        --emerald-glow:rgba(16,185,129,0.25);

        --violet:      #a855f7;
        --violet-soft: rgba(168,85,247,0.12);
        --violet-glow: rgba(168,85,247,0.25);

        --amber:       #f59e0b;
        --amber-soft:  rgba(245,158,11,0.12);
        --amber-glow:  rgba(245,158,11,0.25);

        --red:         #ef4444;
        --green:       #22c55e;
    }

    html, body, [class*="css"],
    p, div, span, h1, h2, h3, h4, label, button, input, li {
        font-family: 'Inter', sans-serif !important;
    }

    .block-container {
        padding: 3.5rem 2.5rem 6rem !important;
        max-width: 1120px !important;
    }

    #MainMenu, footer, header { visibility: hidden; }
    .stApp { background: var(--bg) !important; }

    /* ── dot-grid background overlay ── */
    .stApp::before {
        content: '';
        position: fixed;
        inset: 0;
        background-image: radial-gradient(circle, rgba(255,255,255,0.045) 1px, transparent 1px);
        background-size: 28px 28px;
        pointer-events: none;
        z-index: 0;
    }

    /* ── ambient glow blobs ── */
    .stApp::after {
        content: '';
        position: fixed;
        width: 600px; height: 600px;
        border-radius: 50%;
        background: radial-gradient(circle, rgba(99,102,241,0.08) 0%, transparent 70%);
        top: -200px; left: -200px;
        pointer-events: none;
        z-index: 0;
    }

    /* ═══ HEADER / EYEBROW ═══ */
    .eyebrow {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        color: var(--indigo);
        margin-bottom: 0.6rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .eyebrow::before {
        content: '';
        display: inline-block;
        width: 20px; height: 2px;
        background: var(--indigo);
        border-radius: 2px;
    }

    .hero-title {
        font-size: 3.6rem;
        font-weight: 900;
        letter-spacing: -0.04em;
        line-height: 1;
        color: var(--text);
        margin-bottom: 0.6rem;
    }

    .hero-title span {
        background: linear-gradient(135deg, #6366f1 0%, #a855f7 50%, #ec4899 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }

    .hero-sub {
        font-size: 1.05rem;
        color: var(--muted);
        font-weight: 400;
        line-height: 1.6;
        margin-bottom: 3rem;
        max-width: 480px;
    }

    /* ═══ MODULE CARDS ═══ */
    .module-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 1.75rem;
        height: 230px;
        display: flex;
        flex-direction: column;
        position: relative;
        overflow: hidden;
        transition: border-color 0.3s, transform 0.2s, box-shadow 0.3s;
        margin-bottom: 0.75rem;
    }

    .module-card::after {
        content: attr(data-num);
        position: absolute;
        bottom: -0.5rem; right: 1rem;
        font-size: 6rem;
        font-weight: 900;
        letter-spacing: -0.05em;
        opacity: 0.04;
        color: white;
        line-height: 1;
        pointer-events: none;
    }

    /* Colored top stripe + glow */
    .card-indigo  { border-top: 2px solid var(--indigo);  box-shadow: 0 0 0 0 var(--indigo-glow); }
    .card-emerald { border-top: 2px solid var(--emerald); box-shadow: 0 0 0 0 var(--emerald-glow); }
    .card-violet  { border-top: 2px solid var(--violet);  box-shadow: 0 0 0 0 var(--violet-glow); }
    .card-amber   { border-top: 2px solid var(--amber);   box-shadow: 0 0 0 0 var(--amber-glow); }

    .card-icon-wrap {
        width: 40px; height: 40px;
        border-radius: 10px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.1rem;
        margin-bottom: 1rem;
        flex-shrink: 0;
    }
    .icon-indigo  { background: var(--indigo-soft); }
    .icon-emerald { background: var(--emerald-soft); }
    .icon-violet  { background: var(--violet-soft); }
    .icon-amber   { background: var(--amber-soft); }

    .card-num-badge {
        position: absolute;
        top: 1.25rem; right: 1.25rem;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.1em;
        color: var(--muted);
        background: rgba(255,255,255,0.05);
        border: 1px solid var(--border);
        border-radius: 6px;
        padding: 0.2rem 0.5rem;
    }

    .card-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: var(--text);
        margin-bottom: 0.3rem;
        letter-spacing: -0.02em;
    }

    .card-desc {
        font-size: 0.84rem;
        color: var(--muted);
        flex-grow: 1;
        line-height: 1.55;
    }

    .status-tag {
        display: inline-flex;
        align-items: center;
        gap: 0.35rem;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.04em;
        padding: 0.22rem 0.6rem;
        border-radius: 6px;
        margin-top: 0.75rem;
        width: fit-content;
    }
    .tag-active { background: rgba(34,197,94,0.12); color: #4ade80; border: 1px solid rgba(34,197,94,0.2); }
    .tag-locked { background: rgba(100,116,139,0.1); color: var(--muted);  border: 1px solid var(--border); }

    /* ═══ BUTTONS ═══ */
    div[data-testid="stButton"] > button {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        font-size: 0.85rem !important;
        letter-spacing: 0.01em !important;
        border-radius: 10px !important;
        padding: 0.6rem 1.25rem !important;
        border: 1px solid rgba(255,255,255,0.1) !important;
        background: var(--surface2) !important;
        color: var(--text) !important;
        transition: all 0.2s ease !important;
    }
    div[data-testid="stButton"] > button:hover {
        background: rgba(99,102,241,0.15) !important;
        border-color: var(--indigo) !important;
        color: #a5b4fc !important;
        transform: translateY(-1px) !important;
    }
    div[data-testid="stButton"] > button:disabled {
        opacity: 0.3 !important;
        transform: none !important;
    }

    div[data-testid="stFormSubmitButton"] > button {
        font-family: 'Inter', sans-serif !important;
        background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
        color: white !important;
        border: none !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 0.9rem !important;
        letter-spacing: 0.02em !important;
        padding: 0.7rem 2rem !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 20px rgba(99,102,241,0.3) !important;
    }
    div[data-testid="stFormSubmitButton"] > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 28px rgba(99,102,241,0.45) !important;
    }

    /* ═══ LESSON SECTIONS ═══ */
    .lesson-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 1.75rem 2rem;
        margin-bottom: 0.75rem;
        position: relative;
        overflow: hidden;
    }

    .lesson-card::before {
        content: '';
        position: absolute;
        left: 0; top: 0; bottom: 0;
        width: 3px;
        border-radius: 0 2px 2px 0;
    }
    .lc-indigo::before  { background: var(--indigo); }
    .lc-emerald::before { background: var(--emerald); }
    .lc-violet::before  { background: var(--violet); }

    .lesson-label {
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: var(--muted);
        margin-bottom: 0.4rem;
    }

    .lesson-heading {
        font-size: 1.15rem;
        font-weight: 700;
        color: var(--text);
        letter-spacing: -0.02em;
        margin-bottom: 0.65rem;
    }

    .lesson-body {
        font-size: 0.93rem;
        color: var(--muted2);
        line-height: 1.8;
    }
    .lesson-body strong {
        color: var(--text);
        font-weight: 600;
    }

    /* ═══ QUIZ ═══ */
    .quiz-banner {
        background: linear-gradient(135deg, #1e1b4b 0%, #1a1033 100%);
        border: 1px solid rgba(99,102,241,0.25);
        border-radius: 16px;
        padding: 2rem 2.25rem;
        margin-bottom: 1.5rem;
        position: relative;
        overflow: hidden;
    }
    .quiz-banner::before {
        content: '?';
        position: absolute;
        right: 2rem; top: 50%;
        transform: translateY(-50%);
        font-size: 8rem;
        font-weight: 900;
        color: rgba(99,102,241,0.08);
        line-height: 1;
    }
    .quiz-banner-tag {
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color: #818cf8;
        margin-bottom: 0.4rem;
    }
    .quiz-banner-title {
        font-size: 1.6rem;
        font-weight: 800;
        color: white;
        letter-spacing: -0.03em;
        margin-bottom: 0.35rem;
    }
    .quiz-banner-sub {
        font-size: 0.85rem;
        color: #6366f1;
        font-weight: 500;
    }

    div[role="radiogroup"] {
        background: var(--surface) !important;
        border: 1px solid var(--border) !important;
        border-radius: 12px !important;
        padding: 1.5rem 1.75rem !important;
        margin-bottom: 0.6rem !important;
    }

    /* ═══ RESULT CARD ═══ */
    .result-wrap {
        border-radius: 16px;
        padding: 2rem 2.25rem;
        margin-top: 1.25rem;
        position: relative;
        overflow: hidden;
    }
    .result-pass { background: rgba(16,185,129,0.07); border: 1px solid rgba(16,185,129,0.2); }
    .result-fail { background: rgba(239,68,68,0.07);  border: 1px solid rgba(239,68,68,0.2); }

    .result-tag {
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
    }
    .tag-pass { color: var(--emerald); }
    .tag-fail { color: var(--red); }

    .result-score-big {
        font-size: 4rem;
        font-weight: 900;
        letter-spacing: -0.05em;
        line-height: 1;
        margin-bottom: 0.4rem;
    }
    .score-pass { color: var(--emerald); }
    .score-fail { color: var(--red); }

    .result-score-denom {
        font-size: 1.4rem;
        color: var(--muted);
        font-weight: 500;
    }

    .result-msg {
        font-size: 0.9rem;
        color: var(--muted2);
        margin-top: 0.5rem;
        line-height: 1.6;
    }

    /* ═══ STAT CARDS ═══ */
    .stat-card {
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 14px;
        padding: 1.75rem 1.5rem;
        text-align: center;
        position: relative;
        overflow: hidden;
    }
    .stat-glow {
        position: absolute;
        width: 120px; height: 120px;
        border-radius: 50%;
        top: -40px; left: 50%;
        transform: translateX(-50%);
        filter: blur(30px);
        opacity: 0.25;
        pointer-events: none;
    }
    .stat-value {
        font-size: 3.2rem;
        font-weight: 900;
        letter-spacing: -0.05em;
        color: var(--text);
        line-height: 1;
        margin-bottom: 0.4rem;
    }
    .stat-label {
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--muted);
    }

    /* ═══ PROGRESS BAR ═══ */
    .prog-wrap {
        height: 5px;
        background: rgba(255,255,255,0.07);
        border-radius: 99px;
        overflow: hidden;
        margin-top: 0.85rem;
    }
    .prog-fill {
        height: 5px;
        border-radius: 99px;
        background: linear-gradient(90deg, #6366f1, #a855f7);
    }

    /* ═══ TABLE ═══ */
    .d-table {
        width: 100%;
        border-collapse: collapse;
        background: var(--surface);
        border: 1px solid var(--border);
        border-radius: 14px;
        overflow: hidden;
        font-size: 0.9rem;
    }
    .d-table th {
        background: rgba(255,255,255,0.03);
        padding: 0.85rem 1.5rem;
        text-align: left;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--muted);
        border-bottom: 1px solid var(--border);
    }
    .d-table td {
        padding: 1rem 1.5rem;
        border-bottom: 1px solid var(--border);
        color: var(--text);
    }
    .d-table tr:last-child td { border-bottom: none; }
    .d-table tr:hover td { background: rgba(255,255,255,0.015); }

    /* ═══ DIVIDER ═══ */
    hr {
        border: none !important;
        border-top: 1px solid var(--border) !important;
        margin: 2rem 0 !important;
    }

    /* ═══ PAGE TITLE AREA ═══ */
    .module-page-header {
        margin-bottom: 2rem;
    }
    .module-page-eyebrow {
        font-size: 0.68rem;
        font-weight: 700;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        margin-bottom: 0.5rem;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    .module-page-eyebrow::before {
        content: '';
        display: inline-block;
        width: 16px; height: 2px;
        border-radius: 2px;
    }
    .module-page-title {
        font-size: 2.6rem;
        font-weight: 900;
        letter-spacing: -0.04em;
        color: var(--text);
        margin-bottom: 0;
        line-height: 1.05;
    }

    /* ═══ DECORATIVE SECTION DIVIDER ═══ */
    .section-label-row {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        margin: 2rem 0 1rem;
    }
    .section-label-text {
        font-size: 0.7rem;
        font-weight: 700;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--muted);
        white-space: nowrap;
    }
    .section-label-line {
        flex-grow: 1;
        height: 1px;
        background: var(--border);
    }

    p { color: var(--muted2) !important; line-height: 1.7 !important; }
    h1, h2, h3 { color: var(--text) !important; font-weight: 800 !important; letter-spacing: -0.03em !important; }

    /* Alert styling */
    div[data-testid="stAlert"] { border-radius: 12px !important; }

    /* Sidebar gone */
    section[data-testid="stSidebar"] { display: none !important; }
</style>
""", unsafe_allow_html=True)

# ── Session state ────────────────────────────────────────────────────────────
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'dashboard'
if 'unlocked_modules' not in st.session_state:
    st.session_state.unlocked_modules = ['module_1']
for m in ['1', '2', '3']:
    for k in ['quiz_started', 'quiz_submitted', 'quiz_score']:
        key = f'm{m}_{k}'
        if key not in st.session_state:
            st.session_state[key] = False if k != 'quiz_score' else 0

def navigate(view):
    st.session_state.current_view = view

# ── Quiz Data ────────────────────────────────────────────────────────────────
M1_QUIZ_DATA = [
    {"question": "What do we call the specific time and place where a story happens?",       "options": ["The Plot", "The Characters", "The Setting", "The Title"],                  "answer": "The Setting"},
    {"question": "Where is the main idea of a paragraph usually located?",                   "options": ["In the middle", "At the very end", "In the topic sentence", "In the dictionary"], "answer": "In the topic sentence"},
    {"question": "What are hints around a new word that help you understand its meaning?",   "options": ["Context clues", "Story settings", "Hidden numbers", "Spelling words"],    "answer": "Context clues"},
    {"question": "Who are the people or animals that take part in a story?",                 "options": ["The Authors", "The Readers", "The Characters", "The Settings"],           "answer": "The Characters"},
    {"question": "What is the sequence of events from beginning to end of a story called?", "options": ["The Plot", "The Cover", "The Vocabulary", "The Conclusion"],              "answer": "The Plot"},
]
M2_QUIZ_DATA = [
    {"question": "What is the total sum when you combine 145 and 278?",           "options": ["423", "413", "433", "323"],                                                                  "answer": "423"},
    {"question": "What is the perimeter of a square if one side measures 9 units?", "options": ["18 units", "27 units", "36 units", "81 units"],                                          "answer": "36 units"},
    {"question": "In the fraction 3/4, what does the number 4 represent?",        "options": ["The part we have", "The total equal parts in the whole", "The sum", "The difference"],    "answer": "The total equal parts in the whole"},
    {"question": "What is the product of 15 multiplied by 8?",                    "options": ["100", "110", "120", "130"],                                                                 "answer": "120"},
    {"question": "What is the mathematical term for a flat shape with straight sides?", "options": ["Circle", "Sphere", "Polygon", "Line"],                                               "answer": "Polygon"},
]
M3_QUIZ_DATA = [
    {"question": "What process changes liquid water into an invisible gas?",          "options": ["Condensation", "Evaporation", "Precipitation", "Freezing"],  "answer": "Evaporation"},
    {"question": "What provides the main energy that powers the water cycle?",        "options": ["The Moon", "The Wind", "The Sun", "The Ocean"],              "answer": "The Sun"},
    {"question": "What forms in the sky when water vapor cools and condenses?",       "options": ["Raindrops", "Clouds", "Rivers", "Groundwater"],              "answer": "Clouds"},
    {"question": "Which of the following is an example of precipitation?",            "options": ["Snow falling", "A puddle drying", "Water boiling", "Ice melting"], "answer": "Snow falling"},
    {"question": "Where does a large amount of water collect underground?",           "options": ["Aquifer", "Cloud", "Atmosphere", "Evaporator"],              "answer": "Aquifer"},
]


# ═══════════════════════════════════════════════════════════════════
#  HELPER: render_module — must be defined before if/elif chain
# ═══════════════════════════════════════════════════════════════════
def render_module(m_num, title, eyebrow, icon, accent, accent_soft, lc_class, sections, quiz_data):
    st.button("← Back to Dashboard", key=f"back_m{m_num}", on_click=navigate, args=('dashboard',))
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div class="module-page-header">
        <div class="module-page-eyebrow" style="color:{accent};">
            <span style="background:{accent}; width:16px; height:2px; border-radius:2px; display:inline-block;"></span>
            {eyebrow}
        </div>
        <div class="module-page-title">{icon} {title}</div>
    </div>
    """, unsafe_allow_html=True)

    for i, (label, heading, body) in enumerate(sections):
        st.markdown(f"""
        <div class="lesson-card {lc_class}">
            <div class="lesson-label">{label}</div>
            <div class="lesson-heading">{heading}</div>
            <div class="lesson-body">{body}</div>
        </div>
        """, unsafe_allow_html=True)

    # divider with label
    st.markdown("""
    <div class="section-label-row">
        <span class="section-label-text">Assessment</span>
        <span class="section-label-line"></span>
    </div>
    """, unsafe_allow_html=True)

    started_key   = f'm{m_num}_quiz_started'
    submitted_key = f'm{m_num}_quiz_submitted'
    score_key     = f'm{m_num}_quiz_score'
    start_btn     = f'start_m{m_num}_quiz'
    retake_btn    = f'retake_m{m_num}'
    next_module   = f'module_{int(m_num)+1}'

    if not st.session_state[started_key]:
        st.markdown("""
        <div style="text-align:center; padding:1.5rem 0 0.75rem;">
            <p style="font-size:0.88rem; color:var(--muted) !important; margin:0;">
                Read through all sections above, then take the 5-question quiz.
            </p>
        </div>
        """, unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1.5, 1, 1.5])
        with c2:
            st.button("Start Quiz →", key=start_btn, use_container_width=True)
        if st.session_state.get(start_btn):
            st.session_state[started_key] = True
            st.rerun()

    if st.session_state[started_key]:
        st.markdown(f"""
        <div class="quiz-banner">
            <div class="quiz-banner-tag">Formative Evaluation</div>
            <div class="quiz-banner-title">Knowledge Check</div>
            <div class="quiz-banner-sub">5 questions &nbsp;·&nbsp; Choose one answer each</div>
        </div>
        """, unsafe_allow_html=True)

        with st.form(key=f'm{m_num}_quiz_form', clear_on_submit=False):
            user_answers = []
            for i, q in enumerate(quiz_data):
                st.markdown(f"**{i+1}.&nbsp; {q['question']}**")
                ans = st.radio("", q["options"], key=f"m{m_num}_q_{i}",
                               label_visibility="collapsed", index=None)
                user_answers.append(ans)
                if i < len(quiz_data) - 1:
                    st.markdown("<div style='height:0.25rem'></div>", unsafe_allow_html=True)
            st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
            submit = st.form_submit_button("Submit Answers", use_container_width=False)

        if submit:
            if None in user_answers:
                st.error("Answer all 5 questions before submitting.")
            else:
                score = sum(1 for i, q in enumerate(quiz_data) if user_answers[i] == q["answer"])
                st.session_state[score_key] = score
                st.session_state[submitted_key] = True

        if st.session_state[submitted_key]:
            sc     = st.session_state[score_key]
            passed = sc >= 4
            cls    = "result-pass" if passed else "result-fail"
            tag_c  = "tag-pass"   if passed else "tag-fail"
            sc_c   = "score-pass" if passed else "score-fail"
            tag_t  = "✓ Competency Verified" if passed else "✗ Below Threshold"
            msg    = "Great job — the next module has been unlocked for you." if passed else "Review the lesson sections above and give it another try."

            st.markdown(f"""
            <div class="result-wrap {cls}">
                <div class="result-tag {tag_c}">{tag_t}</div>
                <div>
                    <span class="result-score-big {sc_c}">{sc}</span>
                    <span class="result-score-denom"> / {len(quiz_data)}</span>
                </div>
                <div class="result-msg">{msg}</div>
            </div>
            """, unsafe_allow_html=True)

            if passed and int(m_num) < 3 and next_module not in st.session_state.unlocked_modules:
                st.session_state.unlocked_modules.append(next_module)

            if not passed:
                st.markdown("<div style='height:0.75rem'></div>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns([1.5, 1, 1.5])
                with c2:
                    st.button("Retry Quiz", key=retake_btn, use_container_width=True)
                if st.session_state.get(retake_btn):
                    st.session_state[submitted_key] = False
                    st.rerun()


# ═══════════════════════════════════════════════════════════════════
#  DASHBOARD
# ═══════════════════════════════════════════════════════════════════
if st.session_state.current_view == 'dashboard':

    # Quick stats
    completed = sum([
        st.session_state.m1_quiz_submitted and st.session_state.m1_quiz_score >= 4,
        st.session_state.m2_quiz_submitted and st.session_state.m2_quiz_score >= 4,
        st.session_state.m3_quiz_submitted and st.session_state.m3_quiz_score >= 4,
    ])
    pct = int(completed / 3 * 100)

    st.markdown(f"""
    <div style="margin-bottom: 3rem;">
        <div class="eyebrow">Academic Platform</div>
        <div class="hero-title"><span>DANILO</span></div>
        <div class="hero-sub">
            A structured curriculum with sequential modules.<br>
            Unlock the next subject by mastering the current one.
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Three module cards ──
    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("""
        <div class="module-card card-indigo" data-num="01">
            <span class="card-num-badge">01</span>
            <div class="card-icon-wrap icon-indigo">📖</div>
            <div class="card-title">Reading</div>
            <div class="card-desc">Story elements, main ideas &amp; context clues.</div>
            <div class="status-tag tag-active">● Unlocked</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Open Module →", key="btn_m1", on_click=navigate, args=('module_1',), use_container_width=True)

    with col2:
        m2_locked = 'module_2' not in st.session_state.unlocked_modules
        tag2 = '<div class="status-tag tag-locked">🔒 Requires Reading</div>' if m2_locked else '<div class="status-tag tag-active">● Unlocked</div>'
        st.markdown(f"""
        <div class="module-card card-emerald" data-num="02" style="{'opacity:0.45;' if m2_locked else ''}">
            <span class="card-num-badge">02</span>
            <div class="card-icon-wrap icon-emerald">📐</div>
            <div class="card-title">Mathematics</div>
            <div class="card-desc">Operations, fractions &amp; geometry basics.</div>
            {tag2}
        </div>
        """, unsafe_allow_html=True)
        st.button("Open Module →", key="btn_m2", on_click=navigate, args=('module_2',), disabled=m2_locked, use_container_width=True)

    with col3:
        m3_locked = 'module_3' not in st.session_state.unlocked_modules
        tag3 = '<div class="status-tag tag-locked">🔒 Requires Mathematics</div>' if m3_locked else '<div class="status-tag tag-active">● Unlocked</div>'
        st.markdown(f"""
        <div class="module-card card-violet" data-num="03" style="{'opacity:0.45;' if m3_locked else ''}">
            <span class="card-num-badge">03</span>
            <div class="card-icon-wrap icon-violet">🌊</div>
            <div class="card-title">Natural Sciences</div>
            <div class="card-desc">The water cycle and Earth's hydrosphere.</div>
            {tag3}
        </div>
        """, unsafe_allow_html=True)
        st.button("Open Module →", key="btn_m3", on_click=navigate, args=('module_3',), disabled=m3_locked, use_container_width=True)

    # ── Bottom: Metrics card ──
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    col4, col5 = st.columns([1, 2], gap="medium")

    with col4:
        st.markdown(f"""
        <div class="module-card card-amber" data-num="" style="height:auto; min-height:180px;">
            <span class="card-num-badge">Analytics</span>
            <div class="card-icon-wrap icon-amber">📊</div>
            <div class="card-title">Academic Metrics</div>
            <div class="card-desc">Performance records and curriculum logs.</div>
            <div class="prog-wrap"><div class="prog-fill" style="width:{pct}%"></div></div>
            <div style="font-size:0.72rem; color:var(--muted); margin-top:0.45rem; font-weight:600;">
                {pct}% Complete &nbsp;·&nbsp; {completed}/3 modules passed
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.button("View Metrics →", key="btn_profile", on_click=navigate, args=('profile',), use_container_width=True)

    with col5:
        # Decorative info block
        st.markdown(f"""
        <div style="background:var(--surface); border:1px solid var(--border); border-radius:16px;
                    padding:1.75rem 2rem; height:100%; min-height:180px; position:relative; overflow:hidden;">
            <div style="position:absolute; right:-20px; bottom:-20px; width:160px; height:160px;
                        border-radius:50%; background:radial-gradient(circle, rgba(99,102,241,0.12), transparent 70%);
                        pointer-events:none;"></div>
            <div style="font-size:0.65rem; font-weight:700; letter-spacing:0.14em; text-transform:uppercase;
                        color:var(--muted); margin-bottom:1rem;">How it works</div>
            <div style="display:flex; flex-direction:column; gap:0.65rem;">
                <div style="display:flex; align-items:flex-start; gap:0.75rem;">
                    <div style="background:var(--indigo-soft); color:#818cf8; font-size:0.72rem; font-weight:700;
                                border-radius:6px; padding:0.2rem 0.5rem; flex-shrink:0; margin-top:1px;">01</div>
                    <div style="font-size:0.88rem; color:var(--muted2); line-height:1.5;">
                        Read through the lesson material in each module.
                    </div>
                </div>
                <div style="display:flex; align-items:flex-start; gap:0.75rem;">
                    <div style="background:var(--emerald-soft); color:#34d399; font-size:0.72rem; font-weight:700;
                                border-radius:6px; padding:0.2rem 0.5rem; flex-shrink:0; margin-top:1px;">02</div>
                    <div style="font-size:0.88rem; color:var(--muted2); line-height:1.5;">
                        Pass the 5-question quiz with a score of 4 or higher.
                    </div>
                </div>
                <div style="display:flex; align-items:flex-start; gap:0.75rem;">
                    <div style="background:var(--violet-soft); color:#c084fc; font-size:0.72rem; font-weight:700;
                                border-radius:6px; padding:0.2rem 0.5rem; flex-shrink:0; margin-top:1px;">03</div>
                    <div style="font-size:0.88rem; color:var(--muted2); line-height:1.5;">
                        Unlock the next subject and continue your progress.
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ═══════════════════════════════════════════════════════════════════
#  MODULE 1 — READING
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'module_1':
    render_module(
        m_num='1', title='Reading', eyebrow='Module 01 — Language Arts',
        icon='📖', accent='#6366f1', accent_soft='rgba(99,102,241,0.12)',
        lc_class='lc-indigo',
        sections=[
            ("Section 1.0", "Elements of a Story",
             "Every story has essential parts that help us understand what is happening. "
             "The <strong>setting</strong> tells us when and where the story takes place. "
             "The <strong>characters</strong> are the people, animals, or creatures in the story. "
             "The <strong>plot</strong> is the sequence of events from the beginning to the end."),
            ("Section 1.1", "Finding the Main Idea",
             "When reading a paragraph, it is important to find the <strong>main idea</strong> — the primary "
             "point the author wants to communicate. It is often found in the <strong>topic sentence</strong>, "
             "which is usually the first sentence of the paragraph."),
            ("Section 1.2", "Using Context Clues",
             "Sometimes you will read a word you do not know. Instead of immediately looking it up, "
             "examine the surrounding words for hints. "
             "These helpful hints are called <strong>context clues</strong>."),
        ],
        quiz_data=M1_QUIZ_DATA
    )


# ═══════════════════════════════════════════════════════════════════
#  MODULE 2 — MATHEMATICS
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'module_2':
    render_module(
        m_num='2', title='Mathematics', eyebrow='Module 02 — Quantitative Reasoning',
        icon='📐', accent='#10b981', accent_soft='rgba(16,185,129,0.12)',
        lc_class='lc-emerald',
        sections=[
            ("Section 2.0", "Basic Operations",
             "Mathematics uses operations to solve problems. <strong>Addition</strong> combines two numbers "
             "to find a total sum. <strong>Subtraction</strong> finds the difference. "
             "<strong>Multiplication</strong> is a faster method of repeated addition."),
            ("Section 2.1", "Understanding Fractions",
             "A fraction represents a part of a whole. The top number (<strong>numerator</strong>) shows "
             "how many parts we have. The bottom number (<strong>denominator</strong>) shows how many "
             "equal parts make up the entire whole. The denominator can never be zero."),
            ("Section 2.2", "Basic Geometry",
             "Geometry is the study of shapes and spaces. A <strong>polygon</strong> is a flat shape with "
             "straight sides — like a triangle, square, or rectangle. The distance around the outside "
             "edge of a shape is called the <strong>perimeter</strong>."),
        ],
        quiz_data=M2_QUIZ_DATA
    )


# ═══════════════════════════════════════════════════════════════════
#  MODULE 3 — NATURAL SCIENCES
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'module_3':
    render_module(
        m_num='3', title='Natural Sciences', eyebrow='Module 03 — Earth Science',
        icon='🌊', accent='#a855f7', accent_soft='rgba(168,85,247,0.12)',
        lc_class='lc-violet',
        sections=[
            ("Section 3.0", "Introduction to the Water Cycle",
             "The water cycle is the continuous movement of water on Earth. Water changes its state as it "
             "moves between the ground, the oceans, and the sky. The amount of water on our planet stays "
             "mostly the same — it simply travels to different places."),
            ("Section 3.1", "Evaporation & Condensation",
             "<strong>Evaporation</strong> occurs when the sun heats liquid water, turning it into water "
             "vapor — an invisible gas. When vapor rises and cools, it undergoes "
             "<strong>condensation</strong>, forming the clouds we see overhead."),
            ("Section 3.2", "Precipitation & Collection",
             "When clouds accumulate too much water, it falls back to Earth as "
             "<strong>precipitation</strong> — rain, snow, or hail. This water collects in oceans, lakes, "
             "and underground reservoirs called <strong>aquifers</strong>, ready to restart the cycle."),
        ],
        quiz_data=M3_QUIZ_DATA
    )


# ═══════════════════════════════════════════════════════════════════
#  METRICS / PROFILE
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'profile':
    st.button("← Back to Dashboard", key="back_profile", on_click=navigate, args=('dashboard',))
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom:2rem;">
        <div class="eyebrow">Performance Records</div>
        <div class="hero-title" style="font-size:2.6rem;">Academic Metrics</div>
        <div class="hero-sub" style="font-size:0.95rem; margin-bottom:0;">
            A full breakdown of your quiz scores and curriculum progress.
        </div>
    </div>
    """, unsafe_allow_html=True)

    unlocked_count = len(st.session_state.unlocked_modules)
    completed = sum([
        st.session_state.m1_quiz_submitted and st.session_state.m1_quiz_score >= 4,
        st.session_state.m2_quiz_submitted and st.session_state.m2_quiz_score >= 4,
        st.session_state.m3_quiz_submitted and st.session_state.m3_quiz_score >= 4,
    ])
    score_sum, score_count = 0, 0
    for mn in ['1', '2', '3']:
        if st.session_state[f'm{mn}_quiz_submitted']:
            score_sum   += st.session_state[f'm{mn}_quiz_score']
            score_count += 1
    avg_pct = int(score_sum / (score_count * 5) * 100) if score_count else 0
    prog_pct = int(completed / 3 * 100)

    col1, col2, col3 = st.columns(3, gap="medium")
    with col1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-glow" style="background:#6366f1;"></div>
            <div class="stat-value" style="background:linear-gradient(135deg,#6366f1,#a855f7);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
                {completed}
            </div>
            <div class="stat-label">Modules Passed</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-glow" style="background:#10b981;"></div>
            <div class="stat-value" style="background:linear-gradient(135deg,#10b981,#34d399);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
                {avg_pct}%
            </div>
            <div class="stat-label">Mean Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    with col3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-glow" style="background:#a855f7;"></div>
            <div class="stat-value" style="background:linear-gradient(135deg,#a855f7,#ec4899);
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;">
                {prog_pct}%
            </div>
            <div class="stat-label">Curriculum Progress</div>
        </div>
        """, unsafe_allow_html=True)

    # Progress bar
    st.markdown("<div style='height:1.25rem'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div style="background:var(--surface); border:1px solid var(--border); border-radius:14px;
                padding:1.5rem 2rem; margin-bottom:1.5rem;">
        <div style="display:flex; justify-content:space-between; margin-bottom:0.75rem;">
            <span style="font-size:0.85rem; font-weight:700; color:var(--text);">Overall Progress</span>
            <span style="font-size:0.8rem; color:var(--muted); font-weight:500;">{completed} of 3 modules completed</span>
        </div>
        <div class="prog-wrap" style="height:8px;">
            <div class="prog-fill" style="height:8px; width:{prog_pct}%;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Table
    def m_status(mn):
        sub = st.session_state[f'm{mn}_quiz_submitted']
        sc  = st.session_state[f'm{mn}_quiz_score']
        if sub and sc >= 4:
            return f'<span style="color:#4ade80;font-weight:700;">✓ Verified</span>', f"{sc}/5"
        elif sub:
            return f'<span style="color:#f87171;font-weight:700;">✗ Needs Retry</span>', f"{sc}/5"
        elif f'module_{mn}' in st.session_state.unlocked_modules:
            return f'<span style="color:#fbbf24;font-weight:600;">◷ In Progress</span>', "—"
        else:
            return f'<span style="color:var(--muted);font-weight:500;">🔒 Locked</span>', "—"

    m1s, m1d = m_status('1')
    m2s, m2d = m_status('2')
    m3s, m3d = m_status('3')

    st.markdown(f"""
    <table class="d-table">
        <thead>
            <tr>
                <th>#</th>
                <th>Module</th>
                <th>Status</th>
                <th>Score</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="color:var(--muted);font-size:0.75rem;font-weight:700;">01</td>
                <td style="font-weight:600;">📖 Reading</td>
                <td>{m1s}</td>
                <td style="font-family:monospace;letter-spacing:0.06em;color:var(--muted2);">{m1d}</td>
            </tr>
            <tr>
                <td style="color:var(--muted);font-size:0.75rem;font-weight:700;">02</td>
                <td style="font-weight:600;">📐 Mathematics</td>
                <td>{m2s}</td>
                <td style="font-family:monospace;letter-spacing:0.06em;color:var(--muted2);">{m2d}</td>
            </tr>
            <tr>
                <td style="color:var(--muted);font-size:0.75rem;font-weight:700;">03</td>
                <td style="font-weight:600;">🌊 Natural Sciences</td>
                <td>{m3s}</td>
                <td style="font-family:monospace;letter-spacing:0.06em;color:var(--muted2);">{m3d}</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)
