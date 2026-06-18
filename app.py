import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
from io import BytesIO
from datetime import datetime

st.set_page_config(page_title="Recruitment Count Dashboard", page_icon=":clipboard:", layout="wide")

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

.topbox:after {
    content: "KNIGHT UI";
    position: absolute;
    right: 24px;
    top: 22px;
    color: var(--gold);
    font-size: 10px;
    font-weight: 800;
    letter-spacing: 1.8px;
}

.topbox h1 {
    color: var(--text) !important;
    font-size: 22px !important;
    font-weight: 850 !important;
    margin: 0;
    line-height: 1.2;
}

.topbox p {
    max-width: 800px;
    font-size: 12px !important;
    color: var(--muted) !important;
    margin: 8px 0 0;
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
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: .75px;
    line-height: 1.3;
}

.num {
    font-size: 28px;
    font-weight: 900;
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
    font-weight: 800;
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
    font-weight: 850 !important;
    letter-spacing: 0;
}

h2, h3 {
    margin-top: 0.15rem;
    font-size: 18px !important;
    line-height: 1.25;
}

[data-testid="stMarkdownContainer"] p {
    font-size: 12px;
}

/* TABLE */
[data-testid="stDataFrame"] {
    border-radius: 10px;
    overflow: hidden;
    border: 1px solid var(--line);
    box-shadow: 0 10px 28px rgba(0, 0, 0, 0.20);
}

[data-testid="stDataFrame"] * {
    font-size: 11px !important;
}

