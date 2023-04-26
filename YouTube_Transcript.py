from youtube_transcript_api import YouTubeTranscriptApi

video_id = '5t8Ik8y0NH0'
transcript = YouTubeTranscriptApi.get_transcript(video_id)

with open('transcript.txt', 'w', encoding='utf-8') as f:
    for line in transcript:
        f.write(line['text'] + '\n')
