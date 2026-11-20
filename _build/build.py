"""Static site generator for Aiflow. Run: python3 _build/build.py
Shared head / nav / footer are injected into every page so the output is plain, SEO-friendly HTML."""
from pathlib import Path
import os

ROOT = Path(__file__).resolve().parent.parent
SITE = os.environ.get("SITE_URL", "https://aiflow-agents.vercel.app")
KEYWORDS = ("AI agents, AI automation agency, AI workflow automation, autonomous AI agents, "
            "multi-agent systems, business process automation, AI chatbot development, "
            "LLM integration, AI SaaS, no-code AI, agentic AI, AI for small business, "
            "AI customer support automation, AI developer, hire AI engineer")

LOGO_SVG = '<svg width="16" height="16" viewBox="0 0 24 24" fill="#fff"><circle cx="12" cy="6" r="4"/><circle cx="6" cy="16" r="4"/><circle cx="18" cy="16" r="4"/></svg>'
ARROW = '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'

I = {  # small inline icon set (stroke icons)
 'bolt': '<path d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 'flow': '<circle cx="5" cy="6" r="2.5"/><circle cx="19" cy="6" r="2.5"/><circle cx="12" cy="18" r="2.5"/><path d="M7 7.5 10.5 16M17 7.5 13.5 16M7.5 6h9"/>',
 'brain': '<path d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 6 1V5a2 2 0 0 0-3-1zM15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-6 1"/>',
 'shield': '<path d="M12 3 4 6v6c0 5 3.5 8 8 9 4.5-1 8-4 8-9V6z"/><path d="m9 12 2 2 4-4"/>',
 'chart': '<path d="M4 20V10M10 20V4M16 20v-7M22 20H2"/>',
 'chat': '<path d="M21 12a8 8 0 0 1-11.6 7.1L4 20l1-4.6A8 8 0 1 1 21 12z"/>',
 'plug': '<path d="M9 2v6M15 2v6M6 8h12v4a6 6 0 0 1-12 0zM12 18v4"/>',
 'search': '<circle cx="11" cy="11" r="7"/><path d="m20 20-4-4"/>',
 'mail': '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/>',
 'code': '<path d="m8 8-5 4 5 4M16 8l5 4-5 4M14 4l-4 16"/>',
 'cart': '<circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M2 3h3l3 12h11l2-8H6"/>',
 'users': '<circle cx="9" cy="8" r="3.5"/><path d="M2 20a7 7 0 0 1 14 0M16 4a3.5 3.5 0 0 1 0 7M22 20a7 7 0 0 0-4-6.3"/>',
 'home': '<path d="m3 11 9-7 9 7v9a1 1 0 0 1-1 1h-5v-6H9v6H4a1 1 0 0 1-1-1z"/>',
 'cog': '<circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/>',
 'logout': '<path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4M16 17l5-5-5-5M21 12H9"/>',
 'clock': '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>',
 'globe': '<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/>',
}
def icon(n, s=20):
    return f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">{I[n]}</svg>'

NAV = [("index.html", "home", "Home"), ("solutions.html", "solutions", "Solutions"), ("features.html", "features", "Features"),
       ("customers.html", "customers", "Customers"), ("pricing.html", "pricing", "Pricing"), ("contact.html", "contact", "Contact")]

def head(title, desc, path):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{KEYWORDS}">
<meta name="author" content="Aiflow">
<meta name="robots" content="index, follow">
<link rel="canonical" href="{SITE}/{'' if path == 'index.html' else path}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Aiflow">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{SITE}/{'' if path == 'index.html' else path}">
<meta property="og:image" content="{SITE}/assets/img/og-cover.jpg">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{SITE}/assets/img/og-cover.jpg">
<meta name="theme-color" content="#0d0d0e">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/style.css">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"SoftwareApplication","name":"Aiflow","applicationCategory":"BusinessApplication","operatingSystem":"Web","description":"{desc}","url":"{SITE}","offers":{{"@type":"Offer","price":"0","priceCurrency":"USD"}},"aggregateRating":{{"@type":"AggregateRating","ratingValue":"4.9","ratingCount":"8000"}}}}</script>
</head>"""

SVG_FILTER = """<svg width="0" height="0" style="position:absolute" aria-hidden="true"><filter id="liquid" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.008 0.012" numOctaves="2" seed="7" result="n"/><feGaussianBlur in="n" stdDeviation="2" result="b"/><feDisplacementMap in="SourceGraphic" in2="b" scale="38" xChannelSelector="R" yChannelSelector="G"/></filter></svg>"""

def nav(page):
    links = "".join(f'<a href="{h}" data-page="{p}">{t}</a>' for h, p, t in NAV[1:])
    mlinks = "".join(f'<a class="big" href="{h}" data-page="{p}">{t}</a>' for h, p, t in NAV)
    return f"""<body data-page="{page}">
<div class="curtain"><div class="logo-mark">{LOGO_SVG}</div></div>
<div class="progress"></div>
<div class="cursor-glow" aria-hidden="true"></div>
{SVG_FILTER}
<header class="nav-wrap">
  <nav class="nav" aria-label="Main">
    <a href="index.html" class="logo" aria-label="Aiflow home"><span class="logo-mark">{LOGO_SVG}</span>Aiflow</a>
    <div class="nav-links">{links}</div>
    <div class="nav-actions">
      <a href="login.html" class="signin" data-auth-link>Sign in</a>
      <a href="login.html?mode=signup" class="btn btn-dark btn-sm">Let's Start</a>
      <button class="burger" aria-label="Open menu"><span></span><span></span></button>
    </div>
  </nav>
</header>
<div class="mobile-menu">{mlinks}
  <div class="mm-actions"><a href="login.html" class="btn btn-ghost" data-auth-link>Sign in</a><a href="login.html?mode=signup" class="btn btn-dark">Let's Start <span class="ico">{ARROW}</span></a></div>
</div>
<main>"""

