import streamlit as st
from src.transcript import get_transcript, get_video_metadata
from src.summarizer import YouTubeSummarizer


st.set_page_config(page_title="YouTube Video Summarizer", layout="wide")

st.title("🎥 YouTube Video Summarizer")
st.write("Generate AI-powered summaries using Groq LLM")

# Input section
video_url = st.text_input("Enter YouTube Video URL")

summary_type = st.selectbox(
    "Select Summary Type",
    ["concise", "bullet", "insights", "detailed", "blog", "twitter"]
)

if st.button("Generate Summary"):

    if not video_url:
        st.error("Please enter a valid YouTube URL.")
    else:
        try:
            with st.spinner("Fetching video details..."):
                print("Getting metadata")
                metadata = get_video_metadata(video_url)
                print("Getting Transcript")
                transcript = get_transcript(video_url)
                
            print("Transcript length:", len(transcript))

            st.image(metadata["thumbnail"])
            st.subheader(metadata["title"])
            st.caption(f"Duration: {metadata['length']} seconds")

            summarizer = YouTubeSummarizer()

            with st.spinner("Generating summary..."):
                final_summary = summarizer.generate_summary(
                    transcript, summary_type
                )

            st.markdown("## 📄 Summary")
            st.write(final_summary)

        except Exception as e:
            st.error(f"Error: {str(e)}")
