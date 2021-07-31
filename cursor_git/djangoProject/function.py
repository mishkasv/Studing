import random
numb=16777215
numbrand=random.randint(0,numb)
color='#{:06X}'.format(numbrand)
print(color)