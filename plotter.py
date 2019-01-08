import matplotlib.pyplot as plt
import numpy as np
import ast
import matplotlib.dates as dates

vixdatefile = 'vixdate.txt'
vixpricefile = 'vixprice.txt'
earningdatefile = 'date4.txt'
earningsuprisefile = 'suprise.txt'
alphafile = 'alpha.txt'
alphadatefile = 'alphadate.txt'
alpha2file = 'alpha2.txt'
alphavixfile = 'alphavix.txt'
alphavixdatefile = 'alphavixdate.txt'

with open(vixdatefile,'r') as txtfile:
    vixdate = ast.literal_eval(txtfile.read())
with open(vixpricefile,'r') as txtfile:
    vixprice = [float(i) for i in ast.literal_eval(txtfile.read())]
with open(earningdatefile,'r') as txtfile:
    earningdate = ast.literal_eval(txtfile.read())
with open(earningsuprisefile,'r') as txtfile:
    earningsuprise = [float(i/100) for i in ast.literal_eval(txtfile.read())]
with open(alphafile,'r') as txtfile:
    alpha = [float(i) for i in ast.literal_eval(txtfile.read())]
with open(alphadatefile,'r') as txtfile:
    alphadate = ast.literal_eval(txtfile.read())
with open(alpha2file,'r') as txtfile:
    alpha2 = [float(i) for i in ast.literal_eval(txtfile.read())]
with open(alphavixfile,'r') as txtfile:
    alphavix = [float(i) for i in ast.literal_eval(txtfile.read())]
with open(alphavixdatefile,'r') as txtfile:
    alphavixdate = ast.literal_eval(txtfile.read())

vixdateaxis = dates.datestr2num(vixdate)
earningdateaxis = dates.datestr2num(earningdate)
alphadateaxis = dates.datestr2num(alphadate)
alphavixdateaxis = dates.datestr2num(alphavixdate)

plt.figure(1)
plt.plot(alphadateaxis, alpha2)
plt.ylabel('alpha2percentage')
plt.title('alpha2')
plt.plot(alphadateaxis, [0]*len(alphadateaxis))

plt.figure(2)
plt.plot(vixdateaxis, vixprice)
plt.ylabel('price')
plt.title('vix')
plt.plot(vixdateaxis, [0]*len(vixdateaxis))



plt.show()