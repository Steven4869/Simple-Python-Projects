#TO MAKE A PROGRAM TO PRINT THE NEXT PALINDROME
"""
FOR EXAMPLE
IT SHOULD ASK USER FOR THE INPUT OF NUMBER OF STRINGS
INPUT
NUMBER OF STRINGS:3
451
233
43
OUTPUT
NEXT PALINDROME IS 555
NEXT PALINDROME IS 333
NEXT PALINDROME IS 44
"""
test=int(input("PLEASE ENTER THE NUMBER OF ENTERIES\n"))
for i in range(test):
    number=int(input("ENTER YOUR VALUE\n"))
    while True:
        num=number
        number=number+1
        numm=str(num)
        if numm==numm[::-1]:
            print(f"{numm} is next palindrome")
            break
        else:
            continue
