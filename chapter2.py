from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')

# nameList = bs.findAll('span', {'class':'green'})
nameList = bs.find_all(text='the prince')
print(len(nameList))
# for name in nameList:
#     print(name.get_text())