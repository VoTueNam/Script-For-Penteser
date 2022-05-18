import requests
url = ""
r = requests.get(url, allow_redirects=True)
open('THMlogo.png', 'wb').write(r.content)

url_2 = 'https://download.sysinternals.com/files/PSTools.zip'
r_2 = requests.get(url_2, allow_redirects=True)
open('PSTools.zip', 'wb').write(r_2.content)  