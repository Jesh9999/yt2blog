from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[-1].split("?")[0]
    return None

def fetch_transcript(video_url):
    video_id = get_video_id(video_url)
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([item['text'] for item in transcript_list])
    return full_text
