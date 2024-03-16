def main():
    emails_and_names = {}

    while True:
        email = input("Email: ")
        if email == "":
            break
        name = get_name(email)
        emails_and_names[email] = name

    for email, name in emails_and_names.items():
        print(f"{name} ({email})")

def extract_name_from_email(email):
    parts = email.split("@")[0].split(".")
    name = " ".join(part.capitalize() for part in parts)
    return name


def get_name(email):
    extracted_name = extract_name_from_email(email)
    confirmation = input(f"Is your name {extracted_name}? (Y/n) ")
    if confirmation.lower() in ['', 'y', 'yes']:
        return extracted_name
    else:
        return input("Name: ")

main()
