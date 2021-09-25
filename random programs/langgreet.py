# defined the greet function which takes an input and compares it

def greet(lang):
    if lang == 'english':
        print('Hello')
    elif lang == 'spanish':
        print('Hola')
    elif lang == 'french':
        print('Bonjour')
    else:
        print("Sorry, I don't know that language.")
greeting = input("What language do you speak?")
greeting = greeting.lower()
greet(greeting)