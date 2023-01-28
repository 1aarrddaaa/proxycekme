from bs4 import BeatifulSoup
import requests
  def proxycekme()

     proxies = []

     link = "https://www.sslproxies.org/"

    r = request.get(link)
    s = BeatifulSoup(r.text"html.parser")

       for 1 in s.find_all("tr")[:80]:

          try:


   data = 1.find_all("td")
   address = data[0].text
   port = data[1].text
   type_ = data [4].text
   proxy = address + ":" + port
   proxies.append(proxy)
   except Exception as e:
    print(e)
return proxies

for proxy in proxycekme():

print (proxy)
