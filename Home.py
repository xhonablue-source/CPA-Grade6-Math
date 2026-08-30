import streamlit as st
from _common import inject_css, banner, GOLD

st.set_page_config(
    page_title="CPA Grade 6 Math Launcher",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded",
)

inject_css()
banner("Grade 6 Mathematics — Lesson Launcher")

st.markdown('<div class="big-title">Welcome, Mathematicians!</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">Professor Xavier Honablue, M.Ed.</div>',
    unsafe_allow_html=True,
)
st.write("Pick today's lesson below to get started. Each lesson runs through the E3 Math Station System: Engage, Explore, Enrich.")

st.markdown("---")
st.markdown("### 🗓️ Week 1: First Days of School")

DAYS = [
    dict(
        label="Day 1",
        title="What Is Math?",
        desc="Observe a real object, then simulate an imagined object using geometric shapes on graph paper.",
        page="pages/1_Day_1_What_Is_Math.py",
        ready=True,
    ),
    dict(
        label="Day 2",
        title="Rules & Regulations",
        desc="Learn CPA classroom expectations and procedures, then build our classroom agreement together.",
        page="pages/2_Day_2_Rules_and_Regulations.py",
        ready=True,
    ),
    dict(
        label="Day 3",
        title="Getting to Know You",
        desc="Build a Quad Structure interest survey - name, self-portrait, interests, and a goal for the year.",
        page="pages/3_Day_3_Getting_to_Know_You.py",
        ready=True,
    ),
]

cols = st.columns(3)
for col, day in zip(cols, DAYS):
    with col:
        status_class = "status-ready" if day["ready"] else "status-soon"
        status_text = "READY" if day["ready"] else "COMING SOON"
        st.markdown(
            f"""
            <div class="day-card">
                <span class="status-pill {status_class}">{status_text}</span>
                <h3>{day['label']}: {day['title']}</h3>
                <p>{day['desc']}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        if day["ready"]:
            st.page_link(day["page"], label=f"Open {day['label']} →", icon="📂", use_container_width=True)
        else:
            st.button(f"Open {day['label']} →", disabled=True, use_container_width=True)

st.markdown("---")
st.markdown("### 🔜 More Coming Soon")
st.markdown(
    f"""
    <div class="day-card">
        <span class="status-pill status-soon">PLANNED</span>
        <h3>Week 1 Continued: Interest Surveys</h3>
        <p>Tri Structure (Spark / Struggle / Hope), Pent Structure, Survey Says! Data Day, and the Gallery Walk &amp;
        Class Vision day - built the same way as Day 3 once you're ready to add them.</p>
    </div>
    <div class="day-card">
        <span class="status-pill status-soon">PLANNED</span>
        <h3>Unit 1: Area &amp; Introduction to Algebra</h3>
        <p>Honors and Standard 3-week tracks covering area of parallelograms/triangles, composite figures,
        surface area, and algebraic expressions through area models.</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.caption("Tell Professor Xavier's assistant which lesson to build next, and it'll appear here as a new button.")
