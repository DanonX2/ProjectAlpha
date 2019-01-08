from urllib.request import urlopen
from bs4 import BeautifulSoup
import progressbar as pb

widgets = ['WELCOME \n                 Progress for scraping 1 8 2 5 Days of Data', pb.Percentage(), ' ', pb.Bar(marker=pb.RotatingMarker()), ' ', pb.ETA()]
timer = pb.ProgressBar(widgets=widgets, maxval=1825).start()

months = {1:'Jan', 2:'Feb', 3:'Mar', 4:'Apr', 5:'May', 6:'Jun', 7:'Jul', 8:'Aug', 9:'Sep', 10:'Oct', 11:'Nov', 12:'Dec'}
date = []
suprise = []
progress = 0
for year in range(int(input('starting year')),2019):
    for month in range(1,13):
        if month == 2:
            for day in range(1,29):
                try:
                    url = "https://www.nasdaq.com/earnings/earnings-calendar.aspx?date=" + str(year) + "-" + months[month] + "-" + str(day)
                    html = urlopen(url)
                    soup = BeautifulSoup(html, 'lxml')
                    numofpoints = len(soup.find("table").find_all("tr"))
                    for num in range(1,numofpoints):
                        table = soup.find("table").find_all("tr")[num].find_all("td")
                        date.append(str(table[2]).split()[1])
                        nextitem = str(table[8]).split(">")[2].split("<")[0]
                        try:
                            suprise.append(float(nextitem))
                        except:
                            del date[-1]
                except:
                    pass
                progress += 1
                timer.update(progress)
        else:
            for day in range(1,31):
                try:
                    url = "https://www.nasdaq.com/earnings/earnings-calendar.aspx?date=" + str(year) + "-" + months[month] + "-" + str(day)
                    html = urlopen(url)
                    soup = BeautifulSoup(html, 'lxml')
                    numofpoints = len(soup.find("table").find_all("tr"))
                    for num in range(1,numofpoints):
                        table = soup.find("table").find_all("tr")[num].find_all("td")
                        date.append(str(table[2]).split()[1])
                        nextitem = str(table[8]).split(">")[2].split("<")[0]
                        try:
                            suprise.append(float(nextitem))
                        except:
                            del date[-1]
                except:
                    pass
                progress += 1
                timer.update(progress)
        

with open("date.txt",'w') as txtfile:
    txtfile.write(str(date))
with open("suprise.txt",'w') as txtfile:
    txtfile.write(str(suprise))