[data-testid="stDataFrame"] div[role="grid"] {
    background: #0b1220 !important;
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

/* BUTTON */
.stDownloadButton button {
    width: 100%;
    background: linear-gradient(180deg, #c7a45d, #9e7b33);
    color: #080b12;
    border: 1px solid #e1c985;
    border-radius: 10px;
    padding: 12px 20px;
    font-size: 12px;
    font-weight: 850;
    box-shadow: 0 16px 34px rgba(0, 0, 0, 0.28);
}

.stDownloadButton button:hover {
    background: linear-gradient(180deg, #d6b66d, #ad873d);
    color: #080b12;
    border: 1px solid #e1c985;
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
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="topbox">
<h1>Recruitment Excel Automation</h1>
<p><strong>Production dashboard</strong> for exact recruitment counts, status movement, recruiter performance, pending action, rejection, drop, no-show, and final Excel reporting.</p>
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

def create_excel(df, summary, status_report, recruiter, pending, rejected, dropped, noshow):
    output = BytesIO()

    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        summary.to_excel(writer, sheet_name="Main Summary", index=False)
        status_report.to_excel(writer, sheet_name="Status Counts", index=False)
        recruiter.to_excel(writer, sheet_name="Recruiter Report", index=False)
        pending.to_excel(writer, sheet_name="Pending Candidates", index=False)
        rejected.to_excel(writer, sheet_name="Rejected Candidates", index=False)
        dropped.to_excel(writer, sheet_name="Dropped Candidates", index=False)
        noshow.to_excel(writer, sheet_name="No Show Candidates", index=False)
        df.to_excel(writer, sheet_name="Full Clean Data", index=False)

        workbook = writer.book
        head = workbook.add_format({
            "bold": True,
            "font_color": "white",
            "bg_color": "#111827",
            "border": 1,
            "align": "center"
        })
        cell = workbook.add_format({"border": 1, "align": "center"})
        title = workbook.add_format({"bold": True, "font_size": 18, "font_color": "#111827"})

        for ws in writer.sheets.values():
            ws.set_row(0, 25, head)
            ws.set_column(0, 60, 22)

        dash = workbook.add_worksheet("Dashboard")
        dash.write("A1", "Recruitment Automation Dashboard", title)
        dash.write("A3", "Generated On", head)
        dash.write("B3", datetime.now().strftime("%d-%m-%Y %I:%M %p"), cell)

        dash.write("A5", "Metric", head)
        dash.write("B5", "Count", head)

        row = 5
        for _, r in summary.iterrows():
            dash.write(row, 0, r["Metric"], cell)
            dash.write(row, 1, int(r["Count"]), cell)
            row += 1

        dash.write("D5", "Status", head)
        dash.write("E5", "Count", head)

        row = 5
        for _, r in status_report.iterrows():
            dash.write(row, 3, r["Status"], cell)
            dash.write(row, 4, int(r["Count"]), cell)
            row += 1

        dash.set_column("A:E", 28)

    output.seek(0)
    return output

if uploaded_file:
    df = load_file(uploaded_file)
    df = clean_df(df)

    status_col = find_column(df, ["status", "candidate status", "current status"])
    recruiter_col = find_column(df, ["recruiter", "hr", "owner", "assigned to"])

    if not status_col:
        st.error("Status column not found in uploaded Excel.")
        st.stop()

    total = len(df)

    status_report = count_status(df, status_col)
    summary = make_summary(status_report, total)
    recruiter = recruiter_report(df, recruiter_col, status_col)

    pending = df[df[status_col].isin(PENDING_STATUS)]
    rejected = df[df[status_col].isin(REJECT_STATUS)]
    dropped = df[df[status_col].isin(DROP_STATUS)]
    noshow = df[df[status_col].isin(NO_SHOW_STATUS)]

    m = dict(zip(summary["Metric"], summary["Count"]))

    c1, c2, c3, c4, c5, c6 = st.columns(6, gap="small")
    cards = [
        ("Total Candidates", m["Total Candidates"]),
        ("Yet To Schedule", m["Yet To Schedule"]),
        ("Scheduled", m["Scheduled"]),
        ("Rejected", m["Rejected"]),
        ("Dropped", m["Dropped"]),
        ("Joined", m["Joined"])
    ]

    card_classes = [
        "card-total",
        "card-yts",
        "card-sch",
        "card-rej",
        "card-drop",
        "card-join"
    ]

    for col, (label, value), cls in zip([c1, c2, c3, c4, c5, c6], cards, card_classes):
        with col:
            display_value = f"{int(value):,}"
            st.markdown(f"""
            <div class="card {cls}">
                <div class="lbl">{label}</div>
                <div class="num">{display_value}</div>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Main Counts",
        "Exact Status Counts",
        "Recruiter Wise",
        "Pending",
        "Rejected / Dropped / No Show",
        "Search Full Data"
    ])

    with tab1:
        st.subheader("Main Count Summary")
        st.dataframe(summary, use_container_width=True, hide_index=True)

    with tab2:
        st.subheader("Exact Status Wise Counts")
        st.dataframe(status_report, use_container_width=True, hide_index=True)

    with tab3:
        st.subheader("Recruiter Wise Count Report")
        st.dataframe(recruiter, use_container_width=True, hide_index=True)

    with tab4:
        st.subheader("Pending / Scheduled / Action Required Candidates")
        st.dataframe(pending, use_container_width=True, hide_index=True)

    with tab5:
        a, b, c = st.tabs(["Rejected", "Dropped", "No Show"])

        with a:
            st.write(f"Total Rejected: {len(rejected)}")
            st.dataframe(rejected, use_container_width=True, hide_index=True)

        with b:
            st.write(f"Total Dropped: {len(dropped)}")
            st.dataframe(dropped, use_container_width=True, hide_index=True)

        with c:
            st.write(f"Total No Show: {len(noshow)}")
            st.dataframe(noshow, use_container_width=True, hide_index=True)

    with tab6:
        st.subheader("Search and Filter Full Data")

        all_status = sorted(df[status_col].dropna().unique().tolist())

        selected_status = st.multiselect("Filter by Status", all_status)
        search_text = st.text_input("Search anything: name, email, phone, skill, recruiter, location")

        filtered = filter_table(df, status_col, selected_status, search_text)

        st.write(f"Showing {len(filtered)} records")
        st.dataframe(filtered, use_container_width=True, hide_index=True)

    excel_file = create_excel(df, summary, status_report, recruiter, pending, rejected, dropped, noshow)

    st.download_button(
        "Download Complete Excel Report",
        data=excel_file,
        file_name="recruitment_count_report.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

else:
    st.info("Upload your Excel file to see all counts in browser.")
