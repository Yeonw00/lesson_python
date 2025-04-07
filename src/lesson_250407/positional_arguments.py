# 이 방법은 파라미터를 다 써야함
# def say_something(word, word2, word3):
#     print(word)
#     print(word2)
#     print(word3)

# 값을 튜플에 넣어주는 방법
def say_something(*args):
    for arg in args:
        print(arg)

say_something('Hi', 'Mike', 'Nance')

# 위치인수랑 튜플을 섞어 쓰는 것도 가능
def say_something2(word, *args):
    print('word = ', word)
    for arg in args:
        print(arg)

say_something2('Hi', 'Mike', 'Nance')

# t = ('Mike', "Nancy")
# say_something2('Hi', *t)