FOOT = f"""</main>
<footer>
  <div class="container">
    <div class="foot-grid">
      <div class="reveal">
        <a href="index.html" class="logo"><span class="logo-mark">{LOGO_SVG}</span>Aiflow</a>
        <p class="muted" style="margin-top:14px;max-width:34ch;font-size:14px">Autonomous AI agents that automate work, optimize workflows and deliver smarter outcomes — every single day.</p>
        <form class="newsletter glass" data-simple="Subscribed! Watch your inbox for agent playbooks.">
          <input class="input" style="height:40px;border:0;background:transparent" type="email" placeholder="you@company.com" required aria-label="Email">
          <button class="btn btn-dark btn-sm" type="submit">Subscribe</button>
        </form>
      </div>
      <div class="reveal" data-delay="1"><h4>Product</h4><ul><li><a href="features.html">Features</a></li><li><a href="solutions.html">Solutions</a></li><li><a href="pricing.html">Pricing</a></li><li><a href="dashboard.html">Dashboard</a></li></ul></div>
      <div class="reveal" data-delay="2"><h4>Company</h4><ul><li><a href="customers.html">Customers</a></li><li><a href="contact.html">Contact</a></li><li><a href="contact.html">Book a demo</a></li><li><a href="login.html">Sign in</a></li></ul></div>
      <div class="reveal" data-delay="3"><h4>Resources</h4><ul><li><a href="features.html#integrations">Integrations</a></li><li><a href="pricing.html#faq">FAQ</a></li><li><a href="features.html#security">Security</a></li><li><a href="contact.html">Support</a></li></ul></div>
    </div>
    <div class="foot-big" aria-hidden="true">Aiflow</div>
    <div class="foot-bottom"><span>© <span data-year></span> Aiflow. All rights reserved.</span><span>Built with autonomous AI agents · Privacy · Terms</span></div>
  </div>
</footer>
<script src="assets/js/main.js"></script>
</body>
</html>"""

def page(fname, key, title, desc, body, chrome=True):
    html = head(title, desc, fname)
    if chrome:
        html += nav(key) + body + FOOT
    else:
        html += body
    (ROOT / fname).write_text(html)

def btn(text, href, cls="btn-dark"):
    return f'<a href="{href}" class="btn {cls}">{text} <span class="ico">{ARROW}</span></a>'

LOGOS = [("Slack", "#e01e5a"), ("Notion", "#111"), ("Stripe", "#635bff"), ("Intercom", "#1f8ded"), ("Databricks", "#ff3621"),
         ("Google", "#4285f4"), ("HubSpot", "#ff7a59"), ("Shopify", "#95bf47"), ("Zendesk", "#03363d"), ("Salesforce", "#00a1e0")]
def logos_strip(label="The world's leading enterprises"):
    chips = "".join(f'<div class="logo-chip"><i style="background:{c}"></i>{n}</div>' for n, c in LOGOS) * 2
    return f'<section class="logos"><div class="container reveal"><p>{label}</p><div class="marquee"><div class="marquee-track">{chips}</div></div></div></section>'

def cta(title="Put your first AI agent to work today", sub="Launch in minutes. Scale to thousands of tasks. No engineering team required."):
    return f"""<section class="section-sm"><div class="container"><div class="cta reveal-scale">
<img class="bg" src="assets/img/ai-globe.webp" alt="" loading="lazy">
<span class="eyebrow glass glass-dark" style="padding:6px 14px">✦ Free 14-day trial</span>
<h2 class="h2 split-words" style="margin-top:22px;max-width:18ch;margin-inline:auto">{title}</h2>
<p class="lead">{sub}</p>
<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap">{btn("Book a Demo", "contact.html", "btn-light")}<a href="login.html?mode=signup" class="btn btn-ghost btn-plain" style="color:#fff;border-color:rgba(255,255,255,.25)">Start free</a></div>
</div></div></section>"""

def page_hero(eyebrow, title, lead, extra=""):
    return f"""<section class="page-hero"><div class="blob"></div><div class="container">
<span class="eyebrow glass reveal"><span class="tag">AIFLOW</span>{eyebrow}</span>
<h1 class="display split-words" style="margin-top:22px">{title}</h1>
<p class="lead reveal" data-delay="2">{lead}</p>{extra}
</div></section>"""

AV_COLORS = ["#ff4d1c", "#3d6bff", "#0d0d0e", "#22a06b", "#a855f7"]
def avatars(inits="AKMJ"):
    return '<div class="avatars">' + "".join(f'<span style="background:{AV_COLORS[i % 5]}">{c}</span>' for i, c in enumerate(inits)) + '</div>'

