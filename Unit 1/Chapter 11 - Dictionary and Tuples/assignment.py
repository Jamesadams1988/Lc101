# Create sort_contacts function

# Convert keys into a list, sort list
def sort_contacts(unorganized):
    organized = list(unorganized.keys())
    organized.sort()
    contacts = {}
    # Create a loop based off the length of the list
    for n in range(len(organized)):
        # using tuple assignment put name phone and email variables into a tuple, create a new dict and add that tuple
        name = organized[n]
        phone, email = unorganized.get(name,"none")
        contacts[n] = name, phone, email
    # print values of new dict as a list
    return (list(contacts.values()))
def main():
    print(sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}))
if __name__ == '__main__':
    main()



# using tuple assignment put name phone and email variables into a tuple, create a new list and add that tuple

# print tuple list






# The code below is just for your testing purposes. Make sure you pass all the tests.
# In Vocareum, only put code for the sort_contacts function above

