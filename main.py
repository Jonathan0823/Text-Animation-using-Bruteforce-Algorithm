import time
import string
import random

chars = string.ascii_letters + string.digits + string.punctuation + " "

def bruteforce_animation(text):
    result = ""
    is_running = True

    for letter in text:
        while is_running:
            randomized_char = random.choice(chars)
            time.sleep(0.0005)
            print(result + randomized_char)

            if randomized_char == letter:
                result += letter
                break

    

def main():
    text = input("Enter you want to animate: ")
    bruteforce_animation(text)
    pass

if __name__ == '__main__':
    main()