import streamlit as st

# Page Configuration
st.set_page_config(page_title="Python Learning Hub", page_icon="🐍", layout="wide")

# Custom CSS for Cyberpunk / Tech Vibe
st.markdown("""
    <style>
    .main-title { font-size: 40px; font-weight: bold; color: #00ffcc; text-shadow: 2px 2px #000; }
    .section-box { padding: 15px; border-radius: 10px; background-color: #1e1e2f; border: 1px solid #00ffcc; margin-bottom: 15px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">🐍 Interactive Python Learning Hub</div>', unsafe_allow_html=True)
st.write("Welcome! Is interactive dashboard ki madad se aap Python ke core concepts ko aasani se seekh sakte hain.")

# Sidebar Navigation
st.sidebar.header("Navigation")
topic = st.sidebar.radio("Go to Topic:", [
    "1. Introduction & Basics", 
    "2. Data Types & Operators", 
    "3. Control Flow (Loops & Conditionals)", 
    "4. Functions & Modules",
    "5. Object-Oriented Programming (OOPs)"
])

# ---- TOPIC 1: BASICS ----
if topic == "1. Introduction & Basics":
    st.header("Introduction to Python")
    st.write("Python ek high-level, interpreted aur bohot hi simple programming language hai.")
    
    st.subheader("Your First Python Code")
    st.code('print("Hello, World!")', language="python")
    
    st.subheader("Variables")
    st.write("Python me variables ko declare karne ke liye kisi data type ko likhne ki zaroorat nahi hoti.")
    st.code('x = 5\nname = "Naina"\nprint(type(x))  # Output: <class \'int\'>', language="python")

# ---- TOPIC 2: DATA TYPES ----
elif topic == "2. Data Types & Operators":
    st.header("Data Types & Operators")
    
    tab1, tab2 = st.tabs(["Core Data Types", "Operators"])
    
    with tab1:
        st.markdown("""
        * **Integer / Float:** `x = 10`, `y = 10.5`
        * **String:** `text = "Python"`
        * **List (Mutable):** `my_list =`
        * **Tuple (Immutable):** `my_tuple = (1, 2, 3)`
        * **Dictionary:** `my_dict = {"key": "value"}`
        """)
        
    with tab2:
        st.write("Basic Arithmetic Operators:")
        st.code('add = 5 + 3  # 8\npow = 2 ** 3 # 8 (Power)', language="python")

# ---- TOPIC 3: CONTROL FLOW ----
elif topic == "3. Control Flow (Loops & Conditionals)":
    st.header("Control Flow")
    
    st.subheader("If-Else Condition")
    st.code("""
age = 18
if age >= 18:
    print("You can vote!")
else:
    print("Wait for it.")
    """, language="python")
    
    st.subheader("Loops")
    st.write("**For Loop Example:**")
    st.code("""
for i in range(3):
    print(f"Loop count: {i}")
    """, language="python")

# ---- TOPIC 4: FUNCTIONS ----
elif topic == "4. Functions & Modules":
    st.header("Functions & Modules")
    st.write("Code reusability ke liye hum functions banate hain.")
    
    st.code("""
def greet(name):
    return f"Hello, {name}!"

# Function Call
print(greet("Learner"))
    """, language="python")

# ---- TOPIC 5: OOPS ----
elif topic == "5. Object-Oriented Programming (OOPs)":
    st.header("Object-Oriented Programming (OOPs)")
    st.write("Python ek object-oriented language hai jo Classes aur Objects par kaam karti hai.")
    
    st.code("""
class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
        
    def display_info(self):
        return f"Student: {self.name} | Branch: {self.branch}"

# Object Creation
s1 = Student("Naina", "CSE")
print(s1.display_info())
    """, language="python")
