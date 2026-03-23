import streamlit as st
import os

if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write('[theme]\nbase="light"\nprimaryColor="#1a73e8"\nbackgroundColor="#f1f3f4"\nsecondaryBackgroundColor="#ffffff"\ntextColor="#202124"\nfont="sans serif"\n')

st.set_page_config(
    page_title="DANILO Classroom",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Quiz data ─────────────────────────────────────────────────────────────────
M1 = [
    {"q":"What do we call the specific time and place in which a story unfolds?","o":["The Plot","The Characters","The Setting","The Theme"],"a":"The Setting"},
    {"q":"Where is the main idea of a paragraph most commonly found?","o":["In a footnote","At the very end","In the topic sentence","Between the lines"],"a":"In the topic sentence"},
    {"q":"What are surrounding clues that help a reader decode an unfamiliar word?","o":["Context clues","Phonics hints","Story settings","Grammar rules"],"a":"Context clues"},
    {"q":"Who are the people, animals, or creatures that participate in a story's events?","o":["The Authors","The Narrators","The Characters","The Themes"],"a":"The Characters"},
    {"q":"What is the term for the sequence of events that drives a story from beginning to end?","o":["The Plot","The Cover Page","The Vocabulary","The Epilogue"],"a":"The Plot"},
]
M2 = [
    {"q":"What does reading fluency primarily involve?","o":["Reading as fast as possible","Reading accurately, smoothly, and with natural expression","Memorising every vocabulary word","Reading silently without any lip movement"],"a":"Reading accurately, smoothly, and with natural expression"},
    {"q":"Which technique involves reading the same passage multiple times until it flows effortlessly?","o":["Skimming","Scanning","Repeated reading","Speed reading"],"a":"Repeated reading"},
    {"q":"What is a 'sight word'?","o":["A word with silent letters","A word instantly recognised without sounding it out","A very long word","A word borrowed from another language"],"a":"A word instantly recognised without sounding it out"},
    {"q":"What does reading with 'expression' mean?","o":["Speaking as loudly as possible","Changing your voice to match the emotion and meaning of the text","Reading every word at the same monotone pace","Pausing three seconds after every sentence"],"a":"Changing your voice to match the emotion and meaning of the text"},
    {"q":"Which habit best strengthens reading comprehension over time?","o":["Reading only one type of book","Asking thoughtful questions before, during, and after reading","Skipping all difficult words","Reading only very short sentences"],"a":"Asking thoughtful questions before, during, and after reading"},
]
M3 = [
    {"q":"What is the total sum when you add 145 and 278?","o":["423","413","433","323"],"a":"423"},
    {"q":"What is the perimeter of a square with one side measuring 9 units?","o":["18 units","27 units","36 units","81 units"],"a":"36 units"},
    {"q":"In the fraction 3/4, what does the bottom number 4 represent?","o":["The parts we have","The total equal parts making up the whole","The sum of both numbers","The difference between two numbers"],"a":"The total equal parts making up the whole"},
    {"q":"What is the product of 15 multiplied by 8?","o":["100","110","120","130"],"a":"120"},
    {"q":"What is the correct term for any flat, closed shape bounded by straight sides?","o":["Circle","Sphere","Polygon","Cylinder"],"a":"Polygon"},
]
M4 = [
    {"q":"What process transforms liquid water from rivers and oceans into invisible water vapour?","o":["Condensation","Evaporation","Precipitation","Sublimation"],"a":"Evaporation"},
    {"q":"Which energy source is the primary driver of the entire water cycle?","o":["The Moon's gravity","Geothermal vents","The Sun","Ocean currents"],"a":"The Sun"},
    {"q":"What forms when rising water vapour cools and condenses in the atmosphere?","o":["Raindrops on a window","Clouds","Underground rivers","Aquifers"],"a":"Clouds"},
    {"q":"Which of the following is an example of precipitation?","o":["A puddle drying in the sun","Snow falling from the sky","Steam rising from boiling water","Ice melting in a glass"],"a":"Snow falling from the sky"},
    {"q":"What is the name for an underground layer of permeable rock holding large amounts of freshwater?","o":["A cloud layer","An aquifer","The stratosphere","A water table valve"],"a":"An aquifer"},
]

MODS = {
    "module_1":{
        "k":"1","label":"Reading","section":"Grade 4 — English","teacher":"Ms. Santos",
        "icon":"📖","hbg":"#1a73e8","avatar_bg":"#1557b0",
        "quiz":M1,"next":"module_2","umsg":"Reading Fluency is now unlocked!",
        "topics":[
            ("📚","#e8f0fe","#1a73e8","1.0 — Elements of a Story",
             "Every story is built from essential building blocks that work together to create meaning and bring a narrative to life. The <b>setting</b> establishes the world of the story — not only the physical location but also the time period, culture, atmosphere, and mood in which events unfold. A story set in a rainy medieval castle creates an entirely different feeling from one set on a sun-drenched modern beach, even when the plot is nearly identical. The <b>characters</b> are the living hearts of any narrative — they can be people, animals, mythical creatures, or even everyday objects given a personality. Their hopes, fears, flaws, and relationships create the emotional texture that keeps readers turning pages long after bedtime. The <b>plot</b> is the engine: the carefully ordered chain of events — conflict, rising action, climax, falling action, and resolution — that propels the reader from the opening sentence to the very last word. Mastering these three elements gives you a reliable lens through which to read, analyse, and enjoy any story you encounter, from picture books to classic literature."),
            ("🔍","#e6f4ea","#1e8e3e","1.1 — Finding the Main Idea",
             "Every well-written paragraph revolves around a single central point called the <b>main idea</b>. This is the author's primary message — the one thing they most want you to understand and remember after reading. Skilled readers train themselves to locate this quickly by looking for the <b>topic sentence</b>, which typically appears at or near the beginning of a paragraph and announces its subject clearly and directly. The sentences that follow — called <b>supporting details</b> — provide evidence, examples, statistics, anecdotes, or descriptions that expand on and reinforce the topic sentence. One reliable technique is to pause after reading any paragraph and ask yourself: 'If I had to express this entire paragraph in a single sentence, what would it say?' That mental summary is almost always the main idea. Apply this skill consistently across every text you read — newspaper articles, science chapters, social media posts — and even the most complex material will feel far more approachable and manageable."),
            ("💡","#fef7e0","#b06000","1.2 — Using Context Clues",
             "Encountering an unfamiliar word mid-sentence does not have to interrupt your reading flow. Skilled readers use <b>context clues</b> — the words, phrases, sentences, and even images surrounding the unknown term — to make an educated, confident guess about its meaning without ever pausing to reach for a dictionary. There are several recognisable types. <b>Definition clues</b> occur when the author helpfully explains a word immediately after using it, often signalled by phrases like 'which means,' 'that is,' or 'in other words.' <b>Synonym clues</b> appear when a nearby word shares a similar meaning. <b>Antonym clues</b> use contrast words like 'but,' 'however,' 'unlike,' or 'instead' to hint at an opposite meaning. <b>Example clues</b> illustrate a word's meaning through specific, concrete instances. The wider and more varied your reading, the sharper your context-clue instincts become — turning every unfamiliar word into an exciting opportunity to expand your vocabulary."),
            ("✍️","#fce8e6","#c5221f","1.3 — Building Your Vocabulary",
             "A rich vocabulary is among the most powerful tools any reader, writer, thinker, or communicator can possess. Words are the instruments of thought — the more precise and varied your vocabulary, the more accurately and vividly you can both understand the world and express your own ideas. One deeply effective strategy is keeping a <b>personal vocabulary journal</b>: a dedicated notebook where you record new words, their precise definitions, the original sentence in which you found them, and an original example sentence you craft yourself. Cognitive science research consistently shows that <b>spaced repetition</b> — revisiting new words at gradually increasing intervals — produces dramatically stronger long-term retention than cramming. Another proven strategy is studying <b>Greek and Latin word roots, prefixes, and suffixes</b>. For example, knowing that the Latin root <em>port</em> means 'to carry' instantly unlocks transport, import, export, portable, portfolio, and deportation. Vocabulary knowledge is wonderfully cumulative — each new word you learn makes learning the next one slightly easier."),
        ],
    },
    "module_2":{
        "k":"2","label":"Reading Fluency","section":"Grade 4 — English (Advanced)","teacher":"Ms. Santos",
        "icon":"🗣️","hbg":"#7b1fa2","avatar_bg":"#4a148c",
        "quiz":M2,"next":"module_3","umsg":"Mathematics is now unlocked!",
        "topics":[
            ("🎯","#f3e8fd","#7b1fa2","2.0 — What Is Reading Fluency?",
             "Reading fluency is the essential <b>bridge between recognising individual words on a page and truly comprehending what you read</b>. A fluent reader moves through text with three interlocking qualities: <b>accuracy</b> (decoding words correctly without errors), <b>automaticity</b> (recognising words instantly without conscious effort), and <b>prosody</b> (reading with natural rhythm, appropriate pacing, meaningful pauses, and expressive intonation that mirrors natural speech). When reading is effortful and halting, virtually all of a reader's mental energy is consumed by simply decoding individual words, leaving little capacity for higher-order thinking: inferring meaning, questioning the author, visualising scenes, or connecting ideas. Fluency liberates the brain to operate at a genuinely higher level. Decades of reading research have consistently identified fluency as one of the strongest individual predictors of overall reading comprehension — which means developing it is not optional; it is absolutely foundational."),
            ("🔄","#e8f0fe","#1a73e8","2.1 — The Power of Repeated Reading",
             "<b>Repeated reading</b> is one of the most elegantly simple yet strikingly powerful techniques in all of reading instruction. The method is straightforward: select a short, engaging passage and read it aloud multiple times (usually three to five), tracking your own accuracy, expression, and fluency as you improve with each reading. On your very first encounter, you are largely decoding. By your second reading, you begin to feel the natural shape and rhythm of sentences. By the third and fourth, you are reading with genuine expression and a level of comprehension you could not access before. Think of how a musician learns a new piece: they do not play it once and declare mastery. They rehearse it, refine it, identify trouble spots, and gradually build toward a confident, expressive performance. Reading is the same kind of practised, deliberate skill. A powerful companion is <b>paired reading</b>, where a more skilled reader sits beside a developing reader, reading aloud together — providing a real-time model of fluent, expressive reading."),
            ("👁️","#e6f4ea","#1e8e3e","2.2 — Sight Words and Automaticity",
             "A relatively small set of high-frequency words — called <b>sight words</b> — accounts for an astonishing proportion of all written English text. Words like 'the,' 'and,' 'said,' 'because,' 'through,' 'could,' 'would,' and 'there' appear on virtually every single page. When a reader must laboriously decode these extremely common words on every encounter, reading becomes painfully slow and mentally exhausting, draining energy that should be directed toward comprehension. The goal is complete <b>automaticity</b> — recognising these words as whole, instant, effortless units. Reading scientists call this process <b>orthographic mapping</b> — the deep encoding of a word's spelling, pronunciation, and meaning into long-term memory as a single, retrievable unit. Proven methods include systematic flashcard practice, classroom word walls, word sorts, word games, and — most powerfully — wide, regular, and pleasurable independent reading."),
            ("🧠","#fef7e0","#b06000","2.3 — Active Comprehension Strategies",
             "Deep reading comprehension is not a passive activity — it is an active, ongoing, and intentional conversation between the reader and the text. Expert readers deploy a toolkit of deliberate mental strategies that transform passive decoding into active sense-making. <b>Predicting</b> means forming expectations about what will happen next, based on evidence in the text and your own background knowledge. <b>Questioning</b> involves generating your own genuine questions — transforming you from a recipient into a critical thinker. <b>Visualising</b> means constructing a vivid, detailed mental movie of settings, characters, actions, and emotions — research consistently shows that strong visualisation dramatically improves both comprehension and memory. <b>Summarising</b> requires you to identify what truly matters and restate it concisely in your own words. <b>Making connections</b> — linking new information to personal experience, other texts, or the world — is the mechanism by which truly deep and durable understanding is formed."),
        ],
    },
    "module_3":{
        "k":"3","label":"Mathematics","section":"Grade 4 — Mathematics","teacher":"Mr. Reyes",
        "icon":"🔢","hbg":"#2e7d32","avatar_bg":"#1b5e20",
        "quiz":M3,"next":"module_4","umsg":"Natural Sciences is now unlocked!",
        "topics":[
            ("➕","#e6f4ea","#1e8e3e","3.0 — The Four Basic Operations",
             "All of mathematics rests on four fundamental operations that allow us to manipulate, compare, and understand numbers in every conceivable context. <b>Addition</b> combines two or more quantities to find their total sum — asking, in essence, 'how many altogether?' <b>Subtraction</b> is addition's inverse, finding the difference between quantities — asking 'how many remain?' or 'how much more?' <b>Multiplication</b> is a powerful and elegant shortcut for repeated addition: rather than laboriously adding 9 together seven separate times, we express this instantly as 9 × 7 = 63. Understanding multiplication conceptually — not merely as a set of facts to memorise — is the gateway to virtually all advanced mathematics, from algebra to calculus. <b>Division</b> is multiplication's inverse, partitioning a quantity into equal groups. Mastering all four operations with genuine fluency is a non-negotiable foundation for mathematical success at every stage of education and life."),
            ("½","#e8f0fe","#1a73e8","3.1 — Understanding Fractions",
             "A fraction is a precise, powerful mathematical tool for representing any part of a whole. When we write ¾, the number on top — the <b>numerator</b> (3) — tells us how many equal parts we currently possess. The number on the bottom — the <b>denominator</b> (4) — tells us into how many equal parts the whole has been divided. Imagine a rectangular chocolate bar divided into four equal pieces: eating three of those pieces means you have consumed ¾ of the bar. The denominator can <b>never be zero</b>, because dividing something into zero parts is a mathematical impossibility — it carries no coherent meaning. Fractions can be classified as <b>proper</b> (like ⅔, representing less than one whole), <b>improper</b> (like 7/4, representing more than one whole), or expressed as <b>mixed numbers</b> (like 1¾). A thorough understanding of fractions is the direct foundation for decimals, percentages, ratios, rates, and algebraic thinking."),
            ("📐","#fef7e0","#b06000","3.2 — Shapes, Perimeter, and Area",
             "Geometry is the magnificent branch of mathematics devoted to understanding the properties, relationships, and measurements of points, lines, angles, surfaces, and solid figures. A <b>polygon</b> is any flat, closed, two-dimensional figure entirely bounded by straight sides. Polygons are classified by the number of their sides: triangle (3), quadrilateral (4), pentagon (5), hexagon (6), and so on. Two of the most essential measurements of any flat shape are its <b>perimeter</b> and its <b>area</b>. The perimeter is the total distance around the complete outer boundary of a shape. For a rectangle: perimeter = 2 × (length + width). The area measures how much flat surface the shape covers. For a rectangle: area = length × width. Real-world applications are everywhere: a builder uses perimeter to calculate baseboard; a painter uses area to determine paint quantity; a farmer uses both to plan fields and fencing simultaneously."),
        ],
    },
    "module_4":{
        "k":"4","label":"Natural Sciences","section":"Grade 4 — Science","teacher":"Ms. Cruz",
        "icon":"🌍","hbg":"#e64a19","avatar_bg":"#bf360c",
        "quiz":M4,"next":None,"umsg":"🎉 Congratulations — all modules complete!",
        "topics":[
            ("🌊","#e8f0fe","#1a73e8","4.0 — Introduction to the Water Cycle",
             "The water cycle — known scientifically as the <b>hydrological cycle</b> — is one of Earth's most fundamental and life-sustaining natural processes. It describes the continuous, perpetual journey of water as it moves and transforms among Earth's surface (oceans, rivers, lakes, glaciers, soil), its atmosphere, and its underground systems. Water is never created or destroyed in this process; it simply changes its physical state and its location, cycling through the same pathways it has followed for approximately 4.5 billion years. The total volume of water on Earth has remained essentially constant since our planet formed. This means the water flowing from your tap today has, at some earlier moment, filled a prehistoric ocean, nourished a dinosaur, been locked inside an Antarctic glacier, and fallen as rain over a distant mountain range. Understanding the water cycle is fundamental to meteorology, hydrology, ecology, agriculture, and the science of climate change."),
            ("☀️","#fef7e0","#b06000","4.1 — Evaporation and Condensation",
             "<b>Evaporation</b> is the process by which the Sun's tremendous thermal energy heats liquid water at Earth's surface — primarily in oceans, seas, rivers, and lakes — converting it into water vapour, an invisible gas that rises buoyantly into the atmosphere. Roughly 90% of all atmospheric water vapour originates from ocean evaporation; the remaining 10% comes from the transpiration of land plants (collectively called <b>evapotranspiration</b>). As water vapour rises higher into the troposphere, it encounters progressively colder temperatures. When the vapour cools below a critical threshold called the <b>dew point</b>, it undergoes <b>condensation</b> — reverting from an invisible gas back into microscopic liquid water droplets or tiny ice crystals. These minuscule particles cling to even tinier specks of dust, sea salt, and pollen suspended in the air, clustering together to form the visible, billowing clouds we observe drifting across the sky."),
            ("🌧️","#e6f4ea","#1e8e3e","4.2 — Precipitation and Collection",
             "As clouds continue to grow — accumulating ever-greater quantities of condensed water droplets — gravity eventually overcomes the atmospheric forces keeping the droplets aloft. Water then falls back to Earth's surface as <b>precipitation</b>. The precise form precipitation takes is determined by atmospheric temperature: <b>rain</b> forms when temperatures remain above freezing throughout; <b>snow</b> forms when temperatures stay below freezing from cloud to ground; <b>sleet</b> forms when falling raindrops refreeze before reaching the ground; and <b>hail</b> forms when powerful updrafts inside intense thunderstorms repeatedly carry ice pellets back upward before they finally fall. Once precipitation reaches Earth's surface, water takes multiple pathways: it replenishes oceans, lakes, rivers, and reservoirs; it is drawn up by plant roots; and it seeps into soil through <b>infiltration</b>, percolating downward to recharge underground <b>aquifers</b> — vast reservoirs of freshwater capable of sustaining entire cities and ecosystems."),
        ],
    },
}

# ── Session state ─────────────────────────────────────────────────────────────
if "view" not in st.session_state: st.session_state.view = "home"
if "unlocked" not in st.session_state: st.session_state.unlocked = ["module_1"]
for m in ["1","2","3","4"]:
    for k,d in [("qs",False),("qd",False),("qr",0)]:
        if f"m{m}_{k}" not in st.session_state: st.session_state[f"m{m}_{k}"] = d

def nav(v): st.session_state.view = v

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Inter font + reset ─────────────────────────────────────────── */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

*, html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
    -webkit-font-smoothing: antialiased !important;
    box-sizing: border-box;
}

