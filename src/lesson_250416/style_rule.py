# 파이썬에서는 문장 끝에 ;를 안써도 된다
x = 1;
y = 2;

# 값의 길이는 80개 이내로 하자는 룰이 있기때문에 그 이상일때는 줄바꿈을 할 것
x = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'

# 길이가 긴 변수는 줄바꿈
def test_func(x, y, z,
              asfjslfaj;lfsjlsjfasj;fajfslkdjf;sfjssdfsf='test')

    """
    함수 설명하는 url을 넣을 때는 길이가 80을 넘어도 괜찮음
    see details at: http://sakaijunappspot.com/document//fasdfdlkfjfl;jdgaj;slgksjdgj;lsjgaskgj;ksjg;
    """
    print('test')

# x and y를 괄호로 묶지 않아도 됨
if x and y:
    #스페이스 4개 넣고 들여쓰기
    print('exit')

    # 사전형도 스페이스 4개
    x = {
        'test': 'sss'
    }
    # 한줄로 할 때는 중괄호 다음 스페이스 없음, 콜론 이후에 스페이스 하나 넣어줌
    y = {'test': 'sss'}

    # 스페이스 이렇게 쓸 것
    x, y = y, x

    # 연산자 전 후에도 스페이스 하나 넣어주기
    x + y

    #함수 사이에는 두줄이 띄워져있음
    def a():
        pass


    def b():
        pass

    # 클래스 안에서 메소드 사이에는 줄 하나씩
    # 클래스는 제일 처음은 대문자로하고 camel case 사용
    class ExampleClass():
        # 함수와 변수는 snake case 사용
        def a_and_b(self):
            pass

        def b_and_c(self):
            pass


#import 후에도 두줄 띄워쓰기

word = 'hello'
word2 = '!'


# 직관적으로 알기 쉬움
new_word = word + word2
# 이런경우엔 아래의 방법이 더 보기 쉬울수도 있음
#new_word = '{} $$$$$$ {} !!!!!!'.format(word, word2)

long_word = ""
for word in ['fsdaf', 'dafad', 'dafa']:
    long_word += word

long_word = ""
for word in ['fsdaf', 'dafad', 'dafa']:
    long_word.append("{}fdsafsd".format(word))
new_long_word = ''.join(long_word)

# ""나 ''둘다 괜찮음 -> 회사에 따라서
print('fsdafs')
print("dsfafds")
# 중간에 '를 써야할 때는 ""를 쓸 수도 있고
print("fdsadsf'dsfs")
# 이런 방식도 있음
"fdsfafsd {} fdsafdf".format('test')

# todo를 쓰는 방법
# TODO (odung@gmail.com) 내용

# if문 스타일은 회사의 방식에 따라 쓰면 됨
if x:
    print('exit')
else:
    print('else')

if x: print('exit')
else: print('else')

# 글로벌 변수는 다 대문자
DEFAULT_ROBOT_NAME = 'Roboko'
