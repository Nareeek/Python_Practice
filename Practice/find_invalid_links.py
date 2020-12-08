# Link Verification
# Write a program that, given the URL of a web page, will attempt to download
# every linked page on the page. The program should flag any pages
# that have a 404 “Not Found” status code and print them out as broken links.

import bs4, requests
import pprint as pr
import webbrowser as web

main_url = r'https://docs.python.org/3.7/index.html'

webpage = requests.get(main_url)
soup = bs4.BeautifulSoup(webpage.text, features="html5lib")

print(webpage)

anchors = soup.select('a[href]')
links = []
responses = []

for anchor in anchors:    
    href = anchor.attrs["href"]
    
    if href[:7] != "https:":
        links.append(["https://docs.python.org/3.7/" + href])
        responses.append(requests.get("https://docs.python.org/3.7/" + href))
    else:
        links.append(href)

leftWidth = 60
rightWidth = 0
weblist = []
fail = "404 \'Not Found\'"

for link, response in zip(links, responses):
    if response.status_code != 404:
        text1 = str(str(link) + ' - ')
        text2 = str(response)
        print(text1.ljust(leftWidth, '.') + text2.rjust(rightWidth))
        weblist.append(link)
    elif response.status_code == 404:
        print(text1.ljust(leftWidth, '.') + fail.rjust(rightWidth))
