# GenLegal
⚖️ Legal Jargon Simplifier

A simple Streamlit app that uses Google Gemini to simplify complex legal text for different audiences (General Users, Lawyers, Judges).

Deployed easily on Render in one file (app.py).
--------------------------------------------------------------------------------------------------------------------------------------------
🚀 Features

Paste legal text and get simplified explanations.

Choose audience-specific styles: General User, Lawyer, Judge.

Chat-like interface with history.

Runs entirely in Streamlit (no separate backend).
--------------------------------------------------------------------------------------------------------------------------------------------
🔑 Setup Instructions
1️⃣ Clone the repo
git clone https://github.com/your-username/legal-simplifier.git
cd legal-simplifier

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run locally
streamlit run app.py


Open 👉 http://localhost:8501

🌐 Deploy on Render
--------------------------------------------------------------------------------------------------------------------------------------------
Push your repo to GitHub.

Go to Render
 → New Web Service.

Connect your GitHub repo.

Select Python 3.11+ as the environment.

Set Start Command:

streamlit run app.py --server.port 10000 --server.address 0.0.0.0


Deploy → Render will give you a public URL.
--------------------------------------------------------------------------------------------------------------------------------------------
🔑 API Key

This app uses Google Gemini API.

Get your free API key from Google AI Studio
.

Paste it in the app when prompted.
--------------------------------------------------------------------------------------------------------------------------------------------
🛠 Requirements

See requirements.txt:

streamlit
google-generativeai
