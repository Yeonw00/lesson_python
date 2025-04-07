# 대문자 소문자가 섞인 잘못 쓰인 리스트가 있다면
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()

# def sample_func2(word):
#     return word.lower()

# sample_func = lambda word: word.capitalize()

change_words(l, lambda word: word.capitalize())

change_words(l, lambda word: word.lower())