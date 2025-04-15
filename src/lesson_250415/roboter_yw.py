import csv
from os.path import exists


def ask_name():
    name = input('안녕하세요! 저는 Roboko 입니다. 당신의 이름은 무엇인가요?')
    ask_restaurant(name)

def ask_restaurant(name):
    if not exists('ranking.csv'):
        restaurant = input(f'{name}씨, 좋아하시는 레스토랑의 이름은 무엇인가요?')
        make_restaurant_list(restaurant)
    else:
        popular_restaurant = check_restaurant_list()
        input(f'추천드리는 레스토랑은 {popular_restaurant}입니다.\n이 레스토랑을 좋아하세요?[Yes/No]')
        restaurant = input(f'{name}씨, 좋아하시는 레스토랑의 이름은 무엇인가요?')
        make_restaurant_list(restaurant)

    say_goodbye(name)

def say_goodbye(name):
    print(f'{name}씨, 감사합니다.\n좋은 하루 보내세요! 안녕히가세요.')

def make_restaurant_list(restaurant):
    found = False
    rows = read_restaurant_lists()

    for row in rows:
        if row['Name'] == restaurant:
            row['Count'] = str(int(row['Count']) + 1)
            found = True
            break

    if not found:
        rows.append({'Name': restaurant, 'Count': '1'})

    create_restaurant_list(rows)


def read_restaurant_lists():
    try:
        with open('ranking.csv', 'r', newline='') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []

def create_restaurant_list(rows):
    fieldnames = ['Name', 'Count']
    with open('ranking.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

def check_restaurant_list():
    reader = read_restaurant_lists()
    count = 0
    popular_restaurant = ''
    for row in reader:
        cnt = int(row['Count'])
        if cnt > count:
            popular_restaurant = row['Name']
            count = cnt
    return popular_restaurant


def main():
    ask_name()

if __name__ == '__main__':
    main()


