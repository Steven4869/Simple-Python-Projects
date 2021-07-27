#String functions
str='whatever you LOSE, you Will find it again, But what you throw away you will never get BACK.'
print(str.capitalize())#first charcter capitaly
print(str.upper())
print(str.swapcase())
print(str.title())
print(str.casefold())

print(str.count('you'))
print(str.endswith('BACK.'))
print(str.replace('you','amazing'))
print(str.partition('never'))
print(str.index('get'))

print(str.center(55))
print(str.isdigit())
print(str.isalnum())
print(str.isalpha())
print(str.isdecimal())
print(str.isspace())
print(str.isprintable())
print(str.split())

#Escape characters
print('New York\'s famous hotdog')
print('New\n York')
print('New\t York')
print('New\b York')
print('New\f York')
print('New\r York')