import re

def create_agenda():

    """Creates a dictionary from hardcoded lists"""

    # Define three lists with name, profession and salary

    name = ["perez","rios","gonzalez","zandperl","jobbagy","berenstein"]
    profession = ["architect", "psycologist", "teacher", "engineer", "doctor", "chemist"]
    salary = [40000,3000,100000,55256,378900,7000]

    # Create a dictionary with names as keys

    values = zip(profession, salary)

    agenda = dict(zip(name, values))
    return agenda

def remove_item_by_name(item, agenda):

    removed_val = agenda.pop(item)
    return agenda

def add_item(key, value, agenda):

    """ARGS:""" 

    agenda[key] = value
    return agenda

def search_pattern(pattern, agenda):

    """searches for the string represented in pattern in the keys of the dict"""
    for key in agenda.keys():
        matched = re.findall(pattern, key)
        if len(matched)== 0:
            pass
        else:
            print("Printing the name with the matching pattern:", key)

def display(agenda):

    for key, item in agenda.items():
        print(key, item)    

if __name__ == "__main__": 

    agenda = create_agenda()
    print("First display of the contents of agenda")
    display(agenda)
    agenda = remove_item_by_name("perez", agenda)
    print("Second display of the contents of agenda")
    display(agenda)
    agenda = add_item("perrin", ["economist", 70000], agenda)
    print("Third display of the contents of agenda")
    display(agenda)
    agenda = search_pattern("io", agenda)
    

