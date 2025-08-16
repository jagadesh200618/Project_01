import streamlit as st
from calculator import Calculator
st.text_input("Enter", key="name")

st.button("Submit", on_click=print())

st.session_state.name

# 23 + 34 + 44 - 67 / (34 * 35)
# BODMAS

def InputString(inp: str):
    c = Calculator()
    text = list(map(lambda x: x.strip(), inp.split("+")))
    print(text)


InputString("23 + 34 + 44 - 67 / (34 * 35)")
