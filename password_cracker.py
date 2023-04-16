
import random

# ROBOT FRAMEWORK
try:
    from robot.libraries.BuiltIn import BuiltIn
    from robot.libraries.BuiltIn import _Misc
    import robot.api.logger as logger
    from robot.api.deco import keyword
    ROBOT = False
except Exception:
    ROBOT = False

class Password_Cracker:
    def __init__(self, password='abc'):
        self.password = password
        self.character_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*'

    def result(self, cracked_password, guess_total, guesses):
        result = "Cracked password: {}, Guess total: {}, Guess per character: {}"
        result2 = "Cracked password: {}, Guess total: {}, Maximum guesses allowed: {}"

        if type(guesses) == list:
            return result.format(cracked_password, guess_total, guesses)
        else:
            return result2.format(cracked_password, guess_total, guesses)
        
    def set_password(self):
        self.password = input("Enter password: ")
        return self.password

    # Goes through each character in the password matching the self.character_list if matching appends to cracked_password
    def password_cracker_one(self):
        cracked_password = ""
        guess_total = 0
        character_guesses = 0
        guesses_per_character = []
        for i in range(len(self.password)):
            for j in range(len(self.character_list)):
                if self.password[i] == self.character_list[j]:
                    cracked_password += self.password[i]
                    guess_total += 1
                    character_guesses += 1
                    guesses_per_character.append(character_guesses)
                    character_guesses = 0
                    if cracked_password == self.password:
                        break
                else:
                    guess_total += 1
                    character_guesses += 1

        return self.result(cracked_password, guess_total, guesses_per_character)

    # randomly picks a random character from the self.character_list and appends it to cracked_password if matching to password
    def password_cracker_two(self):
        cracked_password = ""
        guess_total = 0
        character_guesses = 0
        guesses_per_character = []
        random_number = 0
        i = 0
        
        while cracked_password!= self.password:
                random_number = random.randint(0, len(self.character_list)-1)
                if self.password[i] == self.character_list[random_number]:
                    cracked_password += self.character_list[random_number]
                    guess_total += 1
                    character_guesses += 1
                    guesses_per_character.append(character_guesses)
                    character_guesses = 0
                    i += 1
                else:
                    guess_total += 1
                    character_guesses += 1
        
        return self.result(cracked_password, guess_total, guesses_per_character)

    # randomly picks the same amount of characters from the self.character_list and appends them to cracked_password if matching to the password    
    def password_cracker_three(self):
        cracked_password = ""
        guess_total = 0
        max_guesses = 1000000
        random_number = 0

        while cracked_password!= self.password:
            for i in range(len(self.password)):
                random_number = random.randint(0, len(self.character_list)-1)
                cracked_password += self.character_list[random_number]
            if cracked_password == self.password:
                guess_total += 1
                break
            elif guess_total == max_guesses:
                cracked_password = 'EXCEEDED MAX GUESSES'
                break 
            else:
                guess_total += 1
                cracked_password = ""
                continue
        
        return self.result(cracked_password, guess_total, max_guesses)
    

# password_cracker = Password_Cracker('a')
# print(password_cracker.password_cracker_one())
# print(password_cracker.password_cracker_two())
# print(password_cracker.password_cracker_three())
