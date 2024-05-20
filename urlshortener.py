import pyshorteners

link= input("Enter the URl:\n")

shortener=pyshorteners.Shortener()

x= shortener.tinyurl.short(link)

print(x)
