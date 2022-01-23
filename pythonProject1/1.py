import os

z,x,*c =[1,2,3,4,5]
print(z,x,c)

website = input("wwedite sayt: ")

if 'https://' in website:
    os.system("start " + website)
elif "www." in website:
    website = ("https://")+ website
    os.system("start " + website)

else:
    website = ("https://www.") + website
    os.system("start " + website)
