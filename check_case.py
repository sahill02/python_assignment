ch = input("Enter the Character ")

if ch>="A" and ch<="Z":
    print ("Uppercase")
elif ch>="a" and ch<="z":
    print ("Lowercase")
elif ch>="0" and ch<="9":
    print ("digit")
else:
    print ("Specail character")

# if ord(ch)>=65 and ord(ch)<=90:
#     print("Uppercase")
# elif ord(ch)>=97 and ord(ch)<=122:
#     print("Lowercase")
# elif ord(ch)>=48 and ord(ch)<=57:
#     print("Digit")
# else:
#     print("Special Character")
    