# ------------------------------------------------------------------ HOME
home = f"""
<section class="hero">
  <div class="container hero-grid">
    <div class="hero-left">
      <span class="eyebrow glass reveal"><span class="tag">PRO</span>Future of agentic AI</span>
      <h1 class="display split-words">AI Agents That Work for You</h1>
      <p class="lead reveal" data-delay="3">Empower your business with AI agents that automate work, optimize workflows, and deliver smarter outcomes every day.</p>
      <div class="reveal" data-delay="4" style="display:flex;gap:12px;flex-wrap:wrap">{btn("Book a Demo", "contact.html")}<a href="features.html" class="btn btn-ghost">See features</a></div>
      <div class="rating reveal" data-delay="5" style="margin-top:40px">{avatars()}<div><span class="stars">★★★★★</span> <b>4.9</b> rating<br><span class="muted">Trusted by 8,000+ enterprise teams</span></div></div>
    </div>
    <div class="hero-visual reveal-scale" data-delay="2">
      <div class="hero-halo"></div>
      <img src="assets/img/hero-woman.webp" alt="AI agent visualised as a woman with glowing neural network constellations" width="900" height="1265" fetchpriority="high">
    </div>
    <div class="hero-right">
      <div class="agent-card glass glass-liquid reveal-r" data-delay="3">
        <div class="head"><div class="av">{LOGO_SVG}</div><div><small>I know how to</small><div class="typed" data-items='["Research competitors automatically","Create a multi-agent workflow","Automate repetitive business tasks","Reply to support tickets 24/7","Analyze this spreadsheet","Qualify inbound sales leads"]'></div></div></div>
        <ul class="agent-list"><li>Create a multi-agent workflow</li><li>Automate repetitive business tasks</li><li>Research my competitors</li><li>Analyze this spreadsheet</li><li>Qualify inbound sales leads</li></ul>
      </div>
      <div style="display:flex;flex-direction:column;gap:24px;align-items:flex-end;width:100%">
        <div class="stat-card glass reveal-r" data-delay="4">
          <div class="row"><span style="font-size:12px" class="muted">Tasks Automated</span><div><div class="num" data-count="98.4" data-suffix="%">0%</div><div class="up">▲ +12% this week</div></div></div>
          <svg class="spark" viewBox="0 0 260 40" preserveAspectRatio="none"><path d="M0 34 L30 30 L60 32 L90 22 L120 25 L150 16 L180 18 L210 9 L240 11 L260 3" fill="none" stroke="#ff4d1c" stroke-width="2.2" stroke-linecap="round"/></svg>
        </div>
        <h2 class="hero-tag split-words">Your AI Agents<br>Don't Sleep.</h2>
      </div>
    </div>
  </div>
</section>
{logos_strip()}

<section class="section">
  <div class="container">
    <div class="section-head">
      <div><span class="eyebrow reveal">✦ What Aiflow does</span><h2 class="h2 split-words" style="margin-top:14px;max-width:14ch">One platform. Unlimited digital workers.</h2></div>
      <p class="lead reveal">Design, deploy and monitor autonomous agents that plug into the tools your team already uses.</p>
    </div>
    <div class="grid g-3">
      <div class="card spot reveal" data-delay="1"><div class="icon">{icon('flow')}</div><h3 class="h3">Multi-agent workflows</h3><p>Chain specialised agents together — researcher, writer, reviewer — and let them hand off work automatically.</p></div>
      <div class="card spot reveal" data-delay="2"><div class="icon">{icon('bolt')}</div><h3 class="h3">Automate anything</h3><p>From invoices to inbox triage, turn repetitive processes into hands-free pipelines in minutes.</p></div>
      <div class="card spot reveal" data-delay="3"><div class="icon">{icon('chart')}</div><h3 class="h3">Real-time insights</h3><p>Track every run, cost and outcome on a live dashboard and let agents optimise themselves.</p></div>
    </div>
  </div>
</section>

<section class="section dark-band">
  <div class="orb" style="width:500px;height:500px;background:#3d6bff;left:-150px;top:-100px"></div>
  <div class="orb" style="width:400px;height:400px;background:#a855f7;right:-120px;bottom:-120px"></div>
  <div class="container split" style="position:relative">
    <div class="reveal-l">
      <div class="media tilt" style="aspect-ratio:1/1"><img src="assets/img/ai-sphere.webp" alt="Robotic hand holding a glowing AI sphere with a city and tree inside" loading="lazy">
        <div class="float-chip glass glass-dark" style="left:18px;bottom:18px"><span class="dot-live"></span>&nbsp; 1,284 agents running now</div></div>
    </div>
    <div>
      <span class="eyebrow reveal">✦ Agentic intelligence</span>
      <h2 class="h2 split-words" style="margin-top:14px">Agents that think, act and learn — around the clock.</h2>
      <p class="lead reveal" style="margin-top:18px">Aiflow agents reason over your data, use tools, and escalate to humans only when it matters.</p>
      <ul class="check-list reveal" data-delay="2"><li>Connects to 200+ apps out of the box</li><li>Memory that remembers customers, projects and context</li><li>Human-in-the-loop approvals for sensitive actions</li><li>Enterprise-grade security with SOC 2 controls</li></ul>
      <div class="reveal" data-delay="3" style="margin-top:32px">{btn("Explore solutions", "solutions.html", "btn-light")}</div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="metrics">
      <div class="reveal"><div class="v" data-count="8000" data-suffix="+">0</div><p class="muted">Teams onboard</p></div>
      <div class="reveal" data-delay="1"><div class="v" data-count="42" data-suffix="M">0</div><p class="muted">Tasks automated monthly</p></div>
      <div class="reveal" data-delay="2"><div class="v" data-count="73" data-suffix="%">0</div><p class="muted">Average time saved</p></div>
      <div class="reveal" data-delay="3"><div class="v" data-count="24" data-suffix="/7">0</div><p class="muted">Always-on coverage</p></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:20px">
  <div class="container">
    <div class="section-head"><div><span class="eyebrow reveal">✦ How it works</span><h2 class="h2 split-words" style="margin-top:14px">Live in three steps</h2></div>{btn("Start free", "login.html?mode=signup")}</div>
    <div class="steps">
      <div class="step reveal"><span class="n">01</span><h3>Describe the job</h3><p class="muted">Tell Aiflow what you need in plain English. It drafts the agent, tools and guardrails for you.</p></div>
      <div class="step reveal"><span class="n">02</span><h3>Connect your stack</h3><p class="muted">One-click integrations with Slack, Notion, Stripe, Google Workspace, HubSpot and 200 more.</p></div>
      <div class="step reveal"><span class="n">03</span><h3>Deploy &amp; scale</h3><p class="muted">Ship to production, monitor outcomes in real time and scale to thousands of runs a day.</p></div>
    </div>
  </div>
</section>

<section class="section" style="padding-top:20px">
  <div class="container split">
    <div>
      <span class="eyebrow reveal">✦ Customer story</span>
      <p class="quote split-words" style="margin-top:18px">“Aiflow took over 70% of our support queue in two weeks. Our team finally works on what matters.”</p>
      <div class="who reveal"><div class="av" style="background:#3d6bff">SO</div><div><b>Sarah Okafor</b><br><span class="muted">Head of Operations, Lumen Retail</span></div></div>
      <div class="reveal" style="margin-top:30px">{btn("Read more stories", "customers.html", "btn-light")}</div>
    </div>
    <div class="media reveal-r" style="aspect-ratio:4/5"><img src="assets/img/robot-vr.webp" alt="Humanoid AI robot wearing a VR headset" loading="lazy"></div>
  </div>
</section>
{cta()}
"""
page("index.html", "home", "Aiflow — AI Agents That Work for You | AI Workflow Automation",
     "Aiflow builds autonomous AI agents that automate work, optimize workflows and deliver smarter business outcomes 24/7. Book a demo today.", home)

