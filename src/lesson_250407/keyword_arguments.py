def menu(entree='beef', drink='wine'):
    print(entree, drink)

menu(entree='beef', drink='coffee')

def menu2(**kwargs):
    # print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# menu2(entree='beef', drink='coffee')

d = {
    'entree': 'beef',
    'drink': 'iced coffee',
    'dessert': 'ice cream'
}
menu2(**d)

def menu3(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)

menu3('banana', 'apple', 'orange', entree='beef', drink='coffee')