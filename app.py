import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import html
from datetime import datetime

st.set_page_config(page_title="Recruitment Count Dashboard", page_icon=":clipboard:", layout="wide")

st.markdown("""
<style>
.welcome-overlay {
    position: fixed;
    inset: 0;
    z-index: 999999;
    display: grid;
    place-items: center;
    pointer-events: none;
    background:
        radial-gradient(circle at 45% 42%, rgba(124, 58, 237, 0.10), transparent 28%),
        #fbfcff;
    opacity: 1;
    visibility: visible;
    animation: welcomeOverlayHold 1.7s ease forwards;
}

.welcome-text {
    color: #101828;
    font-family: 'Inter', sans-serif;
    font-size: 34px;
    font-weight: 650;
    line-height: 1.15;
    text-align: center;
    padding: 0 18px;
    transform: translateY(18px) scale(.96);
    opacity: 0;
    animation: welcomeTextIn .75s cubic-bezier(.2, .8, .2, 1) forwards;
}

.welcome-text span {
    display: block;
    margin-top: 10px;
    color: #6d48c9;
    font-size: 13px;
    font-weight: 500;
}

.welcome-spinner {
    width: 24px;
    height: 24px;
    margin: 18px auto 0;
    border-radius: 999px;
    border: 3px solid rgba(109, 72, 201, 0.16);
    border-top-color: #6d48c9;
    animation: welcomeSpin .8s linear infinite;
}

@keyframes welcomeTextIn {
    0% {
        opacity: 0;
        transform: translateY(18px) scale(.96);
    }
    18%,
    100% {
        opacity: 1;
        transform: translateY(0) scale(1);
    }
}

@keyframes welcomeSpin {
    to {
        transform: rotate(360deg);
    }
}

@keyframes welcomeOverlayHold {
    0%,
    82% {
        opacity: 1;
        visibility: visible;
    }
    100% {
        opacity: 0;
        visibility: hidden;
    }
}

@media (max-width: 760px) {
    .welcome-text {
        font-size: 25px;
    }

    .welcome-text span {
        font-size: 11px;
    }

    .welcome-spinner {
        width: 21px;
        height: 21px;
        border-width: 2.5px;
    }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div id="welcome-overlay" class="welcome-overlay">
    <div class="welcome-text">
        Welcome To Recruiter Automation
        <span>Preparing your dashboard</span>
        <div class="welcome-spinner"></div>
    </div>
</div>
""", unsafe_allow_html=True)

components.html(
    """
    <script>
    (function () {
        const selectors = [
            'a[href="https://streamlit.io/cloud"]',
            'a[href*="streamlit.io/cloud"]',
            'a[class*="_viewerBadge"]',
            'a[class*="viewerBadge"]',
            'div[class*="_profileContainer"]',
            'div[class*="profileContainer"]',
            'div[class*="_profilePreview"]',
            'div[class*="profilePreview"]',
            '[data-testid="appCreatorAvatar"]',
            'a[href*="share.streamlit.io/user"]'
        ];

        const css = `
            ${selectors.join(',')} {
                display: none !important;
                visibility: hidden !important;
                opacity: 0 !important;
                pointer-events: none !important;
                width: 0 !important;
                height: 0 !important;
                min-width: 0 !important;
                min-height: 0 !important;
                max-width: 0 !important;
                max-height: 0 !important;
                overflow: hidden !important;
                transform: scale(0) !important;
            }
            div[data-testid="stElementContainer"]:has(style),
            div[data-testid="stElementContainer"]:has(iframe[height="0"]),
            div[data-testid="stElementContainer"]:has(iframe[width="0"]),
            div[data-testid="stElementContainer"][width="0px"],
            div[data-testid="stElementContainer"][height="0px"],
            div[data-testid="stElementContainer"]:has(iframe[data-testid="stIFrame"][title="st.iframe"]) {
                display: none !important;
                visibility: hidden !important;
                height: 0 !important;
                min-height: 0 !important;
                max-height: 0 !important;
                width: 0 !important;
                min-width: 0 !important;
                max-width: 0 !important;
                margin: 0 !important;
                padding: 0 !important;
                overflow: hidden !important;
                line-height: 0 !important;
                position: absolute !important;
                inset: 0 auto auto 0 !important;
            }
        `;

        function injectStyle(doc) {
            if (!doc || doc.getElementById('hide-streamlit-cloud-badge')) return;
            const style = doc.createElement('style');
            style.id = 'hide-streamlit-cloud-badge';
            style.textContent = css;
            (doc.head || doc.documentElement).appendChild(style);
        }

        function hideIn(doc) {
            if (!doc) return;
            injectStyle(doc);
            selectors.forEach((selector) => {
                doc.querySelectorAll(selector).forEach((el) => {
                    const target = el.closest('a, div') || el;
                    target.style.setProperty('display', 'none', 'important');
                    target.style.setProperty('visibility', 'hidden', 'important');
                    target.style.setProperty('opacity', '0', 'important');
                    target.style.setProperty('pointer-events', 'none', 'important');
                    target.style.setProperty('width', '0', 'important');
                    target.style.setProperty('height', '0', 'important');
                    target.style.setProperty('overflow', 'hidden', 'important');
                    target.setAttribute('aria-hidden', 'true');
                });
            });
        }

        function hideBadges() {
            hideIn(document);
            try { hideIn(window.parent.document); } catch (e) {}
            try { hideIn(window.top.document); } catch (e) {}
        }

        hideBadges();
        setInterval(hideBadges, 500);
    })();
    </script>
    """,
    height=0,
    width=0,
)

