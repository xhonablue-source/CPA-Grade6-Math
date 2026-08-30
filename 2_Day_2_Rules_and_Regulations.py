import streamlit as st
from _common import inject_css, banner, back_to_launcher, NAVY

st.set_page_config(page_title="Day 2 — Rules & Regulations", page_icon="📋", layout="wide")
inject_css()
back_to_launcher()
banner("Grade 6 Mathematics | Day Two | 55-Minute Period")

SLIDES = [
    "Welcome Back",
    "Engage: Our Classroom Expectations",
    "Explore: What Would You Do?",
    "Enrich: Building Our Class Agreement",
    "Turn It In",
    "What You Just Did",
]

if "day2_slide" not in st.session_state:
    st.session_state.day2_slide = 0


def go_to(i):
    st.session_state.day2_slide = i


def go_next():
    st.session_state.day2_slide = min(st.session_state.day2_slide + 1, len(SLIDES) - 1)


def go_prev():
    st.session_state.day2_slide = max(st.session_state.day2_slide - 1, 0)


with st.sidebar:
    st.markdown(f"<h3 style='color:{NAVY};'>Day 2 Roadmap</h3>", unsafe_allow_html=True)
    st.caption("55-minute period — Rules & Regulations")
    for i, label in enumerate(SLIDES):
        prefix = "▶ " if i == st.session_state.day2_slide else "　"
        st.button(f"{prefix}{i + 1}. {label}", key=f"d2nav_{i}", on_click=go_to, args=(i,), use_container_width=True)
    st.markdown("---")
    st.progress((st.session_state.day2_slide + 1) / len(SLIDES))
    st.caption(f"Slide {st.session_state.day2_slide + 1} of {len(SLIDES)}")

slide = st.session_state.day2_slide

if slide == 0:
    st.markdown('<span class="pace-badge">0-5 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Welcome Back, Mathematicians!</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="quote-box">
        Yesterday you proved you could observe, model, and build like a mathematician.
        Today we set up how our classroom runs so we can do that safely, smoothly, and
        every single day this year.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("Quick recap: we still move through our three stations today - Engage, Explore, and Enrich.")

elif slide == 1:
    st.markdown('<span class="pace-badge">5-20 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Engage: Our Classroom Expectations</div>', unsafe_allow_html=True)
    st.write("At the front board, Professor Xavier walks through how our room works:")

    steps = [
        "<b>Entering the room:</b> come in quietly, pick up any needed materials, and begin the Do-Now on the board.",
        "<b>Getting help:</b> use the signal (raised hand or help card) - keep working on something else while you wait.",
        "<b>Station movement:</b> when it's time to Explore or Enrich, move calmly and bring only what you need.",
        "<b>Materials:</b> manipulatives, markers, and graph paper are shared - use carefully and return them to their bin.",
        "<b>Respect:</b> one voice at a time during Engage; all ideas are welcome during Explore and Enrich.",
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
    st.markdown('<span class="pace-badge">20-35 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Explore: What Would You Do?</div>', unsafe_allow_html=True)
    st.write("Head to the back board with your friends and a dry-erase marker. Talk through each scenario and write your group's answer:")

    scenarios = [
        "You need a pencil, but Professor Xavier is helping another student. What do you do?",
        "Your table is finishing an Explore activity, but you finish early. What do you do?",
        "A classmate disagrees with your answer during Explore. How do you respond?",
        "It's time to switch stations, but you're not finished writing. What do you do?",
    ]
    for i, s in enumerate(scenarios, start=1):
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
        '<div class="warn-box">Be ready to share one of your group\'s answers with the class.</div>',
        unsafe_allow_html=True,
    )

elif slide == 3:
    st.markdown('<span class="pace-badge">35-47 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Enrich: Building Our Class Agreement</div>', unsafe_allow_html=True)
    st.write("Visit the Enrich area with Professor Xavier to help write our Classroom Agreement:")

    steps = [
        "Share one expectation your group discussed at the back board.",
        "As a class, agree on our top 4-6 classroom expectations for the year.",
        "Sign your name on the Classroom Agreement to show you'll help keep our room running well.",
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

elif slide == 4:
    st.markdown('<span class="pace-badge">47-52 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Turn It In</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="quote-box">
        Place your signed copy of the Classroom Agreement in the white box labeled with your class number.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif slide == 5:
    st.markdown('<span class="pace-badge">52-55 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">What You Just Did</div>', unsafe_allow_html=True)
    st.write("Today wasn't about a math standard - it was about building the habits that make math class work all year:")

    icans = [
        ("COMMUNITY", "I can help build and follow a classroom agreement that keeps our learning space safe and fair."),
        ("COLLABORATION", "I can talk through a problem with classmates and consider more than one solution."),
        ("SELF-MANAGEMENT", "I can manage my own materials, movement, and voice during different classroom stations."),
    ]
    for tag, text in icans:
        st.markdown(f'<div class="ican-box"><span class="ican-tag">{tag}</span>{text}</div>', unsafe_allow_html=True)

    st.caption(
        "These habits directly support Michigan's Standards for Mathematical Practice - especially "
        "MP1 (Make sense of problems and persevere) and MP3 (Construct viable arguments and critique "
        "the reasoning of others) - which depend on a classroom where students can think, try, and "
        "talk safely."
    )

    st.markdown(
        """
        <div class="reflect-box">
        You just helped design the rules that will support your own learning all year - that's real
        ownership, not just a list handed to you.
        <br><br>
        <b>Are you proud that you helped build the classroom you'll be learning math in for the
        rest of the year?</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="warn-box">
        📓 Journal It: Copy the three statements above into your math journal, word for word.
        Then, in your workbook, write 2-3 sentences for each one describing a specific moment from
        today where you actually did that - not just "I agreed to it."
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.write("")
nav1, nav2, nav3 = st.columns([1, 3, 1])
with nav1:
    st.button("⬅ Back", on_click=go_prev, disabled=(slide == 0), use_container_width=True, key="d2_back")
with nav3:
    st.button("Next ➡", on_click=go_next, disabled=(slide == len(SLIDES) - 1), use_container_width=True, key="d2_next")
