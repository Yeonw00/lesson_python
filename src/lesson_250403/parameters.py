def menu(entree, drink, dessert):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu('beef', 'beer', 'icecream')
print('##################')
menu(entree='beef', dessert ='icecream', drink = 'beer')
print('##################')
menu('beef', dessert ='icecream', drink = 'beer')
# 이렇게는 에러
# menu( dessert ='icecream','beef', drink = 'beer')

print('##################')
def menu2(entree='beef', drink='beer', dessert='cookie'):
    print('entree = ', entree)
    print('drink = ', drink)
    print('dessert = ', dessert)

menu2(entree='chicken', drink='wine')
print('##################')
# 위치 인수와 키워드 인수는 섞어 쓸 수 있음
menu2('chicken', drink='wine')