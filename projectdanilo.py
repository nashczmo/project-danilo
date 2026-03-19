import streamlit as st
import os

if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write('[theme]\nbase="light"\nprimaryColor="#2563eb"\nbackgroundColor="#f8fafc"\nsecondaryBackgroundColor="#ffffff"\ntextColor="#1f2937"\nfont="sans serif"\n')

st.set_page_config(page_title="DANILO Academic Platform", layout="wide", initial_sidebar_state="collapsed")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    html, body, [class*="css"], p, div, span, h1, h2, h3, h4, h5, h6, li, label, button {
        font-family: 'Inter', sans-serif !important;
    }
    
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 5rem !important;
        max-width: 1200px !important;
    }

    #MainMenu, footer { visibility: hidden; }

    h1 {
        font-weight: 700 !important;
        letter-spacing: -0.02em !important;
        color: #111827 !important;
        border-bottom: 2px solid #e5e7eb !important;
        padding-bottom: 1rem !important;
        margin-bottom: 2rem !important;
    }

    h2 {
        font-weight: 600 !important;
        color: #111827 !important;
        margin-top: 2rem !important;
    }

    p {
        color: #4b5563 !important;
        line-height: 1.7 !important;
        font-size: 1.05rem !important;
    }

    .dashboard-title {
        font-size: 2.25rem;
        font-weight: 700;
        color: #111827;
        margin-bottom: 2rem;
        letter-spacing: -0.02em;
    }

    .module-card {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem;
        height: 200px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        display: flex;
        flex-direction: column;
        margin-bottom: 1rem;
    }

    .module-title {
        font-size: 1.25rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }

    .module-desc {
        font-size: 0.95rem;
        color: #6b7280;
        flex-grow: 1;
    }

    .status-badge {
        display: inline-block;
        padding: 0.25rem 0.75rem;
        border-radius: 9999px;
        font-size: 0.85rem;
        font-weight: 600;
        width: fit-content;
    }

    .status-active {
        background-color: #d1fae5;
        color: #065f46;
    }

    .status-locked {
        background-color: #f3f4f6;
        color: #6b7280;
    }

    div[data-testid="stButton"] > button {
        border-radius: 8px !important;
        font-weight: 600 !important;
        padding: 0.75rem 1rem !important;
        transition: all 0.2s ease !important;
    }

    div[role="radiogroup"] {
        background-color: #ffffff !important;
        border: 1px solid #e5e7eb !important;
        border-radius: 12px !important;
        padding: 1.5rem !important;
        margin-bottom: 2rem !important;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.05) !important;
    }

    .stat-card {
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    .stat-value {
        font-size: 2.5rem;
        font-weight: 700;
        color: #2563eb;
        margin-bottom: 0.5rem;
    }

    .stat-label {
        font-size: 0.875rem;
        color: #4b5563;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }

    table {
        width: 100%;
        border-collapse: collapse;
        background: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 12px;
        overflow: hidden;
    }
    th, td {
        padding: 1rem 1.5rem;
        text-align: left;
        border-bottom: 1px solid #e5e7eb;
    }
    th {
        background-color: #f9fafb;
        font-weight: 600;
        color: #4b5563;
    }
    tr:last-child td {
        border-bottom: none;
    }
</style>
""", unsafe_allow_html=True)

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

M1_QUIZ_DATA = [
    {"question": "What do we call the specific time and place where a story happens?", "options": ["The Plot", "The Characters", "The Setting", "The Title"], "answer": "The Setting"},
    {"question": "Where is the main idea of a paragraph usually located?", "options": ["In the middle", "At the very end", "In the topic sentence", "In the dictionary"], "answer": "In the topic sentence"},
    {"question": "What are hints around a new word called that help you understand its meaning?", "options": ["Context clues", "Story settings", "Hidden numbers", "Spelling words"], "answer": "Context clues"},
    {"question": "Who are the people or animals that take part in a story?", "options": ["The Authors", "The Readers", "The Characters", "The Settings"], "answer": "The Characters"},
    {"question": "What is the sequence of events from the beginning to the end of a story called?", "options": ["The Plot", "The Cover", "The Vocabulary", "The Conclusion"], "answer": "The Plot"}
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

if st.session_state.current_view == 'dashboard':
    st.markdown('<div class="dashboard-title">DANILO Academic Platform</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3, gap="large")
    
    with col1:
        st.markdown("""
        <div class="module-card" style="border-top: 4px solid #2563eb;">
            <div class="module-title" style="color: #2563eb;">Reading</div>
            <div class="module-desc">Understanding Stories and Words</div>
            <div class="status-badge status-active">Accessible</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Access Curriculum", key="btn_m1", on_click=navigate, args=('module_1',), use_container_width=True)

    with col2:
        m2_locked = 'module_2' not in st.session_state.unlocked_modules
        border_color = "#9ca3af" if m2_locked else "#059669"
        title_color = "#4b5563" if m2_locked else "#059669"
        badge_class = "status-locked" if m2_locked else "status-active"
        badge_text = "Requires Reading" if m2_locked else "Accessible"
        
        st.markdown(f"""
        <div class="module-card" style="border-top: 4px solid {border_color};">
            <div class="module-title" style="color: {title_color};">Mathematics</div>
            <div class="module-desc">Foundational Operations and Shapes</div>
            <div class="status-badge {badge_class}">{badge_text}</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Access Curriculum", key="btn_m2", on_click=navigate, args=('module_2',), disabled=m2_locked, use_container_width=True)

    with col3:
        m3_locked = 'module_3' not in st.session_state.unlocked_modules
        border_color_3 = "#9ca3af" if m3_locked else "#4f46e5"
        title_color_3 = "#4b5563" if m3_locked else "#4f46e5"
        badge_class_3 = "status-locked" if m3_locked else "status-active"
        badge_text_3 = "Requires Mathematics" if m3_locked else "Accessible"
        
        st.markdown(f"""
        <div class="module-card" style="border-top: 4px solid {border_color_3};">
            <div class="module-title" style="color: {title_color_3};">Natural Sciences</div>
            <div class="module-desc">The Water Cycle</div>
            <div class="status-badge {badge_class_3}">{badge_text_3}</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Access Curriculum", key="btn_m3", on_click=navigate, args=('module_3',), disabled=m3_locked, use_container_width=True)

    col4, col5, col6 = st.columns(3, gap="large")
    with col4:
        st.markdown("""
        <div style="height: 1rem;"></div>
        <div class="module-card" style="border-top: 4px solid #d97706;">
            <div class="module-title" style="color: #d97706;">Academic Metrics</div>
            <div class="module-desc">Performance Analysis & Records</div>
            <div class="status-badge status-active">Accessible</div>
        </div>
        """, unsafe_allow_html=True)
        st.button("Review Analytics", key="btn_profile", on_click=navigate, args=('profile',), use_container_width=True)

elif st.session_state.current_view == 'module_1':
    st.button("← Return to Dashboard", key="back_m1", on_click=navigate, args=('dashboard',))
    
    st.markdown("<h1>Reading: Understanding Stories and Words</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2>1.0 Elements of a Story</h2>", unsafe_allow_html=True)
    st.markdown("Every story has essential parts that help us understand what is happening. The **setting** tells us when and where the story takes place. The **characters** are the people, animals, or creatures in the story. The **plot** is the sequence of events that take place from the beginning to the end.")
    
    st.markdown("<h2>1.1 Finding the Main Idea</h2>", unsafe_allow_html=True)
    st.markdown("When reading a paragraph, it is important to find the main idea. The main idea is the primary point the author wants to communicate. It is often found in the **topic sentence**, which is usually the first sentence of the paragraph.")
    
    st.markdown("<h2>1.2 Using Context Clues</h2>", unsafe_allow_html=True)
    st.markdown("Sometimes you will read a word you do not know. Instead of immediately using a dictionary, you can look at the surrounding words to guess its meaning. These helpful hints are called **context clues**.")
    
    st.divider()
    
    if not st.session_state.m1_quiz_started:
        st.button("Begin Assessment", key="start_m1_quiz")
        if st.session_state.get('start_m1_quiz'):
            st.session_state.m1_quiz_started = True
            st.rerun()
            
    if st.session_state.m1_quiz_started:
        st.markdown("<h2>Formative Evaluation</h2>", unsafe_allow_html=True)
        
        with st.form(key='m1_quiz_form', clear_on_submit=False):
            m1_user_answers = []
            for i, q in enumerate(M1_QUIZ_DATA):
                st.markdown(f"**{i+1}. {q['question']}**")
                ans = st.radio("Select:", q["options"], key=f"m1_q_{i}", label_visibility="collapsed", index=None)
                m1_user_answers.append(ans)
            st.markdown("<br>", unsafe_allow_html=True)
            submit_m1 = st.form_submit_button(label='Submit Answers')
            
        if submit_m1:
            if None in m1_user_answers:
                st.error("Submission incomplete. Please select an answer for every question.")
            else:
                score = sum([1 for i, q in enumerate(M1_QUIZ_DATA) if m1_user_answers[i] == q["answer"]])
                st.session_state.m1_quiz_score = score
                st.session_state.m1_quiz_submitted = True
            
        if st.session_state.m1_quiz_submitted:
            st.markdown(f"<h3>Score: {st.session_state.m1_quiz_score} / {len(M1_QUIZ_DATA)}</h3>", unsafe_allow_html=True)
            if st.session_state.m1_quiz_score >= 4:
                st.success("Excellent reading comprehension. Competency verified. The Mathematics module is now unlocked.")
                if 'module_2' not in st.session_state.unlocked_modules:
                    st.session_state.unlocked_modules.append('module_2')
            else:
                st.error("Competency threshold not achieved. Reading requires practice. Review the lesson above and attempt the assessment again.")
                st.button("Retry Assessment", key="retake_m1")
                if st.session_state.get('retake_m1'):
                    st.session_state.m1_quiz_submitted = False
                    st.rerun()

elif st.session_state.current_view == 'module_2':
    st.button("← Return to Dashboard", key="back_m2", on_click=navigate, args=('dashboard',))
    
    st.markdown("<h1>Mathematics: Foundational Operations and Shapes</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2>2.0 Basic Operations</h2>", unsafe_allow_html=True)
    st.markdown("Mathematics uses operations to solve problems. **Addition** combines two numbers to find a total sum. **Subtraction** finds the difference between numbers. **Multiplication** is a faster way to do repeated addition.")
    
    st.markdown("<h2>2.1 Fractions</h2>", unsafe_allow_html=True)
    st.markdown("A fraction represents a part of a whole object. The top number (numerator) shows how many parts we have. The bottom number (denominator) shows how many equal parts make up the entire whole. The denominator can never be zero.")
    
    st.markdown("<h2>2.2 Basic Geometry</h2>", unsafe_allow_html=True)
    st.markdown("Geometry is the study of shapes and spaces. A **polygon** is a flat shape with straight sides, like a triangle, square, or rectangle. The distance around the outside edge of a shape is called the **perimeter**.")
    
    st.divider()
    
    if not st.session_state.m2_quiz_started:
        st.button("Begin Assessment", key="start_m2_quiz")
        if st.session_state.get('start_m2_quiz'):
            st.session_state.m2_quiz_started = True
            st.rerun()
            
    if st.session_state.m2_quiz_started:
        st.markdown("<h2>Formative Evaluation</h2>", unsafe_allow_html=True)
        
        with st.form(key='m2_quiz_form', clear_on_submit=False):
            m2_user_answers = []
            for i, q in enumerate(M2_QUIZ_DATA):
                st.markdown(f"**{i+1}. {q['question']}**")
                ans = st.radio("Select:", q["options"], key=f"m2_q_{i}", label_visibility="collapsed", index=None)
                m2_user_answers.append(ans)
            st.markdown("<br>", unsafe_allow_html=True)
            submit_m2 = st.form_submit_button(label='Submit Answers')
            
        if submit_m2:
            if None in m2_user_answers:
                st.error("Submission incomplete. Please select an answer for every question.")
            else:
                score = sum([1 for i, q in enumerate(M2_QUIZ_DATA) if m2_user_answers[i] == q["answer"]])
                st.session_state.m2_quiz_score = score
                st.session_state.m2_quiz_submitted = True
            
        if st.session_state.m2_quiz_submitted:
            st.markdown(f"<h3>Score: {st.session_state.m2_quiz_score} / {len(M2_QUIZ_DATA)}</h3>", unsafe_allow_html=True)
            if st.session_state.m2_quiz_score >= 4:
                st.success("Great calculating! Competency verified. The Natural Sciences module is now unlocked.")
                if 'module_3' not in st.session_state.unlocked_modules:
                    st.session_state.unlocked_modules.append('module_3')
            else:
                st.error("Competency threshold not achieved. Math requires practice. Review the rules of numbers and shapes above, and try the assessment again.")
                st.button("Retry Assessment", key="retake_m2")
                if st.session_state.get('retake_m2'):
                    st.session_state.m2_quiz_submitted = False
                    st.rerun()

elif st.session_state.current_view == 'module_3':
    st.button("← Return to Dashboard", key="back_m3", on_click=navigate, args=('dashboard',))
    
    st.markdown("<h1>Natural Sciences: The Water Cycle</h1>", unsafe_allow_html=True)
    
    st.markdown("<h2>3.0 Introduction to the Cycle</h2>", unsafe_allow_html=True)
    st.markdown("The water cycle is the continuous movement of water on Earth. Water changes its state as it moves between the ground, the oceans, and the sky. The amount of water on our planet stays mostly the same; it simply travels to different places.")
    
    st.markdown("<h2>3.1 Evaporation and Condensation</h2>", unsafe_allow_html=True)
    st.markdown("**Evaporation** happens when the sun heats liquid water in rivers and oceans, turning it into an invisible gas called water vapor. When this vapor rises high into the sky and cools down, it undergoes **condensation**, forming the clouds we see.")
    
    st.markdown("<h2>3.2 Precipitation and Collection</h2>", unsafe_allow_html=True)
    st.markdown("When clouds become too heavy with water, it falls back to Earth. This is called **precipitation**, which can be rain, snow, or hail. This water then collects in oceans, lakes, and underground areas called aquifers, ready to start the cycle again.")
    
    st.divider()
    
    if not st.session_state.m3_quiz_started:
        st.button("Begin Assessment", key="start_m3_quiz")
        if st.session_state.get('start_m3_quiz'):
            st.session_state.m3_quiz_started = True
            st.rerun()
            
    if st.session_state.m3_quiz_started:
        st.markdown("<h2>Formative Evaluation</h2>", unsafe_allow_html=True)
        
        with st.form(key='m3_quiz_form', clear_on_submit=False):
            m3_user_answers = []
            for i, q in enumerate(M3_QUIZ_DATA):
                st.markdown(f"**{i+1}. {q['question']}**")
                ans = st.radio("Select:", q["options"], key=f"m3_q_{i}", label_visibility="collapsed", index=None)
                m3_user_answers.append(ans)
            st.markdown("<br>", unsafe_allow_html=True)
            submit_m3 = st.form_submit_button(label='Submit Answers')
            
        if submit_m3:
            if None in m3_user_answers:
                st.error("Submission incomplete. Please select an answer for every question.")
            else:
                score = sum([1 for i, q in enumerate(M3_QUIZ_DATA) if m3_user_answers[i] == q["answer"]])
                st.session_state.m3_quiz_score = score
                st.session_state.m3_quiz_submitted = True
            
        if st.session_state.m3_quiz_submitted:
            st.markdown(f"<h3>Score: {st.session_state.m3_quiz_score} / {len(M3_QUIZ_DATA)}</h3>", unsafe_allow_html=True)
            if st.session_state.m3_quiz_score >= 4:
                st.success("Fantastic work! Competency verified. You have successfully completed all core modules in the curriculum.")
            else:
                st.error("Competency threshold not achieved. Science is about observation and learning. Read the water cycle steps again, and you will succeed on your next attempt.")
                st.button("Retry Assessment", key="retake_m3")
                if st.session_state.get('retake_m3'):
                    st.session_state.m3_quiz_submitted = False
                    st.rerun()

elif st.session_state.current_view == 'profile':
    st.button("← Return to Dashboard", key="back_profile", on_click=navigate, args=('dashboard',))
    
    st.markdown("<h1>Academic Performance Metrics</h1>", unsafe_allow_html=True)
    
    total_modules = 3
    unlocked_count = len(st.session_state.unlocked_modules)
    progress_percentage = int((unlocked_count / total_modules) * 100)
    
    avg_score = 0
    score_count = 0
    if st.session_state.m1_quiz_submitted:
        avg_score += st.session_state.m1_quiz_score
        score_count += 1
    if st.session_state.m2_quiz_submitted:
        avg_score += st.session_state.m2_quiz_score
        score_count += 1
    if st.session_state.m3_quiz_submitted:
        avg_score += st.session_state.m3_quiz_score
        score_count += 1
        
    final_avg = (avg_score / (score_count * 5) * 100) if score_count > 0 else 0

    col_s1, col_s2, col_s3 = st.columns(3, gap="large")
    with col_s1:
        st.markdown(f"""
        <div class="stat-card">
            <div class="stat-value">{unlocked_count}</div>
            <div class="stat-label">Modules Unlocked</div>
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
            <div class="stat-label">Curriculum Completion</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><h2>Curriculum Logs</h2>", unsafe_allow_html=True)

    m1_status = "Verified" if st.session_state.m1_quiz_submitted and st.session_state.m1_quiz_score >= 4 else "Pending Evaluation"
    m1_score_disp = f"{st.session_state.m1_quiz_score}/5" if st.session_state.m1_quiz_submitted else "N/A"
    
    m2_status = "Restricted Access"
    m2_score_disp = "N/A"
    if 'module_2' in st.session_state.unlocked_modules:
        m2_status = "Verified" if st.session_state.m2_quiz_submitted and st.session_state.m2_quiz_score >= 4 else "Pending Evaluation"
        m2_score_disp = f"{st.session_state.m2_quiz_score}/5" if st.session_state.m2_quiz_submitted else "N/A"

    m3_status = "Restricted Access"
    m3_score_disp = "N/A"
    if 'module_3' in st.session_state.unlocked_modules:
        m3_status = "Verified" if st.session_state.m3_quiz_submitted and st.session_state.m3_quiz_score >= 4 else "Pending Evaluation"
        m3_score_disp = f"{st.session_state.m3_quiz_score}/5" if st.session_state.m3_quiz_submitted else "N/A"

    st.markdown(f"""
    <table>
        <tr>
            <th>Module Identifier</th>
            <th>Competency Status</th>
            <th>Evaluation Metric</th>
        </tr>
        <tr>
            <td style="font-weight: 500;">Reading</td>
            <td style="color: {'#059669' if m1_status == 'Verified' else '#6b7280'}; font-weight: 600;">{m1_status}</td>
            <td style="font-family: monospace; font-size: 1.1rem;">{m1_score_disp}</td>
        </tr>
        <tr>
            <td style="font-weight: 500;">Mathematics</td>
            <td style="color: {'#059669' if m2_status == 'Verified' else '#6b7280'}; font-weight: 600;">{m2_status}</td>
            <td style="font-family: monospace; font-size: 1.1rem;">{m2_score_disp}</td>
        </tr>
        <tr>
            <td style="font-weight: 500;">Natural Sciences</td>
            <td style="color: {'#059669' if m3_status == 'Verified' else '#6b7280'}; font-weight: 600;">{m3_status}</td>
            <td style="font-family: monospace; font-size: 1.1rem;">{m3_score_disp}</td>
        </tr>
    </table>
    """, unsafe_allow_html=True)