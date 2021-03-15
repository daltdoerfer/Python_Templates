hacker1 = {"firstname": "Max", "lastname": "Müller"}

print(hacker1["firstname"])

def hacker_get_name(hacker):
    print(hacker["firstname"] + " " + hacker["lastname"])

company1={"name": "Hacking GmbH"}

def company_get_name(company):
    print(company["name"])

company_get_name(company1)

participants = [
    {"type": "person", "firstname": "Max", "lastname": "Müller"},
    {"type": "company", "name": "Hacking GmbH"}
                ]

for participant in participants: # Geht jedes Dict in der Liste nacheinander durch
    if participant["type"] == "person":
        hacker_get_name(participant)

    else:
        company_get_name(participant)