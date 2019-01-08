import ast
import matplotlib.dates as dates

vixdatefile = 'vixdate.txt'
vixpricefile = 'vixprice.txt'
earningdatefile = 'date4.txt'
earningsuprisefile = 'suprise.txt'
alphafile = 'alpha.txt'
alphadatefile = 'alphadate.txt'
alpha2file = 'alpha2.txt'

alphavix = []
alphavixdate = []

with open(vixdatefile,'r') as txtfile:
    vixdate = ast.literal_eval(txtfile.read())
with open(vixpricefile,'r') as txtfile:
    vixprice = [float(i) for i in ast.literal_eval(txtfile.read())]
with open(alphadatefile,'r') as txtfile:
    alphadate = ast.literal_eval(txtfile.read())
with open(alpha2file,'r') as txtfile:
    alpha2 = [float(i/100) for i in ast.literal_eval(txtfile.read())]
for i in range(0, len(alphadate)):
    for j in range(0, len(vixdate)):
        if dates.datestr2num(alphadate[i]) == dates.datestr2num(vixdate[j]):
            alphavixdate.append(alphadate[i])
            alphavix.append(alpha2[i]/vixprice[j])

with open('alphavix.txt','w') as txtfile:
    txtfile.write(str(alphavix))
with open('alphavixdate.txt','w') as txtfile:
    txtfile.write(str(alphavixdate))