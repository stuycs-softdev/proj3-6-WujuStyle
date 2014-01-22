import urllib2
from bs4 import BeautifulSoup

def getNeighborhoods():
    r = []

    response = urllib2.urlopen("http://en.wikipedia.org/wiki/Neighborhoods_in_New_York_City").read()

    soup = BeautifulSoup(response)


    for x in soup.find("table",attrs={"class":"wikitable"}).find_all("tr"):
        a = x.find_all("td")
        if len(a) > 4:
            k = a[4].get_text()
            for y in k.split(","):
                if y[0] == " ":
                    y = y[1:]
                if y not in r:
                    r.append(y)

    r = sorted(r)
    return r


if __name__ == "__main__":
    for x in getNeighborhoods():
        print x
#    print getNeighborhoods()