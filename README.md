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

 <section class="section">
    <h2>🏗 System Architecture</h2>
    <div class="arch">
      <div class="arch-row"><span class="arch-num">01 </span><b>User</b>&nbsp;<small>(Streamlit UI)</small></div>
      <div class="arch-row"><span class="arch-num">02 </span><b>Transcript Extraction</b>&nbsp;<small>transcript.py</small></div>
      <div class="arch-row"><span class="arch-num">03 </span><b>Text Cleaning &amp; Chunking</b></div>
      <div class="arch-row"><span class="arch-num">04 </span><b>LLM Summarization</b>&nbsp;<small>summarization.py</small></div>
      <div class="arch-row"><span class="arch-num">05 </span><b>Combined Summary Output</b>&nbsp;<small>based on selected type</small></div>
    </div>
  </section>

------------------------------------------------------------------------

## 📂 Project Structure

<pre>src/
├── summarization.py   # LLM integration &amp; chunk-based summarization
└── transcript.py      # Transcript extraction &amp; preprocessing

app.py                 # Streamlit UI &amp; main application entry
requirements.txt
.gitignore</pre>

------------------------------------------------------------------------

## ⚙️ Tech Stack

-   Python 3.11.2
-   Streamlit
-   youtube-transcript-api
-   Groq API
-   openai/gpt-oss-20b model
-   python-dotenv

------------------------------------------------------------------------

<section class="section">
    <h2>🔐 Environment Configuration</h2>
    <p style="color:#555;font-size:14px;margin-bottom:0.6rem;">Create a <code>.env</code> file in the root directory:</p>
    <pre>GROQ_API_KEY=your_groq_api_key_here</pre>
    <p style="color:#999;font-size:13px;margin-top:0.6rem;">Ensure <code>.env</code> is included in <code>.gitignore</code>.</p>
  </section>


------------------------------------------------------------------------

 <section class="section">
    <h2>🛠 Installation Guide</h2>
    <div class="step-label">1. Clone the repository</div>
    <pre>git clone https://github.com/Abhisek8895/YouTube_Video_Summarizer
cd Youtube_Video_Summarizer</pre>
    <div class="step-label">2. Create virtual environment</div>
    <pre>python -m venv venv
# Windows:   venv\Scripts\activate
# Mac/Linux: source venv/bin/activate</pre>
    <div class="step-label">3. Install dependencies</div>
    <pre>pip install -r requirements.txt</pre>
    <div class="step-label">4. Run the application</div>
    <pre>streamlit run app.py</pre>
  </section>

------------------------------------------------------------------------

<section class="section">
    <h2>🎨 Supported Summary Types</h2>
    <div class="info-box">
      <div class="fmt-row"><span class="fmt-key">concise</span><span class="fmt-arrow">→</span><span class="fmt-desc">Short compressed summary</span></div>
      <div class="fmt-row"><span class="fmt-key">bullet</span><span class="fmt-arrow">→</span><span class="fmt-desc">Structured bullet-point summary</span></div>
      <div class="fmt-row"><span class="fmt-key">insights</span><span class="fmt-arrow">→</span><span class="fmt-desc">Key insights &amp; takeaways</span></div>
      <div class="fmt-row"><span class="fmt-key">detailed</span><span class="fmt-arrow">→</span><span class="fmt-desc">In-depth explanatory summary</span></div>
      <div class="fmt-row"><span class="fmt-key">blog</span><span class="fmt-arrow">→</span><span class="fmt-desc">Blog-style rewritten article</span></div>
      <div class="fmt-row"><span class="fmt-key">twitter</span><span class="fmt-arrow">→</span><span class="fmt-desc">Twitter thread style content</span></div>
    </div>
  </section>

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
