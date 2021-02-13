from random import randrange
alpha = 'A0B1C2D3E4F5G6H7I8J9K!L@M#N$O%P^Q&R*S,T.U/V\\*W+X*Y-Z/{}[]^()_'
lenght = int(input('El Lenghto Ofa The Passworda : '))
lines = int(input('El Howa Many Passwordas Yoa Wanta : '))
for x in range(lines):
    print("Random Passwords : ", end="")
    for i in range(lenght):
        ran = randrange(0, len(alpha))
        print(alpha[ran], end="")
    print()