import string

with open('design/email_template.txt') as f:
    # t는 with 밖에서도 사용 가능
    t = string.Template(f.read())

contents = t.substitute(name='Odung', contents='How are you?')
print(contents)
