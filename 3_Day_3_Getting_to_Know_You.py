import streamlit as st
from _common import inject_css, banner, back_to_launcher, NAVY

st.set_page_config(page_title="Day 3 — Getting to Know You", page_icon="🧭", layout="wide")
inject_css()
back_to_launcher()
banner("Grade 6 Mathematics | Day Three | 55-Minute Period")

SLIDES = [
    "Welcome",
    "Engage: Building the Quad",
    "Explore: Talk It Through",
    "Complete Your Quad",
    "Enrich: Share &amp; Reflect",
    "Turn It In",
    "What You Just Did",
]

if "day3_slide" not in st.session_state:
    st.session_state.day3_slide = 0


def go_to(i):
    st.session_state.day3_slide = i


def go_next():
    st.session_state.day3_slide = min(st.session_state.day3_slide + 1, len(SLIDES) - 1)


def go_prev():
    st.session_state.day3_slide = max(st.session_state.day3_slide - 1, 0)


with st.sidebar:
    st.markdown(f"<h3 style='color:{NAVY};'>Day 3 Roadmap</h3>", unsafe_allow_html=True)
    st.caption("55-minute period — Getting to Know You")
    for i, label in enumerate(SLIDES):
        prefix = "▶ " if i == st.session_state.day3_slide else "　"
        st.button(f"{prefix}{i + 1}. {label}", key=f"d3nav_{i}", on_click=go_to, args=(i,), use_container_width=True)
    st.markdown("---")
    st.progress((st.session_state.day3_slide + 1) / len(SLIDES))
    st.caption(f"Slide {st.session_state.day3_slide + 1} of {len(SLIDES)}")

slide = st.session_state.day3_slide

if slide == 0:
    st.markdown('<span class="pace-badge">0-5 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Welcome to Day 3!</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="quote-box">
        You've learned what math is, and you've helped build our classroom agreement.
        Today, we get to know each other - using graph paper and geometry.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("Today's structure: a **Quad** - four equal sections on graph paper, built with a ruler.")

elif slide == 1:
    st.markdown('<span class="pace-badge">5-15 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Engage: Building the Quad</div>', unsafe_allow_html=True)
    st.write("At the front board, Professor Xavier models how to build a Quad Structure:")

    steps = [
        "Take a sheet of graph paper and a ruler.",
        "Draw one straight line down the vertical midline of the page, and one straight line across the horizontal midline.",
        "This creates 4 congruent quadrants - label them Q1, Q2, Q3, and Q4.",
        "Watch as Professor Xavier fills in an example Quad at the front board.",
    ]
    for i, s in enumerate(steps, start=1):
        st.markdown(
            f"""
            <div class="step-row">
                <div class="step-num">{i}</div>
                <div class="step-text">{s}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif slide == 2:
    st.markdown('<span class="pace-badge">15-22 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Explore: Talk It Through</div>', unsafe_allow_html=True)
    st.write("Before writing anything down, head to the back board with a few classmates and a dry-erase marker:")

    prompts = [
        "Brainstorm ideas out loud: what animal would you draw yourself as, and why?",
        "Talk through your favorite subject and something you're good at.",
        "Share one idea for a goal you might set for this school year.",
    ]
    for i, s in enumerate(prompts, start=1):
        st.markdown(
            f"""
            <div class="step-row">
                <div class="step-num">{i}</div>
                <div class="step-text">{s}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown(
        '<div class="warn-box">Talking it through with friends first makes it easier to fill in your own Quad next.</div>',
        unsafe_allow_html=True,
    )

elif slide == 3:
    st.markdown('<span class="pace-badge">22-37 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Complete Your Quad</div>', unsafe_allow_html=True)
    st.write("Now build your own Quad Structure at your seat and fill in all four sections:")

    quads = [
        ("Q1", "Name", "Write your name in large block letters."),
        ("Q2", "Self as an Animal", "Draw yourself as your favorite animal - fast sketch, no overthinking."),
        ("Q3", "Three Things", "List your favorite subject, something you're good at, and something you want to learn this year."),
        ("Q4", "This Year I Want To...", "Write or draw one goal or hope for the school year."),
    ]
    c1, c2 = st.columns(2)
    for col, (tag, title, desc) in zip([c1, c1, c2, c2], quads):
        with col:
            st.markdown(
                f"""
                <div class="station-card">
                <h3>{tag}: {title}</h3>
                <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

elif slide == 4:
    st.markdown('<span class="pace-badge">37-47 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Enrich: Share &amp; Reflect</div>', unsafe_allow_html=True)
    st.write("Visit the Enrich area with Professor Xavier:")

    steps = [
        "Share one quadrant of your choice - read it out loud in a full sentence.",
        "Professor Xavier will ask a follow-up question about your goal or your favorite subject.",
        "Listen to a few classmates share their quadrants too - notice what you have in common.",
    ]
    for i, s in enumerate(steps, start=1):
        st.markdown(
            f"""
            <div class="step-row">
                <div class="step-num">{i}</div>
                <div class="step-text">{s}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif slide == 5:
    st.markdown('<span class="pace-badge">47-52 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Turn It In</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="quote-box">
        Place your completed Quad sheet in the white box labeled with your class number.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif slide == 6:
    st.markdown('<span class="pace-badge">52-55 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">What You Just Did</div>', unsafe_allow_html=True)
    st.write("In plain language, here's what you were able to do today:")

    icans = [
        ("STRUCTURE", "I can use a ruler to divide a page into four congruent quadrants with straight, accurate lines."),
        ("COMMUNICATION", "I can represent information about myself using words and pictures organized within a structure."),
        ("GOAL-SETTING", "I can set one personal goal for the school year and explain it to a partner."),
    ]
    for tag, text in icans:
        st.markdown(f'<div class="ican-box"><span class="ican-tag">{tag}</span>{text}</div>', unsafe_allow_html=True)

    st.caption(
        "Michigan K-12 Mathematics Standards: 6.G.A.3 (draw figures using coordinates/structure), "
        "MP5 (Use appropriate tools strategically), MP6 (Attend to precision). "
        "Michigan ELA Standards: SL.6.1 (collaborative discussion), W.6.3 (descriptive writing)."
    )

    st.markdown(
        """
        <div class="reflect-box">
        You just used precise geometric construction to build a structure, then used that structure
        to communicate real information about yourself to your teacher and classmates.
        <br><br>
        <b>Are you impressed with yourself that a ruler and four boxes just helped this whole class
        get to know each other better?</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="warn-box">
        📓 Journal It: Copy the three statements above into your math journal, word for word.
        Then, in your workbook, write 2-3 sentences for each one describing exactly what you did
        today to earn it - be specific about the steps you took, not just "I did it."
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.write("")
nav1, nav2, nav3 = st.columns([1, 3, 1])
with nav1:
    st.button("⬅ Back", on_click=go_prev, disabled=(slide == 0), use_container_width=True, key="d3_back")
with nav3:
    st.button("Next ➡", on_click=go_next, disabled=(slide == len(SLIDES) - 1), use_container_width=True, key="d3_next")
