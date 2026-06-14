from html import escape

import streamlit as st


BRAND_COLORS = {
    "ink": "#1f2937",
    "muted": "#64748b",
    "surface": "#ffffff",
    "surface_alt": "#f8fafc",
    "line": "#dbe3ef",
    "blue": "#2563eb",
    "teal": "#0f766e",
    "amber": "#d97706",
    "rose": "#e11d48",
    "green": "#16a34a",
}


PLOTLY_TEMPLATE = {
    "layout": {
        "font": {
            "family": "Inter, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif",
            "color": BRAND_COLORS["ink"],
        },
        "paper_bgcolor": "rgba(0,0,0,0)",
        "plot_bgcolor": "rgba(0,0,0,0)",
        "colorway": [
            BRAND_COLORS["blue"],
            BRAND_COLORS["teal"],
            BRAND_COLORS["amber"],
            BRAND_COLORS["rose"],
            BRAND_COLORS["green"],
        ],
        "margin": {
            "l": 32,
            "r": 24,
            "t": 56,
            "b": 36,
        },
        "legend": {
            "orientation": "h",
            "yanchor": "bottom",
            "y": 1.02,
            "xanchor": "right",
            "x": 1,
        },
        "xaxis": {
            "gridcolor": "#edf2f7",
            "zerolinecolor": "#dbe3ef",
        },
        "yaxis": {
            "gridcolor": "#edf2f7",
            "zerolinecolor": "#dbe3ef",
        },
    }
}


