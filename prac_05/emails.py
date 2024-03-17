
"""
Word Occurrences
Estimate: 20 minutes
Actual:   40 minutes
"""

def main():
    """ Print username and email"""
    email_to_name={}
    email = input("Email : ")
    while email!="":
        username = get_name(email)
        enquiry = input(f"Is your name{username}? (Y/n)").upper()
        if enquiry != "Y" and enquiry != "":
            real_name = input("Name :")
        email_to_name[email] = username
        email = input("Email :")
    for email, username in email_to_name.items():
        print(f"{username} ({email})")

def get_name(email):
    """ Get name from the email """
    fullname= email.split("@")[0]
    name=fullname.split(".")
    return " ".join(name).title()
main()



