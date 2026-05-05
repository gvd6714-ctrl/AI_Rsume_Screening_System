# 📄 AI Resume Screening System

An AI-powered Resume Screening System built using **LangChain, OpenAI API, and Streamlit**.  
It analyzes resumes against job descriptions and provides skills extraction, matching, scoring, and explanation.

---

## 🚀 Features

- 📌 Extract key skills from resume
- 🔍 Match resume with job description
- ⭐ Generate ATS score (0–100)
- 🧠 Explain hiring decision clearly
- 📊 Streamlit UI for easy interaction
- 📁 Works with multiple resume samples

---

## 🏗️ Project Structure
resume-screening/
│
├── app.py # Streamlit UI
├── main.py # Backend pipeline
├── .env # OpenAI API key (NOT uploaded to GitHub)
│
├── data/
│ ├── job_desc.txt
│ ├── resume_avg.txt
│ ├── resume_strong.txt
│ ├── resume_weak.txt
│
├── prompts/
│ ├── extract_prompt.py
│ ├── match_prompt.py
│ ├── score_prompt.py
│ ├── explain_prompt.py
│
├── chains/
│ ├── extract_chain.py
│ ├── match_chain.py
│ ├── score_chain.py
│ ├── explain_chain.py

---
Install Dependencies
pip install -r requirements.txt

Setup API Key
OPENAI_API_KEY=your_api_key_here

▶️ Run Project
python main.py

Run Streamlit UI
python -m streamlit run app.py