def apply_theme():
    st.markdown(
        """
        <style>
        :root {
            --sf-ink: #1f2937;
            --sf-muted: #64748b;
            --sf-surface: #ffffff;
            --sf-surface-alt: #f8fafc;
            --sf-line: #dbe3ef;
            --sf-blue: #2563eb;
            --sf-teal: #0f766e;
            --sf-amber: #d97706;
            --sf-rose: #e11d48;
            --sf-green: #16a34a;
        }

        .stApp {
            background:
                radial-gradient(circle at top left, rgba(37, 99, 235, 0.1), transparent 28rem),
                radial-gradient(circle at 90% 8%, rgba(15, 118, 110, 0.08), transparent 24rem),
                linear-gradient(180deg, #f8fafc 0%, #eef3f8 100%);
            color: var(--sf-ink);
        }

        [data-testid="stSidebar"] {
            background: #0f172a;
            border-right: 1px solid rgba(255, 255, 255, 0.08);
        }

        [data-testid="stSidebar"] * {
            color: #e5edf8;
        }

        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span {
            color: #d7e0ec;
        }

        [data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p {
            margin-bottom: 0.35rem;
        }

        [data-testid="stSidebar"] .sf-card {
            background: rgba(15, 23, 42, 0.5);
            border-color: rgba(148, 163, 184, 0.26);
            box-shadow: none;
        }

        [data-testid="stSidebar"] .sf-agent {
            border-bottom-color: rgba(148, 163, 184, 0.22);
        }

        [data-testid="stSidebar"] .sf-agent strong,
        [data-testid="stSidebar"] .sf-agent small {
            color: #e5edf8;
        }

        .block-container {
            padding-top: 2.2rem;
            padding-bottom: 3rem;
            max-width: 1240px;
        }

        h1, h2, h3 {
            letter-spacing: 0;
        }

        hr {
            margin: 1.35rem 0;
            border-color: var(--sf-line);
        }

        div[data-testid="stMetric"] {
            background: rgba(255, 255, 255, 0.86);
            border: 1px solid var(--sf-line);
            border-radius: 8px;
            padding: 1rem 1.05rem;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.06);
        }

        div[data-testid="stMetric"] label {
            color: var(--sf-muted);
            font-weight: 650;
        }

        div[data-testid="stMetricValue"] {
            color: var(--sf-ink);
        }

        .stPlotlyChart,
        [data-testid="stDataFrame"],
        [data-testid="stExpander"] {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid var(--sf-line);
            border-radius: 8px;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
            overflow: hidden;
        }

        .stPlotlyChart {
            padding: 0.55rem;
        }

        .stButton > button {
            min-height: 2.8rem;
            border-radius: 8px;
            border: 1px solid #1d4ed8;
            background: #2563eb;
            color: white;
            font-weight: 700;
            box-shadow: 0 8px 18px rgba(37, 99, 235, 0.22);
        }

        .stButton > button:hover {
            border-color: #1e40af;
            background: #1d4ed8;
            color: white;
        }

        .sf-hero {
            border: 1px solid rgba(37, 99, 235, 0.16);
            border-radius: 8px;
            padding: 1.45rem;
            background:
                linear-gradient(135deg, rgba(255, 255, 255, 0.98), rgba(239, 246, 255, 0.82)),
                radial-gradient(circle at top right, rgba(15, 118, 110, 0.12), transparent 18rem);
            box-shadow: 0 12px 30px rgba(15, 23, 42, 0.07);
            margin-bottom: 1.15rem;
        }

        .sf-hero-top {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
        }

        .sf-eyebrow {
            margin: 0;
            color: var(--sf-teal);
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.08em;
            text-transform: uppercase;
        }

        .sf-hero h1 {
            margin: 0.55rem 0 0 0;
            font-size: clamp(2rem, 4vw, 3.4rem);
            line-height: 1.05;
            color: var(--sf-ink);
        }

        .sf-hero p {
            max-width: 760px;
            margin: 0.85rem 0 0 0;
            color: var(--sf-muted);
            font-size: 1.02rem;
            line-height: 1.65;
        }

        .sf-pill-row {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }

        .sf-pill {
            display: inline-flex;
            align-items: center;
            gap: 0.4rem;
            border: 1px solid rgba(37, 99, 235, 0.18);
            border-radius: 999px;
            background: rgba(255, 255, 255, 0.72);
            color: var(--sf-ink);
            font-size: 0.82rem;
            font-weight: 700;
            padding: 0.36rem 0.68rem;
            white-space: nowrap;
        }

        .sf-pill-muted {
            color: var(--sf-muted);
            font-weight: 650;
        }

        .sf-brand {
            padding: 0.9rem 0 0.35rem 0;
        }

        .sf-brand-mark {
            width: 2.45rem;
            height: 2.45rem;
            display: grid;
            place-items: center;
            border-radius: 8px;
            background: linear-gradient(135deg, #38bdf8, #2563eb);
            color: white;
            font-weight: 900;
            margin-bottom: 0.65rem;
            box-shadow: 0 12px 28px rgba(37, 99, 235, 0.32);
        }

        .sf-brand h2 {
            margin: 0;
            color: #f8fafc;
            font-size: 1.1rem;
        }

        .sf-brand p {
            margin: 0.2rem 0 0 0;
            color: #cbd5e1;
            font-size: 0.86rem;
            line-height: 1.45;
        }

        .sf-section {
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 1rem;
            margin: 1.6rem 0 0.75rem 0;
        }

        .sf-section h2 {
            margin: 0;
            font-size: 1.2rem;
            color: var(--sf-ink);
        }

        .sf-section span {
            color: var(--sf-muted);
            font-size: 0.92rem;
        }

        .sf-card {
            background: rgba(255, 255, 255, 0.9);
            border: 1px solid var(--sf-line);
            border-radius: 8px;
            padding: 1rem;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
        }

        .sf-stat-grid,
        .sf-insight-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 0.85rem;
            margin: 0.35rem 0 1rem 0;
        }

        .sf-stat {
            position: relative;
            overflow: hidden;
            min-height: 8.3rem;
            border: 1px solid var(--sf-line);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.92);
            padding: 1rem;
            box-shadow: 0 12px 28px rgba(15, 23, 42, 0.06);
        }

        .sf-stat::after {
            content: "";
            position: absolute;
            right: -2rem;
            top: -2rem;
            width: 6rem;
            height: 6rem;
            border-radius: 999px;
            background: rgba(37, 99, 235, 0.08);
        }

        .sf-stat-label {
            color: var(--sf-muted);
            font-size: 0.78rem;
            font-weight: 800;
            letter-spacing: 0.06em;
            text-transform: uppercase;
        }

        .sf-stat-value {
            margin-top: 0.5rem;
            color: var(--sf-ink);
            font-size: 2rem;
            line-height: 1;
            font-weight: 850;
        }

        .sf-stat-caption {
            margin-top: 0.5rem;
            color: var(--sf-muted);
            font-size: 0.88rem;
            line-height: 1.45;
        }

        .sf-stat-teal::after { background: rgba(15, 118, 110, 0.1); }
        .sf-stat-amber::after { background: rgba(217, 119, 6, 0.11); }
        .sf-stat-rose::after { background: rgba(225, 29, 72, 0.1); }
        .sf-stat-green::after { background: rgba(22, 163, 74, 0.1); }

        .sf-insight {
            border: 1px solid var(--sf-line);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.9);
            padding: 1rem;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
        }

        .sf-insight strong {
            display: block;
            margin-bottom: 0.35rem;
            color: var(--sf-ink);
            font-size: 1rem;
        }

        .sf-insight p {
            margin: 0;
            color: var(--sf-muted);
            font-size: 0.92rem;
            line-height: 1.5;
        }

        .sf-callout {
            border: 1px solid rgba(37, 99, 235, 0.18);
            border-left: 4px solid var(--sf-blue);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.9);
            padding: 1rem 1.1rem;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
            margin: 0.5rem 0 1rem 0;
        }

        .sf-callout strong {
            display: block;
            color: var(--sf-ink);
            margin-bottom: 0.25rem;
        }

        .sf-callout span {
            color: var(--sf-muted);
            line-height: 1.55;
        }

        .sf-readiness {
            border: 1px solid var(--sf-line);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.9);
            padding: 1rem;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
            margin-bottom: 1rem;
        }

        .sf-readiness-top {
            display: flex;
            align-items: baseline;
            justify-content: space-between;
            gap: 1rem;
            margin-bottom: 0.7rem;
        }

        .sf-readiness strong {
            color: var(--sf-ink);
        }

        .sf-readiness span {
            color: var(--sf-muted);
            font-weight: 700;
        }

        .sf-readiness-track {
            height: 0.78rem;
            border-radius: 999px;
            background: linear-gradient(90deg, #fee2e2 0%, #fef3c7 52%, #dcfce7 100%);
            overflow: hidden;
        }

        .sf-readiness-fill {
            height: 100%;
            border-radius: 999px;
            background: linear-gradient(90deg, #2563eb, #0f766e);
            box-shadow: 0 0 0 1px rgba(255, 255, 255, 0.48) inset;
        }

        .sf-timeline {
            border: 1px solid var(--sf-line);
            border-radius: 8px;
            background: rgba(255, 255, 255, 0.88);
            padding: 0.35rem 1rem;
            box-shadow: 0 10px 24px rgba(15, 23, 42, 0.05);
        }

        .sf-timeline-step {
            display: grid;
            grid-template-columns: 2rem 1fr;
            gap: 0.75rem;
            padding: 0.9rem 0;
            border-bottom: 1px solid var(--sf-line);
        }

        .sf-timeline-step:last-child {
            border-bottom: 0;
        }

        .sf-timeline-index {
            width: 2rem;
            height: 2rem;
            display: grid;
            place-items: center;
            border-radius: 999px;
            background: #eff6ff;
            color: var(--sf-blue);
            font-weight: 850;
        }

        .sf-timeline-step strong {
            display: block;
            color: var(--sf-ink);
            margin-bottom: 0.2rem;
        }

        .sf-timeline-step span {
            color: var(--sf-muted);
            line-height: 1.5;
        }

        .sf-agent {
            display: flex;
            align-items: flex-start;
            gap: 0.75rem;
            padding: 0.85rem 0;
            border-bottom: 1px solid rgba(219, 227, 239, 0.8);
        }

        .sf-agent:last-child {
            border-bottom: 0;
        }

        .sf-agent-dot {
            width: 0.72rem;
            height: 0.72rem;
            margin-top: 0.34rem;
            border-radius: 999px;
            background: var(--sf-green);
            box-shadow: 0 0 0 4px rgba(22, 163, 74, 0.12);
            flex: 0 0 auto;
        }

        .sf-agent strong {
            display: block;
            color: var(--sf-ink);
        }

        .sf-agent small {
            color: var(--sf-muted);
        }

        .sf-flow {
            color: var(--sf-muted);
            font-weight: 800;
            text-align: center;
            margin: 0.55rem 0;
        }

        @media (max-width: 760px) {
            .block-container {
                padding-left: 1rem;
                padding-right: 1rem;
            }

            .sf-hero {
                padding: 1.1rem;
            }

            .sf-section {
                align-items: flex-start;
                flex-direction: column;
            }

            .sf-hero-top {
                align-items: flex-start;
                flex-direction: column;
            }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def sidebar_brand():
    st.markdown(
        """
        <div class="sf-brand">
            <div class="sf-brand-mark">SF</div>
            <h2>SkillForge AI</h2>
            <p>Certification readiness, planning, and workforce insight.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _pill_html(label, value):
    return (
        '<span class="sf-pill">'
        f'<span class="sf-pill-muted">{escape(str(label))}</span>'
        f'{escape(str(value))}'
        '</span>'
    )


def hero(eyebrow, title, body, pills=None):
    pill_html = ""
    if pills:
        pill_html = (
            '<div class="sf-pill-row">'
            + "".join(_pill_html(label, value) for label, value in pills)
            + "</div>"
        )

    st.markdown(
        (
            '<section class="sf-hero">'
            '<div class="sf-hero-top">'
            f'<p class="sf-eyebrow">{escape(str(eyebrow))}</p>'
            '<span class="sf-pill">Agents online</span>'
            '</div>'
            f'<h1>{escape(str(title))}</h1>'
            f'<p>{escape(str(body))}</p>'
            f'{pill_html}'
            '</section>'
        ),
        unsafe_allow_html=True,
    )


def section(title, caption=None):
    caption_html = f"<span>{caption}</span>" if caption else ""
    st.markdown(
        f"""
        <div class="sf-section">
            <h2>{title}</h2>
            {caption_html}
        </div>
        """,
        unsafe_allow_html=True,
    )


def configure_chart(fig, height=None):
    fig.update_layout(template=PLOTLY_TEMPLATE)
    if height:
        fig.update_layout(height=height)
    return fig


def stat_grid(stats):
    cards = []
    for stat in stats:
        tone = escape(str(stat.get("tone", "blue")))
        cards.append(
            '<div class="sf-stat sf-stat-' + tone + '">'
            f'<div class="sf-stat-label">{escape(str(stat["label"]))}</div>'
            f'<div class="sf-stat-value">{escape(str(stat["value"]))}</div>'
            f'<div class="sf-stat-caption">{escape(str(stat.get("caption", "")))}</div>'
            '</div>'
        )

    st.markdown(
        '<div class="sf-stat-grid">' + "".join(cards) + "</div>",
        unsafe_allow_html=True,
    )


def insight_cards(items):
    cards = []
    for item in items:
        cards.append(
            '<div class="sf-insight">'
            f'<strong>{escape(str(item["title"]))}</strong>'
            f'<p>{escape(str(item["body"]))}</p>'
            '</div>'
        )

    st.markdown(
        '<div class="sf-insight-grid">' + "".join(cards) + "</div>",
        unsafe_allow_html=True,
    )


def callout(title, body):
    st.markdown(
        (
            '<div class="sf-callout">'
            f'<strong>{escape(str(title))}</strong>'
            f'<span>{escape(str(body))}</span>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )


def readiness_bar(score, label="Certification readiness"):
    safe_score = max(0, min(100, int(score)))
    st.markdown(
        (
            '<div class="sf-readiness">'
            '<div class="sf-readiness-top">'
            f'<strong>{escape(str(label))}</strong>'
            f'<span>{safe_score}%</span>'
            '</div>'
            '<div class="sf-readiness-track">'
            f'<div class="sf-readiness-fill" style="width: {safe_score}%;"></div>'
            '</div>'
            '</div>'
        ),
        unsafe_allow_html=True,
    )


def workflow_timeline(steps):
    rows = []
    for index, step in enumerate(steps, start=1):
        title, body = step
        rows.append(
            '<div class="sf-timeline-step">'
            f'<div class="sf-timeline-index">{index}</div>'
            '<div>'
            f'<strong>{escape(str(title))}</strong>'
            f'<span>{escape(str(body))}</span>'
            '</div>'
            '</div>'
        )

    st.markdown(
        '<div class="sf-timeline">' + "".join(rows) + "</div>",
        unsafe_allow_html=True,
    )


def agent_list(agents):
    rows = "\n".join(
        (
            '<div class="sf-agent">'
            '<span class="sf-agent-dot"></span>'
            "<div>"
            f"<strong>{name}</strong>"
            f"<small>{description}</small>"
            "</div>"
            "</div>"
        )
        for name, description in agents
    )

    st.markdown(
        f'<div class="sf-card">{rows}</div>',
        unsafe_allow_html=True,
    )
