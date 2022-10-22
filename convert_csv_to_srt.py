import pandas as pd
import time


def convert(n):
    return time.strftime("%H:%M:%S", time.gmtime(n))


def csv_to_srt(path):
    print("CSV to SRT Conversion Started....")
    sub_df = pd.read_csv(path)

    sub_df = sub_df.drop('Unnamed: 0', axis=1)

    print("Total doc length :", len(sub_df.to_dict()['start']))

    start = sub_df.to_dict()['start']
    end = sub_df.to_dict()['end']
    text = sub_df.to_dict()['text']

    abc = ""
    for sub in range(len(start)):
        abc += str(sub + 1) + "\n"
        abc += convert(int(start[sub])) + " --> " + convert(int(end[sub])) + "\n"
        abc += f"<i>{text[sub].strip()}</i>" + "\n\n"

    with open("sub.srt", "w") as f:
        f.write(abc)

    print("CSV to SRT Conversion Ended.")

