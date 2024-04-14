from random import randrange

def generate_number():
    RandNumber = randrange(1000, 10000) # randragne(a, b) b-1, tāpēc 10000, nevis 9999
    return RandNumber


def number_to_digit (RandNumber): #Sadala ciparu uz skaitliem
    digit4 = (RandNumber % 10)
    digit3 = (RandNumber % 100) // 10
    digit2 = (RandNumber % 1000) // 100
    digit1 = (RandNumber // 1000)
    return digit4, digit3, digit2, digit1


def not_same_digits (digit4, digit3, digit2, digit1): #Parbauda ģenereto skaitli, ja ir vienādi cipari, tad ģenerē jaunu
    is_same_digit = False
    if (digit4 == digit3 or digit4 == digit2 or digit4 == digit1 or digit3 == digit2 or digit3 == digit1 or digit2 == digit1):
        is_same_digit = True
        generate_number()
        return is_same_digit
    else:
        is_same_digit = False
        return is_same_digit

is_same_digit = True

while (is_same_digit == True): #Ģenerē skaitli, kamer nav atšķirīgi cipari
    RandNumber = generate_number()
    digit4, digit3, digit2, digit1 = number_to_digit(RandNumber)
    is_same_digit = not_same_digits(digit4, digit3, digit2, digit1)
    

RandDigit4 = digit4 #Saglaba ciparus no funkcijas, lai pēc tām salīdzīnātu ar spēlētāja ievadītajiem cipariem
RandDigit3 = digit3
RandDigit2 = digit2
RandDigit1 = digit1

attemps = 8
print ("Number is generated, you have 8 attemps to guess it")

#print (RandNumber) #Atkļudošanas nolūkam


while (attemps != 0):
    m=0 #Wrong place, but right digit
    p=0 #Right place
    print ("Attemps left: ", attemps)
    PlayerDigit = int(input("Guess the number: "))
    PlayerDigit4, PlayerDigit3, PlayerDigit2, PlayerDigit1 = number_to_digit(PlayerDigit)
    attemps = attemps - 1
    if (PlayerDigit4 == RandDigit4 and PlayerDigit3 == RandDigit3 and PlayerDigit2 == RandDigit2 and PlayerDigit1 == RandDigit1):
        print ("You won! Correct answer was: ", RandNumber)
        exit(0)

    if (PlayerDigit4 == RandDigit3 or PlayerDigit4 == RandDigit2 or PlayerDigit4 == RandDigit1):
        m=m+1
    
    if (PlayerDigit3 == RandDigit4 or PlayerDigit3 == RandDigit2 or PlayerDigit3 == RandDigit1):
        m=m+1
    
    if (PlayerDigit2 == RandDigit4 or PlayerDigit2 == RandDigit3 or PlayerDigit2 == RandDigit1):
        m=m+1
    
    if (PlayerDigit1 == RandDigit4 or PlayerDigit1 == RandDigit3 or PlayerDigit1 == RandDigit2):
        m=m+1
    
    if (PlayerDigit4 == RandDigit4):
        p=p+1

    if (PlayerDigit3 == RandDigit3):
        p=p+1
    
    if (PlayerDigit2 == RandDigit2):
        p=p+1

    if (PlayerDigit1 == RandDigit1):
        p=p+1
    
    print ("Guess:", PlayerDigit, "M:", m, ";", "P:" , p)
    
print ("You lost, correct answer was: ", RandNumber)




