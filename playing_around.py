u=0
for i in range(3):
    u+=i
print(u)

def lol(text="", amount):
    text+="lol "
    if amount=<0:
        print(text)
    else:
        return lol(text,amount-1)
