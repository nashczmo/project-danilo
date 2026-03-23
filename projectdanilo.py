import streamlit as st
import os

if not os.path.exists(".streamlit"):
    os.makedirs(".streamlit")
with open(".streamlit/config.toml", "w") as f:
    f.write('[theme]\nbase="light"\nprimaryColor="#1a73e8"\nbackgroundColor="#f1f3f4"\nsecondaryBackgroundColor="#ffffff"\ntextColor="#202124"\nfont="sans serif"\n')

st.set_page_config(page_title="DANILO Classroom", page_icon="📚", layout="wide", initial_sidebar_state="expanded")

# ─── Quiz data ────────────────────────────────────────────────────────────────
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
        "icon":"📖","color":"#1565c0","header_bg":"#1a73e8",
        "pattern":"repeating-linear-gradient(45deg,rgba(255,255,255,0.06) 0,rgba(255,255,255,0.06) 1px,transparent 0,transparent 50%) 0 0 / 8px 8px",
        "quiz":M1,"next":"module_2","umsg":"Reading Fluency is now unlocked!",
        "topics":[
            ("📚","1.0 — Elements of a Story",
             "Every story is built from essential building blocks that work together to create meaning and bring a narrative to life. The <b>setting</b> establishes the world of the story — not only the physical location but also the time period, culture, atmosphere, and mood in which events unfold. A story set in a rainy medieval castle creates an entirely different feeling from one set on a sun-drenched modern beach, even when the plot is nearly identical. The <b>characters</b> are the living hearts of any narrative — they can be people, animals, mythical creatures, or even everyday objects given a personality. Their hopes, fears, flaws, and relationships create the emotional texture that keeps readers turning pages long after bedtime. The <b>plot</b> is the engine: the carefully ordered chain of events — conflict, rising action, climax, falling action, and resolution — that propels the reader from the opening sentence to the very last word. Mastering these three elements gives you a reliable lens through which to read, analyse, and enjoy any story you encounter."),
            ("🔍","1.1 — Finding the Main Idea",
             "Every well-written paragraph revolves around a single central point called the <b>main idea</b>. This is the author's primary message — the one thing they most want you to understand and remember after reading. Skilled readers train themselves to locate this quickly by looking for the <b>topic sentence</b>, which typically appears at or near the beginning of a paragraph and announces its subject clearly and directly. The sentences that follow — called <b>supporting details</b> — provide evidence, examples, statistics, anecdotes, or descriptions that expand on and reinforce the topic sentence. One reliable technique is to pause after reading any paragraph and ask yourself: 'If I had to express this entire paragraph in a single sentence, what would it say?' That mental summary is almost always the main idea. Apply this skill consistently across every text you read — newspaper articles, science chapters, social media posts — and even the most complex material will feel far more approachable."),
            ("💡","1.2 — Using Context Clues",
             "Encountering an unfamiliar word mid-sentence does not have to interrupt your reading flow. Skilled readers use <b>context clues</b> — the words, phrases, sentences, and even images surrounding the unknown term — to make an educated, confident guess about its meaning without ever pausing to reach for a dictionary. There are several recognisable types of context clues. <b>Definition clues</b> occur when the author helpfully explains a word immediately after using it, often signalled by phrases like 'which means,' 'that is,' or 'in other words.' <b>Synonym clues</b> appear when a nearby word shares a similar meaning, allowing direct comparison. <b>Antonym clues</b> use contrast words like 'but,' 'however,' 'unlike,' or 'instead' to hint at an opposite meaning. <b>Example clues</b> illustrate a word's meaning through specific, concrete instances. The wider and more varied your reading, the sharper your context-clue instincts become — turning every unfamiliar word into an exciting opportunity to expand your vocabulary."),
            ("✍️","1.3 — Building Your Vocabulary",
             "A rich vocabulary is among the most powerful tools any reader, writer, thinker, or communicator can possess. Words are the instruments of thought — the more precise and varied your vocabulary, the more accurately and vividly you can both understand the world and express your own ideas. One deeply effective strategy is keeping a <b>personal vocabulary journal</b>: a dedicated notebook or digital file where you record new words, their precise definitions, the original sentence in which you found them, and an original example sentence you craft yourself. Cognitive science research consistently shows that <b>spaced repetition</b> — revisiting new words at gradually increasing intervals — produces dramatically stronger long-term retention than cramming. Another proven strategy is studying <b>Greek and Latin word roots, prefixes, and suffixes</b>. For example, knowing that the Latin root <em>port</em> means 'to carry' instantly unlocks transport, import, export, portable, portfolio, and deportation. Vocabulary knowledge is wonderfully cumulative — each new word you learn makes learning the next one slightly easier."),
        ],
    },
    "module_2":{
        "k":"2","label":"Reading Fluency","section":"Grade 4 — English (Advanced)","teacher":"Ms. Santos",
        "icon":"🗣️","color":"#4a148c","header_bg":"#7b1fa2",
        "pattern":"repeating-linear-gradient(-45deg,rgba(255,255,255,0.06) 0,rgba(255,255,255,0.06) 1px,transparent 0,transparent 50%) 0 0 / 8px 8px",
        "quiz":M2,"next":"module_3","umsg":"Mathematics is now unlocked!",
        "topics":[
            ("🎯","2.0 — What Is Reading Fluency?",
             "Reading fluency is the essential <b>bridge between recognising individual words on a page and truly comprehending what you read</b>. A fluent reader moves through text with three interlocking qualities: <b>accuracy</b> (decoding words correctly without errors), <b>automaticity</b> (recognising words instantly without conscious, laborious effort), and <b>prosody</b> (reading with natural rhythm, appropriate pacing, meaningful pauses, and expressive intonation that mirrors natural speech). When reading is effortful and halting, virtually all of a reader's mental energy is consumed by simply decoding individual words, leaving little or no cognitive capacity for higher-order thinking: inferring meaning, questioning the author, visualising scenes, or connecting ideas. Fluency liberates the brain to operate at a genuinely higher level. Decades of reading research have consistently identified fluency as one of the strongest individual predictors of overall reading comprehension — which means developing it is not optional; it is absolutely foundational."),
            ("🔄","2.1 — The Power of Repeated Reading",
             "<b>Repeated reading</b> is one of the most elegantly simple yet strikingly powerful techniques in all of reading instruction. The method is straightforward: select a short, engaging passage and read it aloud multiple times (usually three to five), tracking your own accuracy, expression, and fluency as you improve with each reading. On your very first encounter, you are largely decoding. By your second reading, you begin to feel the natural shape and rhythm of sentences. By the third and fourth, you are reading with genuine expression and a level of comprehension you could not access before. Think of how a musician learns a new piece: they do not play it once and declare mastery. They rehearse it, refine it, identify trouble spots, slow down for difficult passages, and gradually build toward a confident, expressive performance. Reading is the same kind of practised, deliberate skill. A powerful companion is <b>paired reading</b>, where a more skilled reader sits beside a developing reader, reading aloud together — providing a real-time model of fluent, expressive reading while allowing the learner to gradually take more responsibility."),
            ("👁️","2.2 — Sight Words and Automaticity",
             "A relatively small set of high-frequency words — called <b>sight words</b> — accounts for an astonishing proportion of all written English text. Words like 'the,' 'and,' 'said,' 'because,' 'through,' 'could,' 'would,' and 'there' appear on virtually every single page. When a reader must laboriously decode these extremely common words character by character on every encounter, reading becomes painfully slow and mentally exhausting, draining energy that should be directed toward comprehension. The goal is complete <b>automaticity</b> — recognising these words as whole, instant, effortless units. Reading scientists call this process <b>orthographic mapping</b> — the deep encoding of a word's spelling, pronunciation, and meaning into long-term memory as a single, retrievable unit. Proven methods include systematic flashcard practice, classroom word walls, word sorts, word games, and — most powerfully — wide, regular, and pleasurable independent reading, which provides the repeated, meaningful exposures necessary for words to become truly automatic."),
            ("🧠","2.3 — Active Comprehension Strategies",
             "Deep reading comprehension is not a passive activity — it is an active, ongoing, and intentional conversation between the reader and the text. Expert readers deploy a toolkit of deliberate mental strategies that transform passive decoding into active sense-making. <b>Predicting</b> means forming expectations about what will happen next, based on evidence in the text and your own background knowledge. <b>Questioning</b> involves generating your own genuine questions — 'Why did the character do that?', 'What will happen if...?', 'Do I agree with this argument?' — transforming you from a recipient into a critical thinker. <b>Visualising</b> means constructing a vivid, detailed mental movie of settings, characters, actions, and emotions — research consistently shows that strong visualisation dramatically improves both comprehension and memory. <b>Summarising</b> requires you to identify what truly matters and restate it concisely in your own words. <b>Making connections</b> — linking new information to personal experience, other texts, or the world — is the mechanism by which truly deep and durable understanding is formed."),
        ],
    },
    "module_3":{
        "k":"3","label":"Mathematics","section":"Grade 4 — Mathematics","teacher":"Mr. Reyes",
        "icon":"🔢","color":"#1b5e20","header_bg":"#2e7d32",
        "pattern":"repeating-linear-gradient(90deg,rgba(255,255,255,0.06) 0,rgba(255,255,255,0.06) 1px,transparent 0,transparent 50%) 0 0 / 8px 8px",
        "quiz":M3,"next":"module_4","umsg":"Natural Sciences is now unlocked!",
        "topics":[
            ("➕","3.0 — The Four Basic Operations",
             "All of mathematics rests on four fundamental operations that allow us to manipulate, compare, and understand numbers in every conceivable context. <b>Addition</b> combines two or more quantities to find their total sum — asking, in essence, 'how many altogether?' <b>Subtraction</b> is addition's inverse, finding the difference between quantities — asking 'how many remain?' or 'how much more?' <b>Multiplication</b> is a powerful and elegant shortcut for repeated addition: rather than laboriously adding 9 together seven separate times, we express this instantly as 9 × 7 = 63. Understanding multiplication conceptually — not merely as a set of facts to memorise — is the gateway to virtually all advanced mathematics, from algebra to calculus. <b>Division</b> is multiplication's inverse, partitioning a quantity into equal groups. Mastering all four operations with genuine fluency — so they require no conscious effort — is a non-negotiable foundation for mathematical success at every stage of education and life."),
            ("½","3.1 — Understanding Fractions",
             "A fraction is a precise, powerful mathematical tool for representing any part of a whole. When we write ¾, the number on top — the <b>numerator</b> (3) — tells us how many equal parts we currently possess or are considering. The number on the bottom — the <b>denominator</b> (4) — tells us into how many equal parts the whole has been divided. Imagine a rectangular chocolate bar divided into four equal pieces: eating three of those pieces means you have consumed ¾ of the bar. The denominator can <b>never be zero</b>, because dividing something into zero parts is a mathematical impossibility — it carries no coherent meaning. Fractions can be classified as <b>proper</b> (numerator smaller than denominator, like ⅔, representing less than one whole), <b>improper</b> (numerator larger, like 7/4, representing more than one whole), or expressed as <b>mixed numbers</b> (like 1¾). A thorough understanding of fractions is the direct foundation for decimals, percentages, ratios, rates, and algebraic thinking."),
            ("📐","3.2 — Shapes, Perimeter, and Area",
             "Geometry is the magnificent branch of mathematics devoted to understanding the properties, relationships, and measurements of points, lines, angles, surfaces, and solid figures. A <b>polygon</b> is any flat, closed, two-dimensional figure entirely bounded by straight sides. Polygons are classified by the number of their sides: triangle (3), quadrilateral (4), pentagon (5), hexagon (6), heptagon (7), and octagon (8). Two of the most essential measurements of any flat shape are its <b>perimeter</b> and its <b>area</b>. The perimeter is the total distance around the complete outer boundary of a shape — imagine an ant walking all the way around the edge and measuring every millimetre of its journey. For a rectangle: perimeter = 2 × (length + width). The area measures how much flat surface the shape covers — how many unit squares fit perfectly inside it. For a rectangle: area = length × width. Real-world applications are everywhere: a builder uses perimeter to calculate baseboard; a painter uses area to determine paint quantity; a farmer uses both to plan fields and fencing."),
        ],
    },
    "module_4":{
        "k":"4","label":"Natural Sciences","section":"Grade 4 — Science","teacher":"Ms. Cruz",
        "icon":"🌍","color":"#bf360c","header_bg":"#e64a19",
        "pattern":"repeating-linear-gradient(135deg,rgba(255,255,255,0.06) 0,rgba(255,255,255,0.06) 1px,transparent 0,transparent 50%) 0 0 / 8px 8px",
        "quiz":M4,"next":None,"umsg":"🎉 Congratulations — all modules complete!",
        "topics":[
            ("🌊","4.0 — Introduction to the Water Cycle",
             "The water cycle — known scientifically as the <b>hydrological cycle</b> — is one of Earth's most fundamental and life-sustaining natural processes. It describes the continuous, perpetual journey of water as it moves and transforms among Earth's surface (oceans, rivers, lakes, glaciers, soil), its atmosphere, and its underground systems. Water is never created or destroyed in this process; it simply changes its physical state (liquid, gas, or solid) and its location, cycling through the same pathways it has followed for approximately 4.5 billion years. The total volume of water on Earth has remained essentially constant since our planet formed. This means the water flowing from your tap today has, at some earlier moment in deep history, filled a prehistoric ocean, nourished a dinosaur, been locked inside an Antarctic glacier, and fallen as rain over a distant mountain range. Understanding the water cycle is fundamental to meteorology, hydrology, ecology, agriculture, and the science of climate change."),
            ("☀️","4.1 — Evaporation and Condensation",
             "<b>Evaporation</b> is the process by which the Sun's tremendous thermal energy heats liquid water at Earth's surface — primarily in oceans, seas, rivers, and lakes — converting it into water vapour, an invisible gas that rises buoyantly into the atmosphere. Roughly 90% of all atmospheric water vapour originates from ocean evaporation; the remaining 10% comes from the transpiration of land plants (collectively called <b>evapotranspiration</b>). As water vapour rises higher into the troposphere, it encounters progressively colder temperatures. When the vapour cools below a critical threshold called the <b>dew point</b>, it undergoes <b>condensation</b> — reverting from an invisible gas back into microscopic liquid water droplets or tiny ice crystals. These minuscule particles cling to even tinier specks of dust, sea salt, pollen, and pollution particles suspended in the air (called condensation nuclei), clustering together to form the visible, billowing clouds we observe drifting across the sky — each one carrying enormous quantities of water across potentially thousands of kilometres."),
            ("🌧️","4.2 — Precipitation and Collection",
             "As clouds continue to grow — accumulating ever-greater quantities of condensed water droplets — gravity eventually overcomes the atmospheric forces that have been keeping the droplets suspended aloft. Water then falls back to Earth's surface as <b>precipitation</b>. The precise form precipitation takes is determined by the temperature of the atmosphere: <b>rain</b> forms when temperatures remain above freezing throughout; <b>snow</b> forms when temperatures stay below freezing from cloud to ground; <b>sleet</b> forms when falling raindrops refreeze before reaching the ground; and <b>hail</b> forms when powerful updrafts inside intense thunderstorms repeatedly carry ice pellets back upward before they finally fall. Once precipitation reaches Earth's surface, water takes multiple pathways: it replenishes oceans, lakes, rivers, and reservoirs; it is drawn up by plant roots and eventually transpired back into the atmosphere; and it seeps into soil through <b>infiltration</b>, percolating downward to recharge underground <b>aquifers</b> — vast, slow-moving reservoirs of freshwater capable of sustaining entire cities, ecosystems, and civilisations long after rainfall has ceased."),
        ],
    },
}

