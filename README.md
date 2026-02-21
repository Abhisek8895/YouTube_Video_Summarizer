# 🎥 YouTube Video Summarizer

### Multi-Format AI Content Transformation System

An AI-powered application that converts long-form YouTube videos into
structured summaries using a Groq-hosted open-source Large Language
Model (LLM).

This system extracts transcripts, processes long content intelligently
using chunking, and generates summaries in multiple user-selected
formats such as concise notes, bullet points, blog articles, and Twitter
threads.

------------------------------------------------------------------------

## 🚀 Features

-   Paste any YouTube video URL
-   Automatic transcript extraction using youtube-transcript-api
-   Transcript cleaning & preprocessing
-   Intelligent chunking for large transcripts
-   LLM-powered summarization
-   Multiple summary formats:
    -   concise
    -   bullet
    -   insights
    -   detailed
    -   blog
    -   twitter
-   Secure API key management using .env
-   Interactive UI built with Streamlit

------------------------------------------------------------------------

## 🧠 Model & Inference

This project uses:

-   Groq (Hosted Inference Provider)
-   Model: openai/gpt-oss-20b

Why Groq? - High-speed inference - Open-source model hosting -
Cost-efficient API usage - Simple REST API integration

------------------------------------------------------------------------

## 🏗 System Architecture

User (Streamlit UI) ↓ Transcript Extraction (transcript.py) ↓ Text
Cleaning & Chunking ↓ LLM Summarization (summarization.py) ↓ Combined
Summary Output (based on selected type)

------------------------------------------------------------------------

## 📂 Project Structure

src/ ├── summarization.py \# LLM integration & chunk-based summarization
├── transcript.py \# Transcript extraction & preprocessing

app.py \# Streamlit UI & main application entry requirements.txt
.gitignore

------------------------------------------------------------------------

## ⚙️ Tech Stack

-   Python 3.11.2
-   Streamlit
-   youtube-transcript-api
-   Groq API
-   openai/gpt-oss-20b model
-   python-dotenv

------------------------------------------------------------------------

## 🔐 Environment Configuration

Create a .env file in the root directory:

GROQ_API_KEY=your_groq_api_key_here

Ensure .env is included in .gitignore.

------------------------------------------------------------------------

## 🛠 Installation Guide

1.  Clone the repository

git clone https://github.com/Abhisek8895/YouTube_Video_Summarizer
cd Youtube-Video-Summarizer

2.  Create virtual environment

python -m venv venv

Activate environment:

Windows: venv\Scripts\activate

Mac/Linux: source venv/bin/activate

3.  Install dependencies

pip install -r requirements.txt

4.  Run the application

streamlit run app.py

------------------------------------------------------------------------

## 🎨 Supported Summary Types

-   concise → Short compressed summary\
-   bullet → Structured bullet-point summary\
-   insights → Key insights & takeaways\
-   detailed → In-depth explanatory summary\
-   blog → Blog-style rewritten article\
-   twitter → Twitter thread style content

------------------------------------------------------------------------

## 🧩 Core Implementation Concepts

-   Chunk-based summarization to handle long transcripts
-   Dynamic prompt engineering based on selected summary type
-   Secure API key handling using environment variables
-   Modular separation of transcript and summarization logic
-   End-to-end AI application workflow using Streamlit

------------------------------------------------------------------------

## 📈 Future Improvements

-   Timestamp-based summarization
-   Multi-video comparison feature
-   Question answering on video content (RAG integration)
-   Whisper-based audio fallback
-   Caching transcripts for performance optimization
-   Logging & structured error handling
-   Cloud deployment (Render / Railway / AWS)

------------------------------------------------------------------------

## 🎯 Resume-Ready Description

YouTube Video Summarizer -- AI Content Transformation System\
Developed an end-to-end LLM-powered application that converts YouTube
videos into multiple structured formats (concise, bullet, blog, twitter
threads) using Groq-hosted open-source LLM (gpt-oss-20b). Implemented
transcript extraction, intelligent chunking for context management,
dynamic prompt engineering, and secure API integration using Python and
Streamlit.

------------------------------------------------------------------------

## 📄 License

MIT License
