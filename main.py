from __future__ import unicode_literals
import os
from yt_dlp import YoutubeDL
import moviepy.editor as mp
import whisper
import pandas as pd
from config import opts_aud, opts_vid, path, url, isdownload, model_name
from convert_csv_to_srt import csv_to_srt


def subtitle_video(download, online_url, aud_opts, vid_opts, model_type, name, audio_file, input_file,
                   uploaded_vid=None):
    try:
        path = f"{name}"
        if not os.path.exists(path):
            os.mkdir(path)
        print('Starting AutoCaptioning...')
        print(f'Results will be stored in {name}')

    except:
        return print('Choose another folder name! This one already has files in it.')

    vid_opts['outtmpl'] = f'{name}/{input_file}'
    aud_opts['outtmpl'] = f'{name}/{audio_file}'

    URLS = [online_url]
    if download:
        with YoutubeDL(aud_opts) as ydl:
            ydl.download(online_url)
        with YoutubeDL(vid_opts) as ydl:
            ydl.download(URLS)
    else:
        # Use local clip if not downloading from youtube
        my_clip = mp.VideoFileClip(uploaded_vid)
        my_clip.audio.write_audiofile(f'{name}/{audio_file}')

    print("Model Loading....")
    # Instantiate whisper model using model_type variable
    model = whisper.load_model(model_type)

    print("Model Loaded")
    print("Started the Translation...")
    # Get text from speech for subtitles from audio file
    result = model.transcribe(f'{name}/{audio_file}', task='translate')

    print("Translation done.")
    # create Subtitle dataframe, and save it
    dict1 = {'start': [], 'end': [], 'text': []}
    for i in result['segments']:
        dict1['start'].append(int(i['start']))
        dict1['end'].append(int(i['end']))
        dict1['text'].append(i['text'])
    df = pd.DataFrame.from_dict(dict1)
    df.to_csv(f'subs.csv')
    print("Saved into CSV file.")


if __name__ == '__main__':
    subtitle_video(
        download=isdownload,
        uploaded_vid=path,
        online_url=url,
        name='run',
        aud_opts=opts_aud,
        vid_opts=opts_vid,
        model_type=model_name,
        audio_file="audio.mp3",
        input_file='video.mp4'
    )
    path = "subs.csv"
    csv_to_srt(path)
