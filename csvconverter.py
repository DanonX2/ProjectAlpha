import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from urllib.request import urlopen
import re
import csv

date = []
price = []

with open('vix.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        date.append(row[0].split(',')[0])
        price.append(row[0].split(',')[1])

with open("vixdate.txt",'w') as txtfile:
    txtfile.write(str(date))
with open("vixprice.txt",'w') as txtfile:
    txtfile.write(str(price))