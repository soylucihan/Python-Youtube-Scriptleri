import youtube_dl
x=str(input("devamm??"))
while len(x)>4:
    a=input("enter url ")
    ydl_opts = {'format': 'bestaudio/best','postprocessors': [{'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '320',}],}

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([a])
    x=str(input("devamm??"))