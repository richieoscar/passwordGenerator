# Press the green button in the gutter to run the script.
import generator.password_generator

if __name__ == '__main__':
    print("PASSWORD GENERATOR PROGRAM")
    numOfAphabets = input("Enter number of alphabets\n")
    numOfDigits = input("Enter number of Digits\n")
    numOfChars = input("Enter number of characters\n")
    gen = generator.password_generator.PasswordGenerator(int(numOfAphabets), int(numOfDigits), int(numOfChars))
    password = gen.build_password()
    print(f"Password = {password}")
