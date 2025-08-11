# 🤖 AI Agent Development with AutoGen

## 📌 Overview
This repository contains a **comprehensive collection of Jupyter notebooks and scripts** demonstrating step-by-step development of AI agents using [AutoGen](https://microsoft.github.io/autogen/).

You will learn to:
- Configure and connect Large Language Models (LLMs)
- Build single and multi-agent conversational systems
- Create specialized agents (e.g., research assistants, math tutors, code copilots)
- Enable web search and external tool integrations
- Implement persistent memory via *Teachable Agents*
- Orchestrate multi-role agents in a **Group Chat company-style workflow**
- Run end-to-end AI-driven coding and analysis tasks

---

## 📂 Repository Structure

| ID  | File / Notebook | Description |
|-----|-----------------|-------------|
| 01  | **Configuring LLMs and setting up Autogen.ipynb** | Environment setup, API configuration, and loading LLMs into AutoGen. |
| 02  | **Building a basic Agent.ipynb** | Creates your first conversational agent with basic prompt-response functionality. |
| 03  | **Multi Agent Conversation.ipynb** | Demonstrates autonomous back-and-forth chats between multiple agents. |
| 04  | **Research assistant design.ipynb** | Builds a research-focused agent capable of structured responses. |
| 05a | **Orchestrate the nested chat.ipynb** | Coordinates nested agent conversations for complex workflows. |
| 05b | **Reviewer Agents.ipynb** | Implements agents that critique and improve outputs from other agents. |
| 06a | **Math Tutor Agent.ipynb** | An interactive tutor that explains math problems step-by-step. |
| 06b | **Research assistant with web search ability.ipynb** | Adds web search capabilities to the research assistant. |
| 07a | **End-to-End Coding Copilot in AutoGen.ipynb** | Creates a coding copilot to generate, test, and refine code. |
| 07b | **Execute user-defined code in Autogen.ipynb** | Safely runs custom code inside AutoGen sessions. |
| 08  | **Teachable Agents** *(Python script)* | Implements a `ConversableAgent` with **persistent teachability**, allowing it to remember facts and improve over time. |
| 09  | **Group Chat with Speaker Selection** *(Python script)* | Multi-agent company simulation with defined speaker rules and task allocation (Planner, Engineer, Executor, Writer, Admin). |
| 10  | **Group Chat for Data Analysis** *(Python script)* | Similar to above but with free-flow group conversation to collaboratively produce stock analysis reports. |

---

## 🛠️ Prerequisites

- **Python** 3.10 or 3.11
- [pip](https://pip.pypa.io/) or [conda](https://docs.conda.io/)
- OpenAI API key ([Get it here](https://platform.openai.com/account/api-keys))
- Recommended: Use a **virtual environment** to avoid dependency conflicts

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/autogen-ai-agents.git
cd autogen-ai-agents
```

### 2. Create & activate environment (conda example)
```bash
conda create -n autogen-agents python=3.11 -y
conda activate autogen-agents
```

### 3. Install dependencies
```bash
pip install "ag2[openai,teachable]" python-dotenv matplotlib pandas yfinance
```
> **Note:** In zsh or Jupyter, always quote extras: `"ag2[teachable]"`

### 4. Configure environment variables
Create a `.env` file in the repo root:
```env
OPENAI_API_KEY=sk-your-openai-key-here
```

---

## ▶️ Running the Notebooks

1. Start Jupyter Lab:
   ```bash
   jupyter lab
   ```
2. Open any notebook in order (start with **01 Configuring LLMs**).
3. Run cells sequentially.

---

## ▶️ Running the Scripts

### **Teachable Agent**
```bash
python teachable_agent.py
```
- Launches a `ConversableAgent` with **Teachability**.
- Persists learned information in `./tmp/interactive/teachability_db`.
- Chat until you type `exit`.

### **Group Chat with Speaker Selection**
```bash
python group_chat_speaker_selection.py
```
- Simulates a company with **Admin**, **Planner**, **Engineer**, **Executor**, and **Writer** roles.
- Uses *allowed speaker transitions* to enforce workflow order.

### **Group Chat for Data Analysis**
```bash
python group_chat_data_analysis.py
```
- Same roles but **free speaker transitions** for more organic collaboration.
- Example task: analyze Apple stock closing prices for the past month.

---

## 💡 Tips & Best Practices

- **Separate Environments:** Keep AutoGen work in its own virtual env to avoid dependency conflicts.
- **Model Names:** Use valid model names like `gpt-4o` or `gpt-4o-mini` (avoid typos like `gtp-4o`).
- **Persistent Memory:** For teachable agents, ensure `path_to_db_dir` is a persistent folder.
- **Quoting in zsh:** Always quote pip extras to avoid shell expansion errors:
  ```bash
  pip install "ag2[openai,teachable]"
  ```

---

## 📜 License
Educational purposes only. Ensure compliance with API provider policies.
