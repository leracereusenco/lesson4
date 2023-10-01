#var = input('Write a name...')

#def functionTest(x): #intre paranteze parametrul care dorim sa-l primim
    #print('Hello', x)

#functionTest(var) #de cate ori va fi scris, de atatea ori se va putea realiza functia


#def calc(a, b ):
    #print(a + b) #hello + name = helloname
    #print(a - b)
    #print(a * b) #hello * string = illegal exception; hello * 3 = hellohellohello
    #print(a / b)

#a = int(input('Enter a first number\n'))
#b = int(input('Enter a second number\n'))

#calc(a, b)


#def calc(a, b = 5):
    #print(a + b) #hello + name = helloname
    #print(a - b)
    #print(a * b) #hello * string = illegal exception; hello * 3 = hellohellohello
    #print(a / b)

#a = int(input('Enter a first number\n'))

#calc(a)


#args - argumente
#def calc(*args):
    #print(args[0] + args[1])
    #print(args[0] - args[1])
    #print(args[0] * args[1])
    #print(args[0] / args[1])

#a = 2
#b = 3

#calc(*args: a, b) #???


#A trece la litere majuscule
#def to_uppercase(word):
    #return word.upper() #primim raspunsul

#def to_uppercase(word):
    #print(word.upper()) #afisam rezultatul

#to_uppercase('hello')


#for i in range(3,5):
    #if i == 4:
        #print('done')
        #break - a opri
        #continue - continua


#def will_be_used_in_future():
    #pass #-trece peste, fara sa fie eroare



#JOC LOGIC
max_hp = 100

player_hp = 100
player_lifes = 3
player_damage = 10
player_armor = 80
nr_hits = 1

player_name = input('Enter player name...\n')

#Functia de atac
def attack(player_hp, player_damage: 20):
    global player_armor, nr_hits, player_lifes #modificator de acces, face ca functia sa vada variabilele propuse in global
    if player_armor - player_damage > 0:
        player_armor = player_armor - player_damage
    else:
        player_hp = player_hp - player_damage
        if player_hp == 0:
            player_lifes = player_lifes - 1
    return player_hp

#Functia heal
def heal(player_hp, heal):
    global max_hp

    if player_hp + heal > max_hp:
        player_hp = max_hp
    else:
        player_hp = player_hp + heal
    return player_hp

#Verificam
#print(attack(player_hp, player_damage))

#Lupta
for i in range(1, 20):
    #terminati ciclul daca hp < 0
    if player_hp > 0:
        player_hp = attack(player_hp, player_damage)
    elif player_lifes == 0:
        ('Game over')
        break
    else:
        print('Game over')
        break

    print('Live', player_hp)
    print('Armor', player_armor)
    print('Hit nr', nr_hits)

else:
    print('You are dead')

for o in range(1, 100):
    if player_hp > 0:
        nr_hits = nr_hits + 1

        #make a miss every 3 hits
        if nr_hits % 3 == 0:
            pass
        else:
            player_hp = attack(player_hp)
        print('----' + player_name + '---')
        print('Live', player_hp)
        print('Armor', player_armor)
        print('Hit nr', nr_hits)

    else:
        break

print('You are dead')



#T/a: de aflat de ce folosim
#def main():
    #var = input('Enter a name\n')
    #functionTest(var)

#if __name__ == '__main__':
    #main()