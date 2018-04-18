# !/usr/bin/env python
# -*- coding:utf-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import re
from music import GetMusic



if __name__ == "__main__":
    url = 'http://music.163.com/discover/toplist'  # 网易云云音乐热歌榜url
    #GetMusic(url)
    #getMusicTag("http://music.163.com/discover/artist/cat?id=1001")
    url = "http://music.163.com/discover/artist/cat?id=1001"
    music = GetMusic()
    music.run(url)
   # for id,link in music.tags.items():
    #    print(id,link)