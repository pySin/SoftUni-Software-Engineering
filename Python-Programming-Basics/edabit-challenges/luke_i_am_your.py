# Luke I am your

# Person	Relation
# Darth Vader	father
# Leia	sister
# Han	brother in law
# R2D2	droid

def relation_to_luke(name):
    relations = {
        "Darth Vader": "father",
        "Leia": "sister",
        "Han": "brother in law",
        "R2D2": "droid"
    }
    return f"Luke, I am your {relations[name]}."


current_name = input()
print(relation_to_luke(current_name))