components.html(
    """
    <script>
    (function () {
        function addTag(doc, tag, attrs) {
            if (!doc) return;
            const key = attrs.name ? `${tag}[name="${attrs.name}"]` : `${tag}[rel="${attrs.rel}"]`;
            if (doc.querySelector(key)) return;
            const el = doc.createElement(tag);
            Object.entries(attrs).forEach(([name, value]) => el.setAttribute(name, value));
            (doc.head || doc.documentElement).appendChild(el);
        }

        function installPwaTags(doc) {
            addTag(doc, 'link', { rel: 'manifest', href: '/app/static/manifest.json' });
            addTag(doc, 'link', { rel: 'icon', href: '/app/static/icon.svg', type: 'image/svg+xml' });
            addTag(doc, 'link', { rel: 'apple-touch-icon', href: '/app/static/icon.svg' });
            addTag(doc, 'meta', { name: 'theme-color', content: '#101828' });
            addTag(doc, 'meta', { name: 'mobile-web-app-capable', content: 'yes' });
            addTag(doc, 'meta', { name: 'apple-mobile-web-app-capable', content: 'yes' });
            addTag(doc, 'meta', { name: 'apple-mobile-web-app-status-bar-style', content: 'black-translucent' });
            addTag(doc, 'meta', { name: 'apple-mobile-web-app-title', content: 'Recruiter' });
        }

        installPwaTags(document);
        try { installPwaTags(window.parent.document); } catch (e) {}
        try { installPwaTags(window.top.document); } catch (e) {}
    })();
    </script>
    """,
    height=0,
    width=0,
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap');

:root {
    --bg: #070a12;
    --bg-2: #0a0f1d;
    --panel: #0f1626;
    --panel-2: #121b2d;
    --panel-3: #172238;
    --line: #24324a;
    --line-soft: #1b263b;
    --text: #e8eef9;
    --muted: #8d9bb2;
    --faint: #5f6f89;
    --gold: #c7a45d;
    --blue: #4c8dff;
    --cyan: #38d6c7;
    --red: #ff5f68;
    --violet: #9a74ff;
    --green: #2ed3a1;
    --shadow: 0 18px 50px rgba(0, 0, 0, 0.34);
}

* {
    font-family: 'Inter', sans-serif !important;
    letter-spacing: 0;
    box-sizing: border-box;
}

.stApp {
    background:
        linear-gradient(180deg, rgba(199, 164, 93, 0.08), rgba(199, 164, 93, 0) 210px),
        linear-gradient(135deg, #060811 0%, #09101e 42%, #070a12 100%);
    color: var(--text);
}

.block-container {
    padding: 18px 28px 34px;
    max-width: 1240px;
}

#MainMenu, footer, header {
    visibility: hidden;
}

/* HIDE TECHNICAL STYLE / SCRIPT INJECTOR ROWS */
div[data-testid="stElementContainer"]:has(style),
div[data-testid="stElementContainer"]:has(iframe[height="0"]),
div[data-testid="stElementContainer"]:has(iframe[width="0"]),
div[data-testid="stElementContainer"][width="0px"],
div[data-testid="stElementContainer"][height="0px"],
div[data-testid="stElementContainer"]:has(iframe[data-testid="stIFrame"][title="st.iframe"]) {
    display: none !important;
    visibility: hidden !important;
    height: 0 !important;
    min-height: 0 !important;
    max-height: 0 !important;
    width: 0 !important;
    min-width: 0 !important;
    max-width: 0 !important;
    margin: 0 !important;
    padding: 0 !important;
    overflow: hidden !important;
    line-height: 0 !important;
    position: absolute !important;
    inset: 0 auto auto 0 !important;
}

/* STREAMLIT CLOUD BADGE / CREATOR PROFILE */
a[href="https://streamlit.io/cloud"],
a[href*="streamlit.io/cloud"],
a[class*="_viewerBadge"],
div[class*="_profileContainer"],
div[class*="_profilePreview"],
[data-testid="appCreatorAvatar"],
[data-testid="appCreatorAvatar"] * {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
    width: 0 !important;
    height: 0 !important;
    min-width: 0 !important;
    min-height: 0 !important;
    max-width: 0 !important;
    max-height: 0 !important;
    overflow: hidden !important;
}

/* HERO */
.topbox {
    background:
        linear-gradient(135deg, rgba(199, 164, 93, 0.14), rgba(76, 141, 255, 0.06) 42%, rgba(46, 211, 161, 0.04)),
        linear-gradient(135deg, #101827 0%, #0d1423 48%, #0a1020 100%);
    color: var(--text) !important;
    padding: 22px 26px;
    border-radius: 12px;
    margin-bottom: 16px;
    box-shadow: var(--shadow);
    border: 1px solid #2c3850;
    position: relative;
    overflow: hidden;
}

.topbox:before {
    content: "";
    position: absolute;
    inset: auto 0 0 0;
    height: 2px;
    background: linear-gradient(90deg, transparent, var(--gold), var(--cyan), transparent);
}

.topbox h1 {
    color: var(--text) !important;
    font-size: 22px !important;
    font-weight: 700 !important;
    margin: 0;
    line-height: 1.2;
}

.topbox p {
    max-width: 800px;
    font-size: 12px !important;
    color: var(--muted) !important;
    margin: 3px 0 0;
    line-height: 1.55;
}

.topbox strong {
    color: var(--gold);
}

/* UPLOADER */
[data-testid="stFileUploader"] {
    background: var(--panel);
    border-radius: 12px;
    padding: 12px;
    border: 1px solid var(--line);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.20);
    margin-bottom: 14px;
}

[data-testid="stFileUploader"] section {
    border-radius: 10px;
    border: 1px dashed #42516b;
    background: #0b1220;
    min-height: 58px;
}

[data-testid="stFileUploader"] label {
    color: var(--text) !important;
    font-size: 12px !important;
    font-weight: 750;
}

[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p {
    color: var(--muted) !important;
    font-size: 11px !important;
}

[data-testid="stFileUploader"] button {
    background: #111a2b !important;
    color: var(--text) !important;
    border: 1px solid var(--line) !important;
    border-radius: 8px !important;
    min-height: 32px;
    font-size: 11px !important;
    font-weight: 750 !important;
}

/* METRIC CARDS */
.card {
    background: linear-gradient(180deg, #121b2d, #0e1524);
    border-radius: 10px;
    padding: 14px 14px 13px;
    min-height: 96px;
    border: 1px solid var(--line);
    box-shadow: 0 12px 28px rgba(0, 0, 0, 0.22);
    position: relative;
    overflow: hidden;
    transition: transform .16s ease, border-color .16s ease, background .16s ease;
}

.card:hover {
    transform: translateY(-1px);
    border-color: #42516b;
    background: linear-gradient(180deg, #152036, #101827);
}

.card:before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 2px;
}

.card:after {
    content: "";
    position: absolute;
    right: 13px;
    top: 14px;
    height: 28px;
    width: 28px;
    border-radius: 7px;
    background: currentColor;
    opacity: 0.12;
}

.card-total { color: var(--gold); }
.card-total:before { background: var(--gold); }
.card-yts { color: #f6b35f; }
.card-yts:before { background: #f6b35f; }
.card-sch { color: var(--blue); }
.card-sch:before { background: var(--blue); }
.card-rej { color: var(--red); }
.card-rej:before { background: var(--red); }
.card-drop { color: var(--violet); }
.card-drop:before { background: var(--violet); }
.card-join { color: var(--green); }
.card-join:before { background: var(--green); }

.lbl {
    max-width: calc(100% - 38px);
    font-size: 9px;
    color: var(--muted);
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .75px;
    line-height: 1.3;
}

.num {
    font-size: 28px;
    font-weight: 700;
    color: currentColor;
    margin-top: 10px;
    letter-spacing: 0;
    line-height: 1;
}

/* TABS */
.stTabs {
    margin-top: 6px;
}

.stTabs [data-baseweb="tab-list"] {
    background: #0b1220;
    border-radius: 10px;
    padding: 4px;
    gap: 4px;
    border: 1px solid var(--line);
    box-shadow: 0 10px 24px rgba(0, 0, 0, 0.20);
}

.stTabs [data-baseweb="tab"] {
    border-radius: 7px;
    padding: 7px 11px;
    min-height: 34px;
    font-size: 11px;
    font-weight: 700;
    color: var(--muted);
    background: transparent;
    border: 1px solid transparent;
}

.stTabs [data-baseweb="tab"]:hover {
    background: #111a2b;
    color: var(--text);
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(180deg, #172238, #111a2b) !important;
    color: white !important;
    border-color: var(--gold) !important;
}

div[data-testid="stTabs"] > div:last-child {
    background: var(--panel);
    border: 1px solid var(--line);
    border-radius: 12px;
    padding: 14px;
    box-shadow: 0 14px 34px rgba(0, 0, 0, 0.24);
    margin-top: 10px;
}

/* HEADINGS */
h1, h2, h3 {
    color: var(--text) !important;
    font-weight: 700 !important;
    letter-spacing: 0;
}

h2, h3 {
    margin-top: 0.15rem;
    font-size: 18px !important;
    line-height: 1.25;
}

.tab-heading-tight {
    margin: 0 !important;
    padding: 0 !important;
    color: var(--text) !important;
    font-size: 18px !important;
    font-weight: 700 !important;
    line-height: 1.25 !important;
}

[data-testid="stMarkdownContainer"] p {
    font-size: 12px;
}

/* TABLE */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--line);
    background: #ffffff;
    box-shadow: 0 10px 24px rgba(16, 24, 40, 0.07);
}

[data-testid="stDataFrame"] * {
    font-size: 11px !important;
}

[data-testid="stDataFrame"] div[role="grid"] {
    background: #ffffff !important;
}

/* INPUTS */
.stTextInput input {
    border-radius: 8px;
    border: 1px solid var(--line);
    padding: 10px 12px;
    background: #0b1220;
    color: var(--text);
    font-size: 12px;
}

.stMultiSelect [data-baseweb="select"] {
    border-radius: 8px;
    background: #0b1220;
    border-color: var(--line) !important;
    color: var(--text);
    font-size: 12px;
}

.stMultiSelect span,
.stTextInput label,
.stMultiSelect label {
    color: var(--muted) !important;
    font-size: 11px !important;
    font-weight: 700 !important;
}

.stTextInput input:focus,
.stMultiSelect [data-baseweb="select"]:focus-within {
    border-color: var(--gold) !important;
    box-shadow: 0 0 0 3px rgba(199, 164, 93, 0.13) !important;
}

[data-testid="stAlert"] {
    border-radius: 10px;
    border: 1px solid var(--line);
    background: var(--panel);
    color: var(--text);
}

[data-testid="stAlert"] * {
    color: var(--text) !important;
    font-size: 12px !important;
}

hr {
    border-color: var(--line-soft);
    margin: 1rem 0;
}

.stDivider {
    border-color: var(--line-soft) !important;
}

@media (max-width: 900px) {
    .block-container {
        padding: 14px 12px 28px;
    }

    .topbox {
        padding: 18px 16px;
        border-radius: 10px;
    }

    .topbox:after {
        position: static;
        display: block;
        margin-bottom: 8px;
    }

    .topbox h1 {
        font-size: 20px !important;
    }

    .num {
        font-size: 26px;
    }
}

/* LIGHT PRODUCTION THEME OVERRIDES */
:root {
    --bg: #f3f6fb;
    --panel: #ffffff;
    --panel-2: #f8fafc;
    --panel-3: #eef3f9;
    --line: #d6dee9;
    --line-soft: #e7edf5;
    --text: #101828;
    --muted: #667085;
    --faint: #98a2b3;
    --gold: #a9791f;
    --blue: #2457d6;
    --cyan: #087f8c;
    --red: #c62838;
    --violet: #6d48c9;
    --green: #087b5b;
    --shadow: 0 18px 46px rgba(16, 24, 40, 0.10);
}

.stApp {
    background:
        linear-gradient(180deg, #eef3f8 0%, rgba(238, 243, 248, 0) 260px),
        var(--bg) !important;
    color: var(--text) !important;
}

.topbox {
    background:
        linear-gradient(135deg, rgba(169, 121, 31, 0.08), rgba(36, 87, 214, 0.05)),
        #ffffff !important;
    color: var(--text) !important;
    border: 1px solid var(--line) !important;
    box-shadow: var(--shadow) !important;
}

.topbox h1 {
    color: var(--text) !important;
}

.topbox p {
    color: var(--muted) !important;
}

.topbox:after {
    color: var(--gold) !important;
}

[data-testid="stFileUploader"],
div[data-testid="stTabs"] > div:last-child,
[data-testid="stAlert"] {
    background: #ffffff !important;
    border-color: var(--line) !important;
    box-shadow: 0 12px 30px rgba(16, 24, 40, 0.08) !important;
}

[data-testid="stFileUploader"] section,
.stTabs [data-baseweb="tab-list"] {
    background: #f8fafc !important;
    border-color: var(--line) !important;
}

[data-testid="stFileUploader"] label,
[data-testid="stAlert"] *,
h1, h2, h3 {
    color: var(--text) !important;
}

[data-testid="stFileUploader"] small,
[data-testid="stFileUploader"] span,
[data-testid="stFileUploader"] p,
[data-testid="stMarkdownContainer"] p {
    color: var(--muted) !important;
}

[data-testid="stFileUploader"] button {
    background: #ffffff !important;
    color: var(--text) !important;
    border-color: var(--line) !important;
}

.card {
    background: #ffffff !important;
    border-color: var(--line) !important;
    box-shadow: 0 12px 26px rgba(16, 24, 40, 0.08) !important;
}

.card:hover {
    background: #ffffff !important;
    border-color: #b8c4d6 !important;
}

.stTabs [data-baseweb="tab"] {
    color: #475467 !important;
}

.stTabs [data-baseweb="tab"]:hover {
    background: #eef3f9 !important;
    color: var(--text) !important;
}

.stTabs [aria-selected="true"] {
    background: #101828 !important;
    color: #ffffff !important;
    border-color: #101828 !important;
}

[data-testid="stDataFrame"] {
    background: #ffffff !important;
    border-color: var(--line) !important;
    box-shadow: 0 10px 24px rgba(16, 24, 40, 0.07) !important;
}

[data-testid="stDataFrame"] div[role="grid"] {
    background: #ffffff !important;
}

.stTextInput input,
.stMultiSelect [data-baseweb="select"] {
    background: #ffffff !important;
    color: var(--text) !important;
    border-color: var(--line) !important;
}

.insight-grid {
    display: grid;
    grid-template-columns: repeat(4, minmax(0, 1fr));
    gap: 10px;
    margin: 0px 0 14px;
}

.insight-card,
.insight-panel {
    background: #ffffff;
    border: 1px solid var(--line);
    border-radius: 10px;
    box-shadow: 0 10px 24px rgba(16, 24, 40, 0.07);
}

.insight-card {
    padding: 12px;
}

.insight-card .mini-lbl {
    font-size: 10px;
    text-align: center;
    font-weight: 500;
    text-transform: uppercase;
    letter-spacing: .7px;
}

.insight-card .mini-num {
    color: var(--text);
    font-size: 24px;
    font-weight: 400;
    margin-top: 6px;
    text-align: center;
}

.insight-panel {
    padding: 14px 16px;
    margin-top: 10px;
}

.insight-panel h4 {
    color: var(--text);
    font-size: 13px;
    font-weight: 700;
    margin: 0 0 8px;
}

.insight-panel ul {
    margin: 0;
    padding-left: 18px;
}

.insight-panel li {
    color: #344054;
    font-size: 12px;
    line-height: 1.55;
    margin: 5px 0;
}

@media (max-width: 900px) {
    .insight-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }
}

/* CREATIVE STRUCTURE AND ALIGNMENT REFINEMENTS */
.topbox {
    display: grid;
    grid-template-columns: minmax(0, 1fr) auto;
    gap: 18px;
    align-items: end;
    padding: 24px 28px 22px !important;
}

.topbox:after {
    position: static !important;
    align-self: start;
    justify-self: end;
}

.topbox h1 {
    max-width: 760px;
}

.topbox p {
    max-width: 760px !important;
}

.overview-strip {
    display: grid;
    grid-template-columns: 1.25fr repeat(3, minmax(0, .75fr));
    gap: 10px;
    margin: 4px 0 14px;
}

.overview-cell {
    background: #ffffff;
    border: 1px solid var(--line);
    border-radius: 10px;
    padding: 11px 12px;
    box-shadow: 0 8px 20px rgba(16, 24, 40, 0.06);
    min-height: 62px;
}

.overview-cell .eyebrow,
.section-kicker {
    color: var(--muted);
    font-size: 9px;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: .8px;
}

.overview-cell .value {
    color: var(--text);
    font-size: 13px;
    font-weight: 600;
    margin-top: 6px;
    overflow-wrap: anywhere;
}

.section-kicker {
    margin: 4px 0 8px;
}

.card {
    min-height: 104px !important;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
}

.card .metric-row {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 10px;
}

.card .metric-note {
    color: var(--faint);
    font-size: 9px;
    font-weight: 750;
    text-transform: uppercase;
    letter-spacing: .45px;
}

.card:after {
    top: auto !important;
    bottom: 13px;
}

.num {
    margin-top: 12px !important;
}

div[data-testid="stTabs"] > div:last-child {
    padding: 16px !important;
}

[data-testid="stDataFrame"] {
    background: #ffffff !important;
    border: 1px solid #d6dee9 !important;
    border-radius: 10px !important;
}

[data-testid="stDataFrame"],
[data-testid="stDataFrame"] *,
[data-testid="stDataFrame"] div,
[data-testid="stDataFrame"] section {
    color: #101828 !important;
}

[data-testid="stDataFrame"] div[role="grid"],
[data-testid="stDataFrame"] [role="grid"],
[data-testid="stDataFrame"] [role="row"],
[data-testid="stDataFrame"] [role="columnheader"],
[data-testid="stDataFrame"] [role="gridcell"] {
    background-color: #ffffff !important;
}

[data-testid="stDataFrame"] canvas {
    background-color: #ffffff !important;
    color-scheme: light !important;
}

[data-testid="stDataFrame"] [role="columnheader"] {
    background-color: #f8fafc !important;
    color: #344054 !important;
    font-weight: 700 !important;
}

@media (max-width: 900px) {
    .topbox,
    .overview-strip {
        grid-template-columns: 1fr;
    }

    .topbox:after {
        justify-self: start;
    }
}

/* FINAL CLEAN PRODUCTION LAYOUT */
.block-container {
    max-width: 1320px !important;
    padding: 16px 18px 30px !important;
}

.topbox {
    display: block !important;
    padding: 20px 22px !important;
    min-height: auto !important;
    margin-bottom: 14px !important;
}

.topbox h1 {
    max-width: 100% !important;
    font-size: 21px !important;
    line-height: 1.15 !important;
}

.topbox p {
    max-width: 850px !important;
}

.topbox:after {
    position: absolute !important;
    right: 22px !important;
    top: 18px !important;
}

.overview-strip {
    grid-template-columns: repeat(4, minmax(0, 1fr)) !important;
    gap: 8px !important;
    margin: 2px 0 12px !important;
}

.overview-cell {
    min-height: 56px !important;
    padding: 10px 12px !important;
    border-radius: 8px !important;
}

.overview-cell .value {
    font-size: 12px !important;
    margin-top: 5px !important;
}

.card {
    min-height: 88px !important;
    padding: 12px 12px 11px !important;
    border-radius: 8px !important;
}

.card:after {
    top: 12px !important;
    bottom: auto !important;
    right: 12px !important;
    width: 24px !important;
    height: 24px !important;
    border-radius: 6px !important;
}

.metric-row {
    display: block !important;
}

.metric-note {
    display: none !important;
}

.num {
    font-size: 26px !important;
    margin-top: 12px !important;
}

.stTabs [data-baseweb="tab-list"] {
    box-shadow: 0 8px 22px rgba(16, 24, 40, 0.07) !important;
}

div[data-testid="stTabs"] > div:last-child {
    box-shadow: 0 10px 26px rgba(16, 24, 40, 0.07) !important;
}

.table-shell {
    width: 100%;
    max-height: 420px;
    overflow: auto;
    background: #ffffff;
    border: 1px solid #d6dee9;
    border-radius: 10px;
    box-shadow: 0 10px 24px rgba(16, 24, 40, 0.07);
}

.light-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    color: #101828;
    font-size: 11px;
}

.light-table thead th {
    position: sticky;
    top: 0;
    z-index: 2;
    background: #f8fafc;
    color: #344054;
    border-bottom: 1px solid #d6dee9;
    font-size: 10px;
    font-weight: 700;
    text-align: left;
    padding: 9px 10px;
    white-space: nowrap;
}

.light-table tbody td {
    background: #ffffff;
    border-bottom: 1px solid #edf1f6;
    color: #101828;
    padding: 8px 10px;
    vertical-align: top;
    white-space: nowrap;
}

.light-table tbody tr:nth-child(even) td {
    background: #fbfcfe;
}

.light-table tbody tr:hover td {
    background: #eef4ff;
}

.table-empty {
    background: #ffffff;
    border: 1px solid #d6dee9;
    border-radius: 10px;
    color: #667085;
    font-size: 12px;
    padding: 14px;
}

@media (max-width: 900px) {
    .overview-strip {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
    }

    .topbox:after {
        position: static !important;
        display: block;
        margin-bottom: 8px;
    }
}

/* PWA MOBILE APP SHELL */
html,
body {
    background: #f3f6fb !important;
    overscroll-behavior-y: contain;
}

@media (max-width: 760px) {
    .stApp {
        background:
            linear-gradient(180deg, #eef3f8 0%, rgba(238, 243, 248, 0) 180px),
            #f3f6fb !important;
    }

    .block-container {
        padding: calc(10px + env(safe-area-inset-top)) 10px calc(84px + env(safe-area-inset-bottom)) !important;
        max-width: 100% !important;
    }

    .topbox {
        border-radius: 14px !important;
        padding: 16px 16px 15px !important;
        margin: 2px 0 10px !important;
        box-shadow: 0 12px 26px rgba(16, 24, 40, 0.09) !important;
    }

    .topbox:after {
        position: static !important;
        display: block !important;
        margin-bottom: 8px !important;
        font-size: 9px !important;
    }

    .topbox h1 {
        font-size: 20px !important;
        line-height: 1.12 !important;
        max-width: 280px !important;
    }

    .topbox p {
        font-size: 12px !important;
        line-height: 1.45 !important;
        margin-top: 8px !important;
    }

    [data-testid="stFileUploader"] {
        border-radius: 13px !important;
        padding: 10px !important;
        margin-bottom: 10px !important;
    }

    [data-testid="stFileUploader"] section {
        min-height: 76px !important;
        border-radius: 11px !important;
        display: flex !important;
        align-items: center !important;
    }

    [data-testid="stFileUploader"] button {
        min-height: 38px !important;
        border-radius: 9px !important;
        padding: 0 14px !important;
    }

    .overview-strip {
        grid-template-columns: 1fr 1fr !important;
        gap: 8px !important;
        margin: 0 0 10px !important;
    }

    .overview-cell {
        min-height: 58px !important;
        padding: 10px !important;
        border-radius: 11px !important;
    }

    .overview-cell .eyebrow,
    .section-kicker {
        font-size: 12px !important;
    }

    .overview-cell .value {
        font-size: 12px !important;
    }

    .section-kicker {
        margin: 8px 0 7px !important;
    }

    [data-testid="stHorizontalBlock"] {
        gap: 8px !important;
        flex-wrap: wrap !important;
    }

    [data-testid="column"]:has(.card) {
        width: calc(50% - 4px) !important;
        flex: 1 1 calc(50% - 4px) !important;
        min-width: calc(50% - 4px) !important;
    }

    .card {
        min-height: 82px !important;
        padding: 11px !important;
        border-radius: 12px !important;
    }

    .card:after {
        width: 21px !important;
        height: 21px !important;
        right: 10px !important;
        top: 11px !important;
    }

    .lbl {
        font-size: 11px !important;
        line-height: 1.2 !important;
        max-width: calc(100% - 28px) !important;
    }

    .num {
        font-size: 24px !important;
        margin-top: 13px !important;
    }

    hr {
        margin: 10px 0 !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        overflow-x: auto !important;
        overflow-y: hidden !important;
        flex-wrap: nowrap !important;
        justify-content: flex-start !important;
        scroll-snap-type: x proximity;
        -webkit-overflow-scrolling: touch;
        padding: 5px !important;
        border-radius: 13px !important;
    }

    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
        display: none;
    }

    .stTabs [data-baseweb="tab"] {
        min-width: max-content !important;
        min-height: 38px !important;
        padding: 8px 12px !important;
        border-radius: 9px !important;
        scroll-snap-align: start;
    }

    div[data-testid="stTabs"] > div:last-child {
        padding: 12px !important;
        border-radius: 13px !important;
        margin-top: 8px !important;
    }

    h2, h3 {
        font-size: 15px !important;
        margin-bottom: 10px !important;
    }

    [data-testid="stMarkdownContainer"] p,
    .stMarkdown p {
        font-size: 11px !important;
    }

    .table-shell {
        max-height: 62vh !important;
        border-radius: 12px !important;
        -webkit-overflow-scrolling: touch;
    }

    .light-table {
        min-width: 680px;
        font-size: 10.5px !important;
    }

    .light-table thead th {
        padding: 8px 9px !important;
        font-size: 11px !important;
    }

    .light-table tbody td {
        padding: 8px 9px !important;
    }

    .stTextInput input,
    .stMultiSelect [data-baseweb="select"] {
        min-height: 40px !important;
        border-radius: 10px !important;
        font-size: 12px !important;
    }

    .insight-grid {
        grid-template-columns: repeat(2, minmax(0, 1fr)) !important;
        gap: 8px !important;
    }

    .insight-card {
        border-radius: 12px !important;
        padding: 11px !important;
    }

    .insight-card .mini-num {
        font-size: 21px !important;
    }

    .insight-panel {
        border-radius: 12px !important;
        padding: 12px !important;
    }

    .insight-panel h4 {
        font-size: 13px !important;
    }

    .insight-panel li {
        font-size: 12px !important;
        line-height: 1.5 !important;
    }

}

/* SIMPLE TAB NAVIGATION */
.stTabs [data-baseweb="tab-list"] {
    display: flex !important;
    align-items: center;
    gap: 4px !important;
    padding: 5px !important;
    background: #ffffff !important;
    border: 1px solid #d6dee9 !important;
    border-radius: 10px !important;
    box-shadow: 0 8px 20px rgba(16, 24, 40, 0.06) !important;
}

.stTabs [data-baseweb="tab"] {
    min-height: 34px !important;
    padding: 7px 12px !important;
    border-radius: 7px !important;
    color: #475467 !important;
    font-size: 11px !important;
    font-weight: 700 !important;
    background: transparent !important;
    border: 1px solid transparent !important;
}

.stTabs [data-baseweb="tab"]:hover {
    background: #f2f4f7 !important;
    color: #101828 !important;
}

.stTabs [aria-selected="true"] {
    background: #101828 !important;
    color: #ffffff !important;
    border-color: #101828 !important;
}

div[data-testid="stTabs"] > div:last-child {
    border-radius: 10px !important;
    border: 1px solid #d6dee9 !important;
    background: #ffffff !important;
    box-shadow: 0 10px 24px rgba(16, 24, 40, 0.06) !important;
}

@media (max-width: 760px) {
    .stTabs [data-baseweb="tab-list"] {
        gap: 4px !important;
        padding: 5px !important;
        border-radius: 10px !important;
        overflow-x: auto !important;
        scrollbar-width: none;
        box-shadow: 0 8px 20px rgba(16, 24, 40, 0.06) !important;
    }

    .stTabs [data-baseweb="tab-list"]::-webkit-scrollbar {
        display: none;
    }

    .stTabs [data-baseweb="tab"] {
        min-height: 36px !important;
        padding: 7px 11px !important;
        flex: 0 0 auto !important;
        white-space: nowrap !important;
    }
}

/* FINAL MOBILE-SAFE CLEANUP */
.stApp,
html,
body {
    background: #f7f9fc !important;
    color: #101828 !important;
}

.topbox,
[data-testid="stFileUploader"],
.overview-cell,
.card,
div[data-testid="stTabs"] > div:last-child,
.insight-card,
.insight-panel,
.table-shell {
    background: #ffffff !important;
    background-image: none !important;
    border: 1px solid #d8e0ea !important;
    box-shadow: none !important;
}

.topbox:before,
.card:before,
.card:after {
    display: none !important;
}

.topbox:after {
    color: #667085 !important;
}

.card:hover,
.stTabs [data-baseweb="tab"]:hover,
.light-table tbody tr:hover td {
    transform: none !important;
    box-shadow: none !important;
}

.card:hover {
    border-color: #d8e0ea !important;
}

[data-testid="stFileUploader"] section {
    background: #ffffff !important;
    border: 1px dashed #c9d3e1 !important;
}

[data-testid="stFileUploader"] button {
    box-shadow: none !important;
}

[data-testid="stFileUploader"] button {
    font-size: 0 !important;
}

[data-testid="stFileUploader"] button * {
    font-size: 0 !important;
    color: transparent !important;
}

[data-testid="stFileUploader"] button::after {
    content: "Upload";
    color: #667085;
    font-size: 12px;
    font-weight: 500;
}

.stTabs [data-baseweb="tab-list"] {
    background: #ffffff !important;
    border: 1px solid #d8e0ea !important;
    box-shadow: none !important;
}

.stTabs [data-baseweb="tab"] {
    background: #ffffff !important;
    color: #475467 !important;
}

.stTabs [data-baseweb="tab"]:hover {
    background: #f7f9fc !important;
    color: #101828 !important;
}

.stTabs [aria-selected="true"] {
    background: #101828 !important;
    color: #ffffff !important;
    border-color: #101828 !important;
}

.table-shell {
    width: 100% !important;
    max-width: 100% !important;
    overflow-x: auto !important;
    overflow-y: auto !important;
    -webkit-overflow-scrolling: touch;
}

.light-table {
    width: max-content !important;
    min-width: 100% !important;
    table-layout: auto !important;
    border-collapse: collapse !important;
}

.light-table thead th,
.light-table tbody td {
    white-space: nowrap !important;
    overflow-wrap: normal !important;
    word-break: normal !important;
    padding: 8px 7px !important;
    line-height: 1.35 !important;
}

.light-table thead th {
    font-size: 9px !important;
}

.light-table tbody td {
    font-size: 12px !important;
}

@media (max-width: 760px) {
    .block-container {
        padding: 8px 8px 70px !important;
    }

    .topbox {
        padding: 13px !important;
        margin-bottom: 8px !important;
        border-radius: 10px !important;
    }

    .topbox h1 {
        max-width: 100% !important;
        font-size: 18px !important;
    }

    .topbox p {
        font-size: 12px !important;
    }

    .overview-strip {
        grid-template-columns: 1fr 1fr !important;
        gap: 6px !important;
    }

    .overview-cell {
        min-height: auto !important;
        padding: 8px !important;
    }

    .overview-cell .value {
        font-size: 12px !important;
    }

    .card {
        min-height: 72px !important;
        padding: 9px !important;
        border-radius: 9px !important;
    }

    .lbl {
        max-width: 100% !important;
        font-size: 7.5px !important;
    }

    .num {
        font-size: 22px !important;
        margin-top: 10px !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        padding: 4px !important;
        gap: 3px !important;
        border-radius: 9px !important;
    }

    .stTabs [data-baseweb="tab"] {
        min-height: 32px !important;
        padding: 6px 9px !important;
        font-size: 10px !important;
        border-radius: 6px !important;
    }

    div[data-testid="stTabs"] > div:last-child {
        padding: 9px !important;
        border-radius: 10px !important;
    }

    .table-shell {
        max-height: 60vh !important;
        border-radius: 9px !important;
    }

    .light-table {
        width: max-content !important;
        min-width: 100% !important;
    }

    .light-table thead th,
    .light-table tbody td {
        padding: 7px 5px !important;
        white-space: nowrap !important;
    }

    .light-table thead th {
        font-size: 11px !important;
    }

    .light-table tbody td {
        font-size: 12px !important;
    }
}

/* MOBILE EXECUTIVE SNAPSHOT ROWS */
@media (max-width: 760px) {
    [data-testid="column"]:has(.card) {
        width: 100% !important;
        flex: 1 1 100% !important;
        min-width: 100% !important;
    }

    .card {
        min-height: 54px !important;
        padding: 12px 14px !important;
        border-radius: 10px !important;
        display: flex !important;
        flex-direction: row !important;
        align-items: center !important;
        justify-content: space-between !important;
        gap: 12px !important;
    }

    .lbl {
        color: #101828 !important;
        font-size: 12px !important;
        font-weight: 500 !important;
        letter-spacing: 0 !important;
        line-height: 1.25 !important;
        text-transform: uppercase !important;
        max-width: none !important;
        flex: 1 1 auto !important;
    }

    .metric-row {
        display: block !important;
        flex: 0 0 auto !important;
    }

    .num {
        font-size: 21px !important;
        font-weight: 500 !important;
        margin: 0 !important;
        line-height: 1 !important;
        text-align: right !important;
        min-width: 52px !important;
    }

    .section-kicker {
        font-size: 9px !important;
        font-weight: 500 !important;
        letter-spacing: .5px !important;
        margin: 10px 0 7px !important;
    }
}

/* FINAL MOBILE ALIGNMENT AND SPACING */
@media (max-width: 760px) {
    .block-container {
        padding: 8px 8px 42px !important;
    }

    .stTabs {
        margin-top: 4px !important;
    }

    .stTabs [data-baseweb="tab-list"] {
        width: 100% !important;
        border-radius: 9px !important;
        padding: 4px !important;
        gap: 3px !important;
        background: #ffffff !important;
        border: 1px solid #d8e0ea !important;
        box-shadow: none !important;
    }

    .stTabs [data-baseweb="tab"] {
        min-height: 32px !important;
        padding: 6px 9px !important;
        border-radius: 6px !important;
        background: #ffffff !important;
        color: #475467 !important;
        border: 1px solid transparent !important;
        font-size: 10px !important;
        font-weight: 500 !important;
    }

    .stTabs [aria-selected="true"] {
        background: #f2f4f7 !important;
        color: #101828 !important;
        border-color: #cfd8e5 !important;
    }

    div[data-testid="stTabs"] > div:last-child {
        width: 100% !important;
        padding: 9px !important;
        margin-top: 6px !important;
        border-radius: 9px !important;
        border: 1px solid #d8e0ea !important;
        box-shadow: none !important;
    }

    h2, h3,
    [data-testid="stHeading"] {
        margin-top: 0 !important;
        margin-bottom: 8px !important;
        padding-top: 0 !important;
    }

    h2, h3 {
        font-size: 15px !important;
        line-height: 1.25 !important;
    }

    .table-shell {
        width: 100% !important;
        margin: 0 !important;
        border-radius: 8px !important;
        border: 1px solid #d8e0ea !important;
    }

    .light-table {
        min-width: 100% !important;
    }

    .light-table thead th {
        padding: 7px 8px !important;
        font-size: 11px !important;
    }

    .light-table tbody td {
        padding: 7px 8px !important;
        font-size: 12px !important;
    }

    [data-testid="stMarkdownContainer"],
    [data-testid="stVerticalBlock"],
    [data-testid="stElementContainer"] {
        margin-top: 0 !important;
    }
}

/* CUTE FLOATING GEOMETRIC BACKGROUND */
.stApp {
    position: relative;
    overflow-x: hidden;
    background:
        radial-gradient(circle at 18% 22%, rgba(124, 58, 237, 0.045), transparent 30%),
        radial-gradient(circle at 82% 16%, rgba(45, 212, 191, 0.04), transparent 28%),
        #fbfcff !important;
}

.stApp:before,
.stApp:after {
    content: "";
    position: fixed;
    pointer-events: none;
    z-index: 0;
    will-change: transform;
}

.stApp:before {
    width: 145px;
    height: 145px;
    left: 9%;
    top: 42%;
    border-radius: 22px;
    background: rgba(168, 125, 255, 0.42);
    border: 4px solid rgba(101, 61, 214, 0.34);
    box-shadow:
        330px 135px 0 36px rgba(168, 125, 255, 0.36),
        760px -175px 0 -16px rgba(84, 218, 229, 0.46),
        1040px 80px 0 42px rgba(168, 125, 255, 0.30),
        805px 310px 0 -28px rgba(168, 125, 255, 0.34);
    filter: drop-shadow(0 18px 28px rgba(124, 58, 237, 0.15));
    opacity: .82;
    transform: rotate(-15deg);
    animation: cuteTileFloat 36s ease-in-out infinite alternate;
}

.stApp:after {
    width: 28px;
    height: 28px;
    left: 17%;
    top: 78%;
    border-radius: 999px;
    background: rgba(103, 232, 249, 0.56);
    border: 5px solid rgba(6, 182, 212, 0.24);
    box-shadow:
        395px -190px 0 -2px rgba(168, 125, 255, 0.50),
        505px -350px 0 2px rgba(103, 232, 249, 0.44),
        1025px 12px 0 0 rgba(103, 232, 249, 0.46),
        900px -235px 0 24px rgba(168, 125, 255, 0.24);
    filter: drop-shadow(0 14px 24px rgba(6, 182, 212, 0.16));
    opacity: .88;
    animation: cuteDotFloat 30s ease-in-out infinite alternate;
}

[data-testid="stAppViewContainer"],
.block-container {
    position: relative;
    z-index: 1;
}

@keyframes cuteTileFloat {
    from {
        transform: translate3d(-16px, -10px, 0) rotate(-15deg) scale(1);
    }
    to {
        transform: translate3d(28px, 24px, 0) rotate(-9deg) scale(1.03);
    }
}

@keyframes cuteDotFloat {
    from {
        transform: translate3d(14px, 12px, 0) scale(1);
    }
    to {
        transform: translate3d(-22px, -18px, 0) scale(1.08);
    }
}

@media (max-width: 760px) {
    .stApp {
        background:
            radial-gradient(circle at 18% 18%, rgba(124, 58, 237, 0.04), transparent 34%),
            #fbfcff !important;
    }

    .stApp:before {
        width: 96px;
        height: 96px;
        left: 66%;
        top: 18%;
        border-radius: 18px;
        border-width: 3px;
        box-shadow:
            -250px 290px 0 -10px rgba(168, 125, 255, 0.34),
            -45px 430px 0 28px rgba(168, 125, 255, 0.25),
            40px 655px 0 -18px rgba(84, 218, 229, 0.34);
        opacity: .62;
    }

    .stApp:after {
        width: 24px;
        height: 24px;
        left: 11%;
        top: 58%;
        border-width: 4px;
        box-shadow:
            250px -230px 0 0 rgba(103, 232, 249, 0.42),
            285px 160px 0 -2px rgba(168, 125, 255, 0.42),
            30px 410px 0 1px rgba(103, 232, 249, 0.40);
        opacity: .68;
    }
}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbox">
<h1>Recruitment Excel Automation</h1>
<p><strong>Production dashboard</strong> for exact recruitment counts, status movement, recruiter performance, pending action, rejection, drop, no-show, and lead review insights.</p>
</div>
""", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Recruitment Excel File", type=["xlsx", "xls", "csv"])

STATUS_ORDER = [
    "YTS - R1", "Sch - R1 - Berribot", "No Show - Berribot",
    "No Show - R1", "Reject - R1 - Berribot", "Reject - R1",
    "R1 Reject-Incruiter", "Drop - R1",
    "YTS - R2", "Sch - R2", "Reject - R2", "Drop - R2",
    "YTS - HRD", "HR / Offer Discussion", "HR Reject",
    "Sch - R3 / Final", "Reject - R3 / Final", "Drop - R3",
    "Screen Reject", "No Show", "Drop",
    "Verbal Offer Decline", "Joined"
]

PENDING_STATUS = [
    "YTS - R1", "YTS - R2", "YTS - HRD",
    "Sch - R1 - Berribot", "Sch - R2", "Sch - R3 / Final",
    "HR / Offer Discussion"
]

REJECT_STATUS = [
    "Reject - R1 - Berribot", "Reject - R1", "R1 Reject-Incruiter",
    "Reject - R2", "Reject - R3 / Final", "HR Reject", "Screen Reject"
]

DROP_STATUS = ["Drop - R1", "Drop - R2", "Drop - R3", "Drop"]

NO_SHOW_STATUS = ["No Show - Berribot", "No Show - R1", "No Show"]

SCHEDULED_STATUS = ["Sch - R1 - Berribot", "Sch - R2", "Sch - R3 / Final"]

def load_file(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    return pd.read_excel(file)

def clean_df(df):
    df.columns = df.columns.astype(str).str.strip()
    df = df.dropna(how="all")

    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype(str).str.strip()
            df[col] = df[col].replace(["nan", "NaN", "None", "NaT"], "")

    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    return df

def find_column(df, possible_names):
    for col in df.columns:
        if col.strip().lower() in possible_names:
            return col
    return None

def count_status(df, status_col):
    counts = df[status_col].value_counts()

    rows = []
    for s in STATUS_ORDER:
        rows.append({"Status": s, "Count": int(counts.get(s, 0))})

    extra = [x for x in counts.index if x not in STATUS_ORDER and str(x).strip() != ""]
    for s in extra:
        rows.append({"Status": s, "Count": int(counts.get(s, 0))})

    report = pd.DataFrame(rows)
    report = report[report["Count"] > 0].reset_index(drop=True)
    report.insert(0, "S.No", range(1, len(report) + 1))
    return report

def render_table(df, height=420):
    if df is None or df.empty:
        st.markdown('<div class="table-empty">No records available.</div>', unsafe_allow_html=True)
        return

    display_df = df.copy().fillna("")
    table_html = display_df.to_html(
        index=False,
        escape=True,
        classes="light-table",
        border=0
    )
    st.markdown(
        f'<div class="table-shell" style="max-height:{height}px">{table_html}</div>',
        unsafe_allow_html=True
    )

def make_summary(status_report, total):
    get = lambda items: int(status_report[status_report["Status"].isin(items)]["Count"].sum())

    summary = pd.DataFrame([
        ["Total Candidates", total],
        ["Yet To Schedule", get(["YTS - R1", "YTS - R2", "YTS - HRD"])],
        ["Scheduled", get(SCHEDULED_STATUS)],
        ["Rejected", get(REJECT_STATUS)],
        ["Dropped", get(DROP_STATUS)],
        ["No Show", get(NO_SHOW_STATUS)],
        ["Offer Discussion", get(["HR / Offer Discussion"])],
        ["Offer Declined", get(["Verbal Offer Decline"])],
        ["Joined", get(["Joined"])]
    ], columns=["Metric", "Count"])

    return summary

def recruiter_report(df, recruiter_col, status_col):
    if not recruiter_col:
        return pd.DataFrame({"Message": ["Recruiter column not found"]})

    temp = df.copy()
    temp[recruiter_col] = temp[recruiter_col].replace("", "Not Mentioned")

    result = temp.groupby(recruiter_col).agg(
        Total=(status_col, "count"),
        Yet_To_Schedule=(status_col, lambda x: x.isin(["YTS - R1", "YTS - R2", "YTS - HRD"]).sum()),
        Scheduled=(status_col, lambda x: x.isin(SCHEDULED_STATUS).sum()),
        Rejected=(status_col, lambda x: x.isin(REJECT_STATUS).sum()),
        Dropped=(status_col, lambda x: x.isin(DROP_STATUS).sum()),
        No_Show=(status_col, lambda x: x.isin(NO_SHOW_STATUS).sum()),
        Joined=(status_col, lambda x: x.eq("Joined").sum())
    ).reset_index()

    return result.sort_values("Total", ascending=False)

def recruiter_lead_review(df, recruiter_col, status_col):
    if not recruiter_col:
        return pd.DataFrame({"Message": ["Recruiter column not found"]})

    temp = df.copy()
    temp[recruiter_col] = temp[recruiter_col].replace("", "Not Mentioned")

    review = temp.groupby(recruiter_col).agg(
        Total=(status_col, "count"),
        YTS=(status_col, lambda x: x.isin(["YTS - R1", "YTS - R2", "YTS - HRD"]).sum()),
        Scheduled=(status_col, lambda x: x.isin(SCHEDULED_STATUS).sum()),
        No_Show=(status_col, lambda x: x.isin(NO_SHOW_STATUS).sum()),
        Rejected=(status_col, lambda x: x.isin(REJECT_STATUS).sum()),
        Dropped=(status_col, lambda x: x.isin(DROP_STATUS).sum()),
        Offer_Discussion=(status_col, lambda x: x.eq("HR / Offer Discussion").sum()),
        Offer_Declined=(status_col, lambda x: x.eq("Verbal Offer Decline").sum()),
        Joined=(status_col, lambda x: x.eq("Joined").sum())
    ).reset_index()

    review["Pending_Action"] = review["YTS"] + review["Scheduled"] + review["Offer_Discussion"]
    review["YTS_%"] = (review["YTS"] / review["Total"] * 100).round(1)
    review["No_Show_%"] = (review["No_Show"] / review["Total"] * 100).round(1)
    review["Reject_%"] = (review["Rejected"] / review["Total"] * 100).round(1)
    review["Drop_%"] = (review["Dropped"] / review["Total"] * 100).round(1)
    review["Join_%"] = (review["Joined"] / review["Total"] * 100).round(1)

    def priority(row):
        if row["YTS"] >= 10 or row["No_Show"] >= 5 or row["Offer_Declined"] >= 2:
            return "High"
        if row["Pending_Action"] >= 8 or row["Rejected"] >= 10 or row["Dropped"] >= 4:
            return "Medium"
        return "Stable"

    review["Lead_Priority"] = review.apply(priority, axis=1)
    return review.sort_values(["Lead_Priority", "Pending_Action", "Total"], ascending=[True, False, False])

def selected_recruiter_name(review_df):
    if review_df.empty or "Message" in review_df.columns:
        return None

    names = review_df.iloc[:, 0].astype(str).tolist()
    return names[0] if names else None

def recruiter_candidate_slice(df, recruiter_col, recruiter_name):
    if not recruiter_col or not recruiter_name:
        return df.iloc[0:0]
    temp = df.copy()
    temp[recruiter_col] = temp[recruiter_col].replace("", "Not Mentioned")
    return temp[temp[recruiter_col].astype(str).str.lower() == str(recruiter_name).lower()]

def build_recruiter_insights(name, stats):
    total = int(stats["Total"])
    yts = int(stats["YTS"])
    scheduled = int(stats["Scheduled"])
    no_show = int(stats["No_Show"])
    rejected = int(stats["Rejected"])
    dropped = int(stats["Dropped"])
    offer_discussion = int(stats["Offer_Discussion"])
    offer_declined = int(stats["Offer_Declined"])
    joined = int(stats["Joined"])
    pending_action = int(stats["Pending_Action"])
    yts_rate = float(stats["YTS_%"])
    no_show_rate = float(stats["No_Show_%"])
    reject_rate = float(stats["Reject_%"])
    drop_rate = float(stats["Drop_%"])
    join_rate = float(stats["Join_%"])

    observations = []
    if yts >= 10 or yts_rate >= 25:
        observations.append(f"The YTS bucket is high at {yts} candidates ({yts_rate}%). Prioritize same-day scheduling follow-ups and clear the oldest pending profiles first.")
    elif yts > 0:
        observations.append(f"There are {yts} YTS candidates pending. Keep the follow-up rhythm tight so this does not become aged pipeline.")

    if no_show >= 5 or no_show_rate >= 12:
        observations.append(f"No-shows are a concern at {no_show} candidates ({no_show_rate}%). Strengthen candidate confirmation, availability validation, and reminder calls before interview slots are blocked.")
    elif no_show > 0:
        observations.append(f"There are {no_show} no-show cases. Reconfirm interest, location, notice period, compensation fit, and interview availability before moving candidates ahead.")

    if rejected >= 10 or reject_rate >= 35:
        observations.append(f"Rejected profiles are high at {rejected} ({reject_rate}%). Review screening quality, role fit, communication clarity, and whether candidates are being mapped to the right requirement.")

    if dropped >= 4 or drop_rate >= 10:
        observations.append(f"Dropped candidates are at {dropped} ({drop_rate}%). Check if drop-offs are due to compensation, notice period, location, competing offers, or delayed follow-up.")

    if offer_discussion > 0:
        observations.append(f"{offer_discussion} candidate(s) are in offer discussion. Keep salary expectation, joining date, counter-offer risk, and document readiness visible to the lead.")

    if offer_declined > 0:
        observations.append(f"{offer_declined} offer decline(s) need a reason-level review. Capture whether the issue was compensation, role mismatch, location, joining timeline, or competing offer.")

    if joined == 0 and total >= 20:
        observations.append(f"No joined candidates are recorded from {total} profiles. The lead may expect a conversion plan from scheduled and offer-stage candidates.")
    elif joined > 0:
        observations.append(f"{joined} candidate(s) joined, giving a join rate of {join_rate}%. Continue tracking offer-to-join risk until the candidate is fully onboarded.")

    if scheduled > 0:
        observations.append(f"{scheduled} candidate(s) are scheduled. Ensure every scheduled candidate has confirmation, interview details, and backup follow-up before the slot.")

    if not observations:
        observations.append("This pipeline looks stable at the moment. Continue maintaining clean status updates and daily follow-up discipline.")

    actions = [
        f"Clear pending action first: {pending_action} candidate(s) are in YTS, scheduled, or offer-discussion stages.",
        "Prepare a short reason summary for every rejected, dropped, no-show, and offer-declined candidate.",
        "Share the next follow-up date and owner for each active candidate.",
        "Validate whether statuses are updated correctly before the lead review."
    ]

    questions = [
        f"Why are {yts} candidate(s) still in YTS, and which ones can be scheduled today?",
        "How old are the YTS candidates, and what is the follow-up plan for each aging profile?",
        f"What caused the {no_show} no-show case(s), and were confirmation calls completed before the interview?",
        "Which candidates need stronger pre-screening before scheduling to reduce no-shows?",
        f"Why were {rejected} candidate(s) rejected, and are the rejection reasons role-fit, communication, technical, salary, or availability related?",
        f"Why did {dropped} candidate(s) drop, and is the reason compensation, notice period, location, another offer, or delayed follow-up?",
        f"What is the current status of {offer_discussion} candidate(s) in offer discussion, and what is blocking closure?",
        f"Why did {offer_declined} candidate(s) decline the offer, and what could prevent similar declines?",
        f"How many of the {scheduled} scheduled candidates are confirmed for interview attendance?",
        f"What is the conversion plan to improve joined count from the current {joined} joined candidate(s)?",
        "Which candidates need immediate lead support, client clarification, salary approval, or faster feedback?",
        "Are all candidate statuses accurate, or are any profiles pending update in the tracker?"
    ]

    return observations, actions, questions

def filter_table(df, status_col, selected_status, search_text):
    filtered = df.copy()

    if selected_status:
        filtered = filtered[filtered[status_col].isin(selected_status)]

    if search_text:
        filtered = filtered[
            filtered.astype(str).apply(
                lambda row: row.str.contains(search_text, case=False, na=False).any(),
                axis=1
            )
        ]

    return filtered

if uploaded_file:
    df = load_file(uploaded_file)
    df = clean_df(df)

    status_col = find_column(df, ["status", "candidate status", "current status"])
    recruiter_col = find_column(df, ["recruiter", "hr", "owner", "assigned to"])

    if not status_col:
        st.error("Status column not found in uploaded Excel.")
        st.stop()

    recruiter_display = recruiter_col if recruiter_col else "Not found"
    st.markdown(f"""
    <div class="overview-strip">
        <div class="overview-cell">
            <div class="eyebrow">Dataset Ready</div>
            <div class="value">{html.escape(uploaded_file.name)}</div>
        </div>
        <div class="overview-cell">
            <div class="eyebrow">Status Column</div>
            <div class="value">{html.escape(str(status_col))}</div>
        </div>
        <div class="overview-cell">
            <div class="eyebrow">Recruiter Column</div>
            <div class="value">{html.escape(str(recruiter_display))}</div>
        </div>
        <div class="overview-cell">
            <div class="eyebrow">Generated</div>
            <div class="value">{datetime.now().strftime("%d %b %Y, %I:%M %p")}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    total = len(df)

    status_report = count_status(df, status_col)
    summary = make_summary(status_report, total)
    recruiter = recruiter_report(df, recruiter_col, status_col)
    lead_review = recruiter_lead_review(df, recruiter_col, status_col)

    pending = df[df[status_col].isin(PENDING_STATUS)]
    rejected = df[df[status_col].isin(REJECT_STATUS)]
    dropped = df[df[status_col].isin(DROP_STATUS)]
    noshow = df[df[status_col].isin(NO_SHOW_STATUS)]

    m = dict(zip(summary["Metric"], summary["Count"]))

    st.markdown('<div class="section-kicker">Executive Snapshot</div>', unsafe_allow_html=True)

    c1, c2, c3, c4, c5, c6 = st.columns(6, gap="small")
    cards = [
        ("Total Candidates", m["Total Candidates"], "Pipeline"),
        ("Yet To Schedule", m["Yet To Schedule"], "Action"),
        ("Scheduled", m["Scheduled"], "Interview"),
        ("Rejected", m["Rejected"], "Quality"),
        ("Dropped", m["Dropped"], "Risk"),
        ("Joined", m["Joined"], "Closure")
    ]

    card_classes = [
        "card-total",
        "card-yts",
        "card-sch",
        "card-rej",
        "card-drop",
        "card-join"
    ]

    for col, (label, value, note), cls in zip([c1, c2, c3, c4, c5, c6], cards, card_classes):
        with col:
            display_value = f"{int(value):,}"
            st.markdown(f"""
            <div class="card {cls}">
                <div class="lbl">{label}</div>
                <div class="metric-row">
                    <div class="num">{display_value}</div>
                    <div class="metric-note">{note}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
        "Main Counts",
        "Exact Status Counts",
        "Recruiter Wise",
        "Pending",
        "Rejected / Dropped / No Show",
        "Search Full Data",
        "Lead Review"
    ])

    with tab1:
        st.subheader("Main Count Summary")
        render_table(summary, height=320)

    with tab2:
        st.subheader("Exact Status Wise Counts")
        render_table(status_report)

    with tab3:
        st.subheader("Recruiter Wise Count Report")
        render_table(recruiter)

    with tab4:
        st.subheader("Pending / Scheduled / Action Required Candidates")
        render_table(pending)

    with tab5:
        a, b, c = st.tabs(["Rejected", "Dropped", "No Show"])

        with a:
            st.write(f"Total Rejected: {len(rejected)}")
            render_table(rejected)

        with b:
            st.write(f"Total Dropped: {len(dropped)}")
            render_table(dropped)

        with c:
            st.write(f"Total No Show: {len(noshow)}")
            render_table(noshow)

    with tab6:
        st.subheader("Search and Filter Full Data")

        all_status = sorted(df[status_col].dropna().unique().tolist())

        selected_status = st.multiselect("Filter by Status", all_status)
        search_text = st.text_input("Search anything: name, email, phone, skill, recruiter, location")

        filtered = filter_table(df, status_col, selected_status, search_text)

        st.write(f"Showing {len(filtered)} records")
        render_table(filtered)

    with tab7:
        st.markdown('<h3 class="tab-heading-tight">Recruiter Lead Review</h3>', unsafe_allow_html=True)

        if not recruiter_col or "Message" in lead_review.columns:
            st.info("Recruiter column not found. Add a recruiter, HR, owner, or assigned-to column to generate lead review insights.")
        else:
            recruiter_names = lead_review[recruiter_col].astype(str).tolist()
            default_name = selected_recruiter_name(lead_review)
            default_index = recruiter_names.index(default_name) if default_name in recruiter_names else 0
            selected_recruiter = recruiter_names[default_index]

            stats = lead_review[lead_review[recruiter_col].astype(str) == str(selected_recruiter)].iloc[0]
            observations, actions, questions = build_recruiter_insights(selected_recruiter, stats)

            st.markdown(f"""
            <div class="insight-grid">
                <div class="insight-card"><div class="mini-lbl">Total Profiles</div><div class="mini-num">{int(stats["Total"]):,}</div></div>
                <div class="insight-card"><div class="mini-lbl">YTS Pending</div><div class="mini-num">{int(stats["YTS"]):,}</div></div>
                <div class="insight-card"><div class="mini-lbl">No Shows</div><div class="mini-num">{int(stats["No_Show"]):,}</div></div>
                <div class="insight-card"><div class="mini-lbl">Lead Priority</div><div class="mini-num">{html.escape(str(stats["Lead_Priority"]))}</div></div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(
                f"""
                <div class="insight-panel">
                    <h4>Professional Summary</h4>
                    <ul>{''.join(f'<li>{html.escape(item)}</li>' for item in observations)}</ul>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="insight-panel">
                    <h4>Recommended Actions</h4>
                    <ul>{''.join(f'<li>{html.escape(item)}</li>' for item in actions)}</ul>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="insight-panel">
                    <h4>Questions the Lead May Ask</h4>
                    <ul>{''.join(f'<li>{html.escape(item)}</li>' for item in questions)}</ul>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.subheader("All Recruiters - Lead Priority View")
            render_table(lead_review)

            focus_rows = recruiter_candidate_slice(df, recruiter_col, selected_recruiter)
            focus_rows = focus_rows[
                focus_rows[status_col].isin(
                    PENDING_STATUS + NO_SHOW_STATUS + DROP_STATUS + REJECT_STATUS + ["HR / Offer Discussion", "Verbal Offer Decline"]
                )
            ]
            st.subheader("Focus Candidates")
            render_table(focus_rows)

else:
    st.info("Waiting for a file to generate counts.")