# ─── Session state ────────────────────────────────────────────────────────────
defaults = {"current_view":"home","unlocked":["module_1"]}
for k,v in defaults.items():
    if k not in st.session_state: st.session_state[k]=v
for m in ["1","2","3","4"]:
    for k,d in [("qs",False),("qd",False),("qr",0)]:
        if f"m{m}_{k}" not in st.session_state: st.session_state[f"m{m}_{k}"]=d

def nav(v): st.session_state.current_view=v

# ─── CSS ──────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Google+Sans:wght@400;500;700&family=Roboto:wght@300;400;500;700&display=swap');

:root{
  --blue:#1a73e8; --blue-dk:#1557b0;
  --green:#0f9d58; --red:#ea4335; --yellow:#f9ab00;
  --gray-50:#f8f9fa; --gray-100:#f1f3f4;
  --gray-200:#e8eaed; --gray-400:#bdc1c6;
  --gray-600:#80868b; --gray-700:#5f6368;
  --gray-900:#202124;
  --surface:#fff; --bg:#f1f3f4;
  --border:1px solid #e0e0e0;
  --r4:4px; --r8:8px; --r12:12px;
  --sh1:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);
  --sh2:0 1px 3px 0 rgba(60,64,67,.3),0 4px 8px 3px rgba(60,64,67,.15);
  --sh3:0 2px 6px 2px rgba(60,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);
}

