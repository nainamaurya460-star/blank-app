import streamlit as st

# --- CONFIG & STYLING ---
st.set_page_config(page_title="Python Mastery Hub", page_icon="🐍", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size: 42px; font-weight: bold; color: #00ffcc; text-align: center; text-shadow: 2px 2px #000; margin-bottom: 20px; }
    .phase-header { background: linear-gradient(90deg, #00ffcc, #333); color: #000; padding: 10px; border-radius: 5px; font-size: 24px; font-weight: bold; margin-top: 30px; margin-bottom: 15px; }
    .sub-header { color: #ff007f; font-size: 20px; font-weight: bold; margin-top: 15px; }
    .example-box { padding: 12px; border-radius: 8px; background-color: #1e1e2f; border-left: 5px solid #00ffcc; margin-bottom: 15px; }
    .practice-box { background-color: #261b3d; border: 1px dashed #ff007f; padding: 15px; border-radius: 10px; margin-top: 20px; }
    stCodeBlock { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">⚡ Ultimate Python Learning Bootcamp ⚡</div>', unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.image("https://img.icons8.com/color/144/000000/python--v1.png", width=90)
st.sidebar.title("Navigation")

phase = st.sidebar.selectbox("Choose Phase:", [
    "Phase 1: The Basics",
    "Phase 2: Data Structures & Functions",
    "Phase 3: Intermediate Python",
    "Phase 4: Advanced Python"
])

# ==========================================
# PHASE 1: THE BASICS
# ==========================================
if phase == "Phase 1: The Basics":
    topic = st.sidebar.radio("Select Topic:", [
        "Intro & Setup", "Variables & Data Types", "Type Casting", "Operators", "Conditional Statements", "Loops & Control"
    ])

    if topic == "Intro & Setup":
        st.markdown('<div class="phase-header">Introduction & Setup</div>', unsafe_allow_html=True)
        st.write("Python ko use karne ke liye aapko official website se ise install karna hota hai. Aap VS Code ya Jupyter Notebook jaise IDEs ka use kar sakte hain.")
        st.markdown('<div class="sub-header">Examples:</div>', unsafe_allow_html=True)
        st.code('print("Hello, World!")', language="python")
        st.code('print("Welcome to Naina\'s Python Hub")', language="python")
        st.code('print(5 + 10)  # Direct Math evaluation', language="python")
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Apna naam aur course 3 alag lines mein print karein.<br>2. Ek simple calculation (multiplication) print statement ke andar karke dikhayein.</div>', unsafe_allow_html=True)

    elif topic == "Variables & Data Types":
        st.markdown('<div class="phase-header">Variables & Data Types</div>', unsafe_allow_html=True)
        st.write("Variables data store karne ke liye use hote hain. Python dynamic hai, isliye type batana nahi padta.")
        st.markdown('<div class="sub-header">Examples:</div>', unsafe_allow_html=True)
        st.code('age = 20  # int\npi = 3.14  # float\nname = "Naina"  # str\nis_student = True  # bool', language="python")
        st.code('print(type(name))  # Output: <class \'str\'>', language="python")
        st.code('a = b = c = 100  # Multiple variables assign karna', language="python")
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Teen variables banayein aur unhe ek single print statement mein check karein.<br>2. Kisi variable ka data type runtime par print karke dekhein.</div>', unsafe_allow_html=True)

    elif topic == "Type Casting":
        st.markdown('<div class="phase-header">Type Casting in Python</div>', unsafe_allow_html=True)
        st.write("Jab ek data type ko forcefully doosre type mein badla jata hai (jaise string ko integer mein), use Type Casting kehte hain.")
        st.markdown('<div class="sub-header">Examples:</div>', unsafe_allow_html=True)
        st.code('num_str = "10"\nnum_int = int(num_str)  # String to Int', language="python")
        st.code('val = float(5)  # Int to Float -> 5.0', language="python")
        st.code('age = 21\nmsg = "My age is " + str(age)  # Int to String for concatenation', language="python")
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. User se do string inputs lein ("20" aur "30"), unhe integers mein badlein aur unka sum nikalen.<br>2. Ek float number ko integer mein badal kar check karein ki decimal points ka kya hota hai.</div>', unsafe_allow_html=True)

    elif topic == "Operators":
        st.markdown('<div class="phase-header">Operators (Arithmetic, Logical, Comparison)</div>', unsafe_allow_html=True)
        st.write("Operators ka use values aur variables par operations perform karne ke liye hota hai.")
        st.markdown('<div class="sub-header">Examples:</div>', unsafe_allow_html=True)
        st.code('res = 10 // 3  # Floor Division (Returns 3)\npow = 2 ** 3  # Power Operator (8)', language="python")
        st.code('is_equal = (5 == 5)  # Comparison (True)', language="python")
        st.code('check = (5 > 2) and (3 < 1)  # Logical AND (False)', language="python")
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Assignment operator (`+=`) ka use karke ek counter variable ko 5 se badhayein.<br>2. Identity operator (`is`) aur Membership operator (`in`) ka ek example likhen.</div>', unsafe_allow_html=True)

    elif topic == "Conditional Statements":
        st.markdown('<div class="phase-header">Conditional Statements (if, elif, else)</div>', unsafe_allow_html=True)
        st.write("Decision making ke liye conditionals ka use hota hai. Python mein indentation ka khas dhyan rakha jata hai.")
        st.markdown('<div class="sub-header">Examples:</div>', unsafe_allow_html=True)
        st.code('marks = 85\nif marks >= 90:\n    print("A")\nelif marks >= 75:\n    print("B")\nelse:\n    print("C")', language="python")
        st.code('num = 10\nmsg = "Even" if num % 2 == 0 else "Odd"  # Ternary Operator', language="python")
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. User se age input lein aur check karein ki wo vote dene ke liye eligible hai ya nahi.<br>2. Ek nested if statement likhein jo number positive hai ya negative, aur even hai ya odd, dono check kare.</div>', unsafe_allow_html=True)

    elif topic == "Loops & Control":
        st.markdown('<div class="phase-header">Loops & Loop Control (for, while, break, continue, pass)</div>', unsafe_allow_html=True)
        st.write("Code ko repeat karne ke liye loops ka aur unhe custom control karne ke liye break, continue aur pass ka use hota hai.")
        st.markdown('<div class="sub-header">Examples:</div>', unsafe_allow_html=True)
        st.code('for i in range(1, 6):\n    if i == 3: continue  # 3 skip ho jayega\n    print(i)', language="python")
        st.code('count = 0\nwhile count < 3:\n    print(count)\n    count += 1', language="python")
        st.code('def future_function():\n    pass  # Future code ke liye placeholder', language="python")
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. While loop ka use karke 10 se 1 tak reverse counting print karein.<br>2. Ek loop banayein jo numbers print kare par jaise hi koi number 7 se divide ho, loop break ho jaye.</div>', unsafe_allow_html=True)

# ==========================================
# PHASE 2: DATA STRUCTURES & FUNCTIONS
# ==========================================
elif phase == "Phase 2: Data Structures & Functions":
    topic = st.sidebar.radio("Select Topic:", [
        "Lists & Tuples", "Dictionaries & Sets", "Functions & Scope", "Lambda & Comprehensions", "String Manipulation"
    ])

    if topic == "Lists & Tuples":
        st.markdown('<div class="phase-header">Lists & Tuples (Mutable vs Immutable)</div>', unsafe_allow_html=True)
        st.markdown('<div class="sub-header">Examples:</div>', unsafe_allow_html=True)
        st.code('fruits = ["apple", "banana"]; fruits.append("mango")  # List is mutable', language="python")
        st.code('coordinates = (10.5, 20.3)  # Tuple is immutable', language="python")
        st.code('sub_list = fruits[0:2]  # Slicing syntax', language="python")
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Ek list banayein, use reverse karein aur uske second element ko delete karein.<br>2. Ek tuple ke andar list dalkar dekhein ki kya us list ko badla ja sakta hai.</div>', unsafe_allow_html=True)

    elif topic == "Dictionaries & Sets":
       elif topic == "Dictionaries & Sets":
        st.markdown('<div class="phase-header">Dictionaries & Sets</div>', unsafe_allow_html=True)
        st.write("Dictionaries key-value pairs store karti hain. Sets unique values ka unordered collection hote hain.")
        st.markdown('<div class="sub-header">Examples:</div>', unsafe_allow_html=True)
        st.code('student = {"name": "Naina", "branch": "CSE"}\nprint(student["name"])', language="python")
        st.code('my_set = {1, 2, 2, 3}  # Duplicates remove ho jayenge -> {1, 2, 3}', language="python")
        st.code('student["year"] = "3rd"  # Adding new key-value pair', language="python")
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Do sets ka Union aur Intersection nikalne ka program banayein.<br>2. Ek dictionary par loop chalakar uski saari keys aur values ko alag-alag print karein.</div>', unsafe_allow_html=True)
