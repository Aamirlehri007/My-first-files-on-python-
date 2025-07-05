# while and For loops


# while loops 

# x=0
# while (x<=5):
#     print(x)
#     x=x+1

#for loops

# for x in range (5, 11):
#     print(x)


# array
days = ["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat","Sun"]

for d in days:
    # if (d=="Sat"):break          # loops stops
    if (d=="Fri"): continue        # "d" will skip
    print(d)