/* Reset */
*,html,body,[class*="css"]{
  font-family:'Roboto',sans-serif !important;
  -webkit-font-smoothing:antialiased;
  box-sizing:border-box;
}
.stApp{background:var(--bg)!important;}
#MainMenu,footer,header{visibility:hidden;}

/* Remove Streamlit padding */
.block-container{padding:0!important;max-width:100%!important;}
.main>div{padding:0!important;}

/* ── Sidebar ── */
section[data-testid="stSidebar"]{
  background:var(--surface)!important;
  border-right:var(--border)!important;
  width:256px!important; min-width:256px!important;
  padding-top:0!important;
}
section[data-testid="stSidebar"]>div{padding:0!important;width:256px!important;}

/* Always-visible sidebar toggle */
[data-testid="collapsedControl"]{
  visibility:visible!important; display:flex!important;
  opacity:1!important; position:fixed!important;
  top:13px!important; left:13px!important;
  z-index:99999!important;
  width:40px!important; height:40px!important;
  border-radius:50%!important;
  background:transparent!important;
  border:none!important; box-shadow:none!important;
  cursor:pointer!important;
  align-items:center!important; justify-content:center!important;
  transition:background .15s ease!important;
}
[data-testid="collapsedControl"]:hover{background:rgba(32,33,36,.08)!important;}
[data-testid="collapsedControl"] svg{color:#5f6368!important; width:22px!important; height:22px!important;}

/* ── All Streamlit buttons → sidebar nav links ── */
div[data-testid="stButton"]>button{
  font-family:'Roboto',sans-serif!important;
  font-size:.875rem!important; font-weight:500!important;
  color:var(--gray-900)!important;
  background:transparent!important; border:none!important;
  border-radius:0 24px 24px 0!important;
  padding:0 24px!important; height:48px!important;
  text-align:left!important; width:100%!important;
  letter-spacing:.01em!important;
  transition:background .15s ease!important;
  cursor:pointer!important; display:flex!important;
  align-items:center!important;
}
div[data-testid="stButton"]>button:hover{background:var(--gray-100)!important;}
div[data-testid="stButton"]>button:active{background:var(--gray-200)!important;}

/* Form submit button override */
div[data-testid="stForm"] div[data-testid="stButton"]>button{
  background:var(--blue)!important; color:#fff!important;
  border-radius:4px!important; padding:0 24px!important;
  height:36px!important; font-size:.875rem!important;
  font-weight:500!important; width:auto!important;
  letter-spacing:.01em!important;
  box-shadow:none!important;
  transition:background .15s ease, box-shadow .15s ease!important;
}
div[data-testid="stForm"] div[data-testid="stButton"]>button:hover{
  background:var(--blue-dk)!important;
  box-shadow:var(--sh1)!important;
}

/* Retry / start buttons */
div[data-testid="stButton"]:has(button:not([disabled]))>button.start-btn,
.action-btn div[data-testid="stButton"]>button{
  background:var(--blue)!important; color:#fff!important;
  border-radius:4px!important; width:auto!important;
  height:36px!important;
}

/* Radio */
div[role="radiogroup"]{
  background:#fff!important; border:var(--border)!important;
  border-radius:var(--r8)!important;
  padding:12px 16px!important; margin-bottom:8px!important;
  box-shadow:none!important;
}
div[role="radiogroup"]:focus-within{
  border-color:var(--blue)!important;
  box-shadow:0 0 0 2px rgba(26,115,232,.15)!important;
}

/* ── Animations ── */
@keyframes fadeUp{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:translateY(0)}}
@keyframes fadeIn{from{opacity:0}to{opacity:1}}
@keyframes scaleUp{from{opacity:0;transform:scale(.97)}to{opacity:1;transform:scale(1)}}
.au{animation:fadeUp .3s ease both}
.ai{animation:fadeIn .25s ease both}
.as{animation:scaleUp .3s ease both}
.d1{animation-delay:.04s}.d2{animation-delay:.08s}.d3{animation-delay:.12s}
.d4{animation-delay:.16s}.d5{animation-delay:.2s}.d6{animation-delay:.24s}

