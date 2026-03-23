import streamlit as st, os

os.makedirs(".streamlit", exist_ok=True)
with open(".streamlit/config.toml","w") as f:
    f.write('[theme]\nbase="light"\nbackgroundColor="#f5f5f7"\nsecondaryBackgroundColor="#ffffff"\ntextColor="#1d1d1f"\nfont="sans serif"\n')

st.set_page_config(page_title="Classroom", page_icon="📚",
                   layout="wide", initial_sidebar_state="expanded")

# ─────────────────────────────────────────────────────────────────────
#  DATA
# ─────────────────────────────────────────────────────────────────────
QUIZ = {
    "1":[
        {"q":"What do we call the time and place in which a story unfolds?","o":["The Plot","The Characters","The Setting","The Theme"],"a":"The Setting"},
        {"q":"Where is the main idea of a paragraph most commonly found?","o":["In a footnote","At the very end","In the topic sentence","In the conclusion"],"a":"In the topic sentence"},
        {"q":"What are surrounding clues that help decode an unfamiliar word called?","o":["Context clues","Phonics hints","Syntax rules","Story beats"],"a":"Context clues"},
        {"q":"Who are the people or creatures that participate in a story's events?","o":["The Authors","The Narrators","The Characters","The Editors"],"a":"The Characters"},
        {"q":"What is the term for the sequence of events driving a story from start to finish?","o":["The Plot","The Cover","The Vocabulary","The Epilogue"],"a":"The Plot"},
    ],
    "2":[
        {"q":"What does reading fluency primarily involve?","o":["Reading as fast as possible","Reading accurately, smoothly, and with natural expression","Memorising every vocabulary word","Subvocalising every syllable"],"a":"Reading accurately, smoothly, and with natural expression"},
        {"q":"Which technique involves reading the same passage multiple times until effortless?","o":["Skimming","Scanning","Repeated reading","Speed reading"],"a":"Repeated reading"},
        {"q":"What is a sight word?","o":["A word with silent letters","A word instantly recognised without sounding it out","A very long compound word","A word borrowed from Latin"],"a":"A word instantly recognised without sounding it out"},
        {"q":"What does reading with expression mean?","o":["Speaking as loudly as possible","Changing your voice to match the emotion and meaning of the text","Reading every word at the exact same pace","Pausing three seconds after each sentence"],"a":"Changing your voice to match the emotion and meaning of the text"},
        {"q":"Which habit best strengthens reading comprehension over time?","o":["Reading only one genre","Asking thoughtful questions before, during, and after reading","Skipping all difficult words","Reading only very short passages"],"a":"Asking thoughtful questions before, during, and after reading"},
    ],
    "3":[
        {"q":"What is the sum of 145 and 278?","o":["423","413","433","323"],"a":"423"},
        {"q":"What is the perimeter of a square with one side of 9 units?","o":["18 units","27 units","36 units","81 units"],"a":"36 units"},
        {"q":"In the fraction 3/4, what does the denominator 4 represent?","o":["Parts we have","Total equal parts in the whole","The product","The quotient"],"a":"Total equal parts in the whole"},
        {"q":"What is the product of 15 × 8?","o":["100","110","120","130"],"a":"120"},
        {"q":"What is the correct term for a flat, closed shape with straight sides?","o":["Circle","Sphere","Polygon","Cylinder"],"a":"Polygon"},
    ],
    "4":[
        {"q":"What transforms liquid water into invisible water vapour?","o":["Condensation","Evaporation","Precipitation","Sublimation"],"a":"Evaporation"},
        {"q":"Which energy source drives the entire water cycle?","o":["The Moon","Geothermal heat","The Sun","Ocean currents"],"a":"The Sun"},
        {"q":"What forms when rising water vapour cools and condenses?","o":["Raindrops","Clouds","Underground rivers","Aquifers"],"a":"Clouds"},
        {"q":"Which is an example of precipitation?","o":["A puddle drying","Snow falling","Steam rising","Ice melting in a glass"],"a":"Snow falling"},
        {"q":"What is an underground layer of permeable rock holding freshwater called?","o":["A cloud layer","An aquifer","The stratosphere","A water valve"],"a":"An aquifer"},
    ],
}

