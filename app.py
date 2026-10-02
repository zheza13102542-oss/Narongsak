"""
แฟ้มงาน ระบบฐานข้อมูลขั้นสูง — ณรงค์ศักดิ์ ประเสริฐศิริสร 664245033
รวมงานทุกชิ้นไว้ในเว็บเดียว: เปิดหน้าแรกแล้วคลิกเข้าไปดูงานแต่ละชิ้น

แก้ข้อมูลงานได้ที่ WORKS ด้านล่างอย่างเดียว ไม่ต้องแตะส่วนอื่น
"""
import json
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).parent

# ───────────────────────── ข้อมูลผู้ทำ ─────────────────────────
OWNER = {
    "name": "ณรงค์ศักดิ์ ประเสริฐศิริสร",
    "student_id": "664245033",
    "group": "66/44",
    "major": "สาขาวิชาวิทยาการคอมพิวเตอร์ มหาวิทยาลัยราชภัฏนครปฐม",
    "course": "ระบบฐานข้อมูลขั้นสูง",
    "github": "",  # ใส่ลิงก์ GitHub ของคุณ เช่น https://github.com/xxxx
}

# ───────────────────────── รายการงาน ─────────────────────────
# kind: "colab" = เปิดใน Colab | "app" = ฝังเว็บ Streamlit ไว้ในหน้า
# notebook: (ไม่บังคับ) ไฟล์ .ipynb ในโฟลเดอร์ notebooks/ ถ้ามี จะแสดงโค้ดและผลลัพธ์ในหน้าเว็บเลย
#           ดาวน์โหลดจาก Colab ได้ที่ File > Download > Download .ipynb
WORKS = [
    {
        "title": "งานที่ 1",
        "desc": "ใส่คำอธิบายงานสั้นๆ ตรงนี้",
        "kind": "colab",
        "url": "https://colab.research.google.com/drive/16Crmgia47GJb6Cxth-sQ4d8jE6Kbaljq",
        "notebook": "notebooks/work1.ipynb",
    },
    {
        "title": "ระบบแนะนำทรงผม (Notebook ส่วนที่ 1)",
        "desc": "ระบบแนะนำทรงผมด้วยกราฟ Neo4j เขียนและทดลองคำสั่ง Cypher ใน Google Colab",
        "tags": ["Neo4j", "Cypher"],
        "kind": "colab",
        "url": "https://colab.research.google.com/drive/1n65rgMpIrAEsFAzJtuLto18_5NTA4hUN",
        "notebook": "notebooks/work2.ipynb",
    },
    {
        "title": "ระบบแนะนำทรงผม (Notebook ส่วนที่ 2)",
        "desc": "ระบบแนะนำทรงผมด้วยกราฟ Neo4j ต่อจากส่วนที่ 1 ใน Google Colab",
        "tags": ["Neo4j", "Cypher"],
        "kind": "colab",
        # ⚠ ตอนนี้เป็นลิงก์เดียวกับงานที่ 1 — เปลี่ยนเป็นลิงก์ที่ถูกต้อง
        "url": "https://colab.research.google.com/drive/16Crmgia47GJb6Cxth-sQ4d8jE6Kbaljq",
        "notebook": "notebooks/work3.ipynb",
    },
    {
        "title": "HairGraph ระบบแนะนำทรงผม",
        "desc": "ระบบแนะนำทรงผมด้วยกราฟ Neo4j Aura + Streamlit บอกเหตุผลได้ทุกคำแนะนำ",
        "kind": "app",
        "url": "https://b39sfnld4ezgbapv3ijnor.streamlit.app/",
        "slides": "slides/hairgraph.pdf",
        "tags": ["Neo4j Aura", "Cypher", "Streamlit"],
    },
]

# ───────────────────────── หน้าตา ─────────────────────────
st.set_page_config(page_title="แฟ้มงาน · ณรงค์ศักดิ์", page_icon="📂", layout="wide")