# ------------------------------------------------------------------ SOLUTIONS
def sol_panel(key, title, img, alt, points, blend=False, on=False):
    li = "".join(f"<li>{p}</li>" for p in points)
    return f"""<div class="tab-panel split{' on' if on else ''}" data-panel="sol:{key}">
<div><h3 class="h2" style="font-size:clamp(1.8rem,3vw,2.6rem)">{title}</h3><ul class="check-list">{li}</ul><div style="margin-top:30px">{btn("Talk to an expert", "contact.html")}</div></div>
<div class="media" style="aspect-ratio:1/1"><img src="assets/img/{img}" alt="{alt}" loading="lazy"></div></div>"""

solutions = page_hero("Solutions", "AI agents for every team", "Pre-built agent blueprints for sales, support, operations and engineering — customised to your business in days, not months.") + f"""
<section class="section" style="padding-top:20px"><div class="container">
  <div class="tabs glass reveal" data-tabs="sol"><button class="on" data-tab="sales">Sales</button><button data-tab="support">Support</button><button data-tab="ops">Operations</button><button data-tab="eng">Engineering</button></div>
  <div style="margin-top:44px">
  {sol_panel("sales", "Close more deals with an AI SDR", "ai-touch.webp", "Human and robot hand reaching toward each other beneath an AI brain", ["Qualifies inbound leads instantly and books meetings","Researches prospects and writes personalised outreach","Updates CRM records automatically after every call"], on=True)}
  {sol_panel("support", "24/7 customer support agents", "ai-globe.webp", "Robotic hand presenting a glowing AI globe", ["Resolves up to 70% of tickets without a human","Answers on WhatsApp, Telegram, Instagram, chat and email","Escalates edge-cases with full context"])}
  {sol_panel("ops", "Operations on autopilot", "ai-sphere.webp", "Robotic hand holding an AI sphere", ["Processes invoices, purchase orders and reports","Reconciles data across spreadsheets and ERPs","Sends daily briefings to every stakeholder"])}
  {sol_panel("eng", "Ship faster with engineering agents", "robot-vr.webp", "Humanoid AI robot with VR headset", ["Triages bugs and drafts pull requests","Monitors logs and opens incidents automatically","Writes documentation from your codebase"])}
  </div>
</div></section>
<section class="section dark-band"><div class="orb" style="width:500px;height:500px;background:#22d3ee;right:-200px;top:-120px;opacity:.25"></div><div class="container" style="position:relative">
  <div class="section-head"><div><span class="eyebrow reveal">✦ Industries</span><h2 class="h2 split-words" style="margin-top:14px;max-width:16ch">Built for the way your industry works</h2></div></div>
  <div class="grid g-4">
    <div class="card spot reveal"><div class="icon">{icon('cart')}</div><h3 class="h3">E-commerce</h3><p>Order tracking, returns and product recommendations.</p></div>
    <div class="card spot reveal" data-delay="1"><div class="icon">{icon('shield')}</div><h3 class="h3">Finance</h3><p>KYC checks, reconciliation and compliance reports.</p></div>
    <div class="card spot reveal" data-delay="2"><div class="icon">{icon('users')}</div><h3 class="h3">Healthcare</h3><p>Appointment scheduling and patient follow-ups.</p></div>
    <div class="card spot reveal" data-delay="3"><div class="icon">{icon('globe')}</div><h3 class="h3">Agencies</h3><p>Client reporting, content and campaign automation.</p></div>
  </div>
</div></section>
{cta("Not sure where to start?", "We'll map your workflows and recommend the agents with the highest ROI — free.")}"""
page("solutions.html", "solutions", "AI Agent Solutions for Sales, Support & Operations | Aiflow",
     "Ready-made AI agent solutions for sales, customer support, operations and engineering. Automate workflows across e-commerce, finance, healthcare and agencies.", solutions)

# ------------------------------------------------------------------ FEATURES
feats = [("brain", "Reasoning engine", "Agents plan multi-step tasks, use tools and self-correct with the latest LLMs."),
         ("flow", "Visual workflow builder", "Drag-and-drop canvas to orchestrate agents, triggers and approvals."),
         ("chat", "Omnichannel chat", "Deploy agents to web chat, WhatsApp, Telegram, Slack and email."),
         ("search", "Knowledge & memory", "Ground answers in your docs, sites and databases with RAG."),
         ("plug", "200+ integrations", "Native connectors plus a REST API and webhooks for anything else."),
         ("chart", "Analytics & observability", "Trace every decision, measure cost and success rate per agent."),
         ("shield", "Guardrails", "Role-based permissions, PII redaction and human approvals."),
         ("code", "Developer SDK", "Extend agents with custom tools in TypeScript or Python."),
         ("clock", "Schedules & triggers", "Run on a cron, on events, or the moment a form is submitted.")]
