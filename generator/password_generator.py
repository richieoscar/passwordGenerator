import random


class PasswordGenerator:

    def __init__(self, numOfAlphabets, numOfDigits, numOfChars):
        self.numOfAlphabets = numOfAlphabets
        self.numOfChars = numOfChars
        self.numOfDigits = numOfDigits

    def generate_alphabets(self):
        listOfAlphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                           "s", "t",
                           "u", "v", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L",
                           "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        alp_res = ""
        for a in listOfAlphabets:
            ranOne = random.choice(listOfAlphabets)
            alp_res += ranOne
            if len(alp_res) == self.numOfAlphabets:
                break
        return alp_res

    def generate_chars(self):
        listOfChars = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "<", ">", "?"]
        char_res = ""
        if self.numOfChars == 0:
            print("Recommend special characters to increase password strength")
            return char_res
        for a in listOfChars:
            ran = random.choice(listOfChars)
            char_res += ran
            if len(char_res) == self.numOfChars:
                break
        return char_res

    def generate_numbers(self):
        num_res = ""
        if self.numOfDigits == 0:
            print("Recommend numbers to increase password strength")
            return num_res
        listOfNumbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        for a in listOfNumbers:
            ran = random.choice(listOfNumbers)
            num_res += str(ran)
            if len(num_res) == self.numOfDigits:
                break
        return num_res

    def build_password(self):
        alphabets = self.generate_alphabets()
        numbers = self.generate_numbers()
        characters = self.generate_chars()
        total = len(alphabets) + len(numbers) + len(characters)
        ans = f"{alphabets}{numbers}{characters}"
        password = ""
        arr = []
        for n in ans:
            arr.append(n)
        random.shuffle(arr)
        for i in arr:
            password += i
        return password
