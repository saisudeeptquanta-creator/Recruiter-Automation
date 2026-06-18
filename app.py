import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import html
import json
import base64
import io
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
    background: radial-gradient(circle at 94% 6%, rgba(203, 120, 199, .46), transparent 20%), radial-gradient(circle at 6% 92%, rgba(112, 151, 235, .38), transparent 22%), radial-gradient(circle at 47% 42%, rgba(255, 219, 102, .34), transparent 17%), linear-gradient(135deg, #f8f8f8 0%, #eadcff 42%, #dff3ff 100%) !important;        #fbfcff;
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
            div[data-testid="stElementContainer"][height="0px"] {
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
            addTag(doc, 'link', { rel: 'icon', href: '/app/static/icon.png', type: 'image/png' });
            addTag(doc, 'link', { rel: 'apple-touch-icon', href: '/app/static/icon.png' });
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
div[data-testid="stElementContainer"][height="0px"] {
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
    background: radial-gradient(circle at 94% 6%, rgba(203, 120, 199, .46), transparent 20%), radial-gradient(circle at 6% 92%, rgba(112, 151, 235, .38), transparent 22%), radial-gradient(circle at 47% 42%, rgba(255, 219, 102, .34), transparent 17%), linear-gradient(135deg, #f8f8f8 0%, #eadcff 42%, #dff3ff 100%) !important;        #fbfcff;
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
    background: radial-gradient(circle at 94% 6%, rgba(203, 120, 199, .46), transparent 20%), radial-gradient(circle at 6% 92%, rgba(112, 151, 235, .38), transparent 22%), radial-gradient(circle at 47% 42%, rgba(255, 219, 102, .34), transparent 17%), linear-gradient(135deg, #f8f8f8 0%, #eadcff 42%, #dff3ff 100%) !important;        #fbfcff;
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
    color: #ffffff !important;
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
    color: #ffffff !important;
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

[data-testid="stFileUploader"] button,
[data-testid="stFileUploader"] [data-testid="baseButton-secondary"] {
    display: inline-flex !important;
    align-items: center !important;
    justify-content: center !important;
    gap: 7px !important;
    min-width: 116px !important;
    font-size: 0 !important;
    line-height: 1 !important;
}

[data-testid="stFileUploader"] button *,
[data-testid="stFileUploader"] [data-testid="baseButton-secondary"] * {
    display: none !important;
    font-size: 0 !important;
    color: transparent !important;
}

[data-testid="stFileUploader"] button::before,
[data-testid="stFileUploader"] [data-testid="baseButton-secondary"]::before {
    content: "";
    width: 15px;
    height: 15px;
    flex: 0 0 15px;
    background-color: #667085;
    -webkit-mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4'/%3E%3Cpolyline points='17 8 12 3 7 8'/%3E%3Cline x1='12' x2='12' y1='3' y2='15'/%3E%3C/svg%3E") center / contain no-repeat;
    mask: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='24' height='24' viewBox='0 0 24 24' fill='none' stroke='black' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4'/%3E%3Cpolyline points='17 8 12 3 7 8'/%3E%3Cline x1='12' x2='12' y1='3' y2='15'/%3E%3C/svg%3E") center / contain no-repeat;
}

[data-testid="stFileUploader"] button::after,
[data-testid="stFileUploader"] [data-testid="baseButton-secondary"]::after {
    content: "Upload";
    color: #667085;
    font-size: 12px !important;
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

st.markdown('<div class="section-kicker">Upload Recruitment File</div>', unsafe_allow_html=True)

with st.expander("Excel / CSV upload", expanded=True):
    components.html(
        """
        <div style="font-family: Inter, system-ui, sans-serif; color:#101828;">
            <input id="office-file" type="file" accept=".xlsx,.xls,.csv"
                style="width:100%; margin-bottom:10px; border:1px solid #d6dee9; border-radius:8px; padding:10px; background:#fff;">
            <textarea id="office-output" readonly placeholder="Choose the Excel/CSV file. Encoded text will appear here."
                style="width:100%; height:150px; border:1px solid #d6dee9; border-radius:8px; padding:10px; font-size:12px;"></textarea>
            <button id="office-copy" type="button"
                style="margin-top:8px; min-height:34px; padding:0 12px; border:1px solid #2457d6; border-radius:8px; background:#2457d6; color:white; font-weight:700;">
                Copy File Data
            </button>
            <div id="office-status" style="margin-top:8px; font-size:12px; color:#667085;">Choose file, copy data, paste below.</div>
        </div>
        <script>
        const fileInput = document.getElementById("office-file");
        const output = document.getElementById("office-output");
        const copy = document.getElementById("office-copy");
        const status = document.getElementById("office-status");

        fileInput.addEventListener("change", () => {
            const file = fileInput.files && fileInput.files[0];
            if (!file) return;
            const reader = new FileReader();
            reader.onload = () => {
                const base64 = String(reader.result).split(",")[1] || "";
                output.value = `${file.name}|${base64}`;
                status.textContent = "File ready. Click Copy File Data, then paste below.";
            };
            reader.onerror = () => {
                status.textContent = "Could not read this file.";
            };
            reader.readAsDataURL(file);
        });

        copy.addEventListener("click", async () => {
            output.select();
            output.setSelectionRange(0, output.value.length);
            try {
                await navigator.clipboard.writeText(output.value);
                status.textContent = "Copied. Paste it in the box below.";
            } catch (e) {
                document.execCommand("copy");
                status.textContent = "Copied. Paste it in the box below.";
            }
        });
        </script>
        """,
        height=270,
    )
    encoded_upload = st.text_area(
        "Paste copied file data here",
        key="encoded_upload",
        height=110,
        placeholder="Paste copied file data here.",
    )

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

def load_encoded_file(encoded_value):
    if not encoded_value or "|" not in encoded_value:
        return None, None

    filename, encoded_data = encoded_value.strip().split("|", 1)
    raw = base64.b64decode(encoded_data)
    buffer = io.BytesIO(raw)
    clean_name = filename.strip() or "office-upload.xlsx"

    if clean_name.lower().endswith(".csv"):
        return pd.read_csv(buffer), clean_name
    return pd.read_excel(buffer), clean_name

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

def find_column_contains(df, keywords):
    lowered = [(col, col.strip().lower()) for col in df.columns]
    for keyword in keywords:
        for col, value in lowered:
            if keyword in value:
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

def reminder_candidates(df, status_col, recruiter_col):
    name_col = find_column(df, ["name", "candidate name", "candidate", "full name"])
    phone_col = find_column_contains(df, ["phone", "mobile", "contact"])
    email_col = find_column_contains(df, ["email", "mail"])
    date_col = find_column_contains(df, ["interview date", "schedule date", "scheduled date", "follow up", "followup", "reminder"])
    time_col = find_column_contains(df, ["interview time", "schedule time", "scheduled time"])

    active_status = PENDING_STATUS + NO_SHOW_STATUS + ["HR / Offer Discussion", "Verbal Offer Decline"]
    active_df = df[df[status_col].isin(active_status)].head(300).copy()

    candidates = []
    for idx, row in active_df.iterrows():
        name = str(row.get(name_col, "")).strip() if name_col else ""
        status = str(row.get(status_col, "")).strip()
        recruiter = str(row.get(recruiter_col, "")).strip() if recruiter_col else ""
        phone = str(row.get(phone_col, "")).strip() if phone_col else ""
        email = str(row.get(email_col, "")).strip() if email_col else ""
        due_hint = ""

        if date_col:
            date_value = row.get(date_col, "")
            if pd.notna(date_value) and str(date_value).strip():
                due_hint = str(date_value).strip()
                if time_col:
                    time_value = row.get(time_col, "")
                    if pd.notna(time_value) and str(time_value).strip():
                        due_hint = f"{due_hint} {str(time_value).strip()}"

        label_parts = [part for part in [name or f"Candidate {idx + 1}", status, recruiter] if part]
        detail_parts = [part for part in [phone, email, due_hint] if part]
        candidates.append({
            "id": str(idx),
            "label": " - ".join(label_parts),
            "name": name or f"Candidate {idx + 1}",
            "status": status,
            "recruiter": recruiter,
            "contact": " | ".join(detail_parts),
            "dueHint": due_hint
        })

    return candidates

def render_reminder_center(candidates):
    candidates_json = json.dumps(candidates, ensure_ascii=True).replace("</", "<\\/")
    parent_notifier_script = """
(function () {
    if (window.RecruiterPanelNotify) return;
    const SW_URL = "/reminder-sw.js";

    async function registerWorker() {
        if (!("serviceWorker" in navigator)) {
            return null;
        }
        try {
            const head = await fetch(SW_URL, { method: "HEAD", cache: "no-store" });
            const contentType = head.headers.get("content-type") || "";
            if (!contentType.includes("javascript")) return null;
        } catch (e) {
            return null;
        }
        try {
            const reg = await navigator.serviceWorker.register(SW_URL, { updateViaCache: "none" });
            try {
                await reg.update();
            } catch (e) {}
            return reg;
        } catch (e) {
            return null;
        }
    }

    function iconUrl() {
        return new URL("/app/static/icon.png", window.location.origin).href;
    }

    async function showWithBrowserNotification(payload) {
        const note = new Notification(payload.title || "Recruitment reminder", {
            body: payload.body || "Recruitment reminder due now.",
            icon: iconUrl(),
            tag: (payload.tag || "recruiter-reminder") + "-" + Date.now(),
            requireInteraction: true,
            silent: false
        });
        note.onclick = function () {
            window.focus();
            note.close();
        };
        return true;
    }

    window.RecruiterPanelNotify = {
        permission() {
            if (!("Notification" in window)) return "unsupported";
            return Notification.permission;
        },
        async request() {
            if (!("Notification" in window)) return "unsupported";
            if (Notification.permission === "default") {
                await Notification.requestPermission();
            }
            registerWorker();
            return Notification.permission;
        },
        async show(payload) {
            if (!("Notification" in window)) {
                throw new Error("Notifications are not supported");
            }
            if (Notification.permission === "default") {
                await Notification.requestPermission();
            }
            if (Notification.permission !== "granted") {
                throw new Error("Notification permission is " + Notification.permission);
            }
            const reg = await registerWorker();
            if (reg && reg.showNotification) {
                await reg.showNotification(payload.title || "Recruitment reminder", {
                    body: payload.body || "Recruitment reminder due now.",
                    icon: iconUrl(),
                    badge: iconUrl(),
                    tag: (payload.tag || "recruiter-reminder") + "-" + Date.now(),
                    renotify: true,
                    requireInteraction: true,
                    silent: false,
                    vibrate: [260, 120, 260, 120, 480],
                    timestamp: Date.now(),
                    data: { url: payload.url || "/" }
                });
                return true;
            }
            return showWithBrowserNotification(payload);
        }
    };
})();
"""
    parent_notifier_json = json.dumps(parent_notifier_script, ensure_ascii=True).replace("</", "<\\/")
    components.html(
        f"""
        <div id="reminder-app"></div>
        <style>
        :root {{
            color-scheme: dark;
            --rem-bg: #0b1220;
            --rem-panel: #111a2b;
            --rem-panel-2: #0f1728;
            --rem-line: #263650;
            --rem-text: #eef4ff;
            --rem-muted: #93a4bd;
            --rem-accent: #2ed3a1;
            --rem-warn: #f6b35f;
            --rem-danger: #ff6b72;
        }}
        body {{
            margin: 0;
            background: transparent;
            color: var(--rem-text);
            font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
        }}
        .reminder-wrap {{
            background: linear-gradient(180deg, #121b2d, #0d1424);
            border: 1px solid var(--rem-line);
            border-radius: 10px;
            padding: 14px;
            box-shadow: 0 16px 34px rgba(0, 0, 0, .24);
        }}
        .reminder-head {{
            display: flex;
            align-items: center;
            justify-content: space-between;
            gap: 12px;
            margin-bottom: 12px;
        }}
        .reminder-title {{
            font-size: 18px;
            line-height: 1.2;
            font-weight: 800;
        }}
        .reminder-subtitle {{
            color: var(--rem-muted);
            font-size: 12px;
            margin-top: 4px;
            line-height: 1.45;
        }}
        .reminder-grid {{
            display: grid;
            grid-template-columns: minmax(0, .95fr) minmax(0, 1.05fr);
            gap: 12px;
        }}
        .reminder-card {{
            background: var(--rem-panel-2);
            border: 1px solid var(--rem-line);
            border-radius: 8px;
            padding: 12px;
            min-width: 0;
        }}
        .reminder-field {{
            display: grid;
            gap: 5px;
            margin-bottom: 10px;
        }}
        .reminder-field label {{
            color: var(--rem-muted);
            font-size: 11px;
            font-weight: 750;
            text-transform: uppercase;
        }}
        .reminder-field input,
        .reminder-field textarea,
        .reminder-field select {{
            width: 100%;
            min-height: 38px;
            background: #0a1020;
            color: var(--rem-text);
            border: 1px solid #31415d;
            border-radius: 7px;
            padding: 9px 10px;
            font-size: 13px;
            outline: none;
        }}
        .reminder-field textarea {{
            min-height: 82px;
            resize: vertical;
        }}
        .push-setup {{
            display: grid;
            gap: 10px;
            margin-bottom: 10px;
            border: 1px solid #263650;
            background: #0a1020;
            border-radius: 8px;
            padding: 10px;
        }}
        .push-actions {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }}
        .push-link {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            min-height: 36px;
            padding: 0 12px;
            border-radius: 7px;
            border: 1px solid rgba(46, 211, 161, .55);
            background: #123229;
            color: #eef4ff;
            font-size: 12px;
            font-weight: 800;
            text-decoration: none;
        }}
        .push-qr {{
            width: 126px;
            height: 126px;
            border-radius: 8px;
            background: #fff;
            border: 1px solid #31415d;
        }}
        .push-status {{
            color: var(--rem-muted);
            font-size: 12px;
            line-height: 1.45;
        }}
        .reminder-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            align-items: center;
        }}
        .reminder-btn {{
            border: 1px solid #375071;
            background: #142037;
            color: var(--rem-text);
            border-radius: 7px;
            min-height: 36px;
            padding: 0 12px;
            font-size: 12px;
            font-weight: 800;
            cursor: pointer;
        }}
        .reminder-btn.primary {{
            border-color: rgba(46, 211, 161, .55);
            background: linear-gradient(135deg, #176d60, #1e5f9b);
        }}
        .reminder-btn.danger {{
            border-color: rgba(255, 107, 114, .55);
            background: #331722;
        }}
        .reminder-status {{
            display: inline-flex;
            align-items: center;
            gap: 7px;
            border: 1px solid var(--rem-line);
            background: #0a1020;
            color: var(--rem-muted);
            border-radius: 999px;
            min-height: 34px;
            padding: 0 11px;
            font-size: 12px;
            font-weight: 750;
        }}
        .reminder-dot {{
            width: 8px;
            height: 8px;
            border-radius: 50%;
            background: var(--rem-warn);
        }}
        .reminder-status.ready .reminder-dot {{
            background: var(--rem-accent);
        }}
        .reminder-list {{
            display: grid;
            gap: 8px;
            max-height: 520px;
            overflow: auto;
            padding-right: 2px;
        }}
        .reminder-item {{
            border: 1px solid #263650;
            background: #0a1020;
            border-radius: 8px;
            padding: 10px;
        }}
        .reminder-item-top {{
            display: flex;
            justify-content: space-between;
            gap: 8px;
        }}
        .reminder-item-title {{
            font-size: 13px;
            font-weight: 800;
            line-height: 1.35;
            overflow-wrap: anywhere;
        }}
        .reminder-item-time {{
            color: var(--rem-accent);
            white-space: nowrap;
            font-size: 11px;
            font-weight: 800;
        }}
        .reminder-item-body {{
            color: var(--rem-muted);
            font-size: 12px;
            margin: 5px 0 9px;
            line-height: 1.45;
            overflow-wrap: anywhere;
        }}
        .reminder-empty {{
            color: var(--rem-muted);
            border: 1px dashed #34445f;
            border-radius: 8px;
            padding: 18px;
            text-align: center;
            font-size: 13px;
        }}
        .reminder-pop {{
            position: fixed;
            inset: 12px;
            z-index: 99999;
            display: none;
            place-items: center;
            background: rgba(2, 6, 16, .74);
            backdrop-filter: blur(7px);
        }}
        .reminder-pop.show {{
            display: grid;
        }}
        .reminder-pop-box {{
            width: min(420px, calc(100vw - 28px));
            background: #101827;
            border: 1px solid rgba(46, 211, 161, .45);
            border-radius: 10px;
            padding: 18px;
            box-shadow: 0 24px 80px rgba(0, 0, 0, .5);
        }}
        .reminder-pop-title {{
            font-size: 18px;
            font-weight: 850;
            line-height: 1.25;
        }}
        .reminder-pop-body {{
            color: var(--rem-muted);
            margin: 8px 0 16px;
            line-height: 1.5;
        }}
        @media (max-width: 760px) {{
            body {{
                min-height: 1160px;
                overflow: visible;
            }}
            .reminder-wrap {{
                padding: 11px;
            }}
            .reminder-head {{
                display: grid;
            }}
            .reminder-grid {{
                grid-template-columns: 1fr;
            }}
            .reminder-row .reminder-btn,
            .reminder-row .reminder-status {{
                flex: 1 1 140px;
                justify-content: center;
            }}
            .reminder-list {{
                max-height: none;
                overflow: visible;
            }}
        }}
        </style>
        <script>
        (function () {{
            const CANDIDATES = {candidates_json};
            const PARENT_NOTIFIER_SCRIPT = {parent_notifier_json};
            const KEY = "recruiterAutomation.reminders.v1";
            const FIRED_KEY = "recruiterAutomation.fired.v1";
            const NTFY_TOPIC_KEY = "recruiterAutomation.ntfyTopic.v1";
            const SW_URL = "/reminder-sw.js";
            const root = document.getElementById("reminder-app");
            let audioReady = false;

            function parentNotifier() {{
                try {{
                    const target = window.parent && window.parent !== window ? window.parent : window;
                    if (!target.RecruiterPanelNotify) {{
                        const script = target.document.createElement("script");
                        script.id = "recruiter-panel-notifier";
                        script.textContent = PARENT_NOTIFIER_SCRIPT;
                        (target.document.head || target.document.documentElement).appendChild(script);
                    }}
                    return target.RecruiterPanelNotify || null;
                }} catch (e) {{
                    return null;
                }}
            }}

            function nowLocalValue(minutesAhead) {{
                const date = new Date(Date.now() + minutesAhead * 60000);
                date.setSeconds(0, 0);
                return new Date(date.getTime() - date.getTimezoneOffset() * 60000).toISOString().slice(0, 16);
            }}

            function parseJSON(key, fallback) {{
                try {{
                    return JSON.parse(localStorage.getItem(key) || JSON.stringify(fallback));
                }} catch (e) {{
                    return fallback;
                }}
            }}

            function reminders() {{
                return parseJSON(KEY, []);
            }}

            function saveReminders(items) {{
                localStorage.setItem(KEY, JSON.stringify(items));
            }}

            function firedMap() {{
                return parseJSON(FIRED_KEY, {{}});
            }}

            function saveFired(items) {{
                localStorage.setItem(FIRED_KEY, JSON.stringify(items));
            }}

            function ntfyTopic() {{
                return (localStorage.getItem(NTFY_TOPIC_KEY) || "").trim().replace(/[^a-zA-Z0-9_-]/g, "");
            }}

            function saveNtfyTopic(value) {{
                localStorage.setItem(NTFY_TOPIC_KEY, String(value || "").trim().replace(/[^a-zA-Z0-9_-]/g, ""));
            }}

            async function sendNtfy(item) {{
                const topic = ntfyTopic();
                if (!topic) return false;
                try {{
                    const response = await fetch(`https://ntfy.sh/${{encodeURIComponent(topic)}}`, {{
                        method: "POST",
                        headers: {{
                            "Title": item.title || "Recruitment reminder",
                            "Priority": "high",
                            "Tags": "bell"
                        }},
                        body: item.body || "Recruitment reminder due now."
                    }});
                    return response.ok;
                }} catch (e) {{
                    return false;
                }}
            }}

            function notificationApi() {{
                return window.Notification || (window.parent && window.parent.Notification);
            }}

            function parentWindow() {{
                try {{
                    return window.parent && window.parent !== window ? window.parent : window;
                }} catch (e) {{
                    return window;
                }}
            }}

            function setFramePermissions() {{
                try {{
                    const doc = window.parent.document;
                    Array.from(doc.querySelectorAll("iframe")).forEach((frame) => {{
                        if (frame.contentWindow !== window) return;
                        const allow = frame.getAttribute("allow") || "";
                        const parts = allow.split(";").map((item) => item.trim()).filter(Boolean);
                        ["notifications", "autoplay", "clipboard-write"].forEach((item) => {{
                            if (!parts.includes(item)) parts.push(item);
                        }});
                        frame.setAttribute("allow", parts.join("; "));
                    }});
                }} catch (e) {{}}
            }}

            function permission() {{
                const notifier = parentNotifier();
                if (notifier && notifier.permission) return notifier.permission();
                const api = notificationApi();
                return api ? api.permission : "unsupported";
            }}

            function escapeText(value) {{
                return String(value || "").replace(/[&<>"']/g, function (ch) {{
                    return {{ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }}[ch];
                }});
            }}

            async function registerWorker() {{
                const nav = window.parent && window.parent.navigator ? window.parent.navigator : navigator;
                if (!("serviceWorker" in nav)) return null;
                try {{
                    const reg = await nav.serviceWorker.register(SW_URL, {{ updateViaCache: "none" }});
                    try {{ await reg.update(); }} catch (e) {{}}
                    return reg;
                }} catch (e) {{
                    return null;
                }}
            }}

            function tone() {{
                if (!audioReady) return;
                try {{
                    const AudioContext = window.AudioContext || window.webkitAudioContext;
                    if (!AudioContext) return;
                    const ctx = new AudioContext();
                    const osc = ctx.createOscillator();
                    const gain = ctx.createGain();
                    osc.type = "sine";
                    osc.frequency.value = 880;
                    gain.gain.setValueAtTime(0.0001, ctx.currentTime);
                    gain.gain.exponentialRampToValueAtTime(0.16, ctx.currentTime + 0.02);
                    gain.gain.exponentialRampToValueAtTime(0.0001, ctx.currentTime + 0.55);
                    osc.connect(gain);
                    gain.connect(ctx.destination);
                    osc.start();
                    osc.stop(ctx.currentTime + 0.58);
                }} catch (e) {{}}
            }}

            function vibrate() {{
                const nav = window.parent && window.parent.navigator ? window.parent.navigator : navigator;
                if (nav.vibrate) nav.vibrate([220, 90, 220, 90, 420]);
            }}

            async function requestPermission() {{
                audioReady = true;
                setFramePermissions();
                const notifier = parentNotifier();
                if (notifier && notifier.request) {{
                    const result = await notifier.request();
                    render();
                    return result;
                }}
                await registerWorker();
                const api = notificationApi();
                if (!api) {{
                    render();
                    return "unsupported";
                }}
                if (api.permission === "default") {{
                    try {{
                        await api.requestPermission();
                    }} catch (e) {{}}
                }}
                render();
                return api.permission;
            }}

            async function showSystemNotification(item) {{
                try {{
                    const notifier = parentNotifier();
                    if (!notifier || !notifier.show) return false;
                    await notifier.show({{
                        title: item.title || "Recruitment reminder",
                        body: item.body || "Recruitment reminder due now.",
                        tag: "recruiter-reminder-" + item.id + "-" + Date.now(),
                        url: "/"
                    }});
                    return true;
                }} catch (e) {{
                    return false;
                }}
            }}

            function showPopup(item) {{
                const pop = document.getElementById("reminder-pop");
                if (!pop) return;
                pop.querySelector(".reminder-pop-title").textContent = item.title || "Recruitment reminder";
                pop.querySelector(".reminder-pop-body").textContent = item.body || "Reminder due now.";
                pop.classList.add("show");
                vibrate();
                tone();
            }}

            async function fire(item) {{
                const fired = firedMap();
                if (fired[item.id]) return;
                fired[item.id] = new Date().toISOString();
                saveFired(fired);
                const ntfySent = await sendNtfy(item);
                const shown = await showSystemNotification(item);
                if (!ntfySent && !shown) showPopup(item);
                render();
            }}

            function dueLabel(value) {{
                const date = new Date(value);
                if (Number.isNaN(date.getTime())) return "Invalid time";
                return date.toLocaleString([], {{ dateStyle: "medium", timeStyle: "short" }});
            }}

            function checkDue() {{
                const items = reminders();
                const fired = firedMap();
                const current = Date.now();
                items.forEach((item) => {{
                    const due = new Date(item.dueAt).getTime();
                    if (!item.done && !fired[item.id] && !Number.isNaN(due) && due <= current) {{
                        fire(item);
                    }}
                }});
            }}

            function addReminder() {{
                audioReady = true;
                const title = document.getElementById("rem-title").value.trim();
                const body = document.getElementById("rem-body").value.trim();
                const dueAt = document.getElementById("rem-due").value;
                if (!title || !dueAt) {{
                    alert("Add a title and reminder time.");
                    return;
                }}
                const items = reminders();
                items.push({{
                    id: String(Date.now()) + "-" + Math.random().toString(16).slice(2),
                    title,
                    body,
                    dueAt: new Date(dueAt).toISOString(),
                    done: false,
                    createdAt: new Date().toISOString()
                }});
                saveReminders(items);
                document.getElementById("rem-title").value = "";
                document.getElementById("rem-body").value = "";
                document.getElementById("rem-due").value = nowLocalValue(30);
                render();
            }}

            function useCandidate() {{
                const selected = CANDIDATES[Number(document.getElementById("rem-candidate").value)];
                if (!selected) return;
                document.getElementById("rem-title").value = "Follow up: " + selected.name;
                document.getElementById("rem-body").value = [
                    selected.status ? "Status: " + selected.status : "",
                    selected.recruiter ? "Owner: " + selected.recruiter : "",
                    selected.contact ? selected.contact : "",
                    selected.dueHint ? "Tracker time: " + selected.dueHint : ""
                ].filter(Boolean).join("\\n");
            }}

            function quick(minutes) {{
                document.getElementById("rem-due").value = nowLocalValue(minutes);
            }}

            function removeReminder(id) {{
                saveReminders(reminders().filter((item) => item.id !== id));
                const fired = firedMap();
                delete fired[id];
                saveFired(fired);
                render();
            }}

            function markDone(id) {{
                saveReminders(reminders().map((item) => item.id === id ? {{ ...item, done: true }} : item));
                render();
            }}

            function testReminder() {{
                audioReady = true;
                saveNtfyTopic(document.getElementById("ntfy-topic").value);
                const testItem = {{
                    id: "test-" + Date.now(),
                    title: "Test recruitment reminder",
                    body: "This is a sample reminder in your phone notification panel.",
                    dueAt: new Date().toISOString()
                }};
                sendNtfy(testItem).then((sent) => {{
                    const status = document.getElementById("ntfy-status");
                    if (status) {{
                        status.textContent = sent
                            ? "Sent to ntfy. Check the phone subscribed to this topic."
                            : "Enter the same ntfy topic your phone is subscribed to.";
                    }}
                }});
                requestPermission().then(() => {{
                    showSystemNotification(testItem).then((shown) => {{
                        if (!shown) {{
                            showPopup({{
                                title: "Test sent",
                                body: ntfyTopic() ? "Check ntfy on your phone." : "Enter your ntfy topic first."
                            }});
                        }}
                    }});
                }});
            }}

            function statusHtml() {{
                const perm = permission();
                const ready = perm === "granted";
                const text = perm === "granted"
                    ? "Notifications ready"
                    : perm === "denied"
                        ? "Notifications blocked"
                        : perm === "unsupported"
                            ? "Notifications unsupported"
                            : "Permission needed";
                return `<span class="reminder-status ${{ready ? "ready" : ""}}"><span class="reminder-dot"></span>${{text}}</span>`;
            }}

            function renderList() {{
                const fired = firedMap();
                const items = reminders()
                    .slice()
                    .sort((a, b) => new Date(a.dueAt).getTime() - new Date(b.dueAt).getTime());
                if (!items.length) {{
                    return '<div class="reminder-empty">No reminders yet. Add one for follow-up calls, interview confirmations, or offer closure.</div>';
                }}
                return items.map((item) => {{
                    const isFired = Boolean(fired[item.id]);
                    const done = item.done || isFired;
                    return `
                    <div class="reminder-item">
                        <div class="reminder-item-top">
                            <div class="reminder-item-title">${{escapeText(item.title)}}</div>
                            <div class="reminder-item-time">${{escapeText(dueLabel(item.dueAt))}}</div>
                        </div>
                        <div class="reminder-item-body">${{escapeText(item.body || (done ? "Completed" : "Pending")).replace(/\\n/g, "<br>")}}</div>
                        <div class="reminder-row">
                            ${{done ? "" : `<button class="reminder-btn" data-done="${{item.id}}">Done</button>`}}
                            <button class="reminder-btn danger" data-remove="${{item.id}}">Delete</button>
                        </div>
                    </div>`;
                }}).join("");
            }}

            function render() {{
                root.innerHTML = `
                <div class="reminder-wrap">
                    <div class="reminder-head">
                        <div>
                            <div class="reminder-title">Realtime Recruiter Reminders</div>
                            <div class="reminder-subtitle">Keep this app open or install it on mobile for the strongest browser notification behavior.</div>
                        </div>
                        <div class="reminder-row">
                            ${{statusHtml()}}
                            <button id="rem-permission" class="reminder-btn primary">Allow</button>
                            <button id="rem-test" class="reminder-btn">Test</button>
                        </div>
                    </div>
                    <div class="reminder-grid">
                        <div class="reminder-card">
                            <div class="reminder-field">
                                <label>ntfy Topic</label>
                                <input id="ntfy-topic" value="${{escapeText(ntfyTopic())}}" placeholder="Same topic subscribed on phone">
                            </div>
                            <div id="ntfy-status" class="reminder-item-body">Install/open ntfy on phone, subscribe to this same topic, then Test.</div>
                            <div class="reminder-field">
                                <label>Candidate</label>
                                <select id="rem-candidate">
                                    <option value="">Manual reminder</option>
                                    ${{CANDIDATES.map((candidate, index) => `<option value="${{index}}">${{escapeText(candidate.label)}}</option>`).join("")}}
                                </select>
                            </div>
                            <div class="reminder-field">
                                <label>Title</label>
                                <input id="rem-title" placeholder="Call candidate / confirm interview">
                            </div>
                            <div class="reminder-field">
                                <label>Details</label>
                                <textarea id="rem-body" placeholder="Candidate, status, phone, meeting link, next action"></textarea>
                            </div>
                            <div class="reminder-field">
                                <label>Reminder Time</label>
                                <input id="rem-due" type="datetime-local" value="${{nowLocalValue(30)}}">
                            </div>
                            <div class="reminder-row">
                                <button class="reminder-btn" data-quick="5">5 min</button>
                                <button class="reminder-btn" data-quick="15">15 min</button>
                                <button class="reminder-btn" data-quick="60">1 hour</button>
                                <button id="rem-add" class="reminder-btn primary">Save Reminder</button>
                            </div>
                        </div>
                        <div class="reminder-card">
                            <div class="reminder-list">${{renderList()}}</div>
                        </div>
                    </div>
                </div>
                <div id="reminder-pop" class="reminder-pop">
                    <div class="reminder-pop-box">
                        <div class="reminder-pop-title"></div>
                        <div class="reminder-pop-body"></div>
                        <div class="reminder-row">
                            <button id="rem-pop-close" class="reminder-btn primary">Dismiss</button>
                        </div>
                    </div>
                </div>`;

                document.getElementById("rem-permission").addEventListener("click", requestPermission);
                document.getElementById("rem-test").addEventListener("click", testReminder);
                document.getElementById("rem-add").addEventListener("click", addReminder);
                document.getElementById("ntfy-topic").addEventListener("input", (event) => saveNtfyTopic(event.target.value));
                document.getElementById("rem-candidate").addEventListener("change", useCandidate);
                document.getElementById("rem-pop-close").addEventListener("click", () => {{
                    document.getElementById("reminder-pop").classList.remove("show");
                }});
                root.querySelectorAll("[data-quick]").forEach((btn) => btn.addEventListener("click", () => quick(Number(btn.dataset.quick))));
                root.querySelectorAll("[data-remove]").forEach((btn) => btn.addEventListener("click", () => removeReminder(btn.dataset.remove)));
                root.querySelectorAll("[data-done]").forEach((btn) => btn.addEventListener("click", () => markDone(btn.dataset.done)));
            }}

            render();
            setFramePermissions();
            registerWorker();
            setInterval(checkDue, 10000);
            document.addEventListener("visibilitychange", checkDue);
            window.addEventListener("storage", render);
            window.addEventListener("focus", checkDue);
            window.addEventListener("focus", render);
            checkDue();
        }})();
        </script>
        """,
        height=1180,
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

encoded_df = None
encoded_filename = None
if "encoded_upload" in st.session_state and st.session_state.encoded_upload.strip():
    try:
        encoded_df, encoded_filename = load_encoded_file(st.session_state.encoded_upload)
    except Exception:
        st.error("Encoded file could not be read. Copy the full encoded text and paste again.")

if encoded_df is not None:
    df = encoded_df
    dataset_name = encoded_filename

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
            <div class="value">{html.escape(str(dataset_name))}</div>
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

    tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
        "Main Counts",
        "Exact Status Counts",
        "Recruiter Wise",
        "Pending",
        "Rejected / Dropped / No Show",
        "Search Full Data",
        "Lead Review",
        "Reminders"
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

    with tab8:
        st.subheader("Realtime Mobile Browser Reminders")
        render_reminder_center(reminder_candidates(df, status_col, recruiter_col))

else:
    st.info("Waiting for a file to generate counts.")