COURSES = {
    "c1":{"id":"1","title":"Reading","sub":"Understanding Stories and Words","teacher":"Ms. Santos","grade":"Grade 4","color":"#0071e3","next":"c2",
          "lessons":[
            ("1.0 — Elements of a Story",
             "Every story is built from three foundational elements. The <b>setting</b> establishes not just a physical location but an entire atmosphere — the rain-slicked streets of a noir city feel completely different from a sun-drenched countryside, even if the same events occur in both. The <b>characters</b> are the human (or non-human) engines of every narrative. What they want, fear, and believe shapes every decision and every conflict. Great characters feel so real they seem to exist beyond the page. The <b>plot</b> is the architecture of the story — the sequence of events that transforms an opening situation into a changed world. A strong plot is not just 'things that happen'; it is causally connected events that feel both surprising and inevitable in retrospect. Understanding these three elements transforms you from a passive reader into an active analyst who can engage deeply with any text."),
            ("1.1 — Finding the Main Idea",
             "The <b>main idea</b> is the single sentence that captures what an entire paragraph is really about. Authors plant this seed in the <b>topic sentence</b> — almost always the first sentence — and then spend the rest of the paragraph watering it with supporting details: examples, statistics, anecdotes, and explanations. A skilled reader develops a mental habit: after every paragraph, pause and ask, 'What is the one thing the author most wants me to take away?' If you can answer that question in your own words without looking back, you have understood the main idea. This habit, practised consistently across thousands of paragraphs, becomes automatic — and it is the single most powerful tool for navigating complex texts in every academic subject."),
            ("1.2 — Context Clues",
             "When you encounter an unfamiliar word, your first instinct might be to stop and look it up. Skilled readers instead reach for <b>context clues</b> — the surrounding text. <b>Definition clues</b> are the most generous: the author defines the word directly ('osmosis, which is the movement of water across a membrane'). <b>Synonym clues</b> place a familiar near-equivalent close by. <b>Antonym clues</b> use contrast markers like 'unlike' or 'however' to reveal meaning through opposition. <b>Inference clues</b> require the reader to synthesise several surrounding ideas. The goal is not to guess randomly — it is to triangulate meaning from evidence, exactly the way a detective reasons from clues to a conclusion."),
            ("1.3 — Vocabulary Building",
             "Vocabulary size is the strongest single predictor of reading comprehension — stronger even than general intelligence. Words cluster in networks: learning <b>port</b> (Latin for 'carry') instantly illuminates transport, import, export, portable, and portfolio. A <b>vocabulary journal</b> — recording new words, their etymology, and an original example sentence — leverages the generation effect: you remember far better what you produce than what you passively read. <b>Spaced repetition</b> — reviewing new words at intervals of 1, 3, 7, and 14 days — moves words from working memory into long-term storage with remarkable efficiency. Aim for at least five genuine encounters with a word before declaring it fully 'learned.'"),
          ]},
    "c2":{"id":"2","title":"Reading Fluency","sub":"Speed, Expression & Comprehension","teacher":"Ms. Santos","grade":"Grade 4","color":"#5856d6","next":"c3",
          "lessons":[
            ("2.0 — What Is Fluency?",
             "Reading fluency sits at the intersection of <b>accuracy</b>, <b>automaticity</b>, and <b>prosody</b>. Accuracy means decoding words correctly. Automaticity means doing so without conscious effort — recognising a word the way you recognise a familiar face, instantly and effortlessly. Prosody is the musical element: the rhythm, pacing, and expressive intonation that transforms a series of words into something that communicates emotion and nuance. When all three operate together, the reader's cognitive resources are freed from the mechanical labour of decoding and become available for the higher-order work of comprehension, inference, and evaluation. Fluency is not a luxury skill; it is the infrastructure upon which all advanced reading is built."),
            ("2.1 — Repeated Reading",
             "<b>Repeated reading</b> works because fluency is a performance skill, and performance skills improve with rehearsal. Choose a passage of 100–200 words at or slightly above your comfortable reading level. Read it aloud once, timing yourself and noting errors. Read it again, focusing on smoothness. Read it a third time, adding natural expression. Research consistently shows that three to five readings of the same passage improve both fluency and comprehension — and crucially, the gains transfer to new, unseen passages. Pair this with <b>echo reading</b> (listening to a fluent model, then reproducing the same passage) and <b>choral reading</b> (reading aloud in unison with others) for maximum effect."),
            ("2.2 — Sight Words",
             "The 300 most common words in English account for approximately 65% of all running text. When a reader must consciously decode these words — sounding out 'the' or 'because' letter by letter — reading grinds to a near-halt. <b>Sight word automaticity</b> is achieved through a process called <b>orthographic mapping</b>: the brain permanently bonds a word's pronunciation, spelling, and meaning into a single, instantly retrievable unit. Flashcard practice, word sorting, word hunts in real texts, and — above all — massive amounts of independent reading all contribute to this mapping. Once the 300 common words are automatic, the cognitive overhead of reading drops dramatically, and comprehension can operate at full capacity."),
            ("2.3 — Comprehension Strategies",
             "Active readers do not wait for understanding to arrive — they create it through deliberate strategies. <b>Predicting</b> forces the brain to engage forward-looking reasoning. <b>Questioning</b> — 'Why did this happen? What does this mean? Do I agree?' — turns reading into a dialogue rather than a monologue. <b>Visualising</b> recruits the brain's spatial and visual systems to build a mental model of the text. <b>Clarifying</b> catches moments of confusion before they compound. <b>Summarising</b> consolidates understanding by requiring the reader to reconstruct the text's structure in their own mind. Research from the National Reading Panel identifies these five strategies as having the strongest evidence base of any comprehension interventions."),
          ]},
    "c3":{"id":"3","title":"Mathematics","sub":"Foundational Operations & Geometry","teacher":"Mr. Reyes","grade":"Grade 4","color":"#34c759","next":"c4",
          "lessons":[
            ("3.0 — The Four Operations",
             "The four arithmetic operations are the grammar of mathematics — the rules that determine how numbers relate and transform. <b>Addition</b> is the most primitive: it models the joining of quantities. <b>Subtraction</b> is its inverse, modelling separation and difference. <b>Multiplication</b> is the profound shortcut that transforms arithmetic from laborious repeated addition into something elegant: 9 × 7 expresses in two symbols what '9 + 9 + 9 + 9 + 9 + 9 + 9' expresses in seventeen. <b>Division</b> is multiplication's mirror, partitioning a whole into equal parts. Fluency in all four operations — not just rote recall, but genuine conceptual understanding — is the prerequisite for every area of mathematics that follows: algebra, geometry, statistics, and calculus all assume it."),
            ("3.1 — Fractions",
             "A fraction encodes a relationship — specifically, the relationship of a part to a whole. The <b>denominator</b> (bottom number) defines the size of the unit: in ¾, the whole has been divided into four equal parts, so each part is one-quarter the size of the whole. The <b>numerator</b> (top number) counts how many of those units we have. This apparently simple structure contains enormous depth. It explains why you cannot add fractions with different denominators without first converting them (you would be adding apples to oranges). It explains why multiplying two fractions produces a smaller result. It underpins the concept of ratio, rate, proportion, probability, and every percentage calculation you will ever perform. The denominator can never be zero because 'dividing into zero parts' is a logical impossibility with no coherent definition."),
            ("3.2 — Shapes & Measurement",
             "Geometry begins with the observation that shapes have measurable properties. The <b>perimeter</b> of any polygon is simply the sum of its side lengths — it answers the question 'how far around?' A rectangle's perimeter is 2(l + w) because it has two pairs of equal sides. The <b>area</b> answers 'how much surface?' For a rectangle, area = l × w, which can be understood visually as the number of unit squares that tile the interior. These two measures capture different aspects of a shape: a very thin, elongated rectangle can have the same perimeter as a square but a fraction of the square's area. Understanding the distinction between perimeter and area — and when each is relevant — is essential for every practical application of geometry, from flooring to fencing to map reading."),
          ]},
    "c4":{"id":"4","title":"Natural Sciences","sub":"The Hydrological Cycle","teacher":"Ms. Cruz","grade":"Grade 4","color":"#ff9500","next":None,
          "lessons":[
            ("4.0 — The Water Cycle",
             "The <b>hydrological cycle</b> is Earth's perpetual water redistribution system, driven primarily by solar energy and shaped by gravity. It has no beginning and no end — water that evaporated from an ancient ocean may have fallen as rain on a Roman aqueduct, been absorbed by a medieval oak, transpired back into the atmosphere, frozen into an alpine glacier, melted into a river, and eventually arrived at your tap. The total volume of water on Earth has been essentially constant for four billion years; what changes is its form and location. This cycle is not merely a curiosity of physical geography — it regulates global temperature, drives weather systems, replenishes freshwater supplies, and transports enormous quantities of dissolved minerals and nutrients across the planet's surface."),
            ("4.1 — Evaporation & Condensation",
             "<b>Evaporation</b> is the energy-absorbing phase transition by which liquid water at Earth's surface — primarily oceans, which cover 71% of the planet — is converted into water vapour by solar radiation. At the molecular level, the most energetic water molecules escape the liquid surface and become part of the gas phase. The oceans contribute roughly 86% of atmospheric water vapour; land evaporation and plant <b>transpiration</b> (collectively 'evapotranspiration') contribute the remainder. As vapour rises, it cools. When temperature drops below the <b>dew point</b>, vapour undergoes <b>condensation</b> — the energy-releasing phase transition back to liquid. Condensation requires a surface: microscopic particles of dust, sea salt, pollen, and even combustion products serve as <b>condensation nuclei</b>, around which droplets form and clouds develop."),
            ("4.2 — Precipitation & Collection",
             "<b>Precipitation</b> occurs when cloud droplets grow — through collision, coalescence, and the Bergeron process — until they are too heavy for updrafts to sustain. They fall as <b>rain</b> (above-freezing atmosphere), <b>snow</b> (below-freezing from cloud to ground), <b:>sleet</b> (rain refreezing en route), or <b>hail</b> (ice pellets repeatedly cycled upward by thunderstorm updrafts). On reaching the surface, water partitions among several pathways: direct <b>runoff</b> into rivers and oceans; <b>infiltration</b> into soil, where it may be taken up by roots, evaporate back from the surface, or percolate deeper to recharge <b>aquifers</b>. Aquifers are subsurface formations of permeable rock, sediment, or soil saturated with groundwater — the source of roughly 30% of global freshwater and the lifeline of vast agricultural regions."),
          ]},
}

