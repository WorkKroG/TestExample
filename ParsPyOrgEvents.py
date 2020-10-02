import requests
from bs4 import BeautifulSoup


def get_url():
    url = "https://www.python.org/events/python-events"
    r = requests.get(url)
    return (r)


def get_soup(r):
    soup = BeautifulSoup(r.text, "html.parser")
    return soup


def get_element(soup):
    get_links = soup.select('#content > div > section > div > div > ul > li')
    get_form_event = soup.select('#content > div > section > div '
                                 '> div > ul > li > p > span')
    return get_links, get_form_event


if __name__ == '__main__':

    r = get_url()
    soup_site = get_soup(r)
    elements = get_element(soup_site)
    links, form_events = elements
    for num_event, link in enumerate(links, 0):
        date_event = link.find('a').text
        name_event = link.find('time').text
        try:
            print(f'Date event: {date_event}\nEvent name: '
                  f'{name_event}\nEvent format: {form_events[num_event].text}\n')
        except IndexError:
            continue