/* ── Top app bar ── */
.topbar{
  position:sticky; top:0; z-index:200;
  background:#fff; border-bottom:var(--border);
  height:64px; display:flex; align-items:center;
  padding:0 8px 0 16px; gap:4px;
}
.topbar-logo{
  display:flex; align-items:center; gap:4px;
  margin-left:8px;
}
.topbar-logo-text{
  font-family:'Google Sans',sans-serif!important;
  font-size:1.375rem; font-weight:400; color:var(--gray-700);
  letter-spacing:-.01em;
}
.topbar-logo-text span{color:var(--green);}
.topbar-spacer{flex:1;}
.topbar-avatar{
  width:32px; height:32px; border-radius:50%;
  background:#1a73e8; color:#fff;
  font-family:'Roboto',sans-serif!important;
  font-size:.875rem; font-weight:500;
  display:flex; align-items:center; justify-content:center;
  cursor:pointer; flex-shrink:0;
}

/* ── Sidebar brand ── */
.sb-header{
  height:64px; display:flex; align-items:center;
  padding:0 16px; gap:4px; border-bottom:var(--border);
}
.sb-logo{
  font-family:'Google Sans',sans-serif!important;
  font-size:1.375rem; font-weight:400; color:var(--gray-700);
}
.sb-logo span{color:var(--green);}
.sb-divider{height:1px;background:var(--gray-200);margin:8px 0;}
.sb-section{
  font-size:.6875rem; font-weight:500;
  color:var(--gray-600); text-transform:uppercase;
  letter-spacing:.08em; padding:8px 16px 4px;
}
.sb-footer{
  padding:12px 16px; font-size:.75rem;
  color:var(--gray-600); border-top:var(--border);
  margin-top:8px;
}

/* ── Main content wrap ── */
.content{padding:24px 32px 80px; width:100%;}

/* ── Home page header ── */
.home-title{
  font-family:'Google Sans',sans-serif!important;
  font-size:1.75rem; font-weight:400; color:var(--gray-900);
  margin:0 0 24px; letter-spacing:-.01em;
}

