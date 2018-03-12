from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    vig = ""
    x = 0
    indiv = []
    rota = []
    for txt in text:
        indiv.append(txt)
    for n in rot:
        rota.append(alphabet_position(n))
    for letters in range(len(indiv)):
        if indiv[letters].isalpha() == True:
            vig = vig + (rotate_character(indiv[letters],rota[(x%(len(rota)))]))
            x = x + 1
        else: 
            vig = vig + indiv[letters]   
    return(vig)
    
def main():
    texts = input("Type a message:")
    rotations = input("Encryption Key:")
    return encrypt(texts,rotations)

if __name__ == '__main__':
    main()
