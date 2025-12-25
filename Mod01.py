# name = "Sonny Smith"
# title = "Data Scientist"
# company = "Tech Solutions Inc."

# print(name[0])          # First character of the name

def generate_signature(name, title, company):
    if name[0] == "A" or name[0] == "B" or name[0] == "C" or name[0] == "D" or name[0] == "E" or name[0] == "F" or name[0] == "G" or name[0] == "H" or name[0] == "I":
        print(f">>{name}, {title} at {company}")
        return ">>" + name + ", " + title + " at " + company
    elif name[0] == "J" or name[0] == "K" or name[0] == "L" or name[0] == "M" or name[0] == "N" or name[0] == "O" or name[0] == "P" or name[0] == "Q" or name[0] == "R":
        print(f"--{name}, {title} at {company}")
        return "--" + name + ", " + title + " at " + company
    else:
        print(f"::{name}, {title} at {company}")
        return "::" + name + ", " + title + " at " + company
