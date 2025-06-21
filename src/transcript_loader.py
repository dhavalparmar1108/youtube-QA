from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi, TranscriptsDisabled
import os 
from src.config import TRANSCRIPT_FILE, TRANSCRIPT_FOLDER

class TranscriptLoader:
    def __init__(self, url : str):
        self.url = url

    def extract_youtube_video_id(self) -> str | None:
        """
        Extracts the video ID from a YouTube URL.

        Supports:
        - https://www.youtube.com/watch?v=VIDEO_ID
        - https://youtu.be/VIDEO_ID
        - https://www.youtube.com/embed/VIDEO_ID

        Returns:
            Video ID string or None if not found
        """
        parsed_url = urlparse(self.url)
        
        # Case 1: Standard watch URL
        if parsed_url.hostname in ["www.youtube.com", "youtube.com"]:
            if parsed_url.path == "/watch":
                return parse_qs(parsed_url.query).get("v", [None])[0]
            elif parsed_url.path.startswith("/embed/"):
                return parsed_url.path.split("/embed/")[1]
        
        # Case 2: Short URL like youtu.be
        if parsed_url.hostname == "youtu.be":
            return parsed_url.path[1:]  # Remove leading slash
        
        return None

    def save_transcript(self):
        # Join the full path
        file_path = os.path.join(TRANSCRIPT_FOLDER, TRANSCRIPT_FILE)

        # Make directory if needed
        os.makedirs(TRANSCRIPT_FOLDER, exist_ok=True)

        # Write the transcript
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.transcript) 

    def load_transcript(self):
        try:
            video_id = self.extract_youtube_video_id()
            # If you don’t care which language, this returns the “best” one
            transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])

            # Flatten it to plain text
            self.transcript = " ".join(chunk["text"] for chunk in transcript_list)

            return self.transcript
            
        except:
            print("No captions available for this video.")