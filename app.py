import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="MetPro Adapt",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
      html, body, [data-testid="stAppViewContainer"], .stApp, [data-testid="stMain"] {
        background: #f8fafc !important;
        margin: 0 !important;
        padding: 0 !important;
      }
      [data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"], footer, #MainMenu {
        display: none !important;
      }
      .block-container, [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: none !important;
      }
      [data-testid="stVerticalBlock"] {
        gap: 0 !important;
      }
      [data-testid="stElementContainer"] {
        margin: 0 !important;
        padding: 0 !important;
      }
      iframe {
        display: block;
        margin: 0 auto !important;
        border: 0 !important;
        background: #fff !important;
      }
      @media (max-width: 559px) {
        html, body, [data-testid="stAppViewContainer"], .stApp, [data-testid="stMain"] {
          background: #fff !important;
        }
      }
    </style>
    """,
    unsafe_allow_html=True,
)

ROOT = Path(__file__).resolve().parent
html = (ROOT / "index.html").read_text(encoding="utf-8")
avatar_path = ROOT / "metpro_avatar.png"
if not avatar_path.exists():
    avatar_path = ROOT / "assets" / "metpro_avatar.png"
avatar_bytes = avatar_path.read_bytes()
avatar_b64 = base64.b64encode(avatar_bytes).decode("ascii")
html = html.replace("__AVATAR_DATA__", f"data:image/png;base64,{avatar_b64}")

components.html(html, height=1320, scrolling=False)
