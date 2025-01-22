import os 
os.system('cls')
import codecs

def rot13_encrypt_decrypt(text):
    return codecs.encode(text, 'rot_13')

def main():
    print("Izvēlieties valodu (ievadiet ciparu) | Choose language (enter a number):")
    print("1. Latviešu")
    print("2. English")
    language_choice = input("Jūsu izvēle | Your choice: ")

    if language_choice == "1":
        lang = "lv"
    elif language_choice == "2":
        lang = "en"
    else:
        print("Nepareiza izvēle | Invalid choice")
        return

    if lang == "lv":
        print("Izvēlieties darbību (ievadiet ciparu):")
        print("1. Šifrēt")
        print("2. Atšifrēt")
    else:
        print("Choose an action (enter a number):")
        print("1. Encrypt")
        print("2. Decrypt")

    action_choice = input("Jūsu izvēle | Your choice: ")

    if action_choice not in ["1", "2"]:
        if lang == "lv":
            print("Nepareiza izvēle")
        else:
            print("Invalid choice")
        return

    if lang == "lv":
        text = input("Ievadiet tekstu, lai apstrādātu: ")
    else:
        text = input("Enter the text to process: ")

    result = rot13_encrypt_decrypt(text)

    if lang == "lv":
        print("Rezultāts:", result)
    else:
        print("Result:", result)

if __name__ == "__main__":
    main()