# ─────────────────────────────────────────────────────────────────────
#  SESSION STATE
# ─────────────────────────────────────────────────────────────────────
if "view"     not in st.session_state: st.session_state.view     = "home"
if "unlocked" not in st.session_state: st.session_state.unlocked = {"c1"}
for c in COURSES:
    for k,d in [("started",False),("done",False),("score",0)]:
        if f"{c}_{k}" not in st.session_state:
            st.session_state[f"{c}_{k}"] = d

def go(v): st.session_state.view = v

# ─────────────────────────────────────────────────────────────────────
#  CSS  — Apple-minimal design system
# ─────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* ── tokens ── */
:root{
  --bg:        #f5f5f7;
  --card:      #ffffff;
  --border:    rgba(0,0,0,0.09);
  --ink:       #1d1d1f;
  --ink2:      #6e6e73;
  --ink3:      #aeaeb2;
  --blue:      #0071e3;
  --blue2:     #0077ed;
  --s1: 0 1px 4px rgba(0,0,0,.06), 0 2px 12px rgba(0,0,0,.05);
  --s2: 0 4px 24px rgba(0,0,0,.10), 0 1px 4px rgba(0,0,0,.05);
  --s3: 0 12px 40px rgba(0,0,0,.14), 0 2px 8px rgba(0,0,0,.06);
  --r:  12px;
  --rr: 16px;
  --ease: cubic-bezier(.4,0,.2,1);
}

/* ── global reset ── */
*, html, body, [class*="css"]{
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
  -webkit-font-smoothing: antialiased !important;
  box-sizing: border-box;
}
.stApp { background: var(--bg) !important; }
#MainMenu, footer, header { visibility: hidden; }

/* ── kill streamlit layout defaults ── */
.block-container { padding: 0 !important; max-width: 100% !important; }
.main > div { padding: 0 !important; }

/* ── sidebar ── */
section[data-testid="stSidebar"] {
  background: rgba(255,255,255,0.82) !important;
  backdrop-filter: blur(28px) saturate(1.6) !important;
  -webkit-backdrop-filter: blur(28px) saturate(1.6) !important;
  border-right: 1px solid var(--border) !important;
  width: 248px !important; min-width: 248px !important;
}
section[data-testid="stSidebar"] > div {
  width: 248px !important; padding: 0 !important;
}

/* always-visible hamburger when sidebar is closed */
[data-testid="collapsedControl"] {
  visibility: visible !important; display: flex !important;
  opacity: 1 !important; position: fixed !important;
  top: 14px !important; left: 14px !important;
  z-index: 9999 !important; width: 38px !important; height: 38px !important;
  background: rgba(255,255,255,.88) !important;
  backdrop-filter: blur(16px) !important;
  border-radius: 50% !important; border: none !important;
  box-shadow: 0 2px 8px rgba(0,0,0,.12) !important;
  cursor: pointer !important; align-items: center !important;
  justify-content: center !important;
  transition: background .15s, box-shadow .15s !important;
}
[data-testid="collapsedControl"]:hover {
  background: #fff !important; box-shadow: 0 4px 16px rgba(0,0,0,.16) !important;
}
[data-testid="collapsedControl"] svg {
  width: 18px !important; height: 18px !important; color: #3c3c3e !important;
}

/* ── all Streamlit buttons → sidebar pill links ── */
div[data-testid="stButton"] > button {
  font-family: 'Inter', sans-serif !important;
  font-size: .875rem !important; font-weight: 500 !important;
  color: var(--ink) !important; background: transparent !important;
  border: none !important; border-radius: var(--r) !important;
  padding: 0 14px !important; height: 44px !important;
  text-align: left !important; width: 100% !important;
  letter-spacing: -.01em !important; cursor: pointer !important;
  transition: background .15s var(--ease), color .15s var(--ease) !important;
  display: flex !important; align-items: center !important;
}
div[data-testid="stButton"] > button:hover {
  background: rgba(0,0,0,.05) !important;
}
div[data-testid="stButton"] > button:active {
  background: rgba(0,0,0,.09) !important;
}

