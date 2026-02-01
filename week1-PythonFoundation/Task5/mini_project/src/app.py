import streamlit as st

st.set_page_config(page_title="Calculator", layout="centered")
st.title("Calculator")

# Initialize session state
if "expression" not in st.session_state:
    st.session_state.expression = ""

# Create a placeholder for the display - we'll fill it AFTER buttons run
display_placeholder = st.empty()

# Button handlers
def press(value):
    if st.session_state.expression == "Error" or st.session_state.expression == "Can't divide by zero":
        st.session_state.expression = ""
    st.session_state.expression += str(value)

def clear():
    st.session_state.expression = ""

def backspace():
    st.session_state.expression = st.session_state.expression[:-1]

def calculate():
    try:
        st.session_state.expression = str(eval(st.session_state.expression))
    except ZeroDivisionError:
        st.session_state.expression = "Can't divide by zero"
    except:
        st.session_state.expression = "Error"

# Buttons layout
buttons = [
    ["C", "⌫", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "", ""],
]

for row in buttons:
    cols = st.columns(4)
    for i, btn in enumerate(row):
        if btn == "":
            continue
        elif btn == "=":
            if cols[i].button("="):
                calculate()
        elif btn == "C":
            if cols[i].button("C"):
                clear()
        elif btn == "⌫":
            if cols[i].button("⌫"):
                backspace()
        else:
            if cols[i].button(btn):
                press(btn)

# NOW fill the display AFTER all buttons have run
# This way it always shows the latest value
display_placeholder.text_area(" ", value=st.session_state.expression, disabled=True, height=80)