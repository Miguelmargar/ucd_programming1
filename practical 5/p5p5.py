answer = input("enter town name: ")

if (answer == "Dublin") or (answer == "dublin") or (answer == "Waterford") or (answer == "waterford") or (answer == "Kilkenny") or (answer == "kilkenny"):
    print("you entered", answer, answer, "is in Leinster")
elif (answer == "Belfast") or (answer == "belfast") or (answer == "Derry") or (answer == "derry") or (answer == "Lisburn") or (answer == "lisburn"):
    print("you entered", answer, answer, "is in Ulster")
elif (answer == "Cork") or (answer == "cork") or (answer == "Limerick") or (answer == "limerick"):
    print("you entered", answer, answer, "is in Munster")
elif (answer == "Galway") or (answer == "galway") or (answer == "Sligo") or (answer == "sligo"):
    print("you entered", answer, answer, "is in Connacht")
else:
    print("Sorry, I didn’t recognise that name.")
