"""
แฟ้มงาน ระบบฐานข้อมูลขั้นสูง — ณรงค์ศักดิ์ ประเสริฐศิริสร 664245033
รวมงานทุกชิ้นไว้ในเว็บเดียว เปิดหน้าแรกแล้วคลิกเข้าไปดูงานแต่ละชิ้น

แก้ข้อมูลได้ที่ OWNER, GROUPS และ WORKS ด้านล่างเท่านั้น
"""
import json
import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

BASE = Path(__file__).parent

# ═════════════════════════ ข้อมูลผู้ทำ ═════════════════════════
OWNER = {
    "name": "ณรงค์ศักดิ์ ประเสริฐศิริสร",
    "name_en": "Narongsak Prasertsirisorn",
    "student_id": "664245033",
    "group": "66/44",
    "major": "สาขาวิชาวิทยาการคอมพิวเตอร์ มหาวิทยาลัยราชภัฏนครปฐม",
    "course": "ระบบฐานข้อมูลขั้นสูง",
    "github": "",  # ใส่ลิงก์ GitHub เช่น https://github.com/xxxx
}

# ═════════════════════════ หมวดงาน ═════════════════════════
# steps=True คืองานในหมวดนี้ทำต่อกันเป็นขั้นตอน จะแสดงเป็นลำดับขั้น
GROUPS = {
    "single": {"title": "งานเดี่ยว", "desc": "", "steps": False},
    "hair": {
        "title": "โปรเจกต์ระบบแนะนำทรงผม",
        "desc": "แนะนำทรงผมจากคนที่ชอบทรงเดียวกัน เก็บความชอบเป็นกราฟใน Neo4j "
                "เริ่มจากทดลองใน Notebook แล้วต่อยอดเป็นเว็บแอปที่ใช้งานได้จริง",
        "steps": True,
        "cover": "slides/cover.png",
    },
}

# ═════════════════════════ รายการงาน ═════════════════════════
# kind: "colab" = เปิดใน Colab | "app" = ฝังเว็บ Streamlit ไว้ในหน้า
# notebook: (ไม่บังคับ) ไฟล์ .ipynb ใน notebooks/ ถ้ามีจะแสดงโค้ดและผลลัพธ์ในหน้าเว็บ
#           ดาวน์โหลดจาก Colab: File > Download > Download .ipynb
WORKS = [
    {
        "group": "single",
        "title": "งานที่ 1",
        "short": "งานที่ 1",
        "desc": "ใส่คำอธิบายงานสั้นๆ ตรงนี้",
        "kind": "colab",
        "url": "https://colab.research.google.com/drive/16Crmgia47GJb6Cxth-sQ4d8jE6Kbaljq",
        "notebook": "notebooks/work1.ipynb",
        "tags": [],
    },
    {
        "group": "hair",
        "title": "ทดลองบน Notebook ส่วนที่ 1",
        "short": "Notebook ส่วนที่ 1",
        "desc": "ทดลองสร้างกราฟความชอบทรงผม และเขียนคำสั่ง Cypher ใน Google Colab",
        "kind": "colab",
        "url": "https://colab.research.google.com/drive/1n65rgMpIrAEsFAzJtuLto18_5NTA4hUN",
        "notebook": "notebooks/work2.ipynb",
        "tags": ["Neo4j", "Cypher", "Python"],
    },
    {
        "group": "hair",
        "title": "ทดลองบน Notebook ส่วนที่ 2",
        "short": "Notebook ส่วนที่ 2",
        "desc": "ต่อจากส่วนที่ 1 ใน Google Colab",
        "kind": "colab",
        # ⚠ ลิงก์นี้ซ้ำกับงานที่ 1 — เปลี่ยนเป็นลิงก์ที่ถูกต้อง
        "url": "https://colab.research.google.com/drive/16Crmgia47GJb6Cxth-sQ4d8jE6Kbaljq",
        "notebook": "notebooks/work3.ipynb",
        "tags": ["Neo4j", "Cypher", "Python"],
    },
    {
        "group": "hair",
        "title": "HairGraph เว็บแอปแนะนำทรงผม",
        "short": "เว็บแอป HairGraph",
        "desc": "เว็บธีมร้านตัดผม 7 เมนู แนะนำทรงผมพร้อมเหตุผล เพิ่ม ลบ แก้ไขข้อมูลได้ เชื่อมกับ Neo4j Aura",
        "kind": "app",
        "url": "https://b39sfnld4ezgbapv3ijnor.streamlit.app/",
        "slides": "slides/hairgraph.pdf",
        "tags": ["Neo4j Aura", "Cypher", "Streamlit"],
    },
]

