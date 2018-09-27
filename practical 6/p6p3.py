# ask user for name 

# if name is Miguel:
#     print this
# elif name is mickey:
#     print that
# else:
#     print other


name = input("please enter your name: ")

if name == "miguel" or name == "Miguel":
    print("That is a cool name!")
elif name == "mickey mouse" or name == "sponge bob":
    print("Not sure that's your real name")
else:
    print("You have a nice name")