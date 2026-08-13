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
      html, body, [data-testid="stAppViewContainer"], .stApp {
        background: #f8fafc !important;
      }
      [data-testid="stHeader"], [data-testid="stToolbar"], footer, #MainMenu {
        display: none !important;
      }
      .block-container {
        padding: 0 !important;
        max-width: none !important;
      }
      iframe {
        display: block;
        margin: 0 auto;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

ROOT = Path(__file__).resolve().parent
html = (ROOT / "index.html").read_text(encoding="utf-8")
avatar_bytes = (ROOT / "metpro_avatar.png").read_bytes()
avatar_b64 = base64.b64encode(avatar_bytes).decode("ascii")
html = html.replace("__AVATAR_DATA__", f"data:image/png;base64,{avatar_b64}")

components.html(html, height=1540, scrolling=False)
