u=0
for i in range(3):
    u+=i
print(u)

def lol(amount, text=""):
    if amount <= 0:
        print(text)
    else:
        text += "lol "
        return lol(amount-1, text)

lol(5)
print("I should really practice my basic python skills more")
