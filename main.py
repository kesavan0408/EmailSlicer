email = input("Enter your Email: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"your user name is{username} & domain is {domainha}")