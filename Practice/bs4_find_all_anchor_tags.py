import requests
import bs4

print("Googling...")

links = ["http://google.com/search?q=python", "https://pythonprogramming.net/parsememcparseface/"]
res = requests.get(links[0])

res.raise_for_status()
print(res.status_code)


soup = bs4.BeautifulSoup(res.text, features = 'lxml')

tags = soup.select('a')

for tag in tags:
    #print(tag, '\n' * 2)
    print(tag.()
    print('\n' * 2)
    
print(len(tags))
