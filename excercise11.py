#Celsius to Farenheit convertor
celsius = float(input("Enter temperature in celsius: \n"))
fahrenheit = (celsius * 9/5) + 32
print(celsius,' Celsius is:',fahrenheit,'Fahrenheit')
#Farenheit to celsius convertor
fahrenheit = float(input("Enter temperature in fahrenheit: \n"))
celsius = (fahrenheit - 32) * 5/9
print(fahrenheit,'in Fahrenheit is:',celsius, 'Celsius')
#Km/hr to m/sec
km=float(input("Enter the speed in km per hour\n"))
b=0.277778 * km
print(km,"km/hr is ",b,"m/sec")
#m/sec to km/hr
m=float(input("Enter the speed in meter per second\n"))
c=3.6 * m
print(m,"m/sec is ",c,"km/hr")