KIND_LABEL = {"colab": "Google Colab", "app": "เว็บแอป"}

# ═════════════════════════ หน้าตา ═════════════════════════
st.set_page_config(page_title="แฟ้มงาน · " + OWNER["name"], page_icon="📂", layout="wide")

CSS = """
<link href="https://fonts.googleapis.com/css2?family=Chonburi&family=Sarabun:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
:root{ --navy:#1C2A42; --navy2:#26375500; --brass:#C9A24A; --brass-ink:#7E611B;
       --ink:#1E2633; --muted:#5B6576; --line:#DCE1E8; --paper:#F4F5F7; --card:#FFFFFF; }
html, body, [class*="css"], .stMarkdown, button, input, textarea { font-family:'Sarabun', sans-serif; }
.block-container{ max-width:1120px; padding-top:3.6rem; }
h1,h2,h3,.display{ font-family:'Chonburi', serif !important; font-weight:400 !important; color:var(--navy); letter-spacing:0; }

/* ── แถบข้าง ── */
[data-testid="stSidebar"]{ background:var(--navy); }
[data-testid="stSidebar"] *{ color:#E6EAF1; }
[data-testid="stSidebar"] .brand{ font-family:'Chonburi',serif; font-size:1.4rem; color:#fff; }
[data-testid="stSidebar"] .brand-sub{ color:var(--brass); font-size:.88rem; margin:-.2rem 0 1rem; }
[data-testid="stSidebar"] .nav-head{ font-size:.8rem; color:#9AA6BA; margin:1.1rem 0 .35rem; font-weight:600; }
[data-testid="stSidebar"] .stButton button{
  justify-content:flex-start; text-align:left; background:transparent; border:1px solid transparent;
  padding:.35rem .7rem; min-height:0; border-radius:6px; }
[data-testid="stSidebar"] .stButton button > div{ justify-content:flex-start; width:100%; }
[data-testid="stSidebar"] .stButton button p{ text-align:left; }
[data-testid="stSidebar"] .stButton button:hover{ background:rgba(255,255,255,.07); border-color:transparent; }
[data-testid="stSidebar"] [data-testid="stElementContainer"]{ margin-bottom:-.6rem; }
[data-testid="stSidebar"] .stButton button[kind="primary"]{ background:rgba(201,162,74,.16); border-left:3px solid var(--brass); }
[data-testid="stSidebar"] .stButton button[kind="primary"] p{ color:#fff; font-weight:600; }
[data-testid="stSidebar"] .who{ font-size:.85rem; color:#B9C2D1; line-height:1.55; }

/* ── หน้าแรก ── */
.hero{ background:var(--navy); color:#fff; border-radius:14px; padding:2rem 2.2rem; margin-bottom:2.2rem;
       display:grid; grid-template-columns:1fr auto; gap:1.5rem; align-items:end; }
.hero .course{ color:var(--brass); font-weight:600; margin:0 0 .4rem; }
.hero .display{ color:#fff; font-size:clamp(1.8rem,4.2vw,2.9rem); line-height:1.2; margin:0; }
.hero .en{ color:#B9C2D1; margin:.3rem 0 0; }
.hero dl{ margin:0; display:grid; grid-template-columns:auto auto; gap:.25rem 1rem; font-size:.95rem; }
.hero dt{ color:#9AA6BA; } .hero dd{ margin:0; color:#fff; font-weight:600; }
@media (max-width:700px){ .hero{ grid-template-columns:1fr; } }

.sec-title{ display:flex; align-items:baseline; gap:.8rem; margin:0 0 .3rem; }
.sec-title .h{ font-family:'Chonburi',serif; font-size:1.6rem; color:var(--navy); line-height:1.3; }
.sec-title span{ color:var(--muted); font-size:.95rem; }
.sec-desc{ color:var(--muted); max-width:70ch; margin:0 0 1.2rem; }

.card{ background:var(--card); border:1px solid var(--line); border-radius:10px; padding:1.1rem 1.2rem 1rem; min-height:13.5rem; margin-bottom:.5rem; }
.card .kind{ font-size:.8rem; font-weight:600; color:var(--muted); }
.card .kind.app{ color:var(--brass-ink); }
.card .t{ font-family:'Chonburi',serif; font-size:1.15rem; color:var(--navy); margin:.3rem 0 .4rem; line-height:1.4; }
.card p{ color:var(--muted); margin:0; font-size:.95rem; line-height:1.55; }
.chip{ display:inline-block; font-size:.76rem; padding:.05rem .55rem; border-radius:999px;
       background:var(--paper); color:var(--muted); margin:.55rem .3rem 0 0; }

/* ลำดับขั้นของโปรเจกต์ */
.track{ display:flex; align-items:center; margin:.2rem 0 .7rem; }
.track .dot{ width:2rem; height:2rem; border-radius:50%; background:var(--navy); color:#fff;
             display:grid; place-items:center; font-weight:700; flex:none; }
.track .dot.last{ background:var(--brass); color:var(--navy); }
.track .bar{ flex:1; height:2px; background:var(--line); margin-left:.6rem; }
.track .step{ font-size:.85rem; color:var(--muted); margin-left:.6rem; white-space:nowrap; }

/* ── หน้างาน ── */
.crumb{ color:var(--muted); font-size:.9rem; margin-bottom:.4rem; }
.crumb b{ color:var(--ink); font-weight:600; }
.page-head h1{ font-size:clamp(1.6rem,3.4vw,2.3rem); margin:.1rem 0 .4rem; line-height:1.3; }
.page-head p{ color:var(--muted); font-size:1.03rem; max-width:70ch; margin:0; }
.facts{ display:flex; flex-wrap:wrap; gap:.5rem 1.6rem; padding:.9rem 0; margin:1rem 0 1.2rem;
        border-top:1px solid var(--line); border-bottom:1px solid var(--line); font-size:.92rem; }
.facts div span{ color:var(--muted); margin-right:.4rem; }
.stepper{ display:flex; gap:.4rem; margin:.6rem 0 0; flex-wrap:wrap; }
.stepper div{ font-size:.82rem; padding:.2rem .7rem; border-radius:999px; border:1px solid var(--line); color:var(--muted); }
.stepper div.on{ background:var(--navy); border-color:var(--navy); color:#fff; }
.note{ background:var(--card); border:1px solid var(--line); border-left:4px solid var(--brass);
       border-radius:8px; padding:.9rem 1.1rem; color:var(--muted); font-size:.94rem; }
.note b{ color:var(--ink); }

.stButton button:focus-visible, a:focus-visible{ outline:3px solid var(--brass); outline-offset:2px; }
</style>
"""
# ตัดบรรทัดว่างออก ไม่งั้น markdown จะแสดง CSS เป็นข้อความ
st.markdown("\n".join(l for l in CSS.splitlines() if l.strip()), unsafe_allow_html=True)

