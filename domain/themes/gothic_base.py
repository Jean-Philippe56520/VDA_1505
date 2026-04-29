DARK_AGE_CSS = """
<style>
:root{
  --bg0:#050509; --bg1:#0B0A12;

  /* cards un peu plus opaques => texte plus lisible */
  --card:rgba(18,17,24,.96);
  --card2:rgba(24,22,32,.96);

  --text:#F2EDE3;
  --text2:rgba(242,237,227,.94);

  /* MUTED trop faible avant => on remonte */
  --muted:rgba(242,237,227,.82);

  --accent:#8E0F1E; --gold:#C6A36A; --border:rgba(198,163,106,.26);
  --shadow:0 14px 40px rgba(0,0,0,.55);

  --r-lg:18px; --space-2:14px; --space-3:18px;

  --font-title:ui-serif,Georgia,"Times New Roman",serif;
  --font-body:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Arial,sans-serif;
}

html, body{
  background:
    radial-gradient(1200px 700px at 15% 0%, rgba(142,15,30,.18) 0%, transparent 60%),
    radial-gradient(900px 600px at 88% 18%, rgba(198,163,106,.10) 0%, transparent 55%),
    linear-gradient(180deg,var(--bg1),var(--bg0)) !important;
  color:var(--text) !important;
  font-family:var(--font-body) !important;
}

/* Force containers transparent */
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stMainBlockContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
.main, .block-container{
  background:transparent !important;
}

[data-testid="stSidebar"]{ display:none; }
section.main > div{ padding-top:1rem; }

/* Cards */
.kiosk-card{
  background:var(--card);
  border:1px solid var(--border);
  border-radius:var(--r-lg);
  padding:var(--space-3);
  box-shadow:var(--shadow);
  margin-bottom:var(--space-2);
  position:relative;
  overflow:hidden;
}

.kiosk-card::before{
  content:"";
  position:absolute; inset:0;
  background:radial-gradient(650px 130px at 16% 0%, rgba(198,163,106,.11), transparent 60%);
  pointer-events:none;
}

/* Titles */
.kiosk-title{
  font-family:var(--font-title);
  margin:0 0 6px 0;
  color:var(--text) !important;
  text-shadow: 0 2px 18px rgba(0,0,0,.45);
}

.kiosk-sub{
  color:var(--muted) !important;
  font-size:.95rem;
}

.smallcaps{
  font-variant:small-caps;
  letter-spacing:.8px;
  color:rgba(242,237,227,.90) !important;  /* plus visible */
  margin-bottom:6px;
}

/* Markdown only inside cards */
.kiosk-card .stMarkdown,
.kiosk-card .stMarkdown p,
.kiosk-card .stMarkdown li,
.kiosk-card .stMarkdown span{
  color:var(--text2) !important;
  line-height:1.60;
  font-size:1.00rem;
}

/* Headings */
.kiosk-card h1,.kiosk-card h2,.kiosk-card h3,
.stMarkdown h1,.stMarkdown h2,.stMarkdown h3{
  color:var(--text) !important;
  font-family:var(--font-title) !important;
  letter-spacing:.2px;
}

/* Buttons */
button:focus-visible{
  outline:2px solid rgba(198,163,106,.95) !important;
  outline-offset:2px !important;
}

button[kind="primary"]{
  background:
    radial-gradient(420px 90px at 15% 12%, rgba(198,163,106,.18), transparent 58%),
    linear-gradient(180deg, rgba(142,15,30,.98), rgba(66,4,11,.98)) !important;
  border:1px solid rgba(198,163,106,.50) !important;
  border-radius:16px !important;
  box-shadow:0 14px 28px rgba(0,0,0,.40) !important;
  font-weight:850 !important;
  transition:transform 120ms ease, filter 120ms ease !important;
}

button[kind="primary"]:hover{ filter:brightness(1.06) !important; transform:translateY(-1px) !important; }
button[kind="primary"]:active{ transform:translateY(0) scale(.995) !important; }

button[kind="secondary"]{
  border:1px solid rgba(198,163,106,.44) !important;
  border-radius:14px !important;
}

/* Seal medallion */
.seal-medallion{
  width:42px; height:42px; border-radius:999px; display:grid; place-items:center;
  background:
    radial-gradient(12px 12px at 30% 30%, rgba(255,255,255,.22), transparent 55%),
    radial-gradient(18px 18px at 70% 85%, rgba(0,0,0,.26), transparent 60%),
    linear-gradient(180deg, rgba(198,163,106,.98), rgba(122,90,40,.98));
  border:1px solid rgba(0,0,0,.25);
  box-shadow: inset 0 2px 6px rgba(0,0,0,.28), 0 8px 18px rgba(0,0,0,.25);
  color:rgba(12,10,10,.94);
  font-weight:900;
  font-size:1.05rem;
}

/* Conversation */
.chat{ display:grid; gap:10px; }

.bubble{
  border-radius:16px;
  border:1px solid rgba(198,163,106,.26);
  padding:12px 14px;
  box-shadow:0 10px 24px rgba(0,0,0,.28);
  max-width:92%;
}

.bubble .role{
  font-variant:small-caps;
  letter-spacing:.7px;
  color:rgba(242,237,227,.88); /* plus visible */
  margin-bottom:6px;
}

.bubble.bot{
  background:var(--card2);
  justify-self:start;
}

/* IMPORTANT: contenu de la bulle BOT => forcé lisible */
.bubble.bot .content{
  color:rgba(242,237,227,.94) !important;
  line-height:1.60;
}

.bubble.pj{
  background:
    radial-gradient(420px 80px at 15% 12%, rgba(198,163,106,.14), transparent 58%),
    linear-gradient(180deg, rgba(142,15,30,.90), rgba(66,4,11,.90));
  border:1px solid rgba(198,163,106,.42);
  justify-self:end;
}
.bubble.pj .content{ color:rgba(242,237,227,.96) !important; }

.fade-in{ animation:fadeIn 220ms ease-out; }
@keyframes fadeIn{ from{opacity:0; transform:translateY(3px);} to{opacity:1; transform:translateY(0);} }
</style>
"""
