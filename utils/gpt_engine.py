from transformers import pipeline

# Load Hugging Face model once
hf_summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def summarize_transcript(transcript):
    if not transcript:
        return "No transcript available."

    # Use a chunk if too long (distilbart limit ~1024 tokens)
    transcript = transcript[:1000]

    try:
        summary = hf_summarizer(transcript, max_length=180, min_length=30, do_sample=False)
        return summary[0]['summary_text']
    except Exception as e:
        return f"⚠️ HuggingFace Summarization Error: {str(e)}"

def extract_keywords_from_blog(blog_text):
    # Dummy fallback keyword extractor — simple logic for now
    import re
    words = re.findall(r'\b\w+\b', blog_text.lower())
    common = [word for word in words if len(word) > 5]
    keywords = list(set(common))[:10]
    return ", ".join(keywords)
