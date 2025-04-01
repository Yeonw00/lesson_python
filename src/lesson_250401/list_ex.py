def get_on_the_car(seat:list[str]) -> bool:
    min = 0
    max = 5
    if min <= len(seat) < max:
        return True
    else:
        return False

def call_get_on_the_car():
    seat = []
    seat.append("p")
    seat.append("p")
    seat.append('p')
    seat.append('p')
    print(get_on_the_car(seat))

call_get_on_the_car()



