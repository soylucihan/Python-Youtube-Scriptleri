#-*- coding: utf-8 -*-
from __future__ import unicode_literals
import youtube_dl


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    a=d['_percent_str']  #yüzde almak için 
    print(a)

ydl_opts = {
    'format': 'best',##En iyi kalitede indirir '(mp4,webm)[height<480]' gibi format ve kalite seçilebilir.
    'logger': MyLogger(),
    'progress_hooks': [my_hook],
}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=L5K3IxINr7A'])
