import streamlit as st

# FORCE CACHE CLEAR
st.cache_data.clear()
st.cache_resource.clear()

st.set_page_config(layout="wide")
st.title("🤖 Agent Architect - DEBUG MODE")

# SHOW YOUR INPUT
spec = st.text_input("Your input:", "Type anything here")
st.write(f"🔍 You typed: **{spec}**")

if st.button("TEST"):
    if "FastAPI" in spec:
        st.success("✅ DETECTED: FastAPI API")
        st.code("from fastapi import FastAPI")
    elif "Streamlit" in spec or "dashboard" in spec:
        st.success("✅ DETECTED: Streamlit Dashboard") 
        st.code("import streamlit as st")
    else:
        st.success("✅ DETECTED: Custom App")
        st.code(f"# App for: {spec}")

st.write("**If you see your input above + correct detection = WORKING!**")