/* ── Design tokens ──────────────────────────────────────────────── */
:root {
    --blue:    #1a73e8;
    --blue-dk: #1557b0;
    --green:   #1e8e3e;
    --red:     #d93025;
    --yellow:  #b06000;
    --purple:  #7b1fa2;
    --bg:      #f1f3f4;
    --surface: #ffffff;
    --border:  #e0e0e0;
    --t1:      #202124;
    --t2:      #5f6368;
    --t3:      #80868b;
    --sh1: 0 1px 2px rgba(60,64,67,.3), 0 1px 3px 1px rgba(60,64,67,.15);
    --sh2: 0 1px 3px rgba(60,64,67,.3), 0 4px 8px 3px rgba(60,64,67,.15);
    --sh3: 0 4px 8px rgba(60,64,67,.2), 0 8px 16px 4px rgba(60,64,67,.12);
}

/* ── App + Streamlit overrides ──────────────────────────────────── */
.stApp { background: var(--bg) !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }
.main > div { padding: 0 !important; }
section[data-testid="stSidebar"] > div { padding-top: 0 !important; }

/* ── Sidebar ────────────────────────────────────────────────────── */
section[data-testid="stSidebar"] {
    background: var(--surface) !important;
    border-right: 1px solid var(--border) !important;
    width: 256px !important;
    min-width: 256px !important;
}
section[data-testid="stSidebar"] > div {
    width: 256px !important;
    padding: 0 !important;
}

