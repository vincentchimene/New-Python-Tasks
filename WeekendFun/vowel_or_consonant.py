#Vowel or Consonant : Ask for one letter. Print "Vowel"
#if it is a, e, i, o, u. Else print "Consonant". If not a letter,
#print "Invalid input"

def check_letter(letter):
    if len(letter) == 1:
        if letter in "aeiou":
            result = "Vowel"
        elif letter in "bcdfghjklmnpqrstvwxyz":
            result = "Consonant"
        else:
            result = "Invalid Input"
    return result



letter = input("Enter a letter: ")
print(check_letter(letter))






