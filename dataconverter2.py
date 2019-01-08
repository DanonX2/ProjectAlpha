import ast

with open('date4.txt', 'r') as txtfile:
    earningdate = ast.literal_eval(txtfile.read())
with open('suprise.txt','r') as txtfile:
    earningsuprise = [float(i/100) for i in ast.literal_eval(txtfile.read())]

alphadate = []
alpha = []

for i in range(0,len(earningdate)):
    if i == 0:
        pass
    else:
        if earningdate[i] != earningdate[i-1]:
            alphadate.append(earningdate[i])
alpha = [0]*len(alphadate)
for i in range(0,len(alphadate)):
    for j in range(0,len(earningdate)):
        if earningdate[j] == alphadate[i]:
            alpha[i] = float(earningsuprise[j]) + float(alpha[i])

with open('alphadate.txt', 'w') as txtfile:
    txtfile.write(str(alphadate))
with open('alpha.txt', 'w') as txtfile:
    txtfile.write(str(alpha))
