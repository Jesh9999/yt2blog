import streamlit as st
from utils.transcript import fetch_transcript
from utils.gpt_engine import summarize_transcript, extract_keywords_from_blog

st.title("📽️ YT2Blog - YouTube to Blog Generator")

video_url = st.text_input("Enter YouTube video URL")

if video_url:
    try:
        transcript = fetch_transcript(video_url)
        st.success("Transcript fetched successfully!")

        if st.button("Generate Blog Article ✍️"):
            with st.spinner("Generating with GPT..."):
                blog_output = summarize_transcript(transcript)
                keywords = extract_keywords_from_blog(blog_output)

                st.subheader("📝 Blog Article")
                st.markdown(blog_output)

                st.subheader("🔍 SEO Keywords")
                st.markdown(f"`{keywords}`")

                st.subheader("📥 Export Blog")
                st.download_button("Download as .txt", blog_output, file_name="blog_article.txt")

    except Exception as e:
        st.error(f"Error: {str(e)}")
