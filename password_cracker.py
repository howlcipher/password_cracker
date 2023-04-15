
import random

password = input("Enter password: ")
character_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'

def result(cracked_password, guess_total, guesses):
    result = "Cracked password: {}, Guess total: {}, Guess per character: {}"
    result2 = "Cracked password: {}, Guess total: {}, Maximum guesses allowed: {}"

    if type(guesses) == list:
        return result.format(cracked_password, guess_total, guesses)
    else:
        return result2.format(cracked_password, guess_total, guesses)

# Goes through each character in the password matching the character_list if matching appends to cracked_password
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

    return result(cracked_password, guess_total, guesses_per_character)

# randomly picks a random character from the character_list and appends it to cracked_password if matching to password
def password_cracker_two():
    cracked_password = ""
    guess_total = 0
    character_guesses = 0
    guesses_per_character = []
    random_number = 0
    i = 0
    
    while cracked_password!= password:
            random_number = random.randint(0, len(character_list)-1)
            if password[i] == character_list[random_number]:
                cracked_password += character_list[random_number]
                guess_total += 1
                character_guesses += 1
                guesses_per_character.append(character_guesses)
                character_guesses = 0
                i += 1
            else:
                guess_total += 1
                character_guesses += 1
    
    return result(cracked_password, guess_total, guesses_per_character)

# randomly picks the same amount of characters from the character_list and appends them to cracked_password if matching to the password    
def password_cracker_three():
    cracked_password = ""
    guess_total = 0
    max_guesses = 100000
    random_number = 0

    while cracked_password!= password:
        for i in range(len(password)):
            random_number = random.randint(0, len(character_list)-1)
            cracked_password += character_list[random_number]
        if cracked_password == password:
            guess_total += 1
            break
        elif guess_total == max_guesses:
            cracked_password = 'EXCEEDED MAX GUESSES'
            break 
        else:
            guess_total += 1
            cracked_password = ""
            continue
    
    return result(cracked_password, guess_total, max_guesses)

print(password_cracker_one())
print(password_cracker_two())
print(password_cracker_three())