"""
Enter emails and names
Estimated completion time: 20-25 minutes.
Actual completion time: (Started at 15 past - Paused at )
"""
email_to_name = {}
email = str(input("Enter your email: "))
while email != "":
    split_1 = email.split("@")
    split_2 = email.split(".")
    name = " ".join(split_2).title()
    selection = str(input(f"Is your name {name}? (Y/n)"))
    if selection.upper() != 'Y' and selection != "":
        name = str(input("Enter your name: "))
    email_to_name[email] = name
    email = str(input("Enter your email: "))
for email, name in email_to_name.items():
    print(f"{name} ({email})")