/* form submit / primary actions */
div[data-testid="stForm"] div[data-testid="stButton"] > button {
  background: var(--blue) !important; color: #fff !important;
  border-radius: 980px !important; padding: 0 22px !important;
  height: 38px !important; font-size: .875rem !important;
  font-weight: 600 !important; width: auto !important;
  text-align: center !important; justify-content: center !important;
  letter-spacing: -.01em !important;
  box-shadow: 0 1px 6px rgba(0,113,227,.25) !important;
  transition: background .15s, transform .12s, box-shadow .15s !important;
}
div[data-testid="stForm"] div[data-testid="stButton"] > button:hover {
  background: var(--blue2) !important;
  box-shadow: 0 4px 16px rgba(0,113,227,.35) !important;
  transform: scale(1.02) !important;
}
div[data-testid="stForm"] div[data-testid="stButton"] > button:active {
  transform: scale(0.98) !important;
}

/* radio groups */
div[role="radiogroup"] {
  background: var(--card) !important; border: 1px solid var(--border) !important;
  border-radius: var(--r) !important; padding: 14px 16px !important;
  margin-bottom: 8px !important; box-shadow: none !important;
  transition: border-color .15s, box-shadow .15s !important;
}
div[role="radiogroup"]:focus-within {
  border-color: var(--blue) !important;
  box-shadow: 0 0 0 3px rgba(0,113,227,.1) !important;
}

/* ── keyframes ── */
@keyframes up {
  from { opacity:0; transform:translateY(16px) }
  to   { opacity:1; transform:translateY(0) }
}
@keyframes dn {
  from { opacity:0; transform:translateY(-10px) }
  to   { opacity:1; transform:translateY(0) }
}
@keyframes fi { from{opacity:0} to{opacity:1} }
@keyframes pop {
  0%   { opacity:0; transform:scale(.9) }
  65%  { transform:scale(1.02) }
  100% { opacity:1; transform:scale(1) }
}
.u0{animation:up .38s var(--ease) both}
.u1{animation:up .38s .06s var(--ease) both}
.u2{animation:up .38s .12s var(--ease) both}
.u3{animation:up .38s .18s var(--ease) both}
.u4{animation:up .38s .24s var(--ease) both}
.u5{animation:up .38s .30s var(--ease) both}
.u6{animation:up .38s .36s var(--ease) both}
.u7{animation:up .38s .42s var(--ease) both}
.pop{animation:pop .42s cubic-bezier(.34,1.4,.64,1) both}
.fi {animation:fi  .3s ease both}

/* ────────────────────────────────────────────────
   SIDEBAR INTERNALS
──────────────────────────────────────────────── */
.sb {
  display:flex; flex-direction:column; height:100vh;
}
.sb-top {
  padding: 20px 16px 14px;
  border-bottom: 1px solid var(--border);
}
.sb-wordmark {
  font-size: 1.125rem; font-weight: 700;
  color: var(--ink); letter-spacing: -.03em; line-height:1;
}
.sb-tagline {
  font-size: .6875rem; font-weight: 500;
  color: var(--ink3); letter-spacing: .04em;
  text-transform: uppercase; margin-top: 2px;
}
.sb-section {
  font-size: .625rem; font-weight: 700;
  color: var(--ink3); text-transform: uppercase;
  letter-spacing: .1em; padding: 16px 14px 4px;
}
.sb-body { flex:1; padding: 6px 6px; overflow-y:auto; }
.sb-footer {
  padding: 12px 16px; font-size: .6875rem;
  color: var(--ink3); border-top: 1px solid var(--border);
  line-height: 1.6;
}

/* ────────────────────────────────────────────────
   TOP NAV BAR
──────────────────────────────────────────────── */
.topnav {
  background: rgba(255,255,255,.82);
  backdrop-filter: blur(28px) saturate(1.6);
  -webkit-backdrop-filter: blur(28px) saturate(1.6);
  border-bottom: 1px solid var(--border);
  position: sticky; top: 0; z-index: 500;
  height: 52px; display: flex; align-items: center;
  padding: 0 28px; gap: 12px;
  animation: dn .3s ease both;
}
.topnav-title {
  font-size: 1rem; font-weight: 700;
  color: var(--ink); letter-spacing: -.02em;
}
.topnav-crumb {
  font-size: .875rem; color: var(--ink3);
  font-weight: 400;
}
.topnav-sep { color: var(--ink3); font-size: .875rem; }
.topnav-pill {
  margin-left: auto;
  width: 32px; height: 32px; border-radius: 50%;
  background: var(--blue); color: #fff;
  font-size: .8125rem; font-weight: 700;
  display: flex; align-items: center; justify-content: center;
  flex-shrink: 0; cursor: pointer;
  box-shadow: 0 2px 8px rgba(0,113,227,.3);
  transition: transform .15s, box-shadow .15s;
}
.topnav-pill:hover {
  transform: scale(1.08);
  box-shadow: 0 4px 14px rgba(0,113,227,.4);
}

/* ────────────────────────────────────────────────
   PAGE WRAPPER
──────────────────────────────────────────────── */
.page {
  padding: 32px 36px 88px;
  max-width: 1360px;
  margin: 0 auto;
}

/* ────────────────────────────────────────────────
   HOME — hero
──────────────────────────────────────────────── */
.hero {
  margin-bottom: 28px;
}
.hero-greeting {
  font-size: 2rem; font-weight: 800;
  color: var(--ink); letter-spacing: -.045em;
  line-height: 1.15; margin-bottom: 6px;
}
.hero-sub {
  font-size: .9375rem; color: var(--ink2);
  font-weight: 400; letter-spacing: -.01em;
}

/* ── stat row ── */
.stats {
  display: grid; grid-template-columns: repeat(4,1fr); gap: 12px;
  margin-bottom: 32px;
}
.stat {
  background: var(--card); border: 1px solid var(--border);
  border-radius: var(--r); padding: 18px 20px;
  box-shadow: var(--s1);
  transition: box-shadow .2s var(--ease), transform .2s var(--ease);
}
.stat:hover { box-shadow: var(--s2); transform: translateY(-1px); }
.stat-n {
  font-size: 1.875rem; font-weight: 800;
  letter-spacing: -.05em; line-height: 1; margin-bottom: 4px;
}
.stat-l {
  font-size: .6875rem; font-weight: 600;
  color: var(--ink3); text-transform: uppercase; letter-spacing: .07em;
}
.stat-bar {
  height: 3px; background: rgba(0,0,0,.06);
  border-radius: 99px; overflow: hidden; margin-top: 14px;
}
.stat-fill {
  height: 100%; border-radius: 99px;
  transition: width 1.2s cubic-bezier(.4,0,.2,1);
}

