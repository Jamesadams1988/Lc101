x = {"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"), "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"), "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}

lists = []
display = {}
xs = 0
for (k,v) in x.items():
    v = list(v)
    name = k
    k = k.lower()
    phone = v[0]
    email = v[1]
    lists.append(name)
    lists.append(phone)
    lists.append(email)
    display[k] = lists
    lists = []
    xs = xs + 1

for n in range(xs):
    if display.get(n) < display.get(n+1):
        temp1 = display[n+1]
        temp2 = display[n]
        display[n] = temp1
        display[n+1] = temp2
print(display)

#print(sort_contacts({"Horney, Karen": ("1-541-656-3010", "karen@psychoanalysis.com"),
#        "Welles, Orson": ("1-312-720-8888", "orson@notlive.com"),
#        "Freud, Anna": ("1-541-754-3010", "anna@psychoanalysis.com")}), [('Freud, Anna', '1-541-754-3010',
#        'anna@psychoanalysis.com'), ('Horney, Karen', '1-541-656-3010', 'karen@psychoanalysis.com'),
#        ('Welles, Orson', '1-312-720-8888', 'orson@notlive.com')])
# contacts = {name: (phone, email), name: (phone, email), etc.}