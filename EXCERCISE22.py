#PRINT NEXT PALINDROME AND THE NUMBER SHOULD BE GREATER THAN 10
"""
def nextpalindrome(n):
    n=n+1
    while not str(n)==str(n)[::-1]:
        n+=1
        return n

if __name__=="__main__":
    size=int(input("enter the number of enteries"))
    numlist=[]
    for i in range(size):
        numlist.append(int(input("enter the numbers")))
    print(f"you have entered {numlist}")
    print(f"output list: {[numlist[i] if numlist[i]<10 else nextpalindrome(numlist[i]) for i in range(size)]}")
"""
def nextSpecialPalindrome(n):
 if n < 10:
  return n
 n = n + 1
 while not str(n) == str(n)[::-1]:
  n += 1
 return n

# listification of Next Palindrome of a given list
def listifyNextPalindrome(li):
 return [nextSpecialPalindrome(i) for i in li]

print(listifyNextPalindrome([1,7,24,89,23,786,245,444]))