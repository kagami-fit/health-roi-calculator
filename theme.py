"""FRACTALブランドテーマ - ROI試算ツール用に抜粋"""

import streamlit as st

COLORS = {
    "primary_dark": "#2D3337",
    "secondary": "#738084",
    "accent": "#E4006F",
    "gold": "#C5BDAB",
    "bg_dark": "#535F62",
    "bg_light": "#EFEFEF",
    "bg_white": "#F8F8F8",
    "white": "#FFFFFF",
    "black": "#000000",
    "border": "#F1F1F1",
    "text": "#2D3337",
    "text_light": "#738184",
}


def apply_theme():
    st.markdown(_get_custom_css(), unsafe_allow_html=True)


def page_header(title: str, subtitle: str = "", icon: str = ""):
    apply_theme()
    display_title = f"{icon} {title}".strip() if icon else title
    st.markdown(
        f"""
        <div class="fr-page-header">
            <h1 class="fr-title">{display_title}</h1>
            {f'<p class="fr-subtitle">{subtitle}</p>' if subtitle else ''}
            <div class="fr-accent-line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def section_header(title_en: str, title_ja: str):
    st.markdown(
        f"""
        <div class="fr-section-header">
            <span class="fr-section-en">{title_en}</span>
            <span class="fr-section-ja">{title_ja}</span>
            <div class="fr-accent-line"></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def metric_card(label: str, value: str, sub: str = "", accent: bool = False):
    bg = COLORS["accent"] if accent else COLORS["primary_dark"]
    st.markdown(
        f"""
        <div class="fr-metric-card" style="background:{bg};">
            <div class="fr-metric-label">{label}</div>
            <div class="fr-metric-value">{value}</div>
            {f'<div class="fr-metric-sub">{sub}</div>' if sub else ''}
        </div>
        """,
        unsafe_allow_html=True,
    )


def _get_custom_css() -> str:
    return f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700&family=Oswald:wght@500&display=swap');

    /* Streamlitのデフォルトヘッダー・フッター・バッジを非表示 */
    #MainMenu {{visibility: hidden !important;}}
    footer {{visibility: hidden !important; display: none !important;}}
    header {{visibility: hidden !important;}}
    .stDeployButton {{display: none !important;}}
    [data-testid="stToolbar"] {{display: none !important;}}
    [data-testid="stDecoration"] {{display: none !important;}}
    [data-testid="stStatusWidget"] {{display: none !important;}}
    [data-testid="stHeader"] {{display: none !important;}}

    /* Community Cloudの "Hosted with Streamlit" / "Created by" バッジ */
    [data-testid="stViewerBadge"],
    [data-testid="stCreatedByBadge"],
    [data-testid="stHostedWithBadge"],
    [data-testid="stAppViewerBadge"],
    [data-testid="stBottomBlockContainer"] > div:last-child,
    .viewerBadge_container__r5tak,
    .styles_viewerBadge__CvC9N,
    .viewerBadge_link__qRIco,
    [class*="viewerBadge"],
    [class*="_viewerBadge"],
    [class*="_profileContainer"],
    [class*="_createdBy"],
    [class*="_hostedWith"],
    a[href*="streamlit.io/cloud"],
    a[href*="share.streamlit.io"],
    a[href*="streamlit.io"][target="_blank"] {{
        display: none !important;
        visibility: hidden !important;
        opacity: 0 !important;
        pointer-events: none !important;
        width: 0 !important;
        height: 0 !important;
    }}

    /* Manage app ボタン（右下） */
    [data-testid="manage-app-button"],
    [data-testid="stAppDeployButton"],
    div[class*="_terminalButton"] {{
        display: none !important;
    }}

    /* 念のため、iframe最下部の固定要素を一掃 */
    .stApp > div:last-child:not([data-testid]) {{
        display: none !important;
    }}

    .stApp {{
        font-family: 'Noto Sans JP', 'Hiragino Kaku Gothic ProN', sans-serif;
        color: {COLORS["text"]};
    }}

    section[data-testid="stSidebar"] {{
        background: {COLORS["primary_dark"]};
    }}
    section[data-testid="stSidebar"] * {{
        color: {COLORS["white"]} !important;
    }}
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stRadio label {{
        color: {COLORS["gold"]} !important;
    }}

    .fr-page-header {{
        text-align: center;
        padding: 2rem 0 1rem;
        margin-bottom: 2rem;
    }}
    .fr-title {{
        font-family: 'Noto Sans JP', sans-serif;
        font-weight: 700;
        font-size: 2.4rem;
        color: {COLORS["primary_dark"]};
        letter-spacing: 0.05em;
        margin: 0;
    }}
    .fr-subtitle {{
        font-size: 1.05rem;
        color: {COLORS["secondary"]};
        margin: 0.5rem 0 0;
        letter-spacing: 0.03em;
    }}
    .fr-accent-line {{
        width: 100px;
        height: 4px;
        background: {COLORS["accent"]};
        margin: 1rem auto 0;
    }}

    .fr-section-header {{
        text-align: center;
        padding: 1.5rem 0 1rem;
        margin: 1rem 0;
    }}
    .fr-section-en {{
        display: block;
        font-family: 'Oswald', sans-serif;
        font-weight: 500;
        font-size: 1.6rem;
        color: {COLORS["secondary"]};
        letter-spacing: 0.07em;
        text-transform: uppercase;
    }}
    .fr-section-ja {{
        display: block;
        font-family: 'Noto Sans JP', sans-serif;
        font-weight: 700;
        font-size: 1.3rem;
        color: {COLORS["primary_dark"]};
        margin-top: 0.3rem;
    }}

    .fr-metric-card {{
        border-radius: 4px;
        padding: 1.5rem 1.2rem;
        text-align: center;
        color: {COLORS["white"]};
        margin-bottom: 1rem;
        box-shadow: 0 0 15px rgba(0,0,0,0.05);
        transition: transform 0.2s ease;
    }}
    .fr-metric-card:hover {{
        transform: translateY(-2px);
    }}
    .fr-metric-label {{
        font-size: 0.85rem;
        opacity: 0.85;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }}
    .fr-metric-value {{
        font-family: 'Oswald', sans-serif;
        font-weight: 500;
        font-size: 2rem;
        letter-spacing: 0.03em;
        line-height: 1.2;
    }}
    .fr-metric-sub {{
        font-size: 0.75rem;
        opacity: 0.7;
        margin-top: 0.4rem;
    }}

    .fr-info-card {{
        background: {COLORS["bg_white"]};
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 0 15px rgba(0,0,0,0.05);
    }}
    .fr-info-title {{
        font-weight: 700;
        font-size: 1rem;
        color: {COLORS["primary_dark"]};
        margin-bottom: 0.5rem;
    }}
    .fr-info-content {{
        font-size: 0.9rem;
        color: {COLORS["secondary"]};
        line-height: 1.85;
    }}

    .stButton > button {{
        background: {COLORS["primary_dark"]} !important;
        color: {COLORS["white"]} !important;
        border: none !important;
        border-radius: 4px !important;
        font-family: 'Noto Sans JP', sans-serif !important;
        font-weight: 700 !important;
        letter-spacing: 0.05em !important;
        padding: 0.6rem 2rem !important;
        transition: all 0.3s ease !important;
    }}
    .stButton > button:hover {{
        background: {COLORS["bg_dark"]} !important;
        transform: translateY(-1px);
    }}

    .stDownloadButton > button {{
        background: {COLORS["secondary"]} !important;
        color: {COLORS["white"]} !important;
        border: none !important;
        border-radius: 4px !important;
        font-family: 'Noto Sans JP', sans-serif !important;
        font-weight: 700 !important;
        transition: all 0.3s ease !important;
    }}
    .stDownloadButton > button:hover {{
        background: #5b6669 !important;
    }}

    .stTextInput input, .stNumberInput input, .stTextArea textarea {{
        border-radius: 4px !important;
        border: 1px solid {COLORS["bg_light"]} !important;
        font-family: 'Noto Sans JP', sans-serif !important;
        transition: all 0.3s ease !important;
    }}
    .stTextInput input:focus, .stNumberInput input:focus, .stTextArea textarea:focus {{
        border-color: {COLORS["accent"]} !important;
        box-shadow: 0 0 0 1px {COLORS["accent"]} !important;
    }}

    hr {{
        border-color: {COLORS["bg_light"]} !important;
    }}

    .fr-table {{
        width: 100%;
        border-collapse: collapse;
        font-family: 'Noto Sans JP', sans-serif;
    }}
    .fr-table thead th {{
        background: {COLORS["bg_light"]};
        color: {COLORS["secondary"]};
        font-weight: 700;
        padding: 1rem;
        text-align: center;
        font-size: 0.9rem;
    }}
    .fr-table tbody td {{
        border-bottom: 1px solid {COLORS["bg_light"]};
        padding: 1rem;
        text-align: center;
        color: {COLORS["secondary"]};
    }}
    .fr-table tbody th {{
        border-bottom: 1px solid {COLORS["bg_light"]};
        padding: 1rem;
        font-weight: 700;
        color: {COLORS["primary_dark"]};
    }}
    .fr-table .accent {{
        color: {COLORS["accent"]};
        font-weight: 700;
    }}

    .fr-footer {{
        background: {COLORS["secondary"]};
        color: {COLORS["white"]};
        padding: 1.5rem;
        text-align: center;
        font-size: 0.85rem;
        margin-top: 3rem;
        border-radius: 4px 4px 0 0;
    }}
    </style>
    """
