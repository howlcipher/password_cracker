
import random

password = input("Enter password: ")
character_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'

def password_cracker_one():
    cracked_password = ""
    guess_total = 0
    character_guesses = 0
    guesses_per_character = []
    for i in range(len(password)):
        for j in range(len(character_list)):
            if password[i] == character_list[j]:
                cracked_password += password[i]
                guess_total += 1
                character_guesses += 1
                guesses_per_character.append(character_guesses)
                character_guesses = 0
                if cracked_password == password:
                    break
            else:
                guess_total += 1
                character_guesses += 1
    result = "Cracked password: {}, Guess total: {}, Guess per character: {}" 
    return result.format(cracked_password, guess_total, guesses_per_character)




def password_cracker_two():
    return -1


print(password_cracker_one())