fcards = "".join(f'<div class="card spot reveal" data-delay="{i % 3 + 1}"><div class="icon">{icon(ic)}</div><h3 class="h3">{t}</h3><p>{d}</p></div>' for i, (ic, t, d) in enumerate(feats))
integr = "".join(f'<div class="logo-chip reveal" data-delay="{i % 5}"><i style="background:{c}"></i>{n}</div>' for i, (n, c) in enumerate(LOGOS))
features = page_hero("Features", "Everything you need to build AI agents", "A complete toolkit for designing, deploying and scaling autonomous agents — with the control your business demands.") + f"""
<section class="section" style="padding-top:20px"><div class="container"><div class="grid g-3">{fcards}</div></div></section>
<section class="section dark-band"><div class="orb" style="width:520px;height:520px;background:#22d3ee;left:-200px;bottom:-200px;opacity:.3"></div>
<div class="container split" style="position:relative">
  <div><span class="eyebrow reveal">✦ Workflow builder</span><h2 class="h2 split-words" style="margin-top:14px">Design agents visually. Ship them instantly.</h2>
  <p class="lead reveal" style="margin-top:18px">Connect triggers, tools and agents on one canvas. Test with live data, then deploy with one click.</p>
  <div class="glass glass-dark reveal" data-delay="2" style="margin-top:30px;border-radius:20px;padding:18px;font-family:ui-monospace,monospace;font-size:13px;line-height:1.8">
    <div><span style="color:#ff7a45">trigger</span> → new_ticket(zendesk)</div>
    <div><span style="color:#22d3ee">agent</span> → classify_intent()</div>
    <div><span style="color:#22d3ee">agent</span> → search_knowledge_base()</div>
    <div><span style="color:#a78bfa">guard</span> → require_approval(if refund &gt; $200)</div>
    <div><span style="color:#4ade80">action</span> → reply_and_close() <span style="opacity:.5">✓ 1.2s</span></div>
  </div></div>
  <div class="media reveal-r" style="background:#000"><img src="assets/img/neon-hand.webp" alt="Neon hand with glowing AI globe and circuit lines" loading="lazy" style="object-fit:contain;padding:20px"></div>
</div></section>
<section class="section" id="integrations"><div class="container center">
  <span class="eyebrow reveal">✦ Integrations</span><h2 class="h2 split-words" style="margin:14px auto 0;max-width:16ch">Plugs into the tools you already love</h2>
  <div style="display:flex;flex-wrap:wrap;gap:12px;justify-content:center;margin-top:44px">{integr}</div>
</div></section>
<section class="section" id="security" style="padding-top:20px"><div class="container"><div class="grid g-3">
  <div class="card reveal"><div class="num-lg" data-count="99.99" data-suffix="%">0</div><p>Uptime SLA on enterprise plans</p></div>
  <div class="card reveal" data-delay="1"><div class="num-lg">SOC 2</div><p>Type II controls, encryption at rest &amp; in transit</p></div>
  <div class="card reveal" data-delay="2"><div class="num-lg">GDPR</div><p>EU data residency and full data-processing agreements</p></div>
</div></div></section>
{cta()}"""
page("features.html", "features", "Features — Build, Deploy & Monitor AI Agents | Aiflow",
     "Explore Aiflow features: visual AI workflow builder, multi-agent orchestration, RAG knowledge base, 200+ integrations, guardrails and analytics.", features)

# ------------------------------------------------------------------ CUSTOMERS
stories = [("Lumen Retail", "#3d6bff", "70%", "of support tickets automated", "Sarah Okafor, Head of Operations", "Aiflow took over most of our support queue in two weeks. CSAT actually went up."),
           ("Northwind Finance", "#ff4d1c", "12h", "saved per analyst every week", "David Mensah, CFO", "Reconciliation that took days now finishes before our morning coffee."),
           ("Kite Health", "#22a06b", "3x", "more appointments booked", "Dr. Amara Bello, Founder", "Our AI receptionist never misses a call — patients love it."),
           ("Orbit Agency", "#a855f7", "$480k", "new pipeline in one quarter", "Leo Martins, CEO", "The AI SDR researches and writes better first emails than we ever did."),
           ("Brightpath EDU", "#0d0d0e", "40k", "student questions answered", "Grace Adeyemi, Director", "Students get instant answers in WhatsApp at 2am. Game-changer."),
           ("Vela Logistics", "#ff7a45", "58%", "faster order processing", "Tom Fischer, COO", "Purchase orders flow straight into our ERP with zero manual typing.")]
scards = "".join(f"""<div class="card spot reveal" data-delay="{i % 3 + 1}"><div style="display:flex;align-items:center;gap:10px;font-weight:600"><span style="width:12px;height:12px;border-radius:4px;background:{c}"></span>{n}</div>
<div class="num-lg" style="margin-top:26px">{v}</div><p style="margin-top:4px">{m}</p><p style="color:var(--ink);font-size:15px;margin-top:22px">“{q}”</p><p style="font-size:13px">— {who}</p></div>""" for i, (n, c, v, m, who, q) in enumerate(stories))
customers = page_hero("Customers", "Teams that run on Aiflow", "From fast-growing startups to global enterprises, 8,000+ teams trust Aiflow agents with their most important work.") + logos_strip("Trusted by") + f"""
<section class="section"><div class="container"><div class="grid g-3">{scards}</div></div></section>
<section class="section dark-band"><div class="container split">
  <div class="media reveal-l" style="aspect-ratio:3/4"><img src="assets/img/ai-touch.webp" alt="Human finger touching a robot finger beneath an AI circuit head" loading="lazy"></div>
  <div><span class="eyebrow reveal">✦ Featured story</span><p class="quote split-words" style="margin-top:18px">“We replaced six disconnected tools with a team of Aiflow agents. It feels like we hired twenty people overnight.”</p>
  <div class="who reveal"><div class="av" style="background:#ff4d1c">LM</div><div><b>Leo Martins</b><br><span class="muted">CEO, Orbit Agency</span></div></div>
  <div class="rating reveal" style="margin-top:36px">{avatars("RTNE")}<div><span class="stars">★★★★★</span> <b>4.9</b> on G2<br><span class="muted">from 1,200+ reviews</span></div></div></div>
</div></section>
{cta("Become our next success story")}"""
page("customers.html", "customers", "Customer Stories — AI Automation Results | Aiflow",
     "See how 8,000+ teams use Aiflow AI agents to automate customer support, sales, finance and operations with measurable ROI.", customers)

