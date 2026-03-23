import streamlit as st
import os

if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write('[theme]\nbase="light"\nprimaryColor="#0071e3"\nbackgroundColor="#f5f5f7"\nsecondaryBackgroundColor="#ffffff"\ntextColor="#1d1d1f"\nfont="sans serif"\n')

st.set_page_config(page_title="DANILO", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=DM+Serif+Display:ital@0;1&display=swap');

    :root {
        --apple-blue: #0071e3;
        --apple-blue-hover: #0077ed;
        --apple-bg: #f5f5f7;
        --apple-card: #ffffff;
        --apple-text: #1d1d1f;
        --apple-secondary: #6e6e73;
        --apple-border: rgba(0,0,0,0.08);
        --apple-shadow: 0 4px 24px rgba(0,0,0,0.07), 0 1px 4px rgba(0,0,0,0.04);
        --apple-shadow-hover: 0 12px 40px rgba(0,0,0,0.13), 0 2px 8px rgba(0,0,0,0.07);
        --reading-color: #0071e3;
        --math-color: #34c759;
        --science-color: #af52de;
        --metrics-color: #ff9f0a;
    }

    html, body, [class*="css"] {
        font-family: 'DM Sans', -apple-system, BlinkMacSystemFont, sans-serif !important;
        background-color: var(--apple-bg) !important;
    }

    .block-container {
        padding: 3rem 2rem 6rem 2rem !important;
        max-width: 1100px !important;
    }

    #MainMenu, footer, header { visibility: hidden; }

    /* ─── Page Title ─── */
    .page-eyebrow {
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: var(--apple-blue);
        margin-bottom: 0.4rem;
    }

    .page-title {
        font-family: 'DM Serif Display', Georgia, serif;
        font-size: 3rem;
        font-weight: 400;
        color: var(--apple-text);
        line-height: 1.1;
        letter-spacing: -0.03em;
        margin-bottom: 0.5rem;
    }

    .page-subtitle {
        font-size: 1.15rem;
        color: var(--apple-secondary);
        font-weight: 400;
        margin-bottom: 2.5rem;
        line-height: 1.5;
    }

    /* ─── Module Cards ─── */
    .module-card {
        background: var(--apple-card);
        border: 1px solid var(--apple-border);
        border-radius: 20px;
        padding: 2rem 1.75rem 1.5rem;
        box-shadow: var(--apple-shadow);
        transition: box-shadow 0.3s ease, transform 0.3s ease;
        height: 220px;
        display: flex;
        flex-direction: column;
        position: relative;
        overflow: hidden;
        margin-bottom: 0.75rem;
    }

    .module-card::before {
        content: '';
        position: absolute;
        top: 0; left: 0; right: 0;
        height: 3px;
        border-radius: 20px 20px 0 0;
    }

    .card-reading::before  { background: var(--reading-color); }
    .card-math::before     { background: var(--math-color); }
    .card-science::before  { background: var(--science-color); }
    .card-metrics::before  { background: var(--metrics-color); }

    .card-icon {
        font-size: 1.8rem;
        margin-bottom: 0.75rem;
        display: block;
    }

    .card-title {
        font-size: 1.15rem;
        font-weight: 600;
        color: var(--apple-text);
        margin-bottom: 0.35rem;
        letter-spacing: -0.01em;
    }

    .card-desc {
        font-size: 0.88rem;
        color: var(--apple-secondary);
        flex-grow: 1;
        line-height: 1.5;
    }

    .pill {
        display: inline-flex;
        align-items: center;
        gap: 0.3rem;
        padding: 0.2rem 0.7rem;
        border-radius: 999px;
        font-size: 0.75rem;
        font-weight: 600;
        letter-spacing: 0.02em;
        margin-top: 0.75rem;
    }

    .pill-active {
        background: rgba(52, 199, 89, 0.12);
        color: #1a7f3c;
    }

    .pill-locked {
        background: rgba(110,110,115,0.1);
        color: #6e6e73;
    }

    /* ─── Buttons ─── */
    div[data-testid="stButton"] > button {
        background: var(--apple-blue) !important;
        color: #ffffff !important;
        border: none !important;
        border-radius: 980px !important;
        font-weight: 500 !important;
        font-size: 0.92rem !important;
        padding: 0.6rem 1.4rem !important;
        letter-spacing: -0.01em !important;
        transition: all 0.2s ease !important;
        box-shadow: none !important;
        font-family: 'DM Sans', sans-serif !important;
    }

    div[data-testid="stButton"] > button:hover {
        background: var(--apple-blue-hover) !important;
        transform: scale(1.02) !important;
    }

    div[data-testid="stButton"] > button:disabled {
        background: rgba(0,0,0,0.08) !important;
        color: rgba(0,0,0,0.25) !important;
        transform: none !important;
    }

    /* Back button */
    div[data-testid="stButton"]:first-of-type > button {
        background: rgba(0,0,0,0.06) !important;
        color: var(--apple-text) !important;
        font-weight: 500 !important;
    }

    div[data-testid="stButton"]:first-of-type > button:hover {
        background: rgba(0,0,0,0.1) !important;
    }

    /* ─── Lesson Content ─── */
    .lesson-section {
        background: var(--apple-card);
        border: 1px solid var(--apple-border);
        border-radius: 18px;
        padding: 2rem 2.25rem;
        margin-bottom: 1rem;
        box-shadow: var(--apple-shadow);
    }

    .lesson-label {
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        color: var(--apple-blue);
        margin-bottom: 0.4rem;
    }

    .lesson-heading {
        font-family: 'DM Serif Display', Georgia, serif;
        font-size: 1.5rem;
        font-weight: 400;
        color: var(--apple-text);
        letter-spacing: -0.02em;
        margin-bottom: 0.75rem;
    }

    .lesson-body {
        font-size: 1rem;
        color: #3a3a3c;
        line-height: 1.75;
    }

    .lesson-body strong {
        color: var(--apple-text);
        font-weight: 600;
    }

    /* ─── Quiz Area ─── */
    .quiz-header {
        background: linear-gradient(135deg, #0071e3 0%, #005bb5 100%);
        border-radius: 18px;
        padding: 1.75rem 2.25rem;
        margin-bottom: 1.5rem;
        color: white;
    }

    .quiz-header-label {
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.1em;
        text-transform: uppercase;
        opacity: 0.75;
        margin-bottom: 0.3rem;
    }

    .quiz-header-title {
        font-family: 'DM Serif Display', Georgia, serif;
        font-size: 1.7rem;
        font-weight: 400;
        letter-spacing: -0.02em;
    }

    .quiz-header-sub {
        font-size: 0.88rem;
        opacity: 0.8;
        margin-top: 0.4rem;
    }

    div[role="radiogroup"] {
        background: var(--apple-card) !important;
        border: 1px solid var(--apple-border) !important;
        border-radius: 14px !important;
        padding: 1.4rem 1.75rem !important;
        margin-bottom: 0.75rem !important;
        box-shadow: var(--apple-shadow) !important;
    }

    div[role="radio"] {
        border-radius: 8px !important;
        padding: 0.5rem 0.75rem !important;
        transition: background 0.15s ease !important;
    }

    div[role="radio"]:hover {
        background: rgba(0,113,227,0.06) !important;
    }

    /* ─── Form submit button ─── */
    div[data-testid="stFormSubmitButton"] > button {
        background: var(--apple-text) !important;
        color: white !important;
        border-radius: 980px !important;
        padding: 0.7rem 2rem !important;
        font-weight: 500 !important;
        font-size: 0.95rem !important;
        border: none !important;
        transition: all 0.2s ease !important;
    }

    div[data-testid="stFormSubmitButton"] > button:hover {
        background: #333 !important;
        transform: scale(1.02) !important;
    }

    /* ─── Alerts ─── */
    div[data-testid="stAlert"] {
        border-radius: 14px !important;
        border: none !important;
    }

    /* ─── Stat Cards ─── */
    .stat-card {
        background: var(--apple-card);
        border: 1px solid var(--apple-border);
        border-radius: 20px;
        padding: 2rem 1.5rem;
        box-shadow: var(--apple-shadow);
        text-align: center;
    }

    .stat-value {
        font-family: 'DM Serif Display', Georgia, serif;
        font-size: 3rem;
        font-weight: 400;
        color: var(--apple-blue);
        letter-spacing: -0.04em;
        line-height: 1;
        margin-bottom: 0.5rem;
    }

    .stat-label {
        font-size: 0.78rem;
        font-weight: 600;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        color: var(--apple-secondary);
    }

    /* ─── Table ─── */
    .apple-table {
        width: 100%;
        border-collapse: collapse;
        background: var(--apple-card);
        border: 1px solid var(--apple-border);
        border-radius: 16px;
        overflow: hidden;
        box-shadow: var(--apple-shadow);
        font-size: 0.95rem;
    }

    .apple-table th {
        background: #fafafa;
        padding: 1rem 1.5rem;
        text-align: left;
        font-size: 0.72rem;
        font-weight: 600;
        letter-spacing: 0.07em;
        text-transform: uppercase;
        color: var(--apple-secondary);
        border-bottom: 1px solid var(--apple-border);
    }

    .apple-table td {
        padding: 1.1rem 1.5rem;
        border-bottom: 1px solid var(--apple-border);
        color: var(--apple-text);
    }

    .apple-table tr:last-child td {
        border-bottom: none;
    }

    .apple-table tr:hover td {
        background: rgba(0,113,227,0.025);
    }

    /* ─── Progress Bar ─── */
    .progress-wrap {
        background: rgba(0,0,0,0.07);
        border-radius: 999px;
        height: 6px;
        margin-top: 1rem;
        overflow: hidden;
    }

    .progress-fill {
        height: 6px;
        border-radius: 999px;
        background: linear-gradient(90deg, #0071e3, #34aadc);
        transition: width 0.5s ease;
    }

    /* ─── Divider ─── */
    hr {
        border: none !important;
        border-top: 1px solid var(--apple-border) !important;
        margin: 2rem 0 !important;
    }

    /* ─── Score display ─── */
    .score-badge {
        display: inline-flex;
        align-items: baseline;
        gap: 0.35rem;
        margin-bottom: 0.5rem;
    }

    .score-num {
        font-family: 'DM Serif Display', Georgia, serif;
        font-size: 3.5rem;
        color: var(--apple-text);
        letter-spacing: -0.04em;
        line-height: 1;
    }

    .score-denom {
        font-size: 1.2rem;
        color: var(--apple-secondary);
        font-weight: 400;
    }

    p, li {
        color: #3a3a3c !important;
        line-height: 1.75 !important;
    }

    h1, h2, h3 {
        font-family: 'DM Serif Display', Georgia, serif !important;
        font-weight: 400 !important;
        letter-spacing: -0.02em !important;
        color: var(--apple-text) !important;
    }

</style>
""", unsafe_allow_html=True)

# ── Session state init ──────────────────────────────────────────────────────
if 'current_view' not in st.session_state:
    st.session_state.current_view = 'dashboard'
if 'unlocked_modules' not in st.session_state:
    st.session_state.unlocked_modules = ['module_1']
for m in ['1', '2', '3']:
    if f'm{m}_quiz_started' not in st.session_state:
        st.session_state[f'm{m}_quiz_started'] = False
    if f'm{m}_quiz_submitted' not in st.session_state:
        st.session_state[f'm{m}_quiz_submitted'] = False
    if f'm{m}_quiz_score' not in st.session_state:
        st.session_state[f'm{m}_quiz_score'] = 0

def navigate(view):
    st.session_state.current_view = view

# ── Quiz Data ───────────────────────────────────────────────────────────────
M1_QUIZ_DATA = [
    {"question": "What do we call the specific time and place where a story happens?", "options": ["The Plot", "The Characters", "The Setting", "The Title"], "answer": "The Setting"},
    {"question": "Where is the main idea of a paragraph usually located?", "options": ["In the middle", "At the very end", "In the topic sentence", "In the dictionary"], "answer": "In the topic sentence"},
    {"question": "What are hints around a new word called that help you understand its meaning?", "options": ["Context clues", "Story settings", "Hidden numbers", "Spelling words"], "answer": "Context clues"},
    {"question": "Who are the people or animals that take part in a story?", "options": ["The Authors", "The Readers", "The Characters", "The Settings"], "answer": "The Characters"},
    {"question": "What is the sequence of events from beginning to end of a story called?", "options": ["The Plot", "The Cover", "The Vocabulary", "The Conclusion"], "answer": "The Plot"}
]

M2_QUIZ_DATA = [
    {"question": "What is the total sum when you combine 145 and 278?", "options": ["423", "413", "433", "323"], "answer": "423"},
    {"question": "What is the perimeter of a square if one side measures 9 units?", "options": ["18 units", "27 units", "36 units", "81 units"], "answer": "36 units"},
    {"question": "In the fraction 3/4, what does the number 4 represent?", "options": ["The part we have", "The total equal parts in the whole", "The sum", "The difference"], "answer": "The total equal parts in the whole"},
    {"question": "What is the product of 15 multiplied by 8?", "options": ["100", "110", "120", "130"], "answer": "120"},
    {"question": "What is the mathematical term for a flat shape with straight sides?", "options": ["Circle", "Sphere", "Polygon", "Line"], "answer": "Polygon"}
]

M3_QUIZ_DATA = [
    {"question": "What process changes liquid water into an invisible gas called water vapor?", "options": ["Condensation", "Evaporation", "Precipitation", "Freezing"], "answer": "Evaporation"},
    {"question": "What provides the main energy that powers the entire water cycle?", "options": ["The Moon", "The Wind", "The Sun", "The Ocean"], "answer": "The Sun"},
    {"question": "What forms in the sky when water vapor cools and condenses?", "options": ["Raindrops", "Clouds", "Rivers", "Groundwater"], "answer": "Clouds"},
    {"question": "Which of the following is an example of precipitation?", "options": ["Snow falling", "A puddle drying", "Water boiling", "Ice melting"], "answer": "Snow falling"},
    {"question": "Where does a large amount of water collect underground?", "options": ["Aquifer", "Cloud", "Atmosphere", "Evaporator"], "answer": "Aquifer"}
]


# ═══════════════════════════════════════════════════════════════════
#  DASHBOARD
# ═══════════════════════════════════════════════════════════════════
if st.session_state.current_view == 'dashboard':

    st.markdown("""
    <div style="margin-bottom: 2.5rem;">
        <div class="page-eyebrow">Academic Platform</div>
        <div class="page-title">DANILO</div>
        <div class="page-subtitle">Your personalized learning journey — one module at a time.</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3, gap="medium")

    with col1:
        st.markdown("""
        <div class="module-card card-reading">
            <span class="card-icon">📖</span>
            <div class="card-title">Reading</div>
            <div class="card-desc">Understanding stories, main ideas, and context clues.</div>
            <span class="pill pill-active">✦ Accessible</span>
        </div>
        """, unsafe_allow_html=True)
        st.button("Start Learning", key="btn_m1", on_click=navigate, args=('module_1',), use_container_width=True)

    with col2:
        m2_locked = 'module_2' not in st.session_state.unlocked_modules
        badge = '<span class="pill pill-locked">🔒 Requires Reading</span>' if m2_locked else '<span class="pill pill-active">✦ Accessible</span>'
        st.markdown(f"""
        <div class="module-card card-math" style="{'opacity:0.6;' if m2_locked else ''}">
            <span class="card-icon">📐</span>
            <div class="card-title">Mathematics</div>
            <div class="card-desc">Foundational operations, fractions, and basic geometry.</div>
            {badge}
        </div>
        """, unsafe_allow_html=True)
        st.button("Start Learning", key="btn_m2", on_click=navigate, args=('module_2',), disabled=m2_locked, use_container_width=True)

    with col3:
        m3_locked = 'module_3' not in st.session_state.unlocked_modules
        badge3 = '<span class="pill pill-locked">🔒 Requires Mathematics</span>' if m3_locked else '<span class="pill pill-active">✦ Accessible</span>'
        st.markdown(f"""
        <div class="module-card card-science" style="{'opacity:0.6;' if m3_locked else ''}">
            <span class="card-icon">🌊</span>
            <div class="card-title">Natural Sciences</div>
            <div class="card-desc">Explore the water cycle and Earth's hydrosphere.</div>
            {badge3}
        </div>
        """, unsafe_allow_html=True)
        st.button("Start Learning", key="btn_m3", on_click=navigate, args=('module_3',), disabled=m3_locked, use_container_width=True)

    st.markdown("<div style='height: 1rem;'></div>", unsafe_allow_html=True)

    col4, col5 = st.columns([1, 2], gap="medium")
    with col4:
        # Calculate quick stats for dashboard
        completed = sum([
            st.session_state.m1_quiz_submitted and st.session_state.m1_quiz_score >= 4,
            st.session_state.m2_quiz_submitted and st.session_state.m2_quiz_score >= 4,
            st.session_state.m3_quiz_submitted and st.session_state.m3_quiz_score >= 4,
        ])
        pct = int(completed / 3 * 100)
        st.markdown(f"""
        <div class="module-card card-metrics" style="height: auto; min-height: 150px;">
            <span class="card-icon">📊</span>
            <div class="card-title">Academic Metrics</div>
            <div class="card-desc">Track your performance and progress records.</div>
            <div class="progress-wrap"><div class="progress-fill" style="width:{pct}%"></div></div>
            <div style="font-size:0.78rem; color:var(--apple-secondary); margin-top:0.4rem;">{pct}% curriculum complete</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("View Analytics", key="btn_profile", on_click=navigate, args=('profile',), use_container_width=True)


# ═══════════════════════════════════════════════════════════════════
#  HELPER: render a lesson module
# ═══════════════════════════════════════════════════════════════════
def render_module(module_key, m_num, title, eyebrow, icon, accent, sections, quiz_data):
    back_key = f"back_m{m_num}"
    st.button("← Dashboard", key=back_key, on_click=navigate, args=('dashboard',))
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="margin-bottom: 2rem;">
        <div class="page-eyebrow" style="color:{accent};">{eyebrow}</div>
        <div class="page-title">{icon} {title}</div>
    </div>
    """, unsafe_allow_html=True)

    for label, heading, body in sections:
        st.markdown(f"""
        <div class="lesson-section">
            <div class="lesson-label">{label}</div>
            <div class="lesson-heading">{heading}</div>
            <div class="lesson-body">{body}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    started_key  = f'm{m_num}_quiz_started'
    submitted_key = f'm{m_num}_quiz_submitted'
    score_key    = f'm{m_num}_quiz_score'
    form_key     = f'm{m_num}_quiz_form'
    start_btn    = f'start_m{m_num}_quiz'
    retake_btn   = f'retake_m{m_num}'
    next_module  = f'module_{int(m_num)+1}'

    if not st.session_state[started_key]:
        st.markdown("""
        <div style="text-align:center; padding: 2rem 0 1rem;">
            <div style="font-size:0.85rem; color:var(--apple-secondary); margin-bottom:1rem;">
                Finished reading? Test your understanding.
            </div>
        </div>
        """, unsafe_allow_html=True)
        c1, c2, c3 = st.columns([1,1,1])
        with c2:
            st.button("Begin Assessment →", key=start_btn, use_container_width=True)
        if st.session_state.get(start_btn):
            st.session_state[started_key] = True
            st.rerun()

    if st.session_state[started_key]:
        st.markdown(f"""
        <div class="quiz-header">
            <div class="quiz-header-label">Formative Evaluation</div>
            <div class="quiz-header-title">Knowledge Check</div>
            <div class="quiz-header-sub">5 questions · Select the best answer for each</div>
        </div>
        """, unsafe_allow_html=True)

        with st.form(key=form_key, clear_on_submit=False):
            user_answers = []
            for i, q in enumerate(quiz_data):
                st.markdown(f"**{i+1}. {q['question']}**")
                ans = st.radio("Select:", q["options"], key=f"m{m_num}_q_{i}",
                               label_visibility="collapsed", index=None)
                user_answers.append(ans)
                if i < len(quiz_data) - 1:
                    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
            st.markdown("<div style='height:0.75rem'></div>", unsafe_allow_html=True)
            submit = st.form_submit_button("Submit Answers", use_container_width=False)

        if submit:
            if None in user_answers:
                st.error("Please answer all questions before submitting.")
            else:
                score = sum(1 for i, q in enumerate(quiz_data) if user_answers[i] == q["answer"])
                st.session_state[score_key] = score
                st.session_state[submitted_key] = True

        if st.session_state[submitted_key]:
            sc = st.session_state[score_key]
            passed = sc >= 4

            st.markdown(f"""
            <div style="background:{'rgba(52,199,89,0.08)' if passed else 'rgba(255,59,48,0.07)'};
                        border:1px solid {'rgba(52,199,89,0.3)' if passed else 'rgba(255,59,48,0.2)'};
                        border-radius:18px; padding:2rem 2.25rem; margin-top:1rem;">
                <div style="font-size:0.72rem;font-weight:600;letter-spacing:0.1em;text-transform:uppercase;
                            color:{'#1a7f3c' if passed else '#c0392b'}; margin-bottom:0.5rem;">
                    {'Competency Verified' if passed else 'Below Threshold'}
                </div>
                <div class="score-badge">
                    <span class="score-num" style="color:{'#34c759' if passed else '#ff3b30'}">{sc}</span>
                    <span class="score-denom">/ {len(quiz_data)}</span>
                </div>
                <div style="font-size:0.95rem; color:var(--apple-secondary); margin-top:0.5rem;">
                    {'Outstanding work — the next module is now unlocked.' if passed else 'Review the lesson material and try again.'}
                </div>
            </div>
            """, unsafe_allow_html=True)

            if passed and int(m_num) < 3:
                if next_module not in st.session_state.unlocked_modules:
                    st.session_state.unlocked_modules.append(next_module)

            if not passed:
                st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
                c1, c2, c3 = st.columns([1,1,1])
                with c2:
                    st.button("Retry Assessment", key=retake_btn, use_container_width=True)
                if st.session_state.get(retake_btn):
                    st.session_state[submitted_key] = False
                    st.rerun()


# ═══════════════════════════════════════════════════════════════════
#  MODULE 1 — READING
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'module_1':
    render_module(
        module_key='module_1', m_num='1',
        title='Reading', eyebrow='Module 01 — Language Arts', icon='📖',
        accent='#0071e3',
        sections=[
            ("Section 1.0", "Elements of a Story",
             "Every story has essential parts that help us understand what is happening. "
             "The <strong>setting</strong> tells us when and where the story takes place. "
             "The <strong>characters</strong> are the people, animals, or creatures in the story. "
             "The <strong>plot</strong> is the sequence of events that take place from beginning to end."),
            ("Section 1.1", "Finding the Main Idea",
             "When reading a paragraph, it is important to find the main idea — the primary point "
             "the author wants to communicate. It is often found in the <strong>topic sentence</strong>, "
             "which is usually the first sentence of the paragraph."),
            ("Section 1.2", "Using Context Clues",
             "Sometimes you will read a word you do not know. Instead of immediately using a dictionary, "
             "you can look at the surrounding words to guess its meaning. "
             "These helpful hints are called <strong>context clues</strong>."),
        ],
        quiz_data=M1_QUIZ_DATA
    )


# ═══════════════════════════════════════════════════════════════════
#  MODULE 2 — MATHEMATICS
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'module_2':
    render_module(
        module_key='module_2', m_num='2',
        title='Mathematics', eyebrow='Module 02 — Quantitative Reasoning', icon='📐',
        accent='#34c759',
        sections=[
            ("Section 2.0", "Basic Operations",
             "Mathematics uses operations to solve problems. <strong>Addition</strong> combines two numbers "
             "to find a total sum. <strong>Subtraction</strong> finds the difference between numbers. "
             "<strong>Multiplication</strong> is a faster way to perform repeated addition."),
            ("Section 2.1", "Understanding Fractions",
             "A fraction represents a part of a whole object. The top number (<strong>numerator</strong>) "
             "shows how many parts we have. The bottom number (<strong>denominator</strong>) shows how many "
             "equal parts make up the entire whole. The denominator can never be zero."),
            ("Section 2.2", "Basic Geometry",
             "Geometry is the study of shapes and spaces. A <strong>polygon</strong> is a flat shape with "
             "straight sides, like a triangle, square, or rectangle. The distance around the outside edge "
             "of a shape is called the <strong>perimeter</strong>."),
        ],
        quiz_data=M2_QUIZ_DATA
    )


# ═══════════════════════════════════════════════════════════════════
#  MODULE 3 — NATURAL SCIENCES
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'module_3':
    render_module(
        module_key='module_3', m_num='3',
        title='Natural Sciences', eyebrow='Module 03 — Earth Science', icon='🌊',
        accent='#af52de',
        sections=[
            ("Section 3.0", "Introduction to the Water Cycle",
             "The water cycle is the continuous movement of water on Earth. Water changes its state "
             "as it moves between the ground, the oceans, and the sky. The amount of water on our "
             "planet stays mostly the same — it simply travels to different places."),
            ("Section 3.1", "Evaporation & Condensation",
             "<strong>Evaporation</strong> happens when the sun heats liquid water in rivers and oceans, "
             "turning it into an invisible gas called water vapor. When this vapor rises high into the sky "
             "and cools down, it undergoes <strong>condensation</strong>, forming the clouds we see."),
            ("Section 3.2", "Precipitation & Collection",
             "When clouds become too heavy with water, it falls back to Earth. This is called "
             "<strong>precipitation</strong>, which can be rain, snow, or hail. This water then collects "
             "in oceans, lakes, and underground areas called <strong>aquifers</strong>, ready to start "
             "the cycle again."),
        ],
        quiz_data=M3_QUIZ_DATA
    )


# ═══════════════════════════════════════════════════════════════════
#  PROFILE / METRICS
# ═══════════════════════════════════════════════════════════════════
elif st.session_state.current_view == 'profile':
    st.button("← Dashboard", key="back_profile", on_click=navigate, args=('dashboard',))
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <div class="page-eyebrow">Performance Records</div>
        <div class="page-title">📊 Academic Metrics</div>
        <div class="page-subtitle">A detailed view of your curriculum progress and scores.</div>
    </div>
    """, unsafe_allow_html=True)

    unlocked_count = len(st.session_state.unlocked_modules)
    progress_percentage = int((unlocked_count / 3) * 100)

    avg_score, score_count = 0, 0
    for mn in ['1','2','3']:
        if st.session_state[f'm{mn}_quiz_submitted']:
            avg_score += st.session_state[f'm{mn}_quiz_score']
            score_count += 1
    final_avg = (avg_score / (score_count * 5) * 100) if score_count > 0 else 0

    completed = sum([
        st.session_state.m1_quiz_submitted and st.session_state.m1_quiz_score >= 4,
        st.session_state.m2_quiz_submitted and st.session_state.m2_quiz_score >= 4,
        st.session_state.m3_quiz_submitted and st.session_state.m3_quiz_score >= 4,
    ])

    col_s1, col_s2, col_s3 = st.columns(3, gap="medium")
    with col_s1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{completed}</div>
            <div class="stat-label">Modules Passed</div>
        </div>
        """, unsafe_allow_html=True)
    with col_s2:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{final_avg:.0f}%</div>
            <div class="stat-label">Mean Accuracy</div>
        </div>
        """, unsafe_allow_html=True)
    with col_s3:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{progress_percentage}%</div>
            <div class="stat-label">Curriculum Progress</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)

    # Progress bar
    st.markdown(f"""
    <div style="background:var(--apple-card); border:1px solid var(--apple-border);
                border-radius:16px; padding:1.5rem 2rem; box-shadow:var(--apple-shadow);
                margin-bottom: 1.5rem;">
        <div style="display:flex; justify-content:space-between; align-items:center; margin-bottom:0.75rem;">
            <span style="font-weight:600; color:var(--apple-text); font-size:0.95rem;">Overall Progress</span>
            <span style="font-size:0.85rem; color:var(--apple-secondary);">{completed} of 3 modules completed</span>
        </div>
        <div class="progress-wrap" style="height:8px;">
            <div class="progress-fill" style="width:{int(completed/3*100)}%; height:8px;"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Determine statuses
    def module_status(mn, min_score=4):
        sub = st.session_state[f'm{mn}_quiz_submitted']
        sc  = st.session_state[f'm{mn}_quiz_score']
        if sub and sc >= min_score:
            return "Verified", f"{sc}/5", "#1a7f3c"
        elif sub:
            return "Needs Retry", f"{sc}/5", "#c0392b"
        elif f'module_{mn}' in st.session_state.unlocked_modules:
            return "In Progress", "—", "#ff9f0a"
        else:
            return "Locked", "—", "#6e6e73"

    m1_s, m1_d, m1_c = module_status('1')
    m2_s, m2_d, m2_c = module_status('2')
    m3_s, m3_d, m3_c = module_status('3')

    st.markdown(f"""
    <table class="apple-table">
        <thead>
            <tr>
                <th>Module</th>
                <th>Subject</th>
                <th>Status</th>
                <th>Score</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td style="color:var(--apple-secondary); font-size:0.8rem;">01</td>
                <td style="font-weight:500;">📖 Reading</td>
                <td style="color:{m1_c}; font-weight:600;">{m1_s}</td>
                <td style="font-family:monospace; letter-spacing:0.05em;">{m1_d}</td>
            </tr>
            <tr>
                <td style="color:var(--apple-secondary); font-size:0.8rem;">02</td>
                <td style="font-weight:500;">📐 Mathematics</td>
                <td style="color:{m2_c}; font-weight:600;">{m2_s}</td>
                <td style="font-family:monospace; letter-spacing:0.05em;">{m2_d}</td>
            </tr>
            <tr>
                <td style="color:var(--apple-secondary); font-size:0.8rem;">03</td>
                <td style="font-weight:500;">🌊 Natural Sciences</td>
                <td style="color:{m3_c}; font-weight:600;">{m3_s}</td>
                <td style="font-family:monospace; letter-spacing:0.05em;">{m3_d}</td>
            </tr>
        </tbody>
    </table>
    """, unsafe_allow_html=True)
