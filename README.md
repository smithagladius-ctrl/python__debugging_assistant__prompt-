# Python Screening Task 2 — AI Debugging Assistant Prompt

This repository contains my submission for **Python Screening Task 2**.  
It includes a natural-language prompt designed for an AI debugging assistant that helps students debug Python code **without directly giving the solution**.

---

## 📂 Files in this repo
- **prompt.md** → The main prompt for the AI assistant.  
- **README.md** → Reasoning, setup instructions, and testing methodology.  
- **examples/** → A few small buggy Python files for testing.  
- **.gitignore** → Ignore unnecessary files.

---

## ⚙️ Setup Instructions
1. Clone this repo:
   ```bash
   git clone https://github.com/<your-username>/python-debugging-assistant-prompt.git
   cd python-debugging-assistant-prompt
2. Open the repository in VS Code or any editor.

3. Read prompt.md for the AI debugging assistant prompt.

4. Run the scripts in examples/ to test the prompt with buggy Python code:

python examples/bug1_syntax.py
python examples/bug2_nameerror.py
python examples/bug3_offbyone.py
python examples/bug4_logic.py

**Reasoning**

Tone & Style: The AI should use a friendly, encouraging, and student-friendly tone, focusing on hints and explanations rather than direct fixes.

Balance: The AI should point out where the bug may be and suggest what concepts to review (e.g., variables, loops, syntax) without rewriting the correct code.

Adaptation:

For beginners → provide simpler explanations, step-by-step hints, and direct references to basic concepts.

For advanced learners → give higher-level hints, suggest debugging strategies, and encourage independent problem-solving.

**Examples**

The examples folder contains small buggy Python programs that can be used to test the AI assistant’s behavior:

bug1_syntax.py → Missing colon in a for loop (syntax error).

bug2_syntax.py → Uses an undefined variable (count instead of cnt).

bug3_syntax.py → Loop skips the last element (off-by-one error).

bug4_syntax.py → Impossible condition (x < 0 and x > 10) causing wrong logic branch.

These help evaluate how well the AI gives hints without directly fixing the code.