import streamlit as st

# --- CONFIG & STYLING ---
st.set_page_config(page_title="Python Mastery Hub", page_icon="🐍", layout="wide")

st.markdown("""
    <style>
    .main-title { font-size: 42px; font-weight: bold; color: #00ffcc; text-align: center; text-shadow: 2px 2px #000; margin-bottom: 20px; }
    .phase-header { background: linear-gradient(90deg, #00ffcc, #333); color: #000; padding: 10px; border-radius: 5px; font-size: 24px; font-weight: bold; margin-top: 30px; margin-bottom: 15px; }
    .sub-header { color: #ff007f; font-size: 22px; font-weight: bold; margin-top: 20px; border-bottom: 1px solid #ff007f; padding-bottom: 5px; }
    .ai-vibe { background-color: #112233; border-left: 5px solid #ff007f; padding: 12px; border-radius: 5px; margin: 10px 0; color: #ff007f; font-weight: bold; }
    .explanation-box { background-color: #1a1a2e; padding: 15px; border-radius: 8px; border: 1px solid #333; margin-bottom: 15px; line-height: 1.6; }
    .practice-box { background-color: #261b3d; border: 1px dashed #00ffcc; padding: 15px; border-radius: 10px; margin-top: 20px; }
    stCodeBlock { border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="main-title">⚡ Ultimate Python & AI Learning Bootcamp ⚡</div>', unsafe_allow_html=True)

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
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Python ek high-level, interpreted language hai jise readable aur clean code likhne ke liye design kiya gaya hai. Iska syntax itna simple hai ki lagta hai aap normal English padh rahe hain. Yeh structural, object-oriented, aur functional programming teeno ko support karti hai.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: Python AI ki sabse sabscche language hai. TensorFlow, PyTorch, aur OpenAI ke saare SDKs Python standard par chalte hain kyunki isme matrix operations aur prototyping behad fast hoti hai.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('print("Hello, World!")  # Screen par text dikhane ke liye', language="python")
        st.code('print("Welcome to Creator\'s Python Hub")  # Simple string output', language="python")
        st.code('print(5 + 10)  # Direct mathematics output screen par', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('import sys\nprint(f"Python Platform: {sys.platform}")  # System details extract karna\nprint(f"Version Info: {sys.version}")', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Apna naam, college aur branch 3 alag lines mein ek hi print statement se print karein.<br>2. Escape characters (\\n, \\t) ka use karke ek design layout print kijiye.</div>', unsafe_allow_html=True)

    elif topic == "Variables & Data Types":
        st.markdown('<div class="phase-header">Variables & Data Types</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Variables memory spaces hote hain jahan data store hota hai. Python dynamic typing follow karta hai, matlab aapko variable ka type pehle se batane ki zaroorat nahi hoti. Core types hain: int, float, str, aur bool.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: Neural Network ke weights hamesha floats hote hain, tokens strings hote hain, aur models ki activation states booleans mein control hoti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('age = 20  # Integer data type\npi = 3.14  # Float (decimal) data type\nmsg = "AI Hub"  # String data type\nis_active = True  # Boolean data type', language="python")
        st.code('print(type(age))  # Output check karne ke liye: <class \'int\'>', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('epochs, learning_rate, model = 100, 0.001, "Llama3"  # Multiple pointer allocation\nprint(f"Model: {model} | Rate: {learning_rate}")', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Char variables banayein aur unhe f-string ka use karke ek informative format mein print karein.<br>2. Ek variable ka data type runtime par integer se string me update karke dikhayein.</div>', unsafe_allow_html=True)

    elif topic == "Type Casting":
        st.markdown('<div class="phase-header">Type Casting in Python</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Jab ek data type ko forcefully doosre type mein badla jata hai, use Type Casting kehte hain. Yeh do tarah ki hoti hai: Implicit (Python khud karta hai) aur Explicit (Developer functions jaise int(), str() ka use karta hai).</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: Jab web scraper se data text form ("0.85") mein aata hai, toh use machine learning model me feed karne se pehle float() mein cast karna compulsory hota hai.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('num_str = "10"\nnum_int = int(num_str)  # String to Integer conversion\nprint(num_int + 5)  # Output: 15', language="python")
        st.code('val = float(5)  # Integer to Float -> 5.0\nprint(val)', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('raw_loss = "0.2456"\nclean_loss = float(raw_loss)  # Raw string precision metrics parsing\nprint(f"Loss percentage: {int(clean_loss * 100)}%")  # Float to Int nested cast', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. User se do string inputs lein ("20" aur "30"), unhe integers mein badlein aur unka sum nikalen.<br>2. Ek float number ko integer mein badal kar check karein ki decimal points ka kya hota hai.</div>', unsafe_allow_html=True)

    elif topic == "Operators":
        st.markdown('<div class="phase-header">Operators</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Operators variables aur values par mathematical aur logical operations karne ke symbol hain. Arithmetic (+, -, *, /), Comparison (==, !=, >), aur Logical (and, or, not) iske core types hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: Loss functions calculation, gradient vectors comparison, aur reinforcement learning ki conditional policy logical operators par hi built hoti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('sum_val = 10 + 5  # Addition (15)\npow_val = 2 ** 3  # Exponentiation / Power operator (8)\nfloor_div = 10 // 3  # Floor division (Returns quotient 3)', language="python")
        st.code('check = (5 == 5)  # Comparison operator (True)', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('loss, accuracy = 0.04, 0.96\nis_optimal = (loss < 0.05) and (accuracy > 0.95)  # Logical operations for model training convergence\nprint(f"Is model ready for production? {is_optimal}")', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Assignment operator (+=) ka use karke ek counter variable ko loop ke bina 5 se badhayein.<br>2. Membership operator (in) ka use karke ek text
        # ==========================================
# PHASE 2: DATA STRUCTURES & FUNCTIONS
# ==========================================
elif phase == "Phase 2: Data Structures & Functions":
    topic = st.sidebar.radio("Select Topic:", [
        "Lists & Tuples", "Dictionaries & Sets", "Functions & Scope", "Lambda & Comprehensions", "String Manipulation"
    ])

    if topic == "Lists & Tuples":
        st.markdown('<div class="phase-header">Lists & Tuples</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Lists mutable (changeable) ordered sequences hain jinhe sequence elements modify karne ke liye banaya jata hai. Tuples hamesha ordered par immutable (fixed) arrays hote hain jo data ko secure rakhte hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: Vector coordinates list matrices, embedding layers, aur pipeline inputs ko data collections structural layout mein represent karti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('my_list =\nmy_list.append(40)  # List modified ->\nprint(my_list[0:2])  # Slicing ->', language="python")
        st.code('my_tuple = (5, 15, 25)  # Fixed sequence', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('embeddings = [[0.12, -0.4], [0.9, 0.34]]  # Nested arrays representing multi-dimensional vectors\nfixed_tensor_shape = (1, 64, 64, 3)  # Input shape for Convolutional Networks (CNN)', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Ek list se duplicate elements remove karne ka program banayein.<br>2. Tuple ko list mein convert karke update karein aur wapas tuple banayein.</div>', unsafe_allow_html=True)

    elif topic == "Dictionaries & Sets":
        st.markdown('<div class="phase-header">Dictionaries & Sets</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Dictionaries key-value optimization maps patterns data fast indexing parsing key hashes par design karti hain. Sets unique values ka unordered collection hote hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: API responses configuration metadata schemas payload definitions structural formats aur key value extraction me dictionaries use hoti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('user = {"id": 101, "role": "admin"}\nprint(user["role"])  # Accessing via key\nmy_set = {1, 2, 2, 3}  # Duplicates automatically filtered -> {1, 2, 3}', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('llm_config = {\n    "model_id": "meta-llama-3",\n    "parameters": {"temperature": 0.7, "max_tokens": 256},\n    "stop_sequences": ["<end>", "STOP"]\n}  # Complex structural configurations mapping json objects', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Do sets ka Union aur Intersection nikalne ka program banayein.<br>2. Ek dictionary par loop chalakar uski saari keys aur values ko properly formatting ke sath print karein.</div>', unsafe_allow_html=True)

    elif topic == "Functions & Scope":
        st.markdown('<div class="phase-header">Functions, Args, Kwargs & Scope</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Functions clean blocks design reusable operational logic modules construct karte hain. Variable tracking operations modular parameters handling *args positional lists processing validation array mapping **kwargs named key-value dictionary parameters control karti hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: Dynamic orchestrator processing pipeline structures modular nodes call customization systems agent wrappers interface call models handling parameters pipelines wrap karti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('def calc_square(n):\n    return n * n\nprint(calc_square(5))  # Reusable block mapping calculations', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('def pipeline_orchestrator(node_name, *args, **kwargs):\n    print(f"Executing Node: {node_name}")\n    print(f"Positional Hyperparameters: {args}")\n    print(f"Keyword Configurations: {kwargs}")\n\npipeline_orchestrator("EmbeddingLayer", 512, dropout=0.2, activation="relu")', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. *args ka use karke ek function banayein jo sabse bada number return kare.<br>2. Global keyword ka use karke function ke andar se global variable ko safely modify karein.</div>', unsafe_allow_html=True)

    elif topic == "Lambda & Comprehensions":
        st.markdown('<div class="phase-header">Lambda Functions & List Comprehensions</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Lambda inline single line temporary expressions maps operations functional inline logic construct karti hain. Comprehensions optimized inline structural array processing sequences expressions clear mapping control execution design loops replacement optimize karti hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: High-speed continuous operational transforms raw values token strings vector list elements real-time processing mapping data token cleaning algorithms performance compute optimize loops inline logic map karti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('multiply = lambda a, b: a * b\nprint(multiply(3, 4))  # Single line calculation\n\nsquares = [x*x for x in range(5)]  # List comprehension ->', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('raw_probabilities = [0.12, 0.85, 0.45, 0.99]\n# Inline threshold filtering for vector probability values using list comprehension\nfiltered_nodes = [float(p) for p in raw_probabilities if p > 0.50]\nprint(f"Active Nodes: {filtered_nodes}")', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. List comprehension ka use karke 1 se 20 tak ke saare odd numbers ki list banayein.<br>2. Lambda function ka use karke ek numerical list ko automatically double mapping algorithm par chalayein.</div>', unsafe_allow_html=True)

    elif topic == "String Manipulation":
        st.markdown('<div class="phase-header">String Manipulation & Regex</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> String operations advanced parsing text patterns string slicing string interpolation regex expression matches extraction processes validation structural formatting layouts mapping algorithms handle karti hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: NLP textual pipelines text pre-processing pipelines token scrubbing entity matching chunking documents dynamic data cleaning strategies raw structured information text analytics system execute karti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('text = "Python Programming"\nprint(text[0:6])  # Slicing -> "Python"\nprint(text.lower())  # Case conversion -> "python programming"', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('import re\nlog_entry = "2026-05-27 SUCCESS: Model convergence reached loss=0.02"\nloss_val = re.findall(r"loss=[\d\.]+", log_entry)  # Text processing pattern parsing strings\nprint(f"Extracted Metrics array tokens: {loss_val}")', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. User se ek email string lein aur regex ka use karke check karein ki wo valid format hai ya nahi.<br>2. Ek long text sentence ke saare spaces ko strip out karke tokens arrays me partition kijiye.</div>', unsafe_allow_html=True)
        # ==========================================
# PHASE 2: DATA STRUCTURES & FUNCTIONS
# ==========================================
elif phase == "Phase 2: Data Structures & Functions":
    topic = st.sidebar.radio("Select Topic:", [
        "Lists & Tuples", "Dictionaries & Sets", "Functions & Scope", "Lambda & Comprehensions", "String Manipulation"
    ])

    if topic == "Lists & Tuples":
        st.markdown('<div class="phase-header">Lists & Tuples</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Lists mutable (changeable) ordered sequences hain jinhe sequence elements modify karne ke liye banaya jata hai. Tuples hamesha ordered par immutable (fixed) arrays hote hain jo data ko secure rakhte hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: Vector coordinates list matrices, embedding layers, aur pipeline inputs ko data collections structural layout mein represent karti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('my_list =\nmy_list.append(40)  # List modified ->\nprint(my_list[0:2])  # Slicing ->', language="python")
        st.code('my_tuple = (5, 15, 25)  # Fixed sequence', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('embeddings = [[0.12, -0.4], [0.9, 0.34]]  # Nested arrays representing multi-dimensional vectors\nfixed_tensor_shape = (1, 64, 64, 3)  # Input shape for Convolutional Networks (CNN)', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Ek list se duplicate elements remove karne ka program banayein.<br>2. Tuple ko list mein convert karke update karein aur wapas tuple banayein.</div>', unsafe_allow_html=True)

    elif topic == "Dictionaries & Sets":
        st.markdown('<div class="phase-header">Dictionaries & Sets</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Dictionaries key-value optimization maps patterns data fast indexing parsing key hashes par design karti hain. Sets unique values ka unordered collection hote hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: API responses configuration metadata schemas payload definitions structural formats aur key value extraction me dictionaries use hoti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('user = {"id": 101, "role": "admin"}\nprint(user["role"])  # Accessing via key\nmy_set = {1, 2, 2, 3}  # Duplicates automatically filtered -> {1, 2, 3}', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('llm_config = {\n    "model_id": "meta-llama-3",\n    "parameters": {"temperature": 0.7, "max_tokens": 256},\n    "stop_sequences": ["<end>", "STOP"]\n}  # Complex structural configurations mapping json objects', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. Do sets ka Union aur Intersection nikalne ka program banayein.<br>2. Ek dictionary par loop chalakar uski saari keys aur values ko properly formatting ke sath print karein.</div>', unsafe_allow_html=True)

    elif topic == "Functions & Scope":
        st.markdown('<div class="phase-header">Functions, Args, Kwargs & Scope</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Functions clean blocks design reusable operational logic modules construct karte hain. Variable tracking operations modular parameters handling *args positional lists processing validation array mapping **kwargs named key-value dictionary parameters control karti hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: Dynamic orchestrator processing pipeline structures modular nodes call customization systems agent wrappers interface call models handling parameters pipelines wrap karti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('def calc_square(n):\n    return n * n\nprint(calc_square(5))  # Reusable block mapping calculations', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('def pipeline_orchestrator(node_name, *args, **kwargs):\n    print(f"Executing Node: {node_name}")\n    print(f"Positional Hyperparameters: {args}")\n    print(f"Keyword Configurations: {kwargs}")\n\npipeline_orchestrator("EmbeddingLayer", 512, dropout=0.2, activation="relu")', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. *args ka use karke ek function banayein jo sabse bada number return kare.<br>2. Global keyword ka use karke function ke andar se global variable ko safely modify karein.</div>', unsafe_allow_html=True)

    elif topic == "Lambda & Comprehensions":
        st.markdown('<div class="phase-header">Lambda Functions & List Comprehensions</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> Lambda inline single line temporary expressions maps operations functional inline logic construct karti hain. Comprehensions optimized inline structural array processing sequences expressions clear mapping control execution design loops replacement optimize karti hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: High-speed continuous operational transforms raw values token strings vector list elements real-time processing mapping data token cleaning algorithms performance compute optimize loops inline logic map karti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('multiply = lambda a, b: a * b\nprint(multiply(3, 4))  # Single line calculation\n\nsquares = [x*x for x in range(5)]  # List comprehension ->', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('raw_probabilities = [0.12, 0.85, 0.45, 0.99]\n# Inline threshold filtering for vector probability values using list comprehension\nfiltered_nodes = [float(p) for p in raw_probabilities if p > 0.50]\nprint(f"Active Nodes: {filtered_nodes}")', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. List comprehension ka use karke 1 se 20 tak ke saare odd numbers ki list banayein.<br>2. Lambda function ka use karke ek numerical list ko automatically double mapping algorithm par chalayein.</div>', unsafe_allow_html=True)

    elif topic == "String Manipulation":
        st.markdown('<div class="phase-header">String Manipulation & Regex</div>', unsafe_allow_html=True)
        st.markdown('<div class="explanation-box"><b>What & Why:</b> String operations advanced parsing text patterns string slicing string interpolation regex expression matches extraction processes validation structural formatting layouts mapping algorithms handle karti hain.</div>', unsafe_allow_html=True)
        st.markdown('<div class="ai-vibe">🤖 Role in AI: NLP textual pipelines text pre-processing pipelines token scrubbing entity matching chunking documents dynamic data cleaning strategies raw structured information text analytics system execute karti hain.</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="sub-header">🔹 Basic Examples:</div>', unsafe_allow_html=True)
        st.code('text = "Python Programming"\nprint(text[0:6])  # Slicing -> "Python"\nprint(text.lower())  # Case conversion -> "python programming"', language="python")
        
        st.markdown('<div class="sub-header">💥 Advance Examples:</div>', unsafe_allow_html=True)
        st.code('import re\nlog_entry = "2026-05-27 SUCCESS: Model convergence reached loss=0.02"\nloss_val = re.findall(r"loss=[\d\.]+", log_entry)  # Text processing pattern parsing strings\nprint(f"Extracted Metrics array tokens: {loss_val}")', language="python")
        
        st.markdown('<div class="practice-box"><h4>📝 Practice Questions:</h4>1. User se ek email string lein aur regex ka use karke check karein ki wo valid format hai ya nahi.<br>2. Ek long text sentence ke saare spaces ko strip out karke tokens arrays me partition kijiye.</div>', unsafe_allow_html=True)
        
