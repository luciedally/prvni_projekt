"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Lucie Dally
email: lck21@seznam.cz
discord: lucie9855
"""
registered_users = {
    'bob': '123',
    'ann': 'pass123',
    'mike': 'password123',
    'liz': 'pass123'
}

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

print(40 * "-")
username = input("username:")
password = input("password:")
print(40 * "-")
if username in registered_users and registered_users[username] == password:
    print(f"Welcome to the app, {username}\nWe have 3 texts to by analyzed.")
    print(40 * "-")
    selected_text = int(input(f"Enter a number btw. 1 and 3 to select: "))
    if 1 <= selected_text <= len(TEXTS):
        selected_text -= 1
        print(40 * "-")
        text = TEXTS[selected_text]
        words = text.split()
        word_lengths = [len(word.strip(".,?!")) for word in words]
        word_counts = {}
        uppercase_words = 0
        lowercase_words = 0
        titlecase_words = 0
        numeric_count = 0
        numeric_sum = 0

        for word in words:
            cleaned_word = word.strip(".,?!")
            if cleaned_word.isnumeric():
                numeric_count += 1
                numeric_sum += int(cleaned_word)
            elif cleaned_word.istitle():
                titlecase_words += 1
            elif cleaned_word.islower():
                lowercase_words += 1
            elif cleaned_word.isupper():
                uppercase_words += 1

            if len(cleaned_word) in word_counts:
                word_counts[len(cleaned_word)] += 1
            else:
                word_counts[len(cleaned_word)] = 1

        print(f"There are {len(words)} words in the selected text.")
        print(f"There are {titlecase_words} titlecase words.")
        print(f"There are {uppercase_words} uppercase words.")
        print(f"There are {lowercase_words} lowercase words.")
        print(f"There are {numeric_count} numeric strings.")
        print(f"The sum of all the numbers {numeric_sum}")
        print(40 * "-")
        print("LEN|    OCCURRENCES    |NR.")
        print(40 * "-")
        for length in range(1, max(word_counts) + 1):
            count = word_counts.get(length, 0)
            stars = '*' * count
            print(f"{length:3}|{stars:19}|{count:2}")

    else:
        print("Invalid text selection. Program terminated.")
else:
    print("unregistered user, terminating the program.")
