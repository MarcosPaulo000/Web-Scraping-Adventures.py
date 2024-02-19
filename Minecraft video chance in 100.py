from selenium import webdriver
from bs4 import BeautifulSoup
from time import sleep
options = webdriver.EdgeOptions()
options.add_argument('--headless')
browser = webdriver.Edge(options=options)
mc_cont = 0
ct = 0
browser.get('https://www.youtube.com')
browser.maximize_window()
sleep(1.5)

yt = BeautifulSoup(browser.page_source, 'html.parser')

while ct < 100:
    videos = yt.findAll('div', attrs={'id': 'content'})

    for video in videos:
        title = video.find('yt-formatted-string', attrs={'id': 'video-title'})
        
        if title:
            titleW = title.text
            
            if 'MINECRAFT' in titleW.upper():
                mc_cont += 1
            
        ct += 1
        if ct == 100:
            break
    browser.refresh()
    sleep(.2)
print(f'After reviewing a hundred youtube videos, i have found \033[35m{mc_cont}\033[m videos with minecraft in their title!')
