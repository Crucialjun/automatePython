import requests

from bs4 import BeautifulSoup

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from datetime import datetime

now = datetime.now()

content = ""


def extract_news(url):
    print("Exctracting Hacker Stories.....")
    cnt = ''
    cnt += ('<b> HN Top Storiess:<b> \n' + '<br>' + '-' * 50 + '<br>')
    response = requests.get(url)
    content = response.content
    soup = BeautifulSoup(content)
    for i, tag in enumerate(soup.find_all('td', attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i + 1) + ' :: ' + tag.text + "\n" + '<br>') if tag.text != 'More' else '')
        return cnt


cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += '<br>-------<br>'
content += '<br><br> End of Message'