# ------------------------------------------------------------------ PRICING
plans = [("Starter", "29", "23", "For solo founders and freelancers automating their first workflows.", ["3 AI agents", "2,000 tasks / month", "Web chat & email channels", "Community support"], False),
         ("Growth", "99", "79", "For growing teams that need multi-agent workflows.", ["15 AI agents", "25,000 tasks / month", "WhatsApp, Telegram & Instagram", "Workflow builder & analytics", "Priority support"], True),
         ("Enterprise", "Custom", "Custom", "For organisations with advanced security and scale.", ["Unlimited agents", "Unlimited tasks", "SSO, SOC 2 & data residency", "Dedicated success manager"], False)]
def plan_card(n, m, y, d, pts, feat, i):
    li = "".join(f"<li>{p}</li>" for p in pts)
    pr = f'<div class="price"><span data-month="${m}" data-year="${y}">${m}</span><small> /month</small></div>' if m != "Custom" else '<div class="price">Custom</div>'
    b = btn("Get started", "login.html?mode=signup", "btn-light" if feat else "btn-dark") if m != "Custom" else btn("Contact sales", "contact.html", "btn-dark")
    return f'<div class="card price-card{" featured" if feat else ""} reveal" data-delay="{i + 1}"><div style="display:flex;justify-content:space-between;align-items:center"><h3 class="h3">{n}</h3>{"<span class=badge>Most popular</span>" if feat else ""}</div><p style="margin:0">{d}</p>{pr}{b}<ul class="check-list" style="margin-top:6px">{li}</ul></div>'
pcards = "".join(plan_card(*p, i) for i, p in enumerate(plans))
faqs = [("Do I need to know how to code?", "No. Describe what you want in plain English and Aiflow builds the agent. Developers can extend anything with our SDK."),
        ("Which AI models do you use?", "Aiflow is model-agnostic. Use the latest frontier models or bring your own API keys."),
        ("Is my data secure?", "Yes. Data is encrypted in transit and at rest, never used to train models, and enterprise plans include SOC 2 and data residency."),
        ("Can you build a custom agent for my business?", "Absolutely — our solutions team designs, builds and maintains custom AI agents and automations for clients."),
        ("Can I cancel anytime?", "Yes, plans are month-to-month and you can cancel from your dashboard in one click.")]
faq_html = "".join(f'<details class="reveal"><summary>{q}</summary><p>{a}</p></details>' for q, a in faqs)
pricing = f"""<section class="page-hero center" style="padding-bottom:20px"><div class="blob" style="left:50%;right:auto;transform:translateX(-50%)"></div><div class="container">
<span class="eyebrow glass reveal"><span class="tag">AIFLOW</span>Pricing</span>
<h1 class="display split-words" style="margin:22px auto 0">Simple pricing that scales</h1>
<p class="lead reveal" data-delay="2" style="margin-top:22px">Start free for 14 days. Upgrade when your agents start saving you hours.</p>
<div class="toggle glass reveal" data-billing><button class="on" data-mode="monthly">Monthly</button><button data-mode="yearly">Yearly · save 20%</button></div>
</div></section>
<section class="section" style="padding-top:0"><div class="container"><div class="grid g-3" style="align-items:center">{pcards}</div></div></section>
<section class="section" id="faq" style="padding-top:20px"><div class="container split" style="align-items:start">
<div><span class="eyebrow reveal">✦ FAQ</span><h2 class="h2 split-words" style="margin-top:14px">Questions, answered</h2><p class="lead reveal" style="margin-top:16px">Can't find what you need? <a href="contact.html" style="text-decoration:underline">Talk to us</a>.</p></div>
<div class="faq">{faq_html}</div></div></section>
{cta()}"""
page("pricing.html", "pricing", "Pricing — AI Agent Plans from $29/month | Aiflow",
     "Transparent pricing for AI agents and workflow automation. Starter, Growth and Enterprise plans with a free 14-day trial.", pricing)

# ------------------------------------------------------------------ CONTACT
contact = page_hero("Contact", "Let's build your AI workforce", "Book a demo, request a custom AI agent, or just say hello. We reply within one business day.") + f"""
<section class="section" style="padding-top:10px"><div class="container split" style="align-items:start">
<form class="card reveal" data-simple="Thanks! Your demo request is in — we'll be in touch within 24 hours." style="padding:34px" novalidate>
  <h2 class="h3">Book a demo</h2>
  <div class="grid g-2" style="gap:0 14px"><div class="field"><label for="c-name">Full name</label><input id="c-name" class="input" required></div>
  <div class="field"><label for="c-email">Work email</label><input id="c-email" type="email" class="input" required></div></div>
  <div class="field"><label for="c-co">Company</label><input id="c-co" class="input"></div>
  <div class="field"><label for="c-need">What do you want to automate?</label><select id="c-need" class="input"><option>Customer support</option><option>Sales &amp; lead generation</option><option>Operations &amp; finance</option><option>Custom AI agent build</option><option>Something else</option></select></div>
  <div class="field"><label for="c-msg">Message</label><textarea id="c-msg" class="input" required placeholder="Tell us about your workflow…"></textarea></div>
  <button class="btn btn-dark" type="submit" style="margin-top:22px">Send request <span class="ico">{ARROW}</span></button>
</form>
<div style="display:grid;gap:20px">
  <div class="media reveal-r" style="aspect-ratio:16/11"><img src="assets/img/ai-globe.webp" alt="AI globe floating above a robotic hand" loading="lazy" style="object-position:center 35%">
    <div class="float-chip glass glass-dark" style="left:18px;bottom:18px;right:18px">Average response time: <b>under 2 hours</b></div></div>
  <div class="grid g-2">
    <div class="card reveal"><div class="icon">{icon('mail')}</div><h3 class="h3" style="font-size:17px">Email</h3><p>hello@aiflow.ai</p></div>
    <div class="card reveal" data-delay="1"><div class="icon">{icon('chat')}</div><h3 class="h3" style="font-size:17px">Live chat</h3><p>Mon–Fri, 24 hours</p></div>
  </div>
</div></div></section>"""
page("contact.html", "contact", "Contact & Book a Demo — Hire AI Automation Experts | Aiflow",
     "Book a demo of Aiflow or hire our team to build custom AI agents, chatbots and workflow automations for your business.", contact)

