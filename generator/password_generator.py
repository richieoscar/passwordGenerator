import random


class PasswordGenerator:

    def __init__(self, numOfAlphabets, numOfDigits, numOfChars):
        self.numOfAlphabets = numOfAlphabets
        self.numOfChars = numOfChars
        self.numOfDigits = numOfDigits

    def generate_alphabets(self):
        listOfAlphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                           "s", "t",
                           "u", "v", "v", "w", "x", "y", "z"]
        alp_res = ""
        for a in listOfAlphabets:
            ranOne = random.randint(0, len(listOfAlphabets) - 1)
            alp_res = alp_res + listOfAlphabets[ranOne]
            if len(alp_res) == self.numOfAlphabets:
                break
        return alp_res

    def generate_chars(self):
        listOfChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?"]
        char_res = ""
        for a in listOfChars:
            ran = random.randint(0, len(listOfChars) - 1)
            char_res = char_res + listOfChars[ran]
            if len(char_res) == self.numOfChars:
                break
        return char_res

    def generate_numbers(self):
        listOfNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        num_res = ""
        for a in listOfNumbers:
            ran = random.randint(0, len(listOfNumbers) - 1)
            num_res = num_res + str(listOfNumbers[ran])
            if len(num_res) == self.numOfDigits:
                break
        return num_res

    def build_password(self):
        alphabets = self.generate_alphabets()
        numbers = self.generate_numbers()
        characters = self.generate_chars()
        ans = f"{alphabets} {numbers} {characters}"
        split_res = ans.split(" ")
        for x in split_res:
            split_res.reverse()
        fin = f"{split_res[0]}{split_res[1]}{split_res[2]}"
        return fin
