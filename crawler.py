from bs4 import BeautifulSoup
import urllib.request
def nyt_word(word):
    url = 'https://www.nytimes.com/'
    content = urllib.request.urlopen(url)

    soup = BeautifulSoup(content, 'lxml')
    headlines = soup.find_all('h2')
    text = soup.find_all('p')
    text_lst= []
    count = 0
    word_lower = word.lower()
    for headline in headlines:
        text_lst.append(headline.get_text())

    for line in text:
        text_lst.append(line.get_text())

    for s in text_lst:
        if word_lower in s.lower():
            count += 1

    print('{} appears on the nytimes.com homepage {} times.'.format(word, count))

nyt_word('the')
