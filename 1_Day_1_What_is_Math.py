import streamlit as st
from _common import inject_css, banner, back_to_launcher, NAVY, GOLD

st.set_page_config(page_title="Day 1 — What Is Math?", page_icon="🔷", layout="wide")
inject_css()
back_to_launcher()
banner("Grade 6 Mathematics | Day One | 55-Minute Period")

SLIDES = [
    "Welcome",
    "The E3 Math Station System",
    "Your First 3 Days at CPA",
    "Day 1: What Is Math?",
    "Engage: Observe & Simulate",
    "Explore: Build Your Own",
    "Enrich: Name Your Creation",
    "Turn It In",
    "What You Just Did",
]

if "day1_slide" not in st.session_state:
    st.session_state.day1_slide = 0


def go_to(i):
    st.session_state.day1_slide = i


def go_next():
    st.session_state.day1_slide = min(st.session_state.day1_slide + 1, len(SLIDES) - 1)


def go_prev():
    st.session_state.day1_slide = max(st.session_state.day1_slide - 1, 0)


with st.sidebar:
    st.markdown(f"<h3 style='color:{NAVY};'>Day 1 Roadmap</h3>", unsafe_allow_html=True)
    st.caption("55-minute period — What Is Math?")
    for i, label in enumerate(SLIDES):
        prefix = "▶ " if i == st.session_state.day1_slide else "　"
        st.button(f"{prefix}{i + 1}. {label}", key=f"nav_{i}", on_click=go_to, args=(i,), use_container_width=True)
    st.markdown("---")
    st.progress((st.session_state.day1_slide + 1) / len(SLIDES))
    st.caption(f"Slide {st.session_state.day1_slide + 1} of {len(SLIDES)}")

slide = st.session_state.day1_slide

