binaryDigit = input("Enter your binary digit: ")
length = len(binaryDigit)
add = 0
invalid = False
for x in range(0, length):
    bintodin = binaryDigit[x]
    if bintodin == "1":
        add += 2**(length - 1 - x)
    elif bintodin == "0":
        pass
    else:
        print("You entered an invalid number")
        invalid = True
        break

if invalid:
    print("Try again next time!")
elif not invalid:
    print(add)