/* Always-visible collapsed toggle */
[data-testid="collapsedControl"] {
    visibility: visible !important;
    display: flex !important;
    opacity: 1 !important;
    position: fixed !important;
    top: 16px !important;
    left: 16px !important;
    z-index: 99999 !important;
    width: 40px !important;
    height: 40px !important;
    border-radius: 50% !important;
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    cursor: pointer !important;
    align-items: center !important;
    justify-content: center !important;
    transition: background .15s !important;
}
[data-testid="collapsedControl"]:hover { background: rgba(32,33,36,.08) !important; }
[data-testid="collapsedControl"] svg { width: 20px !important; height: 20px !important; color: #5f6368 !important; }

/* ── All sidebar nav buttons ────────────────────────────────────── */
div[data-testid="stButton"] > button {
    font-family: 'Inter', sans-serif !important;
    font-size: .875rem !important;
    font-weight: 500 !important;
    color: var(--t1) !important;
    background: transparent !important;
    border: none !important;
    border-radius: 0 24px 24px 0 !important;
    padding: 0 24px !important;
    height: 48px !important;
    width: 100% !important;
    text-align: left !important;
    letter-spacing: 0 !important;
    cursor: pointer !important;
    transition: background .15s ease !important;
    display: flex !important;
    align-items: center !important;
}
div[data-testid="stButton"] > button:hover { background: #f1f3f4 !important; }
div[data-testid="stButton"] > button:active { background: #e8eaed !important; }

/* Form submit button */
div[data-testid="stForm"] div[data-testid="stButton"] > button {
    background: var(--blue) !important;
    color: #fff !important;
    border-radius: 6px !important;
    padding: 0 20px !important;
    height: 38px !important;
    font-size: .875rem !important;
    font-weight: 500 !important;
    width: auto !important;
    text-align: center !important;
    box-shadow: none !important;
    transition: background .15s, box-shadow .15s !important;
}
div[data-testid="stForm"] div[data-testid="stButton"] > button:hover {
    background: var(--blue-dk) !important;
    box-shadow: var(--sh1) !important;
}

/* Radio */
div[role="radiogroup"] {
    background: var(--surface) !important;
    border: 1px solid var(--border) !important;
    border-radius: 8px !important;
    padding: 12px 16px !important;
    margin-bottom: 8px !important;
    box-shadow: none !important;
    transition: border-color .15s, box-shadow .15s !important;
}
div[role="radiogroup"]:focus-within {
    border-color: var(--blue) !important;
    box-shadow: 0 0 0 2px rgba(26,115,232,.12) !important;
}

/* ── Keyframe animations ─────────────────────────────────────────── */
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(14px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes fadeIn {
    from { opacity: 0; }
    to   { opacity: 1; }
}
@keyframes slideDown {
    from { opacity: 0; transform: translateY(-8px); }
    to   { opacity: 1; transform: translateY(0); }
}
@keyframes popIn {
    0%   { opacity: 0; transform: scale(.92); }
    60%  { transform: scale(1.02); }
    100% { opacity: 1; transform: scale(1); }
}
@keyframes shimmer {
    0%   { background-position: -400px 0; }
    100% { background-position: 400px 0; }
}

.anim-up   { animation: fadeUp   .35s cubic-bezier(.4,0,.2,1) both; }
.anim-in   { animation: fadeIn   .3s  ease both; }
.anim-down { animation: slideDown .3s ease both; }
.anim-pop  { animation: popIn    .4s  cubic-bezier(.34,1.4,.64,1) both; }
.d0  { animation-delay: 0s; }
.d1  { animation-delay: .06s; }
.d2  { animation-delay: .12s; }
.d3  { animation-delay: .18s; }
.d4  { animation-delay: .24s; }
.d5  { animation-delay: .30s; }
.d6  { animation-delay: .36s; }

/* ── Sidebar internals ───────────────────────────────────────────── */
.sb-head {
    height: 64px;
    display: flex;
    align-items: center;
    padding: 0 16px;
    border-bottom: 1px solid var(--border);
    gap: 8px;
}
.sb-logo-mark {
    width: 32px; height: 32px;
    border-radius: 6px;
    background: #1e8e3e;
    display: flex; align-items: center; justify-content: center;
    font-size: .9rem; font-weight: 700; color: #fff;
    flex-shrink: 0;
}
.sb-wordmark {
    font-size: 1.0625rem;
    font-weight: 600;
    color: var(--t2);
    letter-spacing: -.01em;
}
.sb-wordmark span { color: #1e8e3e; }
.sb-divider { height: 1px; background: var(--border); margin: 8px 0; }
.sb-label {
    font-size: .6875rem;
    font-weight: 600;
    color: var(--t3);
    text-transform: uppercase;
    letter-spacing: .08em;
    padding: 12px 16px 4px;
}
.sb-foot {
    padding: 12px 16px;
    font-size: .7rem;
    color: var(--t3);
    border-top: 1px solid var(--border);
    margin-top: 8px;
    line-height: 1.6;
}

/* ── Top bar ─────────────────────────────────────────────────────── */
.topbar {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    height: 64px;
    display: flex;
    align-items: center;
    padding: 0 24px;
    gap: 12px;
    position: sticky;
    top: 0;
    z-index: 500;
    animation: slideDown .3s ease both;
}
.topbar-brand {
    display: flex;
    align-items: center;
    gap: 8px;
}
.topbar-logo-mark {
    width: 36px; height: 36px;
    border-radius: 8px;
    background: #1e8e3e;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem; font-weight: 700; color: #fff;
}
.topbar-name {
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--t2);
    letter-spacing: -.01em;
}
.topbar-name span { color: #1e8e3e; }
.topbar-space { flex: 1; }
.topbar-avatar {
    width: 36px; height: 36px;
    border-radius: 50%;
    background: var(--blue);
    color: #fff;
    font-size: .875rem;
    font-weight: 600;
    display: flex; align-items: center; justify-content: center;
    cursor: pointer;
    flex-shrink: 0;
    transition: box-shadow .15s;
}
.topbar-avatar:hover { box-shadow: 0 0 0 3px rgba(26,115,232,.2); }

/* ── Page wrapper ─────────────────────────────────────────────────── */
.page {
    padding: 28px 32px 80px;
    max-width: 1400px;
    margin: 0 auto;
    width: 100%;
}

/* ── Welcome heading ─────────────────────────────────────────────── */
.page-title {
    font-size: 1.625rem;
    font-weight: 700;
    color: var(--t1);
    letter-spacing: -.02em;
    margin: 0 0 20px;
    animation: fadeUp .35s ease both;
}

/* ── Stat strip ──────────────────────────────────────────────────── */
.stats {
    background: var(--surface);
    border-radius: 12px;
    box-shadow: var(--sh1);
    display: flex;
    margin-bottom: 28px;
    overflow: hidden;
    animation: fadeUp .35s ease .06s both;
}
.stat {
    flex: 1;
    padding: 20px 16px;
    text-align: center;
    border-right: 1px solid var(--border);
    transition: background .15s;
}
.stat:last-child { border-right: none; }
.stat:hover { background: #fafafa; }
.stat-n {
    font-size: 1.875rem;
    font-weight: 700;
    letter-spacing: -.03em;
    line-height: 1;
    margin-bottom: 4px;
}
.stat-l {
    font-size: .6875rem;
    font-weight: 600;
    color: var(--t3);
    text-transform: uppercase;
    letter-spacing: .07em;
}

/* ── Section eyebrow ─────────────────────────────────────────────── */
.eyebrow {
    font-size: .6875rem;
    font-weight: 600;
    color: var(--t3);
    text-transform: uppercase;
    letter-spacing: .08em;
    margin: 0 0 12px;
}

/* ── Class card (home) ───────────────────────────────────────────── */
.ccard {
    background: var(--surface);
    border-radius: 12px;
    box-shadow: var(--sh1);
    overflow: hidden;
    transition: box-shadow .2s ease, transform .2s ease;
    cursor: pointer;
    margin-bottom: 0;
    display: flex;
    flex-direction: column;
    height: 100%;
}
.ccard:hover { box-shadow: var(--sh2); transform: translateY(-2px); }
.ccard-head {
    height: 100px;
    position: relative;
    padding: 14px 16px;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    overflow: hidden;
}
.ccard-head::after {
    content: '';
    position: absolute; inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,.3) 0%, transparent 55%);
}
.ccard-dots {
    position: absolute; inset: 0;
    background-image: radial-gradient(circle, rgba(255,255,255,.14) 1.5px, transparent 1.5px);
    background-size: 20px 20px;
}
.ccard-ico {
    position: absolute;
    top: 12px; right: 14px;
    font-size: 1.9rem;
    z-index: 1;
    transition: transform .2s ease;
    line-height: 1;
}
.ccard:hover .ccard-ico { transform: scale(1.1) rotate(-5deg); }
.ccard-title {
    font-size: 1rem;
    font-weight: 700;
    color: #fff;
    letter-spacing: -.02em;
    position: relative; z-index: 1;
    white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
}
.ccard-section {
    font-size: .7rem;
    color: rgba(255,255,255,.85);
    position: relative; z-index: 1;
    margin-top: 2px;
}
.ccard-body { padding: 12px 14px 10px; flex: 1; }
.ccard-teacher { font-size: .75rem; color: var(--t2); margin-bottom: 6px; }
.ccard-foot {
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 6px 14px 10px;
    border-top: 1px solid #f1f3f4;
}
.ccard-count { font-size: .7rem; color: var(--t3); }

/* ── Chips ───────────────────────────────────────────────────────── */
.chip {
    display: inline-flex;
    align-items: center;
    gap: 4px;
    font-size: .6875rem;
    font-weight: 600;
    padding: 3px 10px;
    border-radius: 100px;
    letter-spacing: .01em;
}
.chip-blue   { background: #e8f0fe; color: #1a73e8; }
.chip-green  { background: #e6f4ea; color: #1e8e3e; }
.chip-gray   { background: #f1f3f4; color: #5f6368; }
.chip-red    { background: #fce8e6; color: #d93025; }
.chip-yellow { background: #fef7e0; color: #b06000; }

/* ── Stream banner ───────────────────────────────────────────────── */
.stream-banner {
    border-radius: 12px;
    overflow: hidden;
    height: 200px;
    position: relative;
    display: flex;
    flex-direction: column;
    justify-content: flex-end;
    padding: 24px 28px;
    animation: fadeIn .35s ease both;
}
.stream-banner::before {
    content: '';
    position: absolute; inset: 0;
    background: linear-gradient(to top, rgba(0,0,0,.5) 0%, transparent 60%);
}
.stream-banner-dots {
    position: absolute; inset: 0;
    background-image: radial-gradient(circle, rgba(255,255,255,.1) 1.5px, transparent 1.5px);
    background-size: 22px 22px;
}
.stream-title {
    font-size: 1.75rem;
    font-weight: 700;
    color: #fff;
    letter-spacing: -.03em;
    position: relative; z-index: 1;
    line-height: 1.2;
}
.stream-sub {
    font-size: .875rem;
    color: rgba(255,255,255,.85);
    position: relative; z-index: 1;
    margin-top: 4px;
}

/* ── Tab bar ─────────────────────────────────────────────────────── */
.tabs {
    background: var(--surface);
    border-bottom: 1px solid var(--border);
    display: flex;
    margin-bottom: 24px;
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}
.tab {
    font-size: .875rem;
    font-weight: 500;
    color: var(--t2);
    padding: 14px 20px;
    border-bottom: 3px solid transparent;
    cursor: pointer;
    white-space: nowrap;
    transition: color .15s, border-color .15s, background .15s;
    letter-spacing: -.005em;
}
.tab.active { color: var(--blue); border-bottom-color: var(--blue); }
.tab:hover:not(.active) { background: #f8f9fa; color: var(--t1); }

/* ── Lesson material card ────────────────────────────────────────── */
.lesson-card {
    background: var(--surface);
    border-radius: 10px;
    box-shadow: var(--sh1);
    margin-bottom: 12px;
    overflow: hidden;
    transition: box-shadow .2s ease;
    animation: fadeUp .35s ease both;
}
.lesson-card:hover { box-shadow: var(--sh2); }
.lc-head {
    display: flex;
    align-items: center;
    padding: 14px 16px 12px;
    gap: 12px;
    border-bottom: 1px solid #f1f3f4;
}
.lc-ico {
    width: 40px; height: 40px;
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.15rem;
    flex-shrink: 0;
    transition: transform .2s ease;
}
.lesson-card:hover .lc-ico { transform: scale(1.08); }
.lc-title {
    font-size: .9375rem;
    font-weight: 600;
    color: var(--t1);
    letter-spacing: -.01em;
}
.lc-sub {
    font-size: .75rem;
    color: var(--t3);
    margin-top: 1px;
}
.lc-body {
    padding: 14px 16px 16px;
}
.lc-body p {
    font-size: .875rem !important;
    color: var(--t2) !important;
    line-height: 1.8 !important;
    margin: 0 !important;
}

/* ── Quiz panel ──────────────────────────────────────────────────── */
.quiz-panel {
    background: var(--surface);
    border-radius: 10px;
    box-shadow: var(--sh1);
    overflow: hidden;
    animation: fadeUp .35s ease .1s both;
}
.quiz-panel-head {
    display: flex;
    align-items: center;
    padding: 16px 18px;
    gap: 14px;
    border-bottom: 1px solid #f1f3f4;
}
.quiz-panel-ico {
    width: 44px; height: 44px;
    border-radius: 50%;
    background: #e8f0fe;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    flex-shrink: 0;
}
.quiz-panel-title {
    font-size: .9375rem;
    font-weight: 600;
    color: var(--t1);
    margin: 0;
    letter-spacing: -.01em;
}
.quiz-panel-sub {
    font-size: .75rem;
    color: var(--t3);
    margin: 2px 0 0;
}
.quiz-panel-body { padding: 16px 18px; }
.q-label {
    font-size: .6875rem;
    font-weight: 600;
    color: var(--t3);
    text-transform: uppercase;
    letter-spacing: .08em;
    margin-bottom: 4px;
}
hr.qdiv {
    border: none;
    border-top: 1px solid #f1f3f4;
    margin: 12px 0;
}

/* ── Result cards ────────────────────────────────────────────────── */
.result-pass {
    background: #e6f4ea;
    border: 1px solid #ceead6;
    border-radius: 10px;
    padding: 20px 22px;
    display: flex;
    align-items: flex-start;
    gap: 18px;
    flex-wrap: wrap;
    margin: 14px 0;
    animation: popIn .4s cubic-bezier(.34,1.4,.64,1) both;
}
.result-fail {
    background: #fce8e6;
    border: 1px solid #f5c6c5;
    border-radius: 10px;
    padding: 20px 22px;
    display: flex;
    align-items: flex-start;
    gap: 18px;
    flex-wrap: wrap;
    margin: 14px 0;
    animation: popIn .4s cubic-bezier(.34,1.4,.64,1) both;
}
.result-score {
    font-size: 3rem;
    font-weight: 800;
    line-height: 1;
    letter-spacing: -.05em;
    flex-shrink: 0;
}
.result-pass .result-score { color: #1e8e3e; }
.result-fail .result-score { color: #d93025; }
.result-badge {
    font-size: .6875rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .07em;
    margin-top: 4px;
}
.result-pass .result-badge { color: #1e8e3e; }
.result-fail .result-badge { color: #d93025; }
.result-msg {
    font-size: .875rem;
    color: #3c4043;
    line-height: 1.7;
}
.result-msg strong { color: var(--t1); }

/* ── Grades table ────────────────────────────────────────────────── */
.gtable {
    background: var(--surface);
    border-radius: 12px;
    box-shadow: var(--sh1);
    width: 100%;
    border-collapse: collapse;
    overflow: hidden;
    animation: fadeUp .35s ease .1s both;
}
.gtable th {
    background: #f8f9fa;
    padding: 10px 16px;
    font-size: .6875rem;
    font-weight: 600;
    color: var(--t3);
    text-transform: uppercase;
    letter-spacing: .08em;
    text-align: left;
    border-bottom: 1px solid var(--border);
}
.gtable td {
    padding: 13px 16px;
    border-bottom: 1px solid #f1f3f4;
    font-size: .875rem;
    color: var(--t1);
    vertical-align: middle;
}
.gtable tr:last-child td { border-bottom: none; }
.gtable tr:hover td { background: #f8f9fa; }
.gmono { font-weight: 600; font-size: .875rem; }

/* ── Mobile ──────────────────────────────────────────────────────── */
@media (max-width: 768px) {
    .page { padding: 16px 12px 72px; }
    .topbar { padding: 0 12px; }
    .topbar-name { font-size: .9375rem; }
    .stats { flex-wrap: wrap; }
    .stat { min-width: 130px; border-right: none; border-bottom: 1px solid var(--border); }
    .stat:last-child { border-bottom: none; }
    .stat-n { font-size: 1.5rem; }
    .stream-banner { height: 160px; border-radius: 8px; }
    .stream-title { font-size: 1.35rem; }
    .page-title { font-size: 1.35rem; }
    .gtable { display: block; overflow-x: auto; }
}
@media (max-width: 480px) {
    .page { padding: 12px 10px 72px; }
    .topbar-name { display: none; }
    .stream-title { font-size: 1.2rem; }
    .tabs { gap: 0; }
    .tab { padding: 12px 14px; font-size: .8125rem; }
}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-head">
        <div class="sb-logo-mark">D</div>
        <div class="sb-wordmark">Danilo <span>Classroom</span></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div style="height:6px"></div>', unsafe_allow_html=True)
    st.button("🏠  Home",    on_click=nav, args=("home",),   use_container_width=True)
    st.button("📊  Grades",  on_click=nav, args=("grades",), use_container_width=True)

    st.markdown('<div class="sb-label">Classes</div>', unsafe_allow_html=True)
    for mk, mod in MODS.items():
        locked = mk not in st.session_state.unlocked
        lbl = f"{'🔒  ' if locked else mod['icon']+'  '}{mod['label']}"
        st.button(lbl, on_click=nav, args=(mk,), disabled=locked, use_container_width=True)

    st.markdown('<div style="flex:1"></div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-foot">© 2025 DANILO Classroom<br>All rights reserved.</div>', unsafe_allow_html=True)

# ── Top bar ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
    <div class="topbar-brand">
        <div class="topbar-logo-mark">D</div>
        <div class="topbar-name">Danilo <span>Classroom</span></div>
    </div>
    <div class="topbar-space"></div>
    <div class="topbar-avatar">D</div>
</div>
""", unsafe_allow_html=True)

# ── Page wrapper ──────────────────────────────────────────────────────────────
st.markdown('<div class="page">', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
#  HOME
# ════════════════════════════════════════════════════════════
if st.session_state.view == "home":
    st.markdown('<div class="page-title">Welcome back, Danilo 👋</div>', unsafe_allow_html=True)

    all_m  = ["1","2","3","4"]
    taken  = [st.session_state[f"m{m}_qr"] for m in all_m if st.session_state[f"m{m}_qd"]]
    avg    = (sum(taken)/(len(taken)*5)*100) if taken else 0
    passed = sum(1 for m in all_m if st.session_state[f"m{m}_qd"] and st.session_state[f"m{m}_qr"]>=4)
    unlk   = len(st.session_state.unlocked)

    st.markdown(f"""
    <div class="stats">
        <div class="stat">
            <div class="stat-n" style="color:#1a73e8;">{unlk}/4</div>
            <div class="stat-l">Classes Unlocked</div>
        </div>
        <div class="stat">
            <div class="stat-n" style="color:#1e8e3e;">{passed}/4</div>
            <div class="stat-l">Assessments Passed</div>
        </div>
        <div class="stat">
            <div class="stat-n" style="color:#b06000;">{avg:.0f}%</div>
            <div class="stat-l">Mean Accuracy</div>
        </div>
        <div class="stat">
            <div class="stat-n" style="color:#d93025;">{int(passed/4*100)}%</div>
            <div class="stat-l">Overall Progress</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="eyebrow anim-up d2">Enrolled Classes</div>', unsafe_allow_html=True)

    items = list(MODS.items())
    for row in range(0, len(items), 3):
        cols = st.columns(3, gap="medium")
        for ci, (mk, mod) in enumerate(items[row:row+3]):
            locked = mk not in st.session_state.unlocked
            m = mod["k"]
            done = st.session_state[f"m{m}_qd"] and st.session_state[f"m{m}_qr"] >= 4

            badge = (
                '<span class="chip chip-green">✓ Complete</span>' if done
                else '<span class="chip chip-gray">🔒 Locked</span>' if locked
                else '<span class="chip chip-blue">● Active</span>'
            )
            delay = f"d{min(row*3+ci+1,6)}"

            with cols[ci]:
                st.markdown(f"""
                <div class="ccard anim-up {delay}">
                    <div class="ccard-head" style="background:{mod['hbg']};">
                        <div class="ccard-dots"></div>
                        <div class="ccard-ico">{mod['icon']}</div>
                        <div class="ccard-title">{mod['label']}</div>
                        <div class="ccard-section">{mod['section']}</div>
                    </div>
                    <div class="ccard-body">
                        <div class="ccard-teacher">{mod['teacher']}</div>
                        {badge}
                    </div>
                    <div class="ccard-foot">
                        <span class="ccard-count">{len(mod['quiz'])} questions</span>
                    </div>
                </div>
                """, unsafe_allow_html=True)
                st.button(
                    "Open class →" if not locked else "Locked",
                    key=f"h_{mk}", on_click=nav, args=(mk,),
                    disabled=locked, use_container_width=True,
                )

# ════════════════════════════════════════════════════════════
#  CLASS VIEW
# ════════════════════════════════════════════════════════════
elif st.session_state.view in MODS:
    mk  = st.session_state.view
    mod = MODS[mk]
    m   = mod["k"]
    qd  = mod["quiz"]
    pm  = len(qd) - 1

    st.button("← Back to Home", key=f"back_{mk}", on_click=nav, args=("home",))
    st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)

    # Stream banner
    st.markdown(f"""
    <div class="stream-banner" style="background:{mod['hbg']};">
        <div class="stream-banner-dots"></div>
        <div class="stream-title">{mod['icon']}  {mod['label']}</div>
        <div class="stream-sub">{mod['section']}  ·  {mod['teacher']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs
    st.markdown("""
    <div class="tabs">
        <div class="tab">Stream</div>
        <div class="tab active">Classwork</div>
        <div class="tab">People</div>
    </div>
    """, unsafe_allow_html=True)

    # Two-col layout
    left, right = st.columns([3, 2], gap="large")

    with left:
        st.markdown('<div class="eyebrow">Lesson Material</div>', unsafe_allow_html=True)
        for i, (ico, ibg, itc, title, body) in enumerate(mod["topics"]):
            st.markdown(f"""
            <div class="lesson-card {f'd{i+1}'}">
                <div class="lc-head">
                    <div class="lc-ico" style="background:{ibg};">{ico}</div>
                    <div>
                        <div class="lc-title">{title}</div>
                        <div class="lc-sub">Reading material · {mod['teacher']}</div>
                    </div>
                </div>
                <div class="lc-body"><p>{body}</p></div>
            </div>
            """, unsafe_allow_html=True)

    with right:
        st.markdown('<div class="eyebrow">Assessment</div>', unsafe_allow_html=True)

        sk = f"m{m}_qs"
        uk = f"m{m}_qd"
        ck = f"m{m}_qr"

        st.markdown(f"""
        <div class="quiz-panel">
            <div class="quiz-panel-head">
                <div class="quiz-panel-ico">📋</div>
                <div>
                    <p class="quiz-panel-title">Formative Assessment</p>
                    <p class="quiz-panel-sub">{len(qd)} questions · Pass: {pm}/{len(qd)} · Unlimited retries</p>
                </div>
            </div>
            <div class="quiz-panel-body">
        """, unsafe_allow_html=True)

        if not st.session_state[sk]:
            st.markdown('</div></div>', unsafe_allow_html=True)
            st.button("▶  Start Assessment", key=f"st_{mk}")
            if st.session_state.get(f"st_{mk}"):
                st.session_state[sk] = True
                st.rerun()
        else:
            st.markdown('</div></div>', unsafe_allow_html=True)
            with st.form(key=f"{mk}_form", clear_on_submit=False):
                answers = []
                for i, q in enumerate(qd):
                    st.markdown(f'<div class="q-label">Question {i+1} of {len(qd)}</div>', unsafe_allow_html=True)
                    st.markdown(f"**{q['q']}**")
                    a = st.radio("", q["o"], key=f"{mk}_q{i}", label_visibility="collapsed", index=None)
                    answers.append(a)
                    if i < len(qd) - 1:
                        st.markdown('<hr class="qdiv">', unsafe_allow_html=True)
                st.markdown('<div style="height:6px"></div>', unsafe_allow_html=True)
                submitted = st.form_submit_button("Submit Assessment")

            if submitted:
                if None in answers:
                    st.error("⚠️ Please answer all questions before submitting.")
                else:
                    score = sum(1 for i, q in enumerate(qd) if answers[i] == q["a"])
                    st.session_state[ck] = score
                    st.session_state[uk] = True

            if st.session_state[uk]:
                score  = st.session_state[ck]
                passed = score >= pm
                pct    = int(score / len(qd) * 100)

                if passed:
                    st.markdown(f"""
                    <div class="result-pass">
                        <div>
                            <div class="result-score">{score}/{len(qd)}</div>
                            <div class="result-badge">✓ Passed</div>
                        </div>
                        <div class="result-msg">
                            <strong>Excellent work!</strong> You scored {pct}% and have demonstrated solid mastery of this topic.<br>
                            <span style="color:#1e8e3e;font-weight:600;margin-top:6px;display:block;">{mod['umsg']}</span>
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    nxt = mod.get("next")
                    if nxt and nxt not in st.session_state.unlocked:
                        st.session_state.unlocked.append(nxt)
                else:
                    st.markdown(f"""
                    <div class="result-fail">
                        <div>
                            <div class="result-score">{score}/{len(qd)}</div>
                            <div class="result-badge">✗ Below Pass</div>
                        </div>
                        <div class="result-msg">
                            <strong>Keep going!</strong> You scored {pct}%. Review the lesson cards and try again. You need {pm}/{len(qd)} to pass.
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    if st.button("🔄  Retry Assessment", key=f"rt_{mk}"):
                        st.session_state[uk] = False
                        st.rerun()

# ════════════════════════════════════════════════════════════
#  GRADES
# ════════════════════════════════════════════════════════════
elif st.session_state.view == "grades":
    st.button("← Back to Home", key="back_g", on_click=nav, args=("home",))
    st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)
    st.markdown('<div class="page-title anim-up">Grades</div>', unsafe_allow_html=True)

    all_m  = ["1","2","3","4"]
    subs   = {m: st.session_state[f"m{m}_qd"] for m in all_m}
    scores = {m: st.session_state[f"m{m}_qr"] for m in all_m}
    taken  = [scores[m] for m in all_m if subs[m]]
    avg    = (sum(taken)/(len(taken)*5)*100) if taken else 0
    comp   = sum(1 for m in all_m if subs[m] and scores[m]>=4)
    unlk   = len(st.session_state.unlocked)

    st.markdown(f"""
    <div class="stats anim-up d1">
        <div class="stat">
            <div class="stat-n" style="color:#1a73e8;">{unlk}/4</div>
            <div class="stat-l">Unlocked</div>
        </div>
        <div class="stat">
            <div class="stat-n" style="color:#1e8e3e;">{avg:.0f}%</div>
            <div class="stat-l">Mean Accuracy</div>
        </div>
        <div class="stat">
            <div class="stat-n" style="color:#b06000;">{comp}/4</div>
            <div class="stat-l">Passed</div>
        </div>
        <div class="stat">
            <div class="stat-n" style="color:#d93025;">{int(comp/4*100)}%</div>
            <div class="stat-l">Progress</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="eyebrow anim-up d2">Gradebook</div>', unsafe_allow_html=True)

    rows = ""
    for mk, mod in MODS.items():
        m     = mod["k"]
        total = len(mod["quiz"])
        locked = mk not in st.session_state.unlocked
        sub    = subs[m]; sc = scores[m]; done = sub and sc >= 4

        if locked:
            sh = '<span class="chip chip-gray">🔒 Locked</span>'
            sd = gd = '<span style="color:#bdc1c6;">—</span>'
        elif done:
            sh = '<span class="chip chip-green">✓ Passed</span>'
            sd = f'<span class="gmono" style="color:#1e8e3e;">{sc}/{total}</span>'
            gd = f'<span class="gmono" style="color:#1e8e3e;">{int(sc/total*100)}%</span>'
        elif sub:
            sh = '<span class="chip chip-red">✗ Below Pass</span>'
            sd = f'<span class="gmono" style="color:#d93025;">{sc}/{total}</span>'
            gd = f'<span class="gmono" style="color:#d93025;">{int(sc/total*100)}%</span>'
        else:
            sh = '<span class="chip chip-yellow">○ Not Attempted</span>'
            sd = gd = '<span style="color:#bdc1c6;">—</span>'

        rows += f"""
        <tr>
            <td style="width:34px;font-size:1.1rem;">{mod['icon']}</td>
            <td style="font-weight:600;">{mod['label']}</td>
            <td style="color:#5f6368;font-size:.8rem;">{mod['section']}</td>
            <td style="color:#5f6368;font-size:.8rem;">{mod['teacher']}</td>
            <td>{sh}</td>
            <td>{sd}</td>
            <td>{gd}</td>
        </tr>"""

    st.markdown(f"""
    <table class="gtable">
        <thead>
            <tr>
                <th></th>
                <th>Class</th>
                <th>Topic</th>
                <th>Teacher</th>
                <th>Status</th>
                <th>Score</th>
                <th>Grade</th>
            </tr>
        </thead>
        <tbody>{rows}</tbody>
    </table>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