# ------------------------------------------------------------------ LOGIN
login = f"""<body data-page="login">
<div class="curtain"><div class="logo-mark">{LOGO_SVG}</div></div>
{SVG_FILTER}
<div class="auth">
  <div class="auth-form-wrap">
    <a href="index.html" class="logo reveal"><span class="logo-mark">{LOGO_SVG}</span>Aiflow</a>
    <form id="auth-form" class="auth-form" novalidate>
      <div class="auth-switch reveal"><button type="button" data-mode="login" class="on">Sign in</button><button type="button" data-mode="signup">Sign up</button></div>
      <h1 id="auth-title" class="reveal">Welcome back</h1>
      <p id="auth-sub" class="muted reveal" style="margin-top:8px">Sign in to manage your AI agents.</p>
      <div class="sso reveal" style="margin-top:26px">
        <button type="button"><svg width="18" height="18" viewBox="0 0 48 48"><path fill="#FFC107" d="M43.6 20.5H42V20H24v8h11.3C33.7 32.7 29.2 36 24 36c-6.6 0-12-5.4-12-12s5.4-12 12-12c3 0 5.8 1.1 7.9 3l5.7-5.7C34 6.1 29.3 4 24 4 12.9 4 4 12.9 4 24s8.9 20 20 20 20-8.9 20-20c0-1.3-.1-2.4-.4-3.5z"/><path fill="#FF3D00" d="m6.3 14.7 6.6 4.8C14.7 15.1 19 12 24 12c3 0 5.8 1.1 7.9 3l5.7-5.7C34 6.1 29.3 4 24 4 16.3 4 9.7 8.3 6.3 14.7z"/><path fill="#4CAF50" d="M24 44c5.2 0 9.9-2 13.4-5.2l-6.2-5.2C29.2 35.1 26.7 36 24 36c-5.2 0-9.6-3.3-11.3-8l-6.5 5C9.5 39.6 16.2 44 24 44z"/><path fill="#1976D2" d="M43.6 20.5H42V20H24v8h11.3c-.8 2.2-2.2 4.2-4.1 5.6l6.2 5.2C37 39.2 44 34 44 24c0-1.3-.1-2.4-.4-3.5z"/></svg>Google</button>
        <button type="button"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 .5a12 12 0 0 0-3.8 23.4c.6.1.8-.3.8-.6v-2c-3.3.7-4-1.6-4-1.6-.6-1.4-1.4-1.8-1.4-1.8-1-.7.1-.7.1-.7 1.2.1 1.8 1.2 1.8 1.2 1 1.8 2.8 1.3 3.5 1 .1-.8.4-1.3.7-1.6-2.7-.3-5.5-1.3-5.5-6 0-1.3.5-2.4 1.2-3.2-.1-.3-.5-1.5.1-3.2 0 0 1-.3 3.3 1.2a11.5 11.5 0 0 1 6 0C17.3 4.7 18.3 5 18.3 5c.7 1.7.2 2.9.1 3.2.8.8 1.2 1.9 1.2 3.2 0 4.6-2.8 5.6-5.5 5.9.4.4.8 1.1.8 2.2v3.3c0 .3.2.7.8.6A12 12 0 0 0 12 .5z"/></svg>GitHub</button>
      </div>
      <div class="divider">or continue with email</div>
      <div class="field" data-only="signup" hidden><label for="name">Full name</label><input id="name" class="input" autocomplete="name" placeholder="Jane Doe"><span class="err-msg"></span></div>
      <div class="field"><label for="email">Work email</label><input id="email" type="email" class="input" autocomplete="email" placeholder="you@company.com"><span class="err-msg"></span></div>
      <div class="field"><label for="password">Password</label><div class="pw-wrap"><input id="password" type="password" class="input" autocomplete="current-password" placeholder="At least 8 characters"><button type="button">Show</button></div><span class="err-msg"></span></div>
      <div class="row-between" data-only="login"><label style="display:flex;gap:8px;align-items:center"><input type="checkbox" checked> Remember me</label><a href="#" id="forgot" style="text-decoration:underline">Forgot password?</a></div>
      <p class="muted" data-only="signup" hidden style="font-size:12px;margin-top:14px">By creating an account you agree to our Terms and Privacy Policy.</p>
      <button id="auth-submit" class="btn btn-dark" type="submit" style="width:100%;justify-content:space-between;margin-top:24px;--h:52px"><span>Sign in</span><span class="ico">{ARROW}</span></button>
      <p class="muted" style="font-size:13px;margin-top:22px;text-align:center"><a href="index.html" style="text-decoration:underline">← Back to website</a></p>
    </form>
  </div>
  <div class="auth-art reveal-scale">
    <img src="assets/img/ai-globe.webp" alt="Robotic hand presenting a glowing AI globe">
    <div class="glass glass-dark glass-liquid" style="position:relative">
      <div style="display:flex;gap:10px;align-items:center;font-size:13px"><span class="dot-live"></span> 1,284 agents running right now</div>
      <p style="font-size:22px;letter-spacing:-0.02em;margin-top:12px;line-height:1.3">“Your AI agents don't sleep. Log in and see what they finished while you were away.”</p>
    </div>
  </div>
</div>
<script src="assets/js/main.js"></script>
</body></html>"""
page("login.html", "login", "Sign in or Create an Account | Aiflow", "Log in to Aiflow to build, deploy and monitor your AI agents, or create a free account.", login, chrome=False)

