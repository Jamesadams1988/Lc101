def get_initials(fullname):
    """ TASK: Given a person's name, returns the person's initials (uppercase) """
    # split the fullname into sections in a list using " " as the splitter
    fullname = fullname.split(" ")
    initials = ""
    # utilize 2 loops 1) using each list item as a 2) duration via the characters
    Name_list_length = len(fullname)
    for num in range(Name_list_length):
        x = 0
        for n in fullname[num]:
            if n.isalpha() == True and x == 0:
                initials = initials + n
                x = x + 1
            x = x + 1
    return initials.upper()
def main():
    name = input("What is your full name?")
    inti = get_initials(name)
    print(inti)
if __name__ == '__main__':
    main()