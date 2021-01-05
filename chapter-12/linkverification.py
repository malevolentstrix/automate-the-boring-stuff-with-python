# "Link Verification" practice project in Chapter - 12
# By JITHIN JOHN
import requests
from bs4 import BeautifulSoup
print('Please provide the web address link to be verified')
web_address = input()
res = requests.get(web_address)
res.raise_for_status()
soup = BeautifulSoup(res.text, 'html.parser')
for individual_href in soup.find_all('a'):
    print(individual_href, href=True)