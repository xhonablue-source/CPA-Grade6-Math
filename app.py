"""Shared branding, colors, and CSS for the CPA Grade 6 Math Launcher app."""

import streamlit as st

NAVY = "#1F3864"
GOLD = "#B08D57"
CREAM = "#F2EFE9"


def inject_css():
    st.markdown(
        f"""
        <style>
        .stApp {{ background-color: #FFFFFF; }}
        .block-container {{ padding-top: 2rem; padding-bottom: 3rem; max-width: 1100px; }}

        .cpa-banner {{
            background-color: {NAVY};
            color: white;
            padding: 1.1rem 1.8rem;
            border-radius: 10px;
            margin-bottom: 1.6rem;
        }}
        .cpa-banner h1 {{ margin: 0; font-size: 1.6rem; letter-spacing: 0.5px; }}
        .cpa-banner p {{ margin: 0.2rem 0 0 0; opacity: 0.85; font-size: 0.95rem; }}

        .pace-badge {{
            display: inline-block;
            background-color: {GOLD};
            color: white;
            padding: 0.25rem 0.9rem;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: 700;
            margin-bottom: 1rem;
        }}

        .big-title {{ color: {NAVY}; font-size: 2.1rem; font-weight: 800; margin-bottom: 0.3rem; }}
        .sub-title {{ color: {GOLD}; font-size: 1.15rem; font-weight: 700; margin-bottom: 1.2rem; }}

        .station-card {{
            background-color: {CREAM};
            border-left: 7px solid {GOLD};
            border-radius: 8px;
            padding: 1.3rem 1.5rem;
            margin-bottom: 1rem;
            height: 100%;
        }}
        .station-card h3 {{ color: {NAVY}; margin-top: 0; }}

        .step-row {{ display: flex; align-items: flex-start; margin-bottom: 1rem; }}
        .step-num {{
            background-color: {NAVY};
            color: white;
            border-radius: 50%;
            min-width: 2.1rem;
            height: 2.1rem;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: 800;
            margin-right: 0.9rem;
            flex-shrink: 0;
            margin-top: 0.1rem;
        }}
        .step-text {{ font-size: 1.05rem; line-height: 1.5; padding-top: 0.15rem; }}

        .quote-box {{
            background-color: {CREAM};
            border-left: 7px solid {NAVY};
            border-radius: 8px;
            padding: 1.3rem 1.6rem;
            font-size: 1.15rem;
            font-style: italic;
            color: {NAVY};
            margin-bottom: 1.2rem;
        }}

        .ican-box {{
            background-color: white;
            border: 2px solid {GOLD};
            border-radius: 8px;
            padding: 1rem 1.3rem;
            margin-bottom: 0.8rem;
            font-size: 1.05rem;
        }}
        .ican-tag {{
            display: inline-block;
            background-color: {NAVY};
            color: white;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.15rem 0.6rem;
            border-radius: 6px;
            margin-right: 0.6rem;
        }}

        .reflect-box {{
            background-color: {NAVY};
            color: white;
            border-radius: 10px;
            padding: 1.6rem 1.8rem;
            font-size: 1.2rem;
            line-height: 1.6;
            margin-top: 1rem;
        }}

        .warn-box {{
            background-color: #FFF4E5;
            border-left: 7px solid {GOLD};
            border-radius: 8px;
            padding: 1rem 1.3rem;
            margin-top: 0.8rem;
            font-weight: 600;
            color: #7a5a1e;
        }}

        .day-card {{
            background-color: {CREAM};
            border: 2px solid {GOLD};
            border-radius: 12px;
            padding: 1.4rem 1.5rem 0.6rem 1.5rem;
            margin-bottom: 1rem;
        }}
        .day-card h3 {{ color: {NAVY}; margin: 0 0 0.3rem 0; }}
        .day-card p {{ min-height: 3rem; }}
        .status-pill {{
            display: inline-block;
            font-size: 0.75rem;
            font-weight: 700;
            padding: 0.15rem 0.6rem;
            border-radius: 999px;
            margin-bottom: 0.6rem;
        }}
        .status-ready {{ background-color: #DCEFDC; color: #206020; }}
        .status-soon {{ background-color: #EEEEEE; color: #777777; }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def banner(subtitle="Grade 6 Mathematics"):
    st.markdown(
        f"""
        <div class="cpa-banner">
            <h1>CHANDLER PARK ACADEMY</h1>
            <p>{subtitle}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def back_to_launcher():
    st.page_link("Home.py", label="â¬… Back to Launcher", icon="ðŸ� ")