/* ── section label ── */
.section-label {
  font-size: .6875rem; font-weight: 700;
  color: var(--ink3); text-transform: uppercase;
  letter-spacing: .09em; margin-bottom: 14px;
}

/* ── course cards ── */
.cards-grid {
  display: grid; grid-template-columns: repeat(3,1fr); gap: 14px;
}
.ccard {
  background: var(--card); border-radius: var(--rr);
  border: 1px solid var(--border); box-shadow: var(--s1);
  overflow: hidden; display: flex; flex-direction: column;
  transition: box-shadow .22s var(--ease), transform .22s var(--ease);
  cursor: pointer;
}
.ccard:hover { box-shadow: var(--s3); transform: translateY(-3px); }
.ccard-strip { height: 4px; flex-shrink: 0; }
.ccard-body { padding: 18px 18px 14px; flex: 1; display: flex; flex-direction: column; gap: 6px; }
.ccard-icon { font-size: 1.6rem; line-height: 1; }
.ccard-title {
  font-size: 1rem; font-weight: 700;
  color: var(--ink); letter-spacing: -.02em; margin: 0;
}
.ccard-sub { font-size: .8125rem; color: var(--ink2); line-height: 1.4; }
.ccard-meta {
  font-size: .75rem; color: var(--ink3);
  border-top: 1px solid rgba(0,0,0,.05);
  margin-top: auto; padding-top: 12px;
  display: flex; align-items: center;
  justify-content: space-between;
}
.badge {
  font-size: .6875rem; font-weight: 600; padding: 3px 10px;
  border-radius: 100px; display: inline-flex; align-items: center; gap: 4px;
}
.badge-active { background: rgba(0,113,227,.1); color: var(--blue); }
.badge-done   { background: rgba(52,199,89,.12); color: #248a3d; }
.badge-lock   { background: rgba(0,0,0,.06); color: var(--ink3); }

/* ────────────────────────────────────────────────
   CLASS VIEW
──────────────────────────────────────────────── */
.class-header {
  border-radius: var(--rr); margin-bottom: 24px;
  overflow: hidden; position: relative;
  padding: 32px 32px 28px;
  animation: fi .35s ease both;
}
.class-header::after {
  content: ''; position: absolute; inset: 0;
  background: linear-gradient(135deg,rgba(0,0,0,.18) 0%,transparent 70%);
}
.class-header-content { position: relative; z-index: 1; }
.ch-label {
  font-size: .75rem; font-weight: 600;
  color: rgba(255,255,255,.7); text-transform: uppercase;
  letter-spacing: .1em; margin-bottom: 6px;
}
.ch-title {
  font-size: 1.875rem; font-weight: 800;
  color: #fff; letter-spacing: -.04em; line-height: 1.1;
  margin-bottom: 4px;
}
.ch-sub { font-size: .9375rem; color: rgba(255,255,255,.75); }
.ch-chips {
  display: flex; gap: 8px; flex-wrap: wrap; margin-top: 16px;
}
.wchip {
  background: rgba(255,255,255,.18);
  border: 1px solid rgba(255,255,255,.25);
  backdrop-filter: blur(8px);
  color: #fff; font-size: .75rem; font-weight: 500;
  padding: 4px 12px; border-radius: 100px;
}

/* two-column classwork */
.classwork { display: grid; grid-template-columns: 1fr 360px; gap: 20px; align-items: start; }

/* lesson cards */
.lesson {
  background: var(--card); border: 1px solid var(--border);
  border-radius: var(--r); box-shadow: var(--s1);
  margin-bottom: 10px; overflow: hidden;
  transition: box-shadow .2s var(--ease), border-color .2s var(--ease);
}
.lesson:hover { box-shadow: var(--s2); border-color: rgba(0,0,0,.13); }
.lesson-head {
  display: flex; align-items: center; gap: 12px;
  padding: 14px 16px 12px; border-bottom: 1px solid rgba(0,0,0,.05);
}
.lesson-ico {
  width: 36px; height: 36px; border-radius: 9px;
  display: flex; align-items: center; justify-content: center;
  font-size: 1rem; flex-shrink: 0;
  transition: transform .2s var(--ease);
}
.lesson:hover .lesson-ico { transform: scale(1.08) rotate(-4deg); }
.lesson-title {
  font-size: .9375rem; font-weight: 700;
  color: var(--ink); letter-spacing: -.02em; line-height: 1.2;
}
.lesson-tag { font-size: .6875rem; color: var(--ink3); margin-top: 1px; }
.lesson-body { padding: 14px 16px 16px; }
.lesson-body p {
  font-size: .875rem !important; color: var(--ink2) !important;
  line-height: 1.85 !important; margin: 0 !important;
  letter-spacing: -.005em !important;
}

/* quiz panel */
.qpanel {
  background: var(--card); border: 1px solid var(--border);
  border-radius: var(--rr); box-shadow: var(--s1);
  position: sticky; top: 70px;
}
.qpanel-top {
  padding: 18px 18px 14px; border-bottom: 1px solid rgba(0,0,0,.06);
  display: flex; gap: 12px; align-items: flex-start;
}
.qpanel-ico {
  width: 42px; height: 42px; border-radius: 11px;
  background: rgba(0,113,227,.1);
  display: flex; align-items: center; justify-content: center;
  font-size: 1.2rem; flex-shrink: 0;
}
.qpanel-title {
  font-size: .9375rem; font-weight: 700;
  color: var(--ink); margin: 0; letter-spacing: -.02em;
}
.qpanel-sub { font-size: .75rem; color: var(--ink3); margin-top: 2px; }
.qpanel-body { padding: 16px 18px; }
.qlabel {
  font-size: .625rem; font-weight: 700;
  color: var(--ink3); text-transform: uppercase;
  letter-spacing: .1em; margin-bottom: 4px;
}
.qdivider { border:none; border-top: 1px solid rgba(0,0,0,.06); margin: 12px 0; }

/* result cards */
.res {
  border-radius: var(--r); padding: 18px 20px;
  display: flex; align-items: flex-start; gap: 16px;
  flex-wrap: wrap; margin: 14px 0;
}
.res-pass { background: rgba(52,199,89,.09); border: 1px solid rgba(52,199,89,.28); }
.res-fail { background: rgba(255,59,48,.07); border: 1px solid rgba(255,59,48,.24); }
.res-score {
  font-size: 2.75rem; font-weight: 800;
  letter-spacing: -.06em; line-height: 1; flex-shrink: 0;
}
.res-pass .res-score { color: #248a3d; }
.res-fail .res-score { color: #c91e14; }
.res-tag {
  font-size: .6875rem; font-weight: 700;
  text-transform: uppercase; letter-spacing: .08em; margin-top: 4px;
}
.res-pass .res-tag { color: #248a3d; }
.res-fail .res-tag { color: #c91e14; }
.res-msg { font-size: .8125rem; color: var(--ink2); line-height: 1.7; }
.res-msg b { color: var(--ink); }

/* ────────────────────────────────────────────────
   GRADES
──────────────────────────────────────────────── */
.gtable {
  background: var(--card); border: 1px solid var(--border);
  border-radius: var(--rr); box-shadow: var(--s1);
  width: 100%; border-collapse: collapse; overflow: hidden;
}
.gtable th {
  background: rgba(0,0,0,.025); padding: 10px 18px;
  font-size: .625rem; font-weight: 700; color: var(--ink3);
  text-transform: uppercase; letter-spacing: .09em;
  text-align: left; border-bottom: 1px solid var(--border);
}
.gtable td {
  padding: 14px 18px; border-bottom: 1px solid rgba(0,0,0,.04);
  font-size: .875rem; color: var(--ink); vertical-align: middle;
}
.gtable tr:last-child td { border-bottom: none; }
.gtable tr { transition: background .12s; }
.gtable tr:hover td { background: rgba(0,0,0,.018); }
.gm { font-weight: 700; font-size: .875rem; }

/* ────────────────────────────────────────────────
   MOBILE RESPONSIVE
──────────────────────────────────────────────── */
@media (max-width: 900px) {
  .cards-grid { grid-template-columns: repeat(2,1fr); }
  .classwork   { grid-template-columns: 1fr; }
  .qpanel      { position: static; }
  .stats       { grid-template-columns: repeat(2,1fr); }
}
@media (max-width: 640px) {
  .page        { padding: 16px 14px 72px; }
  .topnav      { padding: 0 14px; }
  .cards-grid  { grid-template-columns: 1fr; }
  .stats       { grid-template-columns: repeat(2,1fr); gap: 8px; }
  .hero-greeting { font-size: 1.5rem; }
  .class-header { padding: 22px 18px 20px; }
  .ch-title    { font-size: 1.4rem; }
  .gtable      { display: block; overflow-x: auto; }
  .qpanel      { border-radius: var(--r); }
}
@media (max-width: 420px) {
  .stats { grid-template-columns: 1fr 1fr; }
  .stat-n { font-size: 1.5rem; }
  .page { padding: 12px 10px 64px; }
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb">
      <div class="sb-top">
        <div class="sb-wordmark">Danilo</div>
        <div class="sb-tagline">Learning Platform</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="sb-section">Menu</div>', unsafe_allow_html=True)
    st.markdown('<div class="sb-body">', unsafe_allow_html=True)
    st.button("🏠  Home",    on_click=go, args=("home",),   use_container_width=True)
    st.button("📊  Grades",  on_click=go, args=("grades",), use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="sb-section">Courses</div>', unsafe_allow_html=True)
    for ck, course in COURSES.items():
        locked = ck not in st.session_state.unlocked
        ico = course["color"]
        lbl = f"{'🔒' if locked else '●'}  {course['title']}"
        st.button(lbl, on_click=go, args=(ck,), disabled=locked, use_container_width=True)

    st.markdown("""
    <div class="sb-footer">
      © 2025 Danilo Learning<br>All rights reserved.
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
#  TOP NAV
# ─────────────────────────────────────────────────────────────────────
v = st.session_state.view
if v == "home":
    topnav_html = '<div class="topnav"><div class="topnav-title">Home</div><div class="topnav-pill">D</div></div>'
elif v == "grades":
    topnav_html = '<div class="topnav"><div class="topnav-crumb">Home</div><div class="topnav-sep">/</div><div class="topnav-title">Grades</div><div class="topnav-pill">D</div></div>'
elif v in COURSES:
    topnav_html = f'<div class="topnav"><div class="topnav-crumb">Home</div><div class="topnav-sep">/</div><div class="topnav-title">{COURSES[v]["title"]}</div><div class="topnav-pill">D</div></div>'
else:
    topnav_html = '<div class="topnav"><div class="topnav-pill">D</div></div>'
st.markdown(topnav_html, unsafe_allow_html=True)

# ─────────────────────────────────────────────────────────────────────
#  PAGE CONTENT
# ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="page">', unsafe_allow_html=True)

# ══════════════════════════════════════════════
#  HOME
# ══════════════════════════════════════════════
if v == "home":
    am = ["1","2","3","4"]
    taken  = [st.session_state[f"c{i}_score"] for i in ["1","2","3","4"] if st.session_state[f"c{i}_done"]]
    avg    = (sum(taken)/(len(taken)*5)*100) if taken else 0
    passed = sum(1 for i in ["1","2","3","4"] if st.session_state[f"c{i}_done"] and st.session_state[f"c{i}_score"]>=4)
    unlk   = len(st.session_state.unlocked)

    st.markdown(f"""
    <div class="hero u0">
      <div class="hero-greeting">Good day, Danilo.</div>
      <div class="hero-sub">You have {len(COURSES) - unlk} course{"s" if len(COURSES)-unlk!=1 else ""} left to unlock. Keep going.</div>
    </div>

    <div class="stats u1">
      <div class="stat">
        <div class="stat-n" style="color:#0071e3;">{unlk}/4</div>
        <div class="stat-l">Unlocked</div>
        <div class="stat-bar"><div class="stat-fill" style="width:{unlk/4*100:.0f}%;background:#0071e3;"></div></div>
      </div>
      <div class="stat">
        <div class="stat-n" style="color:#34c759;">{passed}/4</div>
        <div class="stat-l">Passed</div>
        <div class="stat-bar"><div class="stat-fill" style="width:{passed/4*100:.0f}%;background:#34c759;"></div></div>
      </div>
      <div class="stat">
        <div class="stat-n" style="color:#ff9500;">{avg:.0f}%</div>
        <div class="stat-l">Accuracy</div>
        <div class="stat-bar"><div class="stat-fill" style="width:{min(avg,100):.0f}%;background:#ff9500;"></div></div>
      </div>
      <div class="stat">
        <div class="stat-n" style="color:#5856d6;">{int(passed/4*100)}%</div>
        <div class="stat-l">Progress</div>
        <div class="stat-bar"><div class="stat-fill" style="width:{passed/4*100:.0f}%;background:#5856d6;"></div></div>
      </div>
    </div>

    <div class="section-label u2">Courses</div>
    <div class="cards-grid">
    """, unsafe_allow_html=True)

    # Card HTML in one block
    cards_html = ""
    for idx, (ck, course) in enumerate(COURSES.items()):
        locked = ck not in st.session_state.unlocked
        cid    = course["id"]
        done   = st.session_state[f"c{cid}_done"] and st.session_state[f"c{cid}_score"] >= 4
        bdg = (
            '<span class="badge badge-done">✓ Complete</span>' if done
            else '<span class="badge badge-lock">🔒 Locked</span>' if locked
            else '<span class="badge badge-active">● Active</span>'
        )
        cards_html += f"""
        <div class="ccard u{min(idx+2,7)}">
          <div class="ccard-strip" style="background:{course['color']};"></div>
          <div class="ccard-body">
            <div class="ccard-title">{course['title']}</div>
            <div class="ccard-sub">{course['sub']}</div>
            <div class="ccard-meta">
              <span style="color:var(--ink3);font-size:.75rem;">{course['teacher']} · {course['grade']}</span>
              {bdg}
            </div>
          </div>
        </div>"""

    st.markdown(cards_html + "</div>", unsafe_allow_html=True)

    # Buttons — one per column, matching the grid
    items = list(COURSES.items())
    for row in range(0, len(items), 3):
        cols = st.columns(3, gap="small")
        for ci, (ck, course) in enumerate(items[row:row+3]):
            locked = ck not in st.session_state.unlocked
            with cols[ci]:
                st.button(
                    "Open →" if not locked else "Locked",
                    key=f"h_{ck}", on_click=go, args=(ck,),
                    disabled=locked, use_container_width=True,
                )


# ══════════════════════════════════════════════
#  COURSE VIEW
# ══════════════════════════════════════════════
elif v in COURSES:
    course = COURSES[v]
    cid    = course["id"]
    qdata  = QUIZ[cid]
    pm     = len(qdata) - 1
    color  = course["color"]

    back_col, _ = st.columns([1, 6])
    with back_col:
        st.button("← Back", key=f"bk_{v}", on_click=go, args=("home",))
    st.markdown('<div style="height:6px"></div>', unsafe_allow_html=True)

    # Header banner
    st.markdown(f"""
    <div class="class-header" style="background:{color};">
      <div class="class-header-content">
        <div class="ch-label">{course['grade']} · {course['teacher']}</div>
        <div class="ch-title">{course['title']}</div>
        <div class="ch-sub">{course['sub']}</div>
        <div class="ch-chips">
          <span class="wchip">📖 {len(course['lessons'])} lessons</span>
          <span class="wchip">📋 {len(qdata)} questions</span>
          <span class="wchip">⏱ ~15 min</span>
          <span class="wchip">Pass: {pm}/{len(qdata)}</span>
        </div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # Two-column layout
    st.markdown('<div class="classwork">', unsafe_allow_html=True)
    left_html = '<div>'

    # — Lessons (left) —
    left_html += '<div class="section-label">Lesson Material</div>'
    ico_bg_pairs = [
        ("rgba(0,113,227,.1)","#0071e3"),
        ("rgba(52,199,89,.1)","#248a3d"),
        ("rgba(255,149,0,.12)","#b86000"),
        ("rgba(88,86,214,.1)","#5856d6"),
    ]
    for i, (title, body) in enumerate(course["lessons"]):
        ibg, itc = ico_bg_pairs[i % len(ico_bg_pairs)]
        num = ["①","②","③","④"][i % 4]
        left_html += f"""
        <div class="lesson u{i+1}">
          <div class="lesson-head">
            <div class="lesson-ico" style="background:{ibg};color:{itc};">{num}</div>
            <div>
              <div class="lesson-title">{title}</div>
              <div class="lesson-tag">Reading · {course['teacher']}</div>
            </div>
          </div>
          <div class="lesson-body"><p>{body}</p></div>
        </div>"""

    left_html += '</div>'
    st.markdown(left_html, unsafe_allow_html=True)

    # — Quiz panel (right) —
    sk = f"{v}_started"; uk = f"{v}_done"; ck = f"{v}_score"

    st.markdown(f"""
    <div class="qpanel u0">
      <div class="qpanel-top">
        <div class="qpanel-ico">📋</div>
        <div>
          <div class="qpanel-title">Assessment</div>
          <div class="qpanel-sub">{len(qdata)} questions · {pm}/{len(qdata)} to pass · Unlimited retries</div>
        </div>
      </div>
      <div class="qpanel-body">
    """, unsafe_allow_html=True)

    if not st.session_state[sk]:
        st.markdown('</div></div>', unsafe_allow_html=True)
        st.button("▶  Begin Assessment", key=f"begin_{v}")
        if st.session_state.get(f"begin_{v}"):
            st.session_state[sk] = True
            st.rerun()
    else:
        st.markdown('</div></div>', unsafe_allow_html=True)
        with st.form(key=f"f_{v}", clear_on_submit=False):
            answers = []
            for i, q in enumerate(qdata):
                st.markdown(f'<div class="qlabel">Q{i+1} of {len(qdata)}</div>', unsafe_allow_html=True)
                st.markdown(f"**{q['q']}**")
                a = st.radio("", q["o"], key=f"{v}_q{i}", label_visibility="collapsed", index=None)
                answers.append(a)
                if i < len(qdata)-1:
                    st.markdown('<hr class="qdivider">', unsafe_allow_html=True)
            st.markdown('<div style="height:4px"></div>', unsafe_allow_html=True)
            sub = st.form_submit_button("Submit Assessment")

        if sub:
            if None in answers:
                st.error("Please answer every question before submitting.")
            else:
                sc = sum(1 for i,q in enumerate(qdata) if answers[i]==q["a"])
                st.session_state[ck] = sc
                st.session_state[uk] = True

        if st.session_state[uk]:
            sc = st.session_state[ck]
            ok = sc >= pm
            pct = int(sc/len(qdata)*100)
            cls = "res-pass" if ok else "res-fail"
            tag = "Passed" if ok else "Below pass mark"
            nxt = course.get("next")
            unlock_line = ""
            if ok and nxt and nxt not in st.session_state.unlocked:
                st.session_state.unlocked.add(nxt)
            if ok and nxt:
                unlock_line = f'<span style="color:#248a3d;font-weight:600;font-size:.8125rem;display:block;margin-top:6px;">{COURSES[nxt]["title"]} is now unlocked.</span>'
            elif ok and not nxt:
                unlock_line = '<span style="color:#248a3d;font-weight:600;font-size:.8125rem;display:block;margin-top:6px;">You have completed all courses! 🎉</span>'
            st.markdown(f"""
            <div class="res {cls} pop">
              <div>
                <div class="res-score">{sc}/{len(qdata)}</div>
                <div class="res-tag">{"✓ " if ok else "✗ "}{tag}</div>
              </div>
              <div class="res-msg">
                <b>{"Outstanding." if ok else "Keep going."}</b>
                {"You scored "+str(pct)+"% and have demonstrated mastery of this topic." if ok else "You scored "+str(pct)+"%. Review the lessons and retry."}
                {unlock_line}
              </div>
            </div>
            """, unsafe_allow_html=True)
            if not ok:
                if st.button("🔄  Retry", key=f"retry_{v}"):
                    st.session_state[uk] = False
                    st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)  # close .classwork


# ══════════════════════════════════════════════
#  GRADES
# ══════════════════════════════════════════════
elif v == "grades":
    back_col, _ = st.columns([1,6])
    with back_col:
        st.button("← Back", key="bk_g", on_click=go, args=("home",))
    st.markdown('<div style="height:6px"></div>', unsafe_allow_html=True)

    ids    = ["1","2","3","4"]
    subs   = {i: st.session_state[f"c{i}_done"]  for i in ids}
    scores = {i: st.session_state[f"c{i}_score"] for i in ids}
    taken  = [scores[i] for i in ids if subs[i]]
    avg    = (sum(taken)/(len(taken)*5)*100) if taken else 0
    comp   = sum(1 for i in ids if subs[i] and scores[i]>=4)
    unlk   = len(st.session_state.unlocked)

    st.markdown(f"""
    <div class="stats u0">
      <div class="stat">
        <div class="stat-n" style="color:#0071e3;">{unlk}/4</div>
        <div class="stat-l">Unlocked</div>
        <div class="stat-bar"><div class="stat-fill" style="width:{unlk/4*100:.0f}%;background:#0071e3;"></div></div>
      </div>
      <div class="stat">
        <div class="stat-n" style="color:#34c759;">{avg:.0f}%</div>
        <div class="stat-l">Accuracy</div>
        <div class="stat-bar"><div class="stat-fill" style="width:{min(avg,100):.0f}%;background:#34c759;"></div></div>
      </div>
      <div class="stat">
        <div class="stat-n" style="color:#ff9500;">{comp}/4</div>
        <div class="stat-l">Passed</div>
        <div class="stat-bar"><div class="stat-fill" style="width:{comp/4*100:.0f}%;background:#ff9500;"></div></div>
      </div>
      <div class="stat">
        <div class="stat-n" style="color:#5856d6;">{int(comp/4*100)}%</div>
        <div class="stat-l">Progress</div>
        <div class="stat-bar"><div class="stat-fill" style="width:{comp/4*100:.0f}%;background:#5856d6;"></div></div>
      </div>
    </div>
    <div class="section-label u1" style="margin-top:24px;">Gradebook</div>
    """, unsafe_allow_html=True)

    rows = ""
    for ck, course in COURSES.items():
        cid   = course["id"]
        total = len(QUIZ[cid])
        locked= ck not in st.session_state.unlocked
        sub   = subs[cid]; sc = scores[cid]; done = sub and sc >= 4

        if locked:
            sh = '<span class="badge badge-lock">🔒 Locked</span>'
            sd = gd = '<span style="color:var(--ink3)">—</span>'
        elif done:
            sh = '<span class="badge badge-done">✓ Passed</span>'
            sd = f'<span class="gm" style="color:#248a3d;">{sc}/{total}</span>'
            gd = f'<span class="gm" style="color:#248a3d;">{int(sc/total*100)}%</span>'
        elif sub:
            sh = '<span class="badge" style="background:rgba(255,59,48,.1);color:#c91e14;">✗ Below Pass</span>'
            sd = f'<span class="gm" style="color:#c91e14;">{sc}/{total}</span>'
            gd = f'<span class="gm" style="color:#c91e14;">{int(sc/total*100)}%</span>'
        else:
            sh = '<span class="badge badge-lock">○ Not started</span>'
            sd = gd = '<span style="color:var(--ink3)">—</span>'

        rows += f"""<tr>
          <td>
            <div style="width:10px;height:10px;border-radius:50%;background:{course['color']};display:inline-block;margin-right:8px;"></div>
            <b>{course['title']}</b>
          </td>
          <td style="color:var(--ink2);font-size:.8125rem;">{course['sub']}</td>
          <td style="color:var(--ink2);font-size:.8125rem;">{course['teacher']}</td>
          <td>{sh}</td><td>{sd}</td><td>{gd}</td>
        </tr>"""

    st.markdown(f"""
    <table class="gtable u2">
      <thead><tr>
        <th>Course</th><th>Topic</th><th>Teacher</th>
        <th>Status</th><th>Score</th><th>Grade</th>
      </tr></thead>
      <tbody>{rows}</tbody>
    </table>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
