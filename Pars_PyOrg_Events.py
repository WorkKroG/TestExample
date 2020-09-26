import requests
from bs4 import BeautifulSoup

url = "https://www.python.org/events/python-events"
r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

links = soup.select('#content > div > section > div > div > ul > li')
form_event = soup.select('#content > div > section > div '
                         '> div > ul > li > p > span')
num_event = 0

for link in links:
    date_event = link.find('a').text
    name_event = link.find('time').text
    num_event += 1
    try:
        print(f'Date event: {date_event}\nEvent name: '
              f'{name_event}\nEvent format: {form_event[num_event].text}\n')
    except IndexError:
        continue