# ------------------------------------------------------------------ DASHBOARD
agents = [("Support Concierge", "Running", "12,480"), ("Lead Qualifier", "Running", "3,214"), ("Invoice Processor", "Running", "1,902"),
          ("Competitor Researcher", "Paused", "418"), ("Content Writer", "Running", "860")]
arows = "".join(f'<div class="agent-row"><div><b>{n}</b><br><span class="muted" style="font-size:12px">{t} tasks this month</span></div><span class="pill{" idle" if s == "Paused" else ""}">{s}</span><button class="btn btn-ghost btn-sm" data-toggle>{"Resume" if s == "Paused" else "Pause"}</button></div>' for n, s, t in agents)
bars = "".join(f'<div style="height:{h}%;animation-delay:{i * .06:.2f}s"></div>' for i, h in enumerate([40, 62, 48, 75, 58, 82, 66, 90, 72, 95, 80, 100]))
side_items = [("home", "Overview", True), ("flow", "Agents", False), ("bolt", "Workflows", False), ("chart", "Analytics", False), ("plug", "Integrations", False), ("cog", "Settings", False)]
side = "".join(f'<a href="#" class="item{" on" if on else ""}">{icon(ic, 18)}{t}</a>' for ic, t, on in side_items)
dashboard = f"""<body data-page="dashboard">
<div class="curtain"><div class="logo-mark">{LOGO_SVG}</div></div>
<div class="dash">
  <aside class="side">
    <a href="index.html" class="logo" style="margin-bottom:18px"><span class="logo-mark">{LOGO_SVG}</span>Aiflow</a>
    {side}
    <div class="spacer" style="flex:1"></div>
    <div class="side-foot card" style="padding:18px;background:var(--ink);color:#fff"><b>Upgrade to Growth</b><p style="color:rgba(255,255,255,.6);font-size:13px">Unlock 15 agents and WhatsApp.</p><a href="pricing.html" class="btn btn-light btn-sm" style="margin-top:12px">See plans</a></div>
    <a href="#" class="item" data-logout>{icon('logout', 18)}Log out</a>
  </aside>
  <main>
    <div class="dash-top reveal">
      <div><p class="muted" style="font-size:14px">Good to see you,</p><h1 style="font-size:34px">Welcome back, <span data-user-name>there</span> 👋</h1></div>
      <div style="display:flex;gap:10px;align-items:center"><a href="index.html" class="btn btn-ghost btn-sm">Website</a><a href="#" class="btn btn-dark btn-sm" onclick="aiflowToast('New agent draft created ✨');return false">+ New agent</a><span style="width:40px;height:40px;border-radius:50%;background:var(--accent);color:#fff;display:grid;place-items:center;font-weight:600" data-user-initial>A</span></div>
    </div>
    <div class="grid g-4">
      <div class="kpi reveal"><p class="muted" style="font-size:13px">Tasks completed <span class="dot-live" style="margin-left:6px"></span></p><div class="v" data-live>18,874</div><p style="font-size:12px;color:#128a3e">▲ 12% vs last week</p></div>
      <div class="kpi reveal" data-delay="1"><p class="muted" style="font-size:13px">Hours saved</p><div class="v" data-count="1426">0</div><p style="font-size:12px;color:#128a3e">▲ 8%</p></div>
      <div class="kpi reveal" data-delay="2"><p class="muted" style="font-size:13px">Success rate</p><div class="v" data-count="98.4" data-suffix="%">0</div><p style="font-size:12px;color:#128a3e">▲ 1.2%</p></div>
      <div class="kpi reveal" data-delay="3"><p class="muted" style="font-size:13px">Active agents</p><div class="v" data-count="4">0</div><p style="font-size:12px" class="muted">of 5 deployed</p></div>
    </div>
    <div class="grid" style="grid-template-columns:repeat(auto-fit,minmax(min(100%,380px),1fr));margin-top:20px">
      <div class="kpi reveal"><div style="display:flex;justify-content:space-between"><b>Tasks automated</b><span class="muted" style="font-size:13px">Last 12 weeks</span></div><div class="bars">{bars}</div></div>
      <div class="kpi reveal" data-delay="1"><b>Your agents</b><div style="margin-top:10px">{arows}</div></div>
    </div>
  </main>
</div>
<script src="assets/js/main.js"></script>
</body></html>"""
page("dashboard.html", "dashboard", "Dashboard | Aiflow", "Your Aiflow AI agent dashboard.", dashboard, chrome=False)
(ROOT / "dashboard.html").write_text((ROOT / "dashboard.html").read_text().replace('<meta name="robots" content="index, follow">', '<meta name="robots" content="noindex">'))

# 404
nf = page_hero("404", "This page went to sleep", "Unlike our agents. Let's get you back on track.", f'<div class="reveal" style="margin-top:30px">{btn("Back home", "index.html")}</div>')
page("404.html", "", "Page not found | Aiflow", "Page not found.", nf)

# sitemap + robots
pages = ["", "solutions.html", "features.html", "customers.html", "pricing.html", "contact.html", "login.html"]
(ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
    "".join(f"  <url><loc>{SITE}/{p}</loc><changefreq>weekly</changefreq><priority>{'1.0' if not p else '0.8'}</priority></url>\n" for p in pages) + "</urlset>\n")
(ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /dashboard.html\nSitemap: {SITE}/sitemap.xml\n")
print("built")
