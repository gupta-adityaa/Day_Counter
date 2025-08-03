import streamlit as st
from datetime import date

st.set_page_config(page_title="Multi Day Counter", page_icon="📅")
st.title("📆 Multi Day Counter App")

# Initialize session state for counters
if "counters" not in st.session_state:
    st.session_state.counters = []

# Add new counter
with st.form("add_counter"):
    st.subheader("➕ Add New Counter")
    title = st.text_input("Title", placeholder="e.g. Project Start, Anniversary, Exam Countdown")
    start_date = st.date_input("Select Date", value=date.today())
    submitted = st.form_submit_button("Add Counter")

    if submitted:
        if title.strip() == "":
            st.warning("Please enter a title for the counter.")
        else:
            st.session_state.counters.append({
                "title": title,
                "start_date": start_date
            })
            st.success(f"Added counter: {title}")

st.markdown("---")

# Display all counters
st.subheader("📋 Your Counters")

if not st.session_state.counters:
    st.info("No counters added yet.")
else:
    for idx, counter in enumerate(st.session_state.counters):
        col1, col2 = st.columns([4, 1])
        with col1:
            today = date.today()
            delta = (today - counter["start_date"]).days
            if delta >= 0:
                st.success(f"**{counter['title']}**: {delta} days since {counter['start_date']}")
            else:
                st.info(f"**{counter['title']}**: {abs(delta)} days until {counter['start_date']}")
        with col2:
            if st.button("❌", key=f"delete_{idx}"):
                st.session_state.counters.pop(idx)
                st.experimental_rerun()
