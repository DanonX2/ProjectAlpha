import ast
with open('vixdate.txt','r') as txtfile:
    vixdate = ast.literal_eval(txtfile.read())
with open('alphadate.txt','r') as txtfile:
    alphadate = ast.literal_eval(txtfile.read())
with open('alpha.txt','r') as txtfile:
    alpha = [float(i) for i in ast.literal_eval(txtfile.read())]
alpha2 = []

for i in range(0, len(alphadate)):
    alpha2.append(sum(alpha[:i]))
with open('alpha2.txt','w') as txtfile:
    txtfile.write(str(alpha2))