import ast

with open('date3.txt','r') as txtfile:
    newdate = ast.literal_eval(txtfile.read())
for i in newdate:
    if i == 'class="green">':
        newdate.remove('class="green">')
for i in newdate:
    if i == 'class="green">':
        newdate.remove('class="green">')
for i in newdate:
    if i == 'class="green">':
        newdate.remove('class="green">')
for i in newdate:
    if i == 'class="green">':
        newdate.remove('class="green">')
for i in newdate:
    if i == 'class="green">':
        newdate.remove('class="green">')
for i in newdate:
    if i == 'class="green">':
        newdate.remove('class="green">')
for i in newdate:
    if i == 'class="green">':
        newdate.remove('class="green">')
with open('date4.txt','w') as txtfile:
    txtfile.write(str(newdate))
print(len(newdate))