from helpers import alphabet_position, rotate_character

def encrypt(text,rot):
    x = ""
    for n in text:
        x = x + rotate_character(n,rot)
    return(x)


def main():
    texts = input("Type a message:")
    rotations = input("Rotate by:")
    return encrypt(texts,rotations)

if __name__ == '__main__':
    main()