/* ── Google Classroom card ── */
.gc-card{
  background:#fff; border-radius:var(--r8);
  box-shadow:var(--sh1); overflow:hidden;
  transition:box-shadow .2s ease; cursor:pointer;
  display:flex; flex-direction:column;
  margin-bottom:16px;
}
.gc-card:hover{box-shadow:var(--sh2);}
.gc-card-header{
  height:96px; position:relative;
  padding:16px; display:flex;
  flex-direction:column; justify-content:flex-end;
  overflow:hidden;
}
.gc-card-title{
  font-family:'Google Sans',sans-serif!important;
  font-size:1.125rem; font-weight:400;
  color:#fff; line-height:1.3;
  position:relative; z-index:1;
  white-space:nowrap; overflow:hidden;
  text-overflow:ellipsis;
}
.gc-card-section{
  font-size:.75rem; color:rgba(255,255,255,.85);
  position:relative; z-index:1;
  margin-top:2px;
  white-space:nowrap; overflow:hidden; text-overflow:ellipsis;
}
.gc-card-avatar{
  position:absolute; top:12px; right:12px;
  width:40px; height:40px; border-radius:50%;
  background:rgba(255,255,255,.2);
  display:flex; align-items:center; justify-content:center;
  font-size:1.4rem; z-index:1;
  transition:transform .2s ease;
}
.gc-card:hover .gc-card-avatar{transform:scale(1.08);}
.gc-card-body{
  padding:12px 16px 8px; flex:1;
  border-top:var(--border);
}
.gc-card-teacher{font-size:.75rem; color:var(--gray-700); margin-bottom:4px;}
.gc-card-status{margin-top:6px;}
.gc-card-footer{
  display:flex; align-items:center;
  justify-content:flex-end;
  padding:4px 8px 8px; gap:4px; border-top:var(--border);
}
.gc-chip{
  display:inline-flex; align-items:center; gap:4px;
  font-size:.6875rem; font-weight:500;
  padding:3px 10px; border-radius:100px;
  letter-spacing:.01em;
}
.chip-blue{background:#e8f0fe; color:#1a73e8;}
.chip-green{background:#e6f4ea; color:#1e8e3e;}
.chip-gray{background:var(--gray-100); color:var(--gray-600);}
.chip-red{background:#fce8e6; color:#d93025;}
.chip-yellow{background:#fef7e0; color:#b05f00;}

/* ── Stream page ── */
.stream-banner{
  border-radius:var(--r8); margin-bottom:0;
  overflow:hidden; position:relative;
  height:220px; display:flex;
  flex-direction:column; justify-content:flex-end;
  padding:24px 28px;
}
.stream-banner::before{
  content:'';position:absolute;inset:0;
  background:linear-gradient(to top,rgba(0,0,0,.45) 0%,transparent 55%);
}
.stream-banner-title{
  font-family:'Google Sans',sans-serif!important;
  font-size:2rem; font-weight:400; color:#fff;
  letter-spacing:-.01em; position:relative; z-index:1;
}
.stream-banner-sub{
  font-size:.9rem; color:rgba(255,255,255,.85);
  position:relative; z-index:1; margin-top:4px;
}
.stream-tabs{
  background:#fff; border-bottom:var(--border);
  display:flex; gap:0; margin-bottom:0;
}
.stream-tab{
  font-family:'Google Sans',sans-serif!important;
  font-size:.875rem; font-weight:500; color:var(--gray-600);
  padding:14px 24px; border-bottom:3px solid transparent;
  cursor:pointer; transition:color .15s,border-color .15s;
  letter-spacing:.01em; white-space:nowrap;
}
.stream-tab.active{color:var(--blue); border-bottom-color:var(--blue);}
.stream-tab:hover:not(.active){color:var(--gray-900); background:var(--gray-50);}

/* ── Material card (lesson/assignment) ── */
.mat-card{
  background:#fff; border-radius:var(--r8);
  box-shadow:var(--sh1); margin-bottom:12px;
  overflow:hidden;
  transition:box-shadow .2s ease;
  animation:fadeUp .3s ease both;
}
.mat-card:hover{box-shadow:var(--sh2);}
.mat-card-header{
  display:flex; align-items:center;
  padding:14px 16px 10px; gap:12px;
  border-bottom:var(--border);
}
.mat-card-icon{
  width:40px; height:40px; border-radius:50%;
  display:flex; align-items:center; justify-content:center;
  font-size:1.2rem; flex-shrink:0;
}
.mat-card-title{
  font-family:'Google Sans',sans-serif!important;
  font-size:.9375rem; font-weight:500; color:var(--gray-900);
}
.mat-card-sub{font-size:.75rem; color:var(--gray-600); margin-top:1px;}
.mat-card-body{padding:14px 16px 16px;}
.mat-card-body p{
  font-size:.875rem!important; color:var(--gray-700)!important;
  line-height:1.8!important; margin:0!important;
}

/* ── Quiz card ── */
.quiz-card{
  background:#fff; border-radius:var(--r8);
  box-shadow:var(--sh1); margin:16px 0 12px;
  padding:16px 20px; display:flex;
  align-items:flex-start; gap:14px;
}
.quiz-card-icon{
  width:44px; height:44px; border-radius:50%;
  background:#e8f0fe; display:flex;
  align-items:center; justify-content:center;
  font-size:1.3rem; flex-shrink:0;
}
.quiz-card-title{
  font-family:'Google Sans',sans-serif!important;
  font-size:.9375rem; font-weight:500; color:var(--gray-900);
  margin:0;
}
.quiz-card-sub{font-size:.75rem; color:var(--gray-600); margin:2px 0 0;}
.q-num{
  font-size:.6875rem; font-weight:500;
  color:var(--gray-600); text-transform:uppercase;
  letter-spacing:.08em; margin-bottom:4px;
}

/* ── Grade result ── */
.grade-pass{
  background:#e6f4ea; border:1px solid #ceead6;
  border-radius:var(--r8); padding:20px 24px;
  display:flex; align-items:center; gap:20px;
  margin:14px 0; flex-wrap:wrap;
  animation:scaleUp .35s cubic-bezier(.34,1.56,.64,1) both;
}
.grade-fail{
  background:#fce8e6; border:1px solid #f5c6c5;
  border-radius:var(--r8); padding:20px 24px;
  display:flex; align-items:center; gap:20px;
  margin:14px 0; flex-wrap:wrap;
  animation:scaleUp .35s cubic-bezier(.34,1.56,.64,1) both;
}
.grade-score{
  font-family:'Google Sans',sans-serif!important;
  font-size:3rem; font-weight:400; line-height:1;
  letter-spacing:-.03em; flex-shrink:0;
}
.grade-pass .grade-score{color:#1e8e3e;}
.grade-fail .grade-score{color:#d93025;}
.grade-label{
  font-size:.6875rem; font-weight:500;
  text-transform:uppercase; letter-spacing:.08em; margin-top:4px;
}
.grade-pass .grade-label{color:#1e8e3e;}
.grade-fail .grade-label{color:#d93025;}
.grade-msg{font-size:.875rem; color:var(--gray-700); line-height:1.65;}
.grade-msg strong{color:var(--gray-900);}

/* ── Grades table page ── */
.grades-table{
  background:#fff; border-radius:var(--r8);
  box-shadow:var(--sh1); width:100%;
  border-collapse:collapse; overflow:hidden;
}
.grades-table th{
  background:var(--gray-50); padding:10px 16px;
  font-size:.6875rem; font-weight:500; color:var(--gray-600);
  text-transform:uppercase; letter-spacing:.08em;
  text-align:left; border-bottom:var(--border);
}
.grades-table td{
  padding:13px 16px; border-bottom:1px solid #f1f3f4;
  font-size:.875rem; color:var(--gray-900);
  vertical-align:middle;
}
.grades-table tr:last-child td{border-bottom:none;}
.grades-table tr:hover td{background:var(--gray-50);}
.g-mono{font-family:'Roboto Mono','Courier New',monospace; font-weight:500; font-size:.875rem;}

/* ── Stat strip ── */
.stat-strip{
  background:#fff; border-radius:var(--r8);
  box-shadow:var(--sh1); padding:20px 24px;
  margin-bottom:24px; display:flex;
  gap:0;
}
.stat-item{
  flex:1; text-align:center;
  border-right:var(--border);
}
.stat-item:last-child{border-right:none;}
.stat-val{
  font-family:'Google Sans',sans-serif!important;
  font-size:1.75rem; font-weight:400;
  letter-spacing:-.02em; line-height:1;
  margin-bottom:4px;
}
.stat-lbl{
  font-size:.6875rem; font-weight:500;
  color:var(--gray-600); text-transform:uppercase;
  letter-spacing:.06em;
}
.prog-bar{height:3px;background:var(--gray-200);border-radius:99px;overflow:hidden;margin-top:10px 24px 0;}
.prog-fill{height:100%;border-radius:99px;transition:width .8s ease;}

/* ── Divider ── */
hr.mat{border:none;border-top:var(--border);margin:10px 0;}

/* ── Mobile ── */
@media(max-width:768px){
  .content{padding:16px 12px 72px;}
  .stream-banner{height:160px;}
  .stream-banner-title{font-size:1.4rem;}
  .grades-table{display:block;overflow-x:auto;}
  .stat-strip{flex-wrap:wrap;}
  .stat-item{min-width:120px; border-right:none; border-bottom:var(--border); padding-bottom:12px; margin-bottom:12px;}
  .stat-item:last-child{border-bottom:none; margin-bottom:0; padding-bottom:0;}
}
</style>
""", unsafe_allow_html=True)

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-header">
      <div class="sb-logo">Danilo <span>Classroom</span></div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div style="height:8px"></div>', unsafe_allow_html=True)
    st.button("🏠  Home", on_click=nav, args=("home",), use_container_width=True)
    st.button("📊  Grades", on_click=nav, args=("grades",), use_container_width=True)

    st.markdown('<div class="sb-section">Classes</div>', unsafe_allow_html=True)
    for mk, mod in MODS.items():
        locked = mk not in st.session_state.unlocked
        label = f"{'🔒  ' if locked else mod['icon']+'  '}{mod['label']}"
        st.button(label, on_click=nav, args=(mk,), disabled=locked, use_container_width=True)

    st.markdown("""
    <div class="sb-footer">© 2025 DANILO Learning<br>All rights reserved.</div>
    """, unsafe_allow_html=True)

# ─── Top bar ──────────────────────────────────────────────────────────────────
st.markdown("""
<div class="topbar">
  <div class="topbar-logo">
    <svg width="40" height="40" viewBox="0 0 40 40" style="flex-shrink:0"><rect width="40" height="40" rx="8" fill="#0F9D58"/><text x="20" y="28" text-anchor="middle" font-size="22" fill="white" font-family="sans-serif">D</text></svg>
    <span class="topbar-logo-text" style="margin-left:8px;">Danilo <span>Classroom</span></span>
  </div>
  <div class="topbar-spacer"></div>
  <div class="topbar-avatar">D</div>
</div>
""", unsafe_allow_html=True)

# ─── Content wrapper ──────────────────────────────────────────────────────────
st.markdown('<div class="content">', unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════════════
#  HOME
# ════════════════════════════════════════════════════════════════════
if st.session_state.current_view == "home":
    st.markdown('<div class="home-title au">Welcome, Danilo 👋</div>', unsafe_allow_html=True)

    # Stat strip
    all_m = ["1","2","3","4"]
    sc_taken = [st.session_state[f"m{m}_qr"] for m in all_m if st.session_state[f"m{m}_qd"]]
    avg_acc = (sum(sc_taken)/(len(sc_taken)*5)*100) if sc_taken else 0
    passed = sum(1 for m in all_m if st.session_state[f"m{m}_qd"] and st.session_state[f"m{m}_qr"]>=4)
    unlocked = len(st.session_state.unlocked)

    st.markdown(f"""
    <div class="stat-strip au d1">
      <div class="stat-item">
        <div class="stat-val" style="color:#1a73e8;">{unlocked}/4</div>
        <div class="stat-lbl">Classes Unlocked</div>
      </div>
      <div class="stat-item">
        <div class="stat-val" style="color:#0f9d58;">{passed}/4</div>
        <div class="stat-lbl">Assessments Passed</div>
      </div>
      <div class="stat-item">
        <div class="stat-val" style="color:#f9ab00;">{avg_acc:.0f}%</div>
        <div class="stat-lbl">Mean Accuracy</div>
      </div>
      <div class="stat-item">
        <div class="stat-val" style="color:#ea4335;">{int(passed/4*100)}%</div>
        <div class="stat-lbl">Overall Progress</div>
      </div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<p style="font-size:.75rem;font-weight:500;color:#5f6368;text-transform:uppercase;letter-spacing:.08em;margin:0 0 12px;" class="au d2">Enrolled Classes</p>', unsafe_allow_html=True)

    # Class cards — 3 per row
    items = list(MODS.items())
    for row in range(0, len(items), 3):
        cols = st.columns(3, gap="medium")
        for ci, (mk, mod) in enumerate(items[row:row+3]):
            locked = mk not in st.session_state.unlocked
            m = mod["k"]
            submitted = st.session_state[f"m{m}_qd"]
            score = st.session_state[f"m{m}_qr"]
            done = submitted and score >= 4

            if done:
                badge = '<span class="gc-chip chip-green">✓ Complete</span>'
            elif locked:
                badge = '<span class="gc-chip chip-gray">🔒 Locked</span>'
            else:
                badge = '<span class="gc-chip chip-blue">● Active</span>'

            delay = f"d{min(row*3+ci+1,6)}"
            with cols[ci]:
                st.markdown(f"""
                <div class="gc-card {delay} au">
                  <div class="gc-card-header" style="background:{mod['header_bg']};background-image:{mod['pattern']};">
                    <div class="gc-card-avatar">{mod['icon']}</div>
                    <div class="gc-card-title">{mod['label']}</div>
                    <div class="gc-card-section">{mod['section']}</div>
                  </div>
                  <div class="gc-card-body">
                    <div class="gc-card-teacher">{mod['teacher']}</div>
                    <div class="gc-card-status">{badge}</div>
                  </div>
                  <div class="gc-card-footer">
                    <span style="font-size:.7rem;color:#80868b;">{len(mod['quiz'])} questions</span>
                  </div>
                </div>""", unsafe_allow_html=True)
                st.button(
                    "Open class →" if not locked else "Locked",
                    key=f"home_{mk}", on_click=nav, args=(mk,),
                    disabled=locked, use_container_width=True
                )

# ════════════════════════════════════════════════════════════════════
#  CLASS / STREAM VIEW
# ════════════════════════════════════════════════════════════════════
elif st.session_state.current_view in MODS:
    mk = st.session_state.current_view
    mod = MODS[mk]
    m = mod["k"]
    qd = mod["quiz"]
    pm = len(qd) - 1

    # Back button
    col_back, col_space = st.columns([1,8])
    with col_back:
        st.button("← Home", key=f"back_{mk}", on_click=nav, args=("home",))

    # Stream banner
    st.markdown(f"""
    <div class="stream-banner" style="background:{mod['header_bg']};background-image:{mod['pattern']};">
      <div class="stream-banner-title">{mod['icon']} {mod['label']}</div>
      <div class="stream-banner-sub">{mod['section']} · {mod['teacher']}</div>
    </div>""", unsafe_allow_html=True)

    # Fake tabs — show Classwork always
    st.markdown("""
    <div class="stream-tabs">
      <div class="stream-tab">Stream</div>
      <div class="stream-tab active">Classwork</div>
      <div class="stream-tab">People</div>
    </div>""", unsafe_allow_html=True)

    st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)

    # Two-column layout: lessons left, quiz right
    left, right = st.columns([3, 2], gap="large")

    with left:
        st.markdown('<p style="font-size:.6875rem;font-weight:500;color:#5f6368;text-transform:uppercase;letter-spacing:.08em;margin:0 0 10px;">Lesson Material</p>', unsafe_allow_html=True)
        for i, (ico, title, body) in enumerate(mod["topics"]):
            icon_colors = ["#e8f0fe","#e6f4ea","#fce8e6","#fef7e0"]
            icon_text_colors = ["#1a73e8","#1e8e3e","#d93025","#b05f00"]
            ic = icon_colors[i % len(icon_colors)]
            itc = icon_text_colors[i % len(icon_text_colors)]
            st.markdown(f"""
            <div class="mat-card d{i+1}">
              <div class="mat-card-header">
                <div class="mat-card-icon" style="background:{ic};color:{itc};">{ico}</div>
                <div>
                  <div class="mat-card-title">{title}</div>
                  <div class="mat-card-sub">Reading material</div>
                </div>
              </div>
              <div class="mat-card-body"><p>{body}</p></div>
            </div>""", unsafe_allow_html=True)

    with right:
        st.markdown('<p style="font-size:.6875rem;font-weight:500;color:#5f6368;text-transform:uppercase;letter-spacing:.08em;margin:0 0 10px;">Assessment</p>', unsafe_allow_html=True)

        st.markdown(f"""
        <div class="quiz-card">
          <div class="quiz-card-icon">📋</div>
          <div>
            <p class="quiz-card-title">Formative Assessment</p>
            <p class="quiz-card-sub">{len(qd)} questions · Pass: {pm}/{len(qd)} · Unlimited retries</p>
          </div>
        </div>""", unsafe_allow_html=True)

        sk = f"m{m}_qs"
        uk = f"m{m}_qd"
        ck = f"m{m}_qr"

        if not st.session_state[sk]:
            st.button("▶  Start Quiz", key=f"st_{mk}")
            if st.session_state.get(f"st_{mk}"):
                st.session_state[sk] = True
                st.rerun()

        if st.session_state[sk]:
            with st.form(key=f"{mk}_form", clear_on_submit=False):
                answers = []
                for i, q in enumerate(qd):
                    st.markdown(f'<div class="q-num">Question {i+1} of {len(qd)}</div>', unsafe_allow_html=True)
                    st.markdown(f"**{q['q']}**")
                    a = st.radio("", q["o"], key=f"{mk}_q{i}", label_visibility="collapsed", index=None)
                    answers.append(a)
                    if i < len(qd)-1:
                        st.markdown('<hr class="mat">', unsafe_allow_html=True)
                st.markdown('<div style="height:4px"></div>', unsafe_allow_html=True)
                submitted = st.form_submit_button("Submit")

            if submitted:
                if None in answers:
                    st.error("⚠️ Please answer all questions.")
                else:
                    score = sum(1 for i,q in enumerate(qd) if answers[i]==q["a"])
                    st.session_state[ck] = score
                    st.session_state[uk] = True

            if st.session_state[uk]:
                score = st.session_state[ck]
                ok = score >= pm
                pct = int(score/len(qd)*100)
                cls = "grade-pass" if ok else "grade-fail"
                badge = "✓ Passed" if ok else "✗ Below pass mark"
                msg = (
                    f"<strong>Excellent work!</strong> You scored {pct}% and have demonstrated mastery of this topic. <span style='color:#1e8e3e;font-weight:500;'>{mod['umsg']}</span>"
                    if ok else
                    f"<strong>Keep trying.</strong> You scored {pct}%. Review the lesson cards on the left and submit again — you need {pm}/{len(qd)} to pass."
                )
                st.markdown(f"""
                <div class="{cls}">
                  <div>
                    <div class="grade-score">{score}/{len(qd)}</div>
                    <div class="grade-label">{badge}</div>
                  </div>
                  <div class="grade-msg">{msg}</div>
                </div>""", unsafe_allow_html=True)
                if ok:
                    nxt = mod.get("next")
                    if nxt and nxt not in st.session_state.unlocked:
                        st.session_state.unlocked.append(nxt)
                else:
                    if st.button("🔄 Retry", key=f"rt_{mk}"):
                        st.session_state[uk] = False
                        st.rerun()

# ════════════════════════════════════════════════════════════════════
#  GRADES
# ════════════════════════════════════════════════════════════════════
elif st.session_state.current_view == "grades":
    col_back, _ = st.columns([1,8])
    with col_back:
        st.button("← Home", key="back_g", on_click=nav, args=("home",))

    st.markdown('<div class="home-title au">Grades</div>', unsafe_allow_html=True)

    all_m = ["1","2","3","4"]
    subs   = {m: st.session_state[f"m{m}_qd"] for m in all_m}
    scores = {m: st.session_state[f"m{m}_qr"] for m in all_m}
    taken  = [scores[m] for m in all_m if subs[m]]
    avg_a  = (sum(taken)/(len(taken)*5)*100) if taken else 0
    comp   = sum(1 for m in all_m if subs[m] and scores[m]>=4)
    unl    = len(st.session_state.unlocked)

    st.markdown(f"""
    <div class="stat-strip au d1">
      <div class="stat-item">
        <div class="stat-val" style="color:#1a73e8;">{unl}/4</div>
        <div class="stat-lbl">Unlocked</div>
      </div>
      <div class="stat-item">
        <div class="stat-val" style="color:#0f9d58;">{avg_a:.0f}%</div>
        <div class="stat-lbl">Mean Accuracy</div>
      </div>
      <div class="stat-item">
        <div class="stat-val" style="color:#f9ab00;">{comp}/4</div>
        <div class="stat-lbl">Passed</div>
      </div>
      <div class="stat-item">
        <div class="stat-val" style="color:#ea4335;">{int(comp/4*100)}%</div>
        <div class="stat-lbl">Progress</div>
      </div>
    </div>""", unsafe_allow_html=True)

    rows = ""
    for mk, mod in MODS.items():
        m = mod["k"]; total = len(mod["quiz"])
        locked = mk not in st.session_state.unlocked
        sub = subs[m]; sc = scores[m]; done = sub and sc>=4

        if locked:
            sh = '<span class="gc-chip chip-gray">🔒 Locked</span>'
            sd = gd = '<span style="color:#bdc1c6;">—</span>'
        elif done:
            sh = '<span class="gc-chip chip-green">✓ Passed</span>'
            sd = f'<span class="g-mono" style="color:#1e8e3e;">{sc}/{total}</span>'
            gd = f'<span class="g-mono" style="color:#1e8e3e;">{int(sc/total*100)}%</span>'
        elif sub:
            sh = '<span class="gc-chip chip-red">✗ Below Pass</span>'
            sd = f'<span class="g-mono" style="color:#d93025;">{sc}/{total}</span>'
            gd = f'<span class="g-mono" style="color:#d93025;">{int(sc/total*100)}%</span>'
        else:
            sh = '<span class="gc-chip chip-yellow">○ Not Attempted</span>'
            sd = gd = '<span style="color:#bdc1c6;">—</span>'

        rows += f"""
        <tr>
          <td style="width:36px;font-size:1.15rem;">{mod['icon']}</td>
          <td style="font-weight:500;">{mod['label']}</td>
          <td style="color:#5f6368;font-size:.8rem;">{mod['section']}</td>
          <td style="color:#5f6368;font-size:.8rem;">{mod['teacher']}</td>
          <td>{sh}</td>
          <td>{sd}</td>
          <td>{gd}</td>
        </tr>"""

    st.markdown(f"""
    <table class="grades-table au d2">
      <thead>
        <tr>
          <th></th><th>Class</th><th>Topic</th><th>Teacher</th>
          <th>Status</th><th>Score</th><th>Grade</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