if slide == 0:
    st.markdown('<span class="pace-badge">0-3 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Welcome!</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">To Chandler Park Academy Mathematics</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="quote-box">
        "I am Professor Xavier Honablue, M.Ed. — and I will be your teacher for the year ahead."
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("Take a seat, take a breath, and get ready to think like a mathematician.")

elif slide == 1:
    st.markdown('<span class="pace-badge">3-8 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Introducing the E3 Math Station System</div>', unsafe_allow_html=True)
    st.write("Every activity we do this year will move through three stations. Here's how they work:")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="station-card">
            <h3>🖥️ ENGAGE</h3>
            <b>Front Smart Board &amp; Webcam</b>
            <p>Whole-class instruction. Professor Xavier models the task at the front board so everyone starts together.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="station-card">
            <h3>🧑‍🤝‍🧑 EXPLORE</h3>
            <b>Back Board with Friends</b>
            <p>Grab a dry-erase marker and head to the back board. Work with classmates to try the task yourselves.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="station-card">
            <h3>💡 ENRICH</h3>
            <b>Enrich Area</b>
            <p>Meet with Professor Xavier for deeper learning, clarification, and an extra challenge.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif slide == 2:
    st.markdown('<span class="pace-badge">8-11 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Your First 3 Days at CPA</div>', unsafe_allow_html=True)
    st.write("Here's how we'll use the E3 system to kick off the year:")

    c1, c2, c3 = st.columns(3)
    days = [
        ("Day 1", "What Is Math?", "Observe. Simulate. Build with shapes.", True),
        ("Day 2", "Rules & Regulations", "How our classroom and school work.", False),
        ("Day 3", "Getting to Know You", "Interest surveys and community building.", False),
    ]
    for col, (day, title, desc, is_today) in zip([c1, c2, c3], days):
        with col:
            border = GOLD if is_today else "#cccccc"
            today_tag = '<span class="pace-badge">TODAY</span><br>' if is_today else ""
            st.markdown(
                f"""
                <div class="station-card" style="border-left-color:{border};">
                {today_tag}
                <h3>{day}: {title}</h3>
                <p>{desc}</p>
                </div>
                """,
                unsafe_allow_html=True,
            )

elif slide == 3:
    st.markdown('<span class="pace-badge">11-15 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Day 1: What Is Math?</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="quote-box">
        Math is a numerical or graphical representation of an observation —
        or a simulation of an imagined observation.
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        **Today, you will:**
        - **Observe** a real object.
        - **Simulate** an imagined object of your own.
        - Do both using geometric shapes drawn on graph paper.
        """
    )

elif slide == 4:
    st.markdown('<span class="pace-badge">15-30 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Engage: Observe &amp; Simulate</div>', unsafe_allow_html=True)
    st.write("At the front board, we'll observe a dragonfly together. Then, at your seat:")

    steps = [
        "<b>Quad your paper.</b> Divide your graph paper into 4 equal sections.",
        "<b>Draw a diagonal line</b> about 7-8 inches long straight through the center of the graph.",
        "<b>Observe the dragonfly</b> at the front board. Using the provided geometric shape manipulatives, simulate the dragonfly along your diagonal line.",
        "<b>Build a ledge</b> along the side of your page. Show every shape you used, and keep a tally of how many of each shape you used.",
        "<b>Be exact.</b> Only straight lines earn the prize today - press your pencil firmly against the shape and draw carefully.",
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
    st.markdown(
        '<div class="warn-box">This completes the ENGAGE portion of today\'s project.</div>',
        unsafe_allow_html=True,
    )

elif slide == 5:
    st.markdown('<span class="pace-badge">30-42 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Explore: Build Your Own</div>', unsafe_allow_html=True)
    st.write("Now head to a second sheet of graph paper and work with friends at the back board to try it yourselves:")

    steps = [
        "Get a <b>second sheet</b> of graph paper.",
        "This time, <b>you</b> quad the paper yourself - draw your own dividing lines.",
        "Design and build <b>your own imagined object</b> using the geometric shape manipulatives.",
        "Keep the <b>same tally system</b> as before: a ledge showing your shapes and a count of each.",
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

elif slide == 6:
    st.markdown('<span class="pace-badge">42-49 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Enrich: Name Your Creation</div>', unsafe_allow_html=True)
    st.write("Visit the Enrich area to meet with Professor Xavier:")

    steps = [
        "Bring your <b>tally</b> (the shapes and counts) to the Enrich area.",
        "Professor Xavier will show you how to use your tally to <b>name</b> your simulated object.",
        "This is where math becomes a language - your shape-tally becomes your object's name.",
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

elif slide == 7:
    st.markdown('<span class="pace-badge">49-52 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">Turn It In</div>', unsafe_allow_html=True)
    st.markdown(
        """
        <div class="quote-box">
        Place both graph-paper sheets - your dragonfly (Engage) and your own object (Explore) -
        in the white box labeled with your class number.
        </div>
        """,
        unsafe_allow_html=True,
    )

elif slide == 8:
    st.markdown('<span class="pace-badge">52-55 min</span>', unsafe_allow_html=True)
    st.markdown('<div class="big-title">What You Just Did</div>', unsafe_allow_html=True)
    st.write("In plain language, here's what you were able to do today:")

    icans = [
        ("MODEL", "I can use shapes and drawings to model something I observe in the real world."),
        ("PRECISION", "I can carefully and precisely construct geometric figures using tools."),
        ("DATA", "I can represent and organize information using a tally."),
    ]
    for tag, text in icans:
        st.markdown(f'<div class="ican-box"><span class="ican-tag">{tag}</span>{text}</div>', unsafe_allow_html=True)

    st.caption(
        "Michigan K-12 Mathematics Standards - Standards for Mathematical Practice: "
        "MP4 (Model with mathematics), MP5 (Use appropriate tools strategically), "
        "MP6 (Attend to precision)."
    )

    st.markdown(
        """
        <div class="reflect-box">
        Take a second and think about that: you just modeled a real-world observation using
        geometric reasoning, built it with precise, careful construction, and organized your
        results with data. That is exactly what the Michigan Math Standards ask a mathematician
        to do.
        <br><br>
        <b>Are you impressed with yourself that you already did something that sounds this
        complex&nbsp;&mdash;&nbsp;on Day One?</b>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.write("")
st.write("")
nav1, nav2, nav3 = st.columns([1, 3, 1])
with nav1:
    st.button("⬅ Back", on_click=go_prev, disabled=(slide == 0), use_container_width=True, key="d1_back")
with nav3:
    st.button("Next ➡", on_click=go_next, disabled=(slide == len(SLIDES) - 1), use_container_width=True, key="d1_next")
