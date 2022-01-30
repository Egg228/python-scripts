

while True:
    try:
        a = float(input("Enter the number"))
        break

    except ValueError:
        print("you entered something else")
print("All OK")