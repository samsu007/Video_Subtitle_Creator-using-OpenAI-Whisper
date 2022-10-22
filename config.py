opts_aud = {
    'format': 'mp3/bestaudio/best',
    'keep-video': True,
    'postprocessors': [{  # Extract audio using ffmpeg
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3', }]}

opts_vid = {'format': 'mp4/bestvideo/best'}

url = None  # "https://www.youtube.com/watch?v=gUF6WUq0Cf4"  # online url
# or #
path = "samplepath"  # local file path

isdownload = False  # if online_url set download = True else False

model_name = "base"  # check more details here : https://github.com/openai/whisper
