# Python program to display user name followed by Good Afternoon

# name = input("Enter your name: ")
name ="Alok"
print("Good afternoon " + name)

# Write a program to fill in a letter template given below with name and date

Template = f'''
    Good afternoon, {name}
'''
print(Template)

# Spaces in a string

st = 'This is a     double space'
vall = st.find("  ")
# (vall > 0) ? print("Double spaces present") : print("Not double spaces are there")