st.markdown(
    """
<link href="https://fonts.googleapis.com/css2?family=Chonburi&family=Sarabun:wght@400;600;700&display=swap" rel="stylesheet">
<style>
:root{ --navy:#1C2A42; --brass:#C9A24A; --ink:#1E2633; --muted:#5B6576; --line:#D9DEE6; --paper:#F4F5F7; }
html, body, [class*="css"], .stMarkdown, button, input { font-family:'Sarabun', sans-serif; }
h1,h2,h3,.display { font-family:'Chonburi', serif !important; font-weight:400 !important; color:var(--navy); letter-spacing:0; }
[data-testid="stSidebar"]{ background:var(--navy); }
[data-testid="stSidebar"] *{ color:#E9ECF2; }
[data-testid="stSidebar"] .brand{ font-family:'Chonburi',serif; font-size:1.35rem; color:#fff; line-height:1.3; }
[data-testid="stSidebar"] .brand small{ display:block; font-family:'Sarabun'; font-size:.85rem; color:var(--brass); margin-top:.2rem; }

.hero{ border-left:6px solid var(--brass); padding:.4rem 0 .4rem 1.4rem; margin:.5rem 0 2rem; }
.hero .display{ font-size:clamp(2rem,5vw,3.4rem); line-height:1.15; margin:0; }
.hero p{ color:var(--muted); font-size:1.05rem; margin:.6rem 0 0; max-width:60ch; }

.row{ display:grid; grid-template-columns:3.2rem 1fr; gap:1rem; padding:1.1rem 0 .3rem; border-top:1px solid var(--line); }
.row .no{ font-family:'Chonburi',serif; font-size:2rem; color:var(--brass); line-height:1; }
.row h3{ margin:0 0 .25rem; font-size:1.3rem; }
.row p{ margin:0; color:var(--muted); }
.chip{ display:inline-block; font-size:.78rem; padding:.05rem .55rem; border-radius:999px; border:1px solid var(--line); color:var(--muted); margin:.45rem .3rem 0 0; }
.chip.app{ border-color:var(--brass); color:#8A6A1F; }
.note{ background:#fff; border:1px solid var(--line); border-radius:8px; padding:.8rem 1rem; color:var(--muted); font-size:.92rem; }
.stButton button:focus-visible, a:focus-visible{ outline:3px solid var(--brass); outline-offset:2px; }
</style>
""",
    unsafe_allow_html=True,
)

PAGES = ["หน้าแรก"] + [f"{i+1}. {w['title']}" for i, w in enumerate(WORKS)]
if "page" not in st.session_state:
    st.session_state.page = PAGES[0]


def go(page: str):
    st.session_state.page = page


# ───────────────────────── แถบข้าง ─────────────────────────
with st.sidebar:
    st.markdown(
        f'<div class="brand">แฟ้มงาน<small>{OWNER["course"]}</small></div>',
        unsafe_allow_html=True,
    )
    st.write("")
    st.radio("เลือกงาน", PAGES, key="page", label_visibility="collapsed")
    st.divider()
    st.caption(f'{OWNER["name"]}  \n{OWNER["student_id"]} · กลุ่ม {OWNER["group"]}')
    if OWNER["github"]:
        st.link_button("GitHub", OWNER["github"], width="stretch")


# ───────────────────────── ตัวช่วย ─────────────────────────
@st.cache_data(show_spinner="กำลังเตรียมสไลด์…")
def pdf_pages(path: str) -> list[bytes]:
    import pymupdf

    doc = pymupdf.open(path)
    return [p.get_pixmap(matrix=pymupdf.Matrix(1.6, 1.6)).tobytes("png") for p in doc]


def show_slides(path: str):
    file = BASE / path
    if not file.exists():
        st.info(f"ยังไม่พบไฟล์สไลด์ `{path}` — วางไฟล์ PDF ไว้ที่ตำแหน่งนี้ใน GitHub")
        return
    pages = pdf_pages(str(file))
    key = f"slide_{path}"
    st.session_state.setdefault(key, 1)

    c1, c2, c3 = st.columns([1, 2, 1])
    if c1.button("◀ ก่อนหน้า", width="stretch", disabled=st.session_state[key] <= 1, key=key + "_p"):
        st.session_state[key] -= 1
        st.rerun()
    c2.markdown(
        f"<p style='text-align:center;margin:.45rem 0;color:#5B6576'>สไลด์ {st.session_state[key]} / {len(pages)}</p>",
        unsafe_allow_html=True,
    )
    if c3.button("ถัดไป ▶", width="stretch", disabled=st.session_state[key] >= len(pages), key=key + "_n"):
        st.session_state[key] += 1
        st.rerun()

    st.image(pages[st.session_state[key] - 1], width="stretch")
    with st.expander("ดูสไลด์ทั้งหมด"):
        cols = st.columns(3)
        for i, img in enumerate(pages):
            cols[i % 3].image(img, caption=f"สไลด์ {i+1}", width="stretch")
    st.download_button("ดาวน์โหลดสไลด์ (PDF)", file.read_bytes(), file_name=file.name, mime="application/pdf")


