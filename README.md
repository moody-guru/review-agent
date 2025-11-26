# 🤖 AI Pull Request Reviewer Agent
**Built for the Lyzr AI Backend Engineering Challenge**

This is an autonomous code review agent that listens for GitHub Pull Requests, analyzes the code changes using LLM, and posts constructive feedback directly to the PR comments.

## 🚀 Key Features
* **Event-Driven Architecture:** Uses GitHub Webhooks for real-time processing.
* **Secure Tunneling:** Integrates with Ngrok/Serveo to expose local services securely.
* **AI-Powered Analysis:** Leverages LLMs (Gemini/OpenAI) to detect security flaws (SQLi), performance issues (O(n^2)), and logic bugs. 
* **Observability Dashboard:** Includes a Streamlit UI to monitor review logs and system status in real-time.
* **Asynchronous Processing:** Uses FastAPI BackgroundTasks to ensure webhook delivery is never blocked.

## 🛠️ Tech Stack
* **Backend:** Python, FastAPI, Uvicorn
* **AI/LLM:** LangChain, Google Gemini 2.0
* **Integration:** GitHub Apps API (JWT Authentication), PyGithub
* **Frontend:** Streamlit
* **Infrastructure:** Ngrok (Tunneling)

## ⚙️ How to Run Locally

### 1. Prerequisites
* Python 3.9+
* A GitHub App (with permissions for Pull Requests & Contents)
* Google Gemini API Key

### 2. Installation
```bash
git clone https://github.com/moody-guru/review-agent.git
cd lyzr-challenge
pip install -r requirements.txt
```
<img width="1918" height="1005" alt="Screenshot 2025-11-26 143340" src="https://github.com/user-attachments/assets/57265bc4-13de-4d76-bdc7-adb2dd7134ef" />
<img width="1460" height="762" alt="2" src="https://github.com/user-attachments/assets/65d8b2ca-4538-44ce-8408-2e46fed09c87" />


