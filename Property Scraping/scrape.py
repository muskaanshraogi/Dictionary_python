import requests
import pandas
from bs4 import BeautifulSoup

area = str(input("\nEnter the locality : "))
area = area.replace(" ","-")
city = str(input("\nEnter the city : "))

r = requests.get("https://www.magicbricks.com/property-for-sale/residential-real-estate?proptype=Multistorey-Apartment,Builder-Floor-Apartment,Penthouse,Studio-Apartment&Locality=" + area + "&cityName=" + city)
soup = BeautifulSoup(r.content,"html.parser")
all = soup.find_all("div",{"class":"m-srp-card__container"})

l = []

for item in all:
    d = {}
    d["Locality"] = item.find("span", {"class":"m-srp-card__title"}).text.replace("\n","").replace("\t","").replace("  ","")
    try:
        d["Price"] = item.find("div", {"class":"m-srp-card__price"}).text
    except:
        d["Price"] = "None"
    for feature in item.find_all("div", {"class":"m-srp-card__desc"}):
        for title, value in zip(item.find_all("div", {"class":"m-srp-card__summary__title"}),item.find_all("div", {"class":"m-srp-card__summary__info"})):
            if "carpet area" in title.text:
                d["Carpet Area"] = value.text
            if "status" in title.text:
                d["Status"] = value.text.replace("\n","").replace("\t","").replace("  ","")
            if "floor" in title.text:
                d["Floor"] = value.text
            if "transaction" in title.text:
                d["Transaction"] = value.text
    l.append(d)

df = pandas.DataFrame(l)
df.to_csv("properties.csv")