def show_notebook(path: str):
    """แสดงไฟล์ .ipynb: ข้อความ markdown, โค้ด และผลลัพธ์"""
    nb = json.loads((BASE / path).read_text(encoding="utf-8"))
    for cell in nb.get("cells", []):
        src = "".join(cell.get("source", []))
        if cell["cell_type"] == "markdown":
            st.markdown(src)
        elif cell["cell_type"] == "code" and src.strip():
            st.code(src, language="python")
            for out in cell.get("outputs", []):
                data = out.get("data", {})
                if "image/png" in data:
                    st.image(base64.b64decode(data["image/png"]))
                elif "text/html" in data and "<table" in "".join(data["text/html"]):
                    components.html("".join(data["text/html"]), height=320, scrolling=True)
                elif "text/plain" in data:
                    st.text("".join(data["text/plain"])[:4000])
                elif out.get("output_type") == "stream":
                    st.text("".join(out.get("text", []))[:4000])


# ───────────────────────── หน้าแรก ─────────────────────────
def home():
    st.markdown(
        f"""
<div class="hero">
  <p style="margin:0;color:#8A6A1F;font-weight:600">{OWNER["course"]}</p>
  <div class="display">{OWNER["name"]}</div>
  <p>{OWNER["student_id"]} · กลุ่ม {OWNER["group"]}<br>{OWNER["major"]}</p>
</div>
""",
        unsafe_allow_html=True,
    )
    st.markdown("### งานทั้งหมด")
    for i, w in enumerate(WORKS):
        kind = '<span class="chip app">เว็บแอป</span>' if w["kind"] == "app" else '<span class="chip">Google Colab</span>'
        tags = "".join(f'<span class="chip">{t}</span>' for t in w.get("tags", []))
        slides = '<span class="chip">มีสไลด์</span>' if w.get("slides") else ""
        left, right = st.columns([5, 1.4], vertical_alignment="center")
        left.markdown(
            f'<div class="row"><div class="no">{i+1}</div><div><h3>{w["title"]}</h3>'
            f'<p>{w["desc"]}</p>{kind}{slides}{tags}</div></div>',
            unsafe_allow_html=True,
        )
        right.button("เปิดดูงาน", key=f"open_{i}", on_click=go, args=(PAGES[i + 1],), width="stretch")


# ───────────────────────── หน้างาน ─────────────────────────
def work_page(i: int):
    w = WORKS[i]
    st.button("← กลับหน้าแรก", on_click=go, args=(PAGES[0],))
    st.markdown(f"# {i+1}. {w['title']}")
    st.write(w["desc"])

    if w["kind"] == "colab":
        st.link_button("เปิดใน Google Colab", w["url"], type="primary")
        nb = w.get("notebook")
        if nb and (BASE / nb).exists():
            st.divider()
            show_notebook(nb)
        else:
            st.markdown(
                '<div class="note">Colab ไม่อนุญาตให้ฝังในเว็บอื่น จึงต้องกดปุ่มเพื่อเปิด '
                f'ถ้าอยากให้โค้ดแสดงในหน้านี้ด้วย ให้ดาวน์โหลดไฟล์ .ipynb จาก Colab แล้ววางไว้ที่ <code>{nb}</code></div>',
                unsafe_allow_html=True,
            )
        return

    # งานที่เป็นเว็บแอป
    tabs = st.tabs(["เว็บแอป", "สไลด์นำเสนอ"] if w.get("slides") else ["เว็บแอป"])
    with tabs[0]:
        st.link_button("เปิดเว็บแอปในแท็บใหม่", w["url"], type="primary")
        st.caption("ถ้าเว็บด้านล่างขึ้นว่าแอปหลับอยู่ ให้กดปลุก (Yes, get this app back up) แล้วรอสักครู่")
        src = w["url"].rstrip("/") + "/?embed=true"
        if hasattr(st, "iframe"):
            st.iframe(src, height=820)
        else:
            components.iframe(src, height=820, scrolling=True)
    if w.get("slides"):
        with tabs[1]:
            show_slides(w["slides"])


# ───────────────────────── เลือกหน้า ─────────────────────────
idx = PAGES.index(st.session_state.page)
home() if idx == 0 else work_page(idx - 1)
