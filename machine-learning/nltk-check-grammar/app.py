import streamlit as st
from rake_nltk import Rake
import nltk
import re
import spacy
from difflib import get_close_matches

nltk.download('stopwords', quiet=True)
nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)

st.set_page_config(page_title="Grammar & Keywords", page_icon="✍️", layout="centered")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Source+Sans+3:wght@400;600&display=swap');
html, body, [class*="css"] { font-family: 'Source Sans 3', sans-serif; background-color: #0f0f0f; color: #e8e4dc; }
h1,h2,h3 { font-family: 'Playfair Display', serif; }
.stTextArea textarea {
    background-color: #1a1a1a !important; color: #e8e4dc !important;
    border: 1px solid #333 !important; border-radius: 8px !important;
    font-family: 'Source Sans 3', sans-serif !important; font-size: 15px !important;
}
.stButton > button {
    background: linear-gradient(135deg, #c9a96e, #a07840); color: #0f0f0f;
    font-weight: 700; border: none; border-radius: 6px; padding: 0.6rem 2rem;
    font-size: 15px; letter-spacing: 0.05em; transition: opacity 0.2s;
}
.stButton > button:hover { opacity: 0.85; }
.error-item {
    background: #1f1414; border-left: 3px solid #c0392b;
    border-radius: 0 6px 6px 0; padding: 0.7rem 1rem; margin-bottom: 0.6rem; font-size: 14px;
}
.error-item .wrong { color: #e74c3c; font-weight: 600; }
.error-item .arrow { color: #888; margin: 0 6px; }
.error-item .fix   { color: #2ecc71; font-weight: 600; }
.error-item .etype { display:inline-block; font-size:11px; background:#2a1a1a; color:#e07070;
                     border-radius:4px; padding:1px 6px; margin-left:6px; vertical-align:middle; }
.error-item .msg   { color: #aaa; font-size: 13px; margin-top: 4px; }
.keyword-tag {
    display: inline-block; background: #1e1a12; border: 1px solid #c9a96e55;
    color: #c9a96e; padding: 4px 12px; border-radius: 20px; margin: 4px;
    font-size: 13px; font-weight: 600;
}
.section-title {
    font-family: 'Playfair Display', serif; font-size: 1.1rem; color: #c9a96e;
    margin-bottom: 0.8rem; border-bottom: 1px solid #2a2a2a; padding-bottom: 0.4rem;
}
.stat-box { display:inline-block; background:#1a1a1a; border:1px solid #2a2a2a;
            border-radius:8px; padding:0.5rem 1.2rem; margin-right:0.5rem; text-align:center; }
.stat-num   { font-size:1.5rem; font-weight:700; color:#c9a96e; }
.stat-label { font-size:11px; color:#777; text-transform:uppercase; letter-spacing:0.08em; }
.corrected-box {
    background: #0e1f14; border: 1px solid #2ecc7155; border-radius: 10px;
    padding: 1.2rem 1.5rem; color: #b8f5c8; font-size: 15px; line-height: 1.8;
}
</style>
""", unsafe_allow_html=True)

# ── Load spaCy ────────────────────────────────────────────────────────────────
@st.cache_resource
def load_nlp():
    try:
        return spacy.load("en_core_web_sm")
    except OSError:
        from spacy.cli import download
        download("en_core_web_sm")
        return spacy.load("en_core_web_sm")

nlp = load_nlp()

# ── Build valid English word set (including all conjugations) ─────────────────
# Auto-generate past/ing/3sg forms so valid words are NEVER flagged as misspelled
def _build_valid_set():
    base_verbs = """miss work go do make take come leave run stand sit read write speak listen
    walk play learn teach open close meet send receive buy sell build break fix check call wait
    want need plan try understand keep feel give think know find use help start follow move turn
    eat drink sleep ask look watch say tell show drive bring hold fall become begin grow draw
    fly swim catch throw lose choose forget forgive keep mean pay raise ring rise run see
    shine sing sink speak spend spread stand steal strike swear sweep wake wear win write""".split()

    valid = set()
    for v in base_verbs:
        valid.add(v)
        # -ed form
        if v.endswith('e'):
            valid.add(v + 'd')
        elif v.endswith('y') and len(v) > 1 and v[-2] not in 'aeiou':
            valid.add(v[:-1] + 'ied')
        else:
            valid.add(v + 'ed')
        # -ing form
        if v.endswith('ie'):
            valid.add(v[:-2] + 'ying')
        elif v.endswith('e') and not v.endswith('ee'):
            valid.add(v[:-1] + 'ing')
        else:
            valid.add(v + 'ing')
        # -s / -es form
        if v.endswith(('s', 'x', 'z', 'o')) or v.endswith(('ch', 'sh')):
            valid.add(v + 'es')
        else:
            valid.add(v + 's')

    # Irregular past tenses
    irregulars = """went done made took came left ran stood sat read wrote spoke walked played
    learned taught opened closed met sent received bought sold built broke fixed checked called
    waited wanted needed planned tried understood kept felt gave thought knew found used helped
    started followed moved turned ate drank slept asked looked watched said told showed drove
    brought held fell became began grew drew flew swam caught threw lost chose forgot forgave
    meant paid rang rose saw shone sang sank spent spread stole struck swore swept woke wore
    won written spoken grown drawn flown swum caught thrown lost chosen forgotten forgiven kept
    meant paid rung risen seen shone sung sunk spent spread stolen struck sworn swept woken worn
    won fell grown ran swam drove brought held became began""".split()
    valid.update(irregulars)

    # Common adjectives, nouns, adverbs that difflib might wrongly "correct"
    extras = """missed worked going goes coming leaving running standing sitting reading writing
    speaking listening missing working making taking helping starting following moving turning
    eating drinking sleeping asking looking watching saying telling showing missed trained
    tomorrow yesterday today morning evening night early late again already still yet just
    really very quite almost never always often sometimes usually actually basically finally
    probably definitely certainly perhaps maybe possibly obviously clearly simply exactly
    different important possible necessary available beautiful wonderful terrible horrible
    amazing interesting exciting boring difficult easy simple complex serious funny happy
    sad angry tired hungry thirsty cold hot warm cool big small large little old new good
    bad great nice fine wrong right true false strong weak fast slow long short high low
    early late young old rich poor busy free full empty open closed hard soft light dark
    train trains bus buses car cars plane planes bike bikes road roads street streets
    station stations airport airports office offices school schools hospital hospitals
    market markets bank banks store stores shop shops library libraries home homes
    house houses room rooms door doors window windows table tables chair chairs
    book books phone phones computer computers water food money time day days week weeks
    month months year years morning mornings evening evenings night nights""".split()
    valid.update(extras)

    return valid

VALID_WORDS = _build_valid_set()

# ── Full English word list for fuzzy candidate matching ──────────────────────
_RAW = """the be to of and a in that have it for not on with he as you do at this his by
from they we say her she or an will my one all would there their what so up out if about
who get which go me when make can like time no just him know take people into year your
good some could them see other than then now look only come its over think also back after
use two how our work first well way even new want because any these give day most us
above across again against almost alone along already although always among another anything
around away ball bank bear beat began behind believe belong best better bit black blood blue
board body book born both box boy bring broke brother building built call came car carry
case cat change children choose city clear close cold colour common complete copy cost
country cover cut dark deep describe died different direct discuss distance divide does dog
done draw drink drive dry during early east eight either else end enough ever every
everywhere far few find fly follow food force form four free friend front full game gave
girl give glass god going gold got great green ground grow half hand hang hard head heard
heart high hold hour human hundred important include indeed inside instead keep kind known
large last later learn left less light line live long look lose lot low main many mark
might mile mind minute miss model money moon more morning most mother move much music
natural near need nine north notice often old once open order other over own page paper
particular past pattern peace person place plan plant point poor position possible power
pretty probably problem process product prove pull question quick quite reach read ready
real reason red represent rest result right river road rock room round school sea second
seem set seven shape show side simple since six sleep slow small song soon sound south
special square start state still stop story straight strong study such sun sure surface
system table tell ten third though thousand three throughout today together told top town
tree try turn under understand unit until upon usually very voice wait war watch water week
went west while whole wide wind without wonder word world write yes yet young area ask fast
felt field figure fill fish fit five floor free front full game gave girl glass going gold
got great green ground grow half hand hang hard head heard heart high hold hour include
indeed inside instead keep known large learn left less line local minute model money moon
morning mother move natural need nine north notice open order paper particular past pattern
peace personal plan play poor post pretty process product prove question run saw sea seem
seven shape since six slow song soon space special square straight strong sun sure surface
table third thousand throughout today told town travel tree try understand unit voice wait
war watch wide wonder wrote play space travel local personal post office home school
hospital market station airport bank store shop library gym park university college hotel
restaurant church mosque temple train bus plane bike road street building
yesterday tomorrow today morning evening tonight already now soon early late
missed worked trained called missed arrived failed passed helped""".split()

ENGLISH_WORDS = list(set(w.lower() for w in _RAW if len(w) > 2))

# ── Constants ─────────────────────────────────────────────────────────────────
SKIP_SPELL = {
    "i", "a", "ok", "dr", "mr", "mrs", "ms", "st", "vs", "etc",
    "eg", "ie", "am", "pm", "hi", "hey", "gonna", "wanna", "gotta",
    "yeah", "yep", "nope", "hmm", "uh", "um"
}

MODALS    = {"should", "could", "would", "will", "can", "may", "might", "must", "shall"}
AUX_BE    = {"am", "is", "are", "was", "were"}
AUX_HAVE  = {"has", "have", "had"}

# Nouns that always need "the" (locations + common transport)
NEEDS_THE = {
    "office", "hospital", "school", "market", "station", "airport",
    "bank", "store", "shop", "library", "gym", "park", "university",
    "college", "hotel", "restaurant", "church", "mosque", "temple",
    "train", "bus", "plane", "subway", "metro"
}

# Past-tense time words
PAST_MARKERS   = {"yesterday", "ago", "last", "recently", "earlier", "previously", "formerly"}
# Future-tense time words
FUTURE_MARKERS = {"tomorrow", "soon", "later", "next", "tonight", "eventually"}

# Verb helper functions
def make_ing(base: str) -> str:
    b = base.lower()
    if b.endswith("ie"):   return b[:-2] + "ying"
    if b.endswith("e") and not b.endswith("ee"): return b[:-1] + "ing"
    if (len(b) >= 3 and b[-1] not in "aeiouywxh"
            and b[-2] in "aeiou" and b[-3] not in "aeiou"):
        return b + b[-1] + "ing"
    return b + "ing"

def make_3sg(base: str) -> str:
    b = base.lower()
    if b.endswith(("s","x","z","o")) or b.endswith(("ch","sh")): return b + "es"
    if b.endswith("y") and b[-2] not in "aeiou": return b[:-1] + "ies"
    return b + "s"

# ── Fuzzy spell correction ────────────────────────────────────────────────────
def fuzzy_correct(word: str) -> str:
    lower = word.lower()
    if lower in SKIP_SPELL or len(lower) <= 2:
        return word
    # KEY FIX: if word is already a valid English form, don't touch it
    if lower in VALID_WORDS:
        return word
    # Also check against the broader candidate list
    if lower in set(ENGLISH_WORDS):
        return word
    for cutoff in (0.82, 0.76):
        matches = get_close_matches(lower, ENGLISH_WORDS, n=1, cutoff=cutoff)
        if matches:
            return matches[0]
    return word

def get_spell_corrections(text: str):
    corrections = []
    seen = set()
    for token in re.findall(r'\b[a-zA-Z]+\b', text):
        lower = token.lower()
        if lower in seen or lower in SKIP_SPELL or len(lower) <= 2:
            continue
        seen.add(lower)
        fixed = fuzzy_correct(lower)
        if fixed != lower:
            corrections.append((token, fixed))
    return corrections

# ── Grammar checks ────────────────────────────────────────────────────────────
def check_grammar(doc, text: str):
    errors = []
    tokens = list(doc)

    # Detect time-marker context for tense rules
    text_lower = text.lower()
    has_past_marker   = any(m in text_lower for m in PAST_MARKERS)
    has_future_marker = any(m in text_lower for m in FUTURE_MARKERS)

    i = 0
    while i < len(tokens):
        tok   = tokens[i]
        lower = tok.text.lower()
        pos   = tok.pos_
        tag   = tok.tag_
        dep   = tok.dep_

        # ── Rule 1: be-aux + non-progressive verb → progressive ───────────────
        # "am works" → "am working", "is go" → "is going"
        if lower in AUX_BE and pos in ("AUX", "VERB"):
            if i + 1 < len(tokens):
                nxt = tokens[i + 1]
                nxt_l = nxt.text.lower()
                if (nxt.pos_ in ("VERB",) and nxt.tag_ not in ("VBG",)
                        and nxt_l not in AUX_BE and nxt_l not in MODALS
                        and nxt_l not in AUX_HAVE):
                    base = nxt.lemma_.lower()
                    ing  = make_ing(base)
                    if nxt_l != ing:
                        errors.append({
                            "wrong": f"{tok.text} {nxt.text}",
                            "fix":   f"{tok.text} {ing}",
                            "type":  "Grammar",
                            "explanation": f"After '{tok.text}' use progressive form: '{tok.text} {ing}'"
                        })
                        text = re.sub(
                            r'\b' + re.escape(tok.text) + r'\s+' + re.escape(nxt.text) + r'\b',
                            f"{tok.text} {ing}", text, count=1, flags=re.IGNORECASE
                        )

        # ── Rule 2: has/have + past-tense verb (VBD) → simple past ───────────
        # "has missed" (wrong) → "missed"
        # Note: has/have + VBN (past participle) is valid perfect tense — leave alone
        if lower in ("has", "have") and pos in ("AUX", "VERB"):
            if i + 1 < len(tokens):
                nxt = tokens[i + 1]
                if nxt.tag_ == "VBD":  # past tense (not participle)
                    errors.append({
                        "wrong": f"{tok.text} {nxt.text}",
                        "fix":   nxt.text,
                        "type":  "Grammar",
                        "explanation": f"'{tok.text} {nxt.text}' is incorrect; use simple past: '{nxt.text}'"
                    })
                    text = re.sub(
                        r'\b' + re.escape(tok.text) + r'\s+' + re.escape(nxt.text) + r'\b',
                        nxt.text, text, count=1, flags=re.IGNORECASE
                    )

        # ── Rule 3: modal + non-base verb → base form ─────────────────────────
        # "should leaves" → "should leave", "can goes" → "can go"
        if lower in MODALS:
            for j in range(i + 1, min(i + 4, len(tokens))):
                nxt = tokens[j]
                if nxt.pos_ == "VERB":
                    base = nxt.lemma_.lower()
                    if nxt.text.lower() != base:
                        errors.append({
                            "wrong": f"{tok.text} {nxt.text}",
                            "fix":   f"{tok.text} {base}",
                            "type":  "Grammar",
                            "explanation": f"After modal '{tok.text}', use base verb form: '{base}'"
                        })
                        text = re.sub(
                            r'\b' + re.escape(nxt.text) + r'\b',
                            base, text, count=1, flags=re.IGNORECASE
                        )
                    break

        # ── Rule 4: Subject-verb agreement he/she/it + bare verb ──────────────
        if dep == "nsubj" and pos == "PRON" and lower in ("he", "she", "it"):
            verb = tok.head
            if verb.pos_ == "VERB" and verb.tag_ == "VB":
                fix = make_3sg(verb.lemma_)
                errors.append({
                    "wrong": f"{tok.text} {verb.text}",
                    "fix":   f"{tok.text} {fix}",
                    "type":  "Agreement",
                    "explanation": f"'{tok.text}' needs '{fix}' not '{verb.text}'"
                })
                text = re.sub(r'\b' + re.escape(verb.text) + r'\b', fix, text, count=1)

        # ── Rule 5: Missing article before singular countable nouns ───────────
        if pos == "NOUN" and tag == "NN" and lower in NEEDS_THE:
            has_det     = any(c.dep_ == "det" for c in tok.children)
            prev        = tokens[i - 1] if i > 0 else None
            prev_is_det = prev and prev.pos_ == "DET" if prev else False
            if not has_det and not prev_is_det:
                errors.append({
                    "wrong": tok.text,
                    "fix":   f"the {tok.text}",
                    "type":  "Grammar",
                    "explanation": f"Missing article: use 'the {tok.text}'"
                })
                text = re.sub(
                    r'(?<!\bthe )\b' + re.escape(tok.text) + r'\b',
                    f"the {tok.text}", text, count=1
                )

        # ── Rule 6: tomorrow + past tense verb → fix tense conflict ───────────
        # "missed train tomorrow" → "tomorrow" should be "yesterday"
        if lower == "tomorrow":
            # Check if there's a past tense verb in the sentence
            has_past_verb = any(
                t.tag_ in ("VBD", "VBN") for t in doc
            )
            if has_past_verb:
                errors.append({
                    "wrong": "tomorrow",
                    "fix":   "yesterday",
                    "type":  "Tense",
                    "explanation": "Past tense verb conflicts with 'tomorrow'; use 'yesterday'"
                })
                text = re.sub(r'\btomorrow\b', 'yesterday', text, flags=re.IGNORECASE)

        # ── Rule 7: yesterday + future/present verb → fix tense conflict ──────
        if lower == "yesterday":
            has_present_verb = any(
                t.tag_ in ("VBP", "VBZ", "VB") and t.pos_ == "VERB"
                for t in doc
            )
            if has_present_verb:
                # Find the present verb and suggest past form
                for t in doc:
                    if t.tag_ in ("VBP", "VBZ") and t.pos_ == "VERB":
                        lemma = t.lemma_
                        past  = lemma + "d" if lemma.endswith("e") else lemma + "ed"
                        errors.append({
                            "wrong": t.text,
                            "fix":   past,
                            "type":  "Tense",
                            "explanation": f"'yesterday' needs past tense: use '{past}' not '{t.text}'"
                        })
                        text = re.sub(r'\b' + re.escape(t.text) + r'\b', past, text, count=1)
                        break

        # ── Rule 8: Wrong word order "home go" → "go home" ───────────────────
        if pos == "VERB" and dep == "ROOT" and "?" not in text:
            FOLLOW_WORDS = {"home", "here", "there", "away", "back", "outside", "inside"}
            for child in tok.children:
                if child.dep_ in ("advmod", "npadvmod") and child.i < tok.i:
                    if child.text.lower() in FOLLOW_WORDS:
                        errors.append({
                            "wrong": f"{child.text} {tok.text}",
                            "fix":   f"{tok.text} {child.text}",
                            "type":  "Word Order",
                            "explanation": f"Verb '{tok.text}' should come before '{child.text}'"
                        })
                        text = re.sub(
                            r'\b' + re.escape(child.text) + r'\s+' + re.escape(tok.text) + r'\b',
                            f"{tok.text} {child.text}", text, count=1, flags=re.IGNORECASE
                        )

        # ── Rule 9: Question word order "what should time I" → "what time should I" ──
        if lower in ("what", "when", "where", "which", "how") and "?" in text:
            if i + 1 < len(tokens) and tokens[i + 1].text.lower() in MODALS:
                modal_tok = tokens[i + 1]
                if i + 2 < len(tokens) and tokens[i + 2].pos_ == "NOUN":
                    noun_tok    = tokens[i + 2]
                    wrong_order = f"{tok.text} {modal_tok.text} {noun_tok.text}"
                    right_order = f"{tok.text} {noun_tok.text} {modal_tok.text}"
                    errors.append({
                        "wrong": wrong_order,
                        "fix":   right_order,
                        "type":  "Word Order",
                        "explanation": f"Noun phrase comes before modal in questions: '{right_order}'"
                    })
                    text = re.sub(
                        re.escape(wrong_order), right_order, text, count=1, flags=re.IGNORECASE
                    )

        i += 1

    # ── Rule 10: Space before punctuation ─────────────────────────────────────
    if re.search(r'\w\s+[?.!,;:]', text):
        errors.append({
            "wrong": "word [space] ?/./!",
            "fix":   "word?/word./word!",
            "type":  "Punctuation",
            "explanation": "Remove the space before punctuation marks"
        })
        text = re.sub(r'\s+([?.!,;:])', r'\1', text)

    # ── Rule 11: Lowercase pronoun 'i' ────────────────────────────────────────
    if re.search(r'(?<![a-zA-Z])\bi\b(?![a-zA-Z])', text):
        errors.append({
            "wrong": "i",
            "fix":   "I",
            "type":  "Capitalization",
            "explanation": "The pronoun 'I' must always be capitalized"
        })
    text = re.sub(r'(?<![a-zA-Z])\bi\b(?![a-zA-Z])', 'I', text)

    # ── Rule 12: Sentence-start capitalization ────────────────────────────────
    def cap_first(m): return m.group(0).capitalize()
    new_text = re.sub(r'(?:^|(?<=[.!?])\s+)([a-z])', cap_first, text)
    if new_text != text:
        errors.append({
            "wrong": text[0] if text else "",
            "fix":   text[0].upper() if text else "",
            "type":  "Capitalization",
            "explanation": "First word of a sentence must be capitalized"
        })
        text = new_text

    text = re.sub(r'  +', ' ', text).strip()
    return errors, text

# ── Full pipeline ─────────────────────────────────────────────────────────────
def analyse(text: str):
    errors          = []
    corrected       = text
    corrected_words = set()

    # Step 1: Fuzzy spell correction (valid words are protected)
    for original, fixed in get_spell_corrections(text):
        errors.append({
            "wrong": original,
            "fix":   fixed,
            "type":  "Spelling",
            "explanation": f"'{original}' is misspelled; corrected to '{fixed}'"
        })
        corrected = re.sub(r'\b' + re.escape(original) + r'\b', fixed, corrected, flags=re.IGNORECASE)
        corrected_words.add(original.lower())

    # Step 2: Parse CORRECTED text with spaCy (key: clean input = better tags)
    doc = nlp(corrected)

    # Step 3: Grammar checks
    grammar_errors, corrected = check_grammar(doc, corrected)
    errors.extend(grammar_errors)

    return errors, corrected, corrected_words

# ── Keyword extraction (strip misspelled tokens) ──────────────────────────────
def extract_keywords(text: str, corrected_words: set) -> list:
    clean = " ".join(w for w in text.split() if w.lower() not in corrected_words)
    if not clean.strip():
        return []
    rake = Rake()
    rake.extract_keywords_from_text(clean)
    return rake.get_ranked_phrases()

# ── UI ────────────────────────────────────────────────────────────────────────
st.markdown("<h1 style='margin-bottom:0'>Grammar & Keywords</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#888;margin-top:4px'>NLP-powered spell-check, grammar analysis + RAKE keyword extraction</p>", unsafe_allow_html=True)
st.markdown("---")

prompt = st.text_area(
    "Enter your text below:",
    placeholder="e.g.  i has missed train tomorrow ?",
    height=160,
)

if st.button("Analyse Text ✦"):
    if not prompt.strip():
        st.warning("Please enter some text first.")
    else:
        with st.spinner("Analysing..."):
            errors, corrected_text, corrected_words = analyse(prompt)
            keywords = extract_keywords(prompt, corrected_words)

        word_count = len(prompt.split())
        st.markdown(f"""
        <div style='margin-bottom:1.4rem'>
            <div class='stat-box'><div class='stat-num'>{word_count}</div><div class='stat-label'>Words</div></div>
            <div class='stat-box'><div class='stat-num'>{len(errors)}</div><div class='stat-label'>Issues Found</div></div>
            <div class='stat-box'><div class='stat-num'>{len(keywords)}</div><div class='stat-label'>Keywords</div></div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns([1, 1], gap="medium")

        with col1:
            st.markdown("<div class='section-title'>Errors Found</div>", unsafe_allow_html=True)
            if not errors:
                st.success("No errors found — great writing!")
            else:
                for e in errors:
                    st.markdown(f"""
                    <div class='error-item'>
                        <span class='wrong'>"{e['wrong']}"</span>
                        <span class='arrow'>→</span>
                        <span class='fix'>"{e['fix']}"</span>
                        <span class='etype'>{e['type']}</span>
                        <div class='msg'>{e['explanation']}</div>
                    </div>
                    """, unsafe_allow_html=True)

        with col2:
            st.markdown("<div class='section-title'>Extracted Keywords</div>", unsafe_allow_html=True)
            if not keywords:
                st.info("No keywords extracted.")
            else:
                tags_html = "".join(f"<span class='keyword-tag'>{kw}</span>" for kw in keywords)
                st.markdown(f"<div style='line-height:2.4'>{tags_html}</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown("<div class='section-title'>Corrected Text</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='corrected-box'>{corrected_text}</div>", unsafe_allow_html=True)