if "page" not in st.session_state:
    st.session_state.page = -1  # -1 = หน้าแรก, 0.. = ลำดับใน WORKS


def go(i: int):
    st.session_state.page = i


def works_in(group: str):
    return [(i, w) for i, w in enumerate(WORKS) if w["group"] == group]


def chips(tags):
    return "".join(f'<span class="chip">{t}</span>' for t in tags)


# ═════════════════════════ แถบข้าง ═════════════════════════
with st.sidebar:
    st.markdown(
        f'<div class="brand">แฟ้มงาน</div><div class="brand-sub">{OWNER["course"]}</div>',
        unsafe_allow_html=True,
    )
    st.button("หน้าแรก", on_click=go, args=(-1,), width="stretch",
              type="primary" if st.session_state.page == -1 else "secondary")
    for gkey, g in GROUPS.items():
        items = works_in(gkey)
        if not items:
            continue
        st.markdown(f'<div class="nav-head">{g["title"]}</div>', unsafe_allow_html=True)
        for n, (i, w) in enumerate(items, 1):
            label = f"ขั้นที่ {n} · {w['short']}" if g["steps"] else w["short"]
            st.button(label, key=f"nav_{i}", on_click=go, args=(i,), width="stretch",
                      type="primary" if st.session_state.page == i else "secondary")
    st.divider()
    st.markdown(
        f'<div class="who">{OWNER["name"]}<br>รหัส {OWNER["student_id"]} · กลุ่ม {OWNER["group"]}</div>',
        unsafe_allow_html=True,
    )
    if OWNER["github"]:
        st.link_button("GitHub", OWNER["github"], width="stretch")


# ═════════════════════════ ตัวช่วย ═════════════════════════
@st.cache_data(show_spinner="กำลังเตรียมสไลด์…")
def pdf_pages(path: str) -> list[bytes]:
    import pymupdf

    doc = pymupdf.open(path)
    return [p.get_pixmap(matrix=pymupdf.Matrix(1.6, 1.6)).tobytes("png") for p in doc]


def show_slides(path: str):
    file = BASE / path
    if not file.exists():
        st.info(f"ยังไม่พบไฟล์สไลด์ `{path}` ให้วางไฟล์ PDF ไว้ที่ตำแหน่งนี้ใน GitHub")
        return
    pages = pdf_pages(str(file))
    key = f"slide_{path}"
    st.session_state.setdefault(key, 1)
    cur = st.session_state[key]

    st.image(pages[cur - 1], width="stretch")
    c1, c2, c3 = st.columns([1, 2, 1], vertical_alignment="center")
    if c1.button("◀ ก่อนหน้า", width="stretch", disabled=cur <= 1, key=key + "_p"):
        st.session_state[key] -= 1
        st.rerun()
    c2.markdown(f"<p style='text-align:center;margin:0;color:#5B6576'>สไลด์ {cur} จาก {len(pages)}</p>",
                unsafe_allow_html=True)
    if c3.button("ถัดไป ▶", width="stretch", disabled=cur >= len(pages), key=key + "_n"):
        st.session_state[key] += 1
        st.rerun()

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


def embed(url: str, height: int = 820):
    if hasattr(st, "iframe"):
        st.iframe(url, height=height)
    else:
        components.iframe(url, height=height, scrolling=True)


def work_card(i: int, w: dict, step: int | None = None, last: bool = False):
    if step is not None:
        st.markdown(
            f'<div class="track"><div class="dot{" last" if last else ""}">{step}</div>'
            f'<div class="step">ขั้นที่ {step}</div><div class="bar"></div></div>',
            unsafe_allow_html=True,
        )
    kind_cls = " app" if w["kind"] == "app" else ""
    extra = " · มีสไลด์" if w.get("slides") else ""
    st.markdown(
        f'<div class="card"><div class="kind{kind_cls}">{KIND_LABEL[w["kind"]]}{extra}</div>'
        f'<div class="t">{w["title"]}</div><p>{w["desc"]}</p>{chips(w.get("tags", []))}</div>',
        unsafe_allow_html=True,
    )
    st.button("เปิดดูงาน", key=f"open_{i}", on_click=go, args=(i,), width="stretch",
              type="primary" if w["kind"] == "app" else "secondary")


# ═════════════════════════ หน้าแรก ═════════════════════════
def home():
    st.markdown(
        f"""
<div class="hero">
  <div>
    <p class="course">แฟ้มงานรายวิชา{OWNER["course"]}</p>
    <div class="display">{OWNER["name"]}</div>
    <p class="en">{OWNER["name_en"]}</p>
  </div>
  <dl>
    <dt>รหัสนักศึกษา</dt><dd>{OWNER["student_id"]}</dd>
    <dt>กลุ่มเรียน</dt><dd>{OWNER["group"]}</dd>
    <dt>จำนวนงาน</dt><dd>{len(WORKS)} ชิ้น</dd>
  </dl>
</div>
""",
        unsafe_allow_html=True,
    )

    for gkey, g in GROUPS.items():
        items = works_in(gkey)
        if not items:
            continue
        st.markdown(
            f'<div class="sec-title"><div class="h">{g["title"]}</div><span>{len(items)} ชิ้น</span></div>',
            unsafe_allow_html=True,
        )
        cover = g.get("cover")
        if cover and (BASE / cover).exists():
            c1, c2 = st.columns([3, 2], gap="large", vertical_alignment="center")
            c1.markdown(f'<p class="sec-desc">{g["desc"]}</p>', unsafe_allow_html=True)
            c2.image(str(BASE / cover), width="stretch")
            st.write("")
        elif g["desc"]:
            st.markdown(f'<p class="sec-desc">{g["desc"]}</p>', unsafe_allow_html=True)

        if g["steps"]:
            cols = st.columns(len(items), gap="medium")
            for n, ((i, w), col) in enumerate(zip(items, cols), 1):
                with col:
                    work_card(i, w, step=n, last=n == len(items))
        else:
            cols = st.columns(3, gap="medium")
            for k, (i, w) in enumerate(items):
                with cols[k % 3]:
                    work_card(i, w)
        st.write("")
        st.write("")


# ═════════════════════════ หน้างาน ═════════════════════════
def work_page(i: int):
    w = WORKS[i]
    g = GROUPS[w["group"]]
    items = works_in(w["group"])
    pos = [j for j, _ in items].index(i)

    st.markdown(f'<div class="crumb">หน้าแรก / {g["title"]} / <b>{w["short"]}</b></div>',
                unsafe_allow_html=True)
    stepper = ""
    if g["steps"]:
        stepper = '<div class="stepper">' + "".join(
            f'<div class="{"on" if j == i else ""}">ขั้นที่ {n} {x["short"]}</div>'
            for n, (j, x) in enumerate(items, 1)
        ) + "</div>"
    st.markdown(f'<div class="page-head"><h1>{w["title"]}</h1><p>{w["desc"]}</p>{stepper}</div>',
                unsafe_allow_html=True)

    tools = ", ".join(w.get("tags", [])) or "-"
    st.markdown(
        f'<div class="facts"><div><span>ประเภท</span>{KIND_LABEL[w["kind"]]}</div>'
        f'<div><span>เครื่องมือ</span>{tools}</div>'
        f'<div><span>หมวด</span>{g["title"]}</div></div>',
        unsafe_allow_html=True,
    )

    if w["kind"] == "colab":
        st.link_button("เปิดใน Google Colab", w["url"], type="primary")
        st.write("")
        nb = w.get("notebook")
        if nb and (BASE / nb).exists():
            show_notebook(nb)
        else:
            st.markdown(
                '<div class="note"><b>เปิดงานนี้ด้วยปุ่มด้านบน</b> เพราะ Colab ไม่ให้ฝังลงในเว็บอื่น<br>'
                f'ถ้าอยากให้โค้ดแสดงในหน้านี้ ให้ดาวน์โหลดไฟล์ .ipynb จาก Colab แล้ววางไว้ที่ <code>{nb}</code></div>',
                unsafe_allow_html=True,
            )
    else:
        tabs = st.tabs(["เว็บแอป", "สไลด์นำเสนอ"] if w.get("slides") else ["เว็บแอป"])
        with tabs[0]:
            c1, c2 = st.columns([1, 3], vertical_alignment="center")
            c1.link_button("เปิดในแท็บใหม่", w["url"], type="primary", width="stretch")
            c2.caption("ถ้าแอปขึ้นว่าหลับอยู่ ให้กดปุ่มปลุกแอปแล้วรอประมาณ 30 วินาที")
            embed(w["url"].rstrip("/") + "/?embed=true")
        if w.get("slides"):
            with tabs[1]:
                show_slides(w["slides"])

    # ไปขั้นก่อนหน้า / ถัดไป ในหมวดเดียวกัน
    if g["steps"] and len(items) > 1:
        st.divider()
        c1, _, c3 = st.columns([1, 1, 1])
        if pos > 0:
            j, x = items[pos - 1]
            c1.button(f"◀ ขั้นที่ {pos}: {x['short']}", on_click=go, args=(j,), width="stretch")
        if pos < len(items) - 1:
            j, x = items[pos + 1]
            c3.button(f"ขั้นที่ {pos + 2}: {x['short']} ▶", on_click=go, args=(j,), width="stretch")


# ═════════════════════════ เลือกหน้า ═════════════════════════
if st.session_state.page == -1:
    home()
else:
    work_page(st.session_state.page)
