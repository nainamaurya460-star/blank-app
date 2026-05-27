import streamlit as st

# --- CONFIG & STYLING ---
st.set_page_config(page_title="Python Mastery Hub", page_icon="🐍", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size: 45px; font-weight: bold; color: #00ffcc; text-align: center; text-shadow: 2px 2px #000; margin-bottom: 10px; }
    .phase-header { background: linear-gradient(90deg, #00ffcc, #333); color: #000; padding: 10px; border-radius: 5px; font-size: 24px; font-weight: bold; margin-top: 30px; }
    .topic-card { background-color: #1e1e2f; border-left: 5px solid #00ffcc; padding: 15px; border-radius: 8px; margin-bottom: 20px; }
    .example-header { color: #ff007f; font-weight: bold; margin-top: 10px; }
    .practice-box { background-color: #261b3d; border: 1px dashed #ff007f; padding: 15px; border-radius: 10px; margin-top: 15px; }
    stCodeBlock { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://img.icons8.com/color/144/000000/python--v1.png", width=100)
st.sidebar.title("Python Roadmap")

phase = st.sidebar.selectbox("Choose Phase:", [
    "Phase 1: The Basics",
    "Phase 2: Data Structures & Functions",
    "Phase 3: Intermediate Python",
    "Phase 4: Advanced Python"
])

# --- CONTENT LOGIC ---

# ==========================================
# PHASE 1: THE BASICS
# ==========================================
if phase == "Phase 1: The Basics":
    st.markdown('<div class="main-title">Phase 1: The Foundation 🧱</div>', unsafe_allow_html=True)
    
    topic = st.sidebar.radio("Select Topic:", [
        "Intro & Setup", "Variables & Types", "Type Casting", "Operators", "Conditionals", "Loops & Control"
    ])

    if topic == "Intro & Setup":
        st.markdown('<div class="phase-header">Introduction & Setup</div>', unsafe_allow_html=True)
        st.write("Python install karne ke liye python.org par jayein. Popular IDEs: VS Code, PyCharm, aur Jupyter.")
        st.subheader("Examples:")
        st.code('print("Hello, World!")', language="python")
        st.code('print(5 + 10) # Simple Math', language="python")
        st.code('print("Naina\'s Hub") # Using escape characters', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Apna naam 5 baar print karne ka program banayein.<br>2. Ek program likhein jo "Welcome to Python" do alag lines mein print kare.</div>', unsafe_allow_html=True)

    elif topic == "Variables & Types":
        st.markdown('<div class="phase-header">Variables & Data Types</div>', unsafe_allow_html=True)
        st.write("Variables data store karne ke containers hote hain.")
        st.subheader("Examples:")
        st.code('x = 10 # Integer\ny = 10.5 # Float\nname = "Python" # String\nis_valid = True # Boolean', language="python")
        st.code('print(type(x)) # Data type check karna', language="python")
        st.code('a, b, c = 1, 2, "Test" # Multiple assignment', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Char variables banayein (int, float, str, bool) aur unke types print karein.<br>2. Do numbers ko variables mein store karke unka product nikalen.</div>', unsafe_allow_html=True)

    elif topic == "Loops & Control":
        st.markdown('<div class="phase-header">Loops & Loop Control</div>', unsafe_allow_html=True)
        st.write("For loops range ke liye aur While loops condition ke liye use hote hain.")
        st.subheader("Examples:")
        st.code('for i in range(5): print(i) # For loop', language="python")
        st.code('while x < 5: print(x); x+=1 # While loop', language="python")
        st.code('if i == 3: break # Loop todna', language="python")
        st.code('if i == 2: continue # Iteration skip karna', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. 1 se 20 tak saare Even numbers print karein.<br>2. Ek infinite while loop banayein jo "stop" likhne par break ho jaye.</div>', unsafe_allow_html=True)

# ==========================================
# PHASE 2: DATA STRUCTURES & FUNCTIONS
# ==========================================
elif phase == "Phase 2: Data Structures & Functions":
    st.markdown('<div class="main-title">Phase 2: Core Python 🧠</div>', unsafe_allow_html=True)
    
    topic = st.sidebar.radio("Select Topic:", [
        "Lists & Tuples", "Dicts & Sets", "Functions & Args", "Lambda & Comprehensions", "String Manipulation"
    ])

    if topic == "Lists & Tuples":
        st.markdown('<div class="phase-header">Lists & Tuples</div>', unsafe_allow_html=True)
        st.write("Lists mutable (changeable) hoti hain, Tuples immutable (fixed) hoti hain.")
        st.subheader("Examples:")
        st.code('my_list = [1, 2, 3]; my_list.append(4) # List update', language="python")
        st.code('my_tuple = (1, 2, 3) # Tuple fixed hai', language="python")
        st.code('print(my_list[0:2]) # Slicing', language="python")
        st.code('my_list.sort() # Sorting', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Ek list se duplicate elements remove karne ka program banayein.<br>2. Tuple ko list mein convert karke update karein aur wapas tuple banayein.</div>', unsafe_allow_html=True)

    elif topic == "Functions & Args":
        st.markdown('<div class="phase-header">Functions, *args & **kwargs</div>', unsafe_allow_html=True)
        st.write("Functions code ko reusable banate hain.")
        st.subheader("Examples:")
        st.code('def add(a, b): return a + b', language="python")
        st.code('def multi_sum(*args): return sum(args) # Variable arguments', language="python")
        st.code('def info(**kwargs): print(kwargs) # Dictionary arguments', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Ek function banayein jo check kare ki number Prime hai ya nahi.<br>2. *args ka use karke ek calculator function banayein jo kitne bhi numbers add kar sake.</div>', unsafe_allow_html=True)

# ==========================================
# PHASE 3: INTERMEDIATE PYTHON
# ==========================================
elif phase == "Phase 3: Intermediate Python":
    st.markdown('<div class="main-title">Phase 3: Building Apps 🚀</div>', unsafe_allow_html=True)
    
    topic = st.sidebar.radio("Select Topic:", [
        "File Handling", "Exception Handling", "Modules & Packages", "OOP Basics", "The 4 Pillars of OOP"
    ])

    if topic == "OOP Basics":
        st.markdown('<div class="phase-header">Classes & Objects</div>', unsafe_allow_html=True)
        st.write("OOP (Object Oriented Programming) real-world entities ko simulate karta hai.")
        st.subheader("Examples:")
        st.code("""
class Car:
    def __init__(self, brand):
        self.brand = brand
    def show(self):
        return f"Car brand is {self.brand}"

c1 = Car("Tesla")
print(c1.show())
        """, language="python")
        st.code('class Student: pass # Empty class', language="python")
        st.code('setattr(obj, "age", 20) # Dynamic attributes', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Ek "Bank" class banayein jisme deposit aur withdraw methods hon.<br>2. Class variable aur instance variable ka diff dikhane ke liye ek example likhen.</div>', unsafe_allow_html=True)

    elif topic == "The 4 Pillars of OOP":
        st.markdown('<div class="phase-header">Inheritance, Polymorphism, Encapsulation, Abstraction</div>', unsafe_allow_html=True)
        st.subheader("Examples:")
        st.code('class Child(Parent): # Inheritance', language="python")
        st.code('self.__private_var = 10 # Encapsulation', language="python")
        st.code('def speak(self): # Polymorphism (Same method, diff class)', language="python")
        st.code('from abc import ABC, abstractmethod # Abstraction', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Ek Inheritance hierarchy banayein: Animal -> Dog.<br>2. Private variable ko access karne ke liye getter aur setter methods banayein.</div>', unsafe_allow_html=True)

# ==========================================
# PHASE 4: ADVANCED PYTHON
# ==========================================
elif phase == "Phase 4: Advanced Python":
    st.markdown('<div class="main-title">Phase 4: Expert Level 🔥</div>', unsafe_allow_html=True)
    
    topic = st.sidebar.radio("Select Topic:", [
        "Iterators & Generators", "Decorators", "Dunder Methods", "Concurrency (Asyncio)", "Metaprogramming"
    ])

    if topic == "Iterators & Generators":
        st.markdown('<div class="phase-header">Iterators & yield</div>', unsafe_allow_html=True)
        st.write("Generators memory save karne ke liye 'yield' use karte hain.")
        st.subheader("Examples:")
        st.code("""
def my_gen():
    yield 1
    yield 2

for val in my_gen(): print(val)
        """, language="python")
        st.code('it = iter([1, 2]); next(it) # Iterator Protocol', language="python")
        st.code('(x*x for x in range(10)) # Generator Expression', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Fibonacci series ke liye ek generator banayein.<br>2. Custom Iterator class banayein jo numbers ko reverse print kare.</div>', unsafe_allow_html=True)

    elif topic == "Concurrency (Asyncio)":
        st.markdown('<div class="phase-header">Asyncio, Threading, Multiprocessing</div>', unsafe_allow_html=True)
        st.write("Tasks ko parallel chalane ke liye use hota hai.")
        st.subheader("Examples:")
        st.code("""
import asyncio
async def main():
    print("Wait...")
    await asyncio.sleep(1)
    print("Done!")

asyncio.run(main())
        """, language="python")
        st.code('from threading import Thread # I/O Bound tasks', language="python")
        st.code('from multiprocessing import Process # CPU Bound tasks', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Do functions ko asycronously ek sath chalane ka code likhen.<br>2. Threading aur Multiprocessing ke beech ka difference table form mein samjhayein.</div>', unsafe_allow_html=True)
