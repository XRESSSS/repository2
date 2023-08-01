from pywebio.input import input as pw_input
from pywebio.input import NUMBER, PASSWORD, TEXT, DATETIME, COLOR
from pywebio.output import put_success, put_warning, put_code, popup, put_markdown, toast

user_nikname = str(pw_input('Enter ur nickname', required=False)).title().strip()
# user_age = str(pw_input('Enter ur age')).lstrip('0')
user_age = str(pw_input('Enter ur age', type=NUMBER, required=True)).lstrip('-')

admin = 'Eugeny'
promouter = 'John'

is_admin = user_nikname == admin
is_promouter = user_nikname == promouter
is_not_admin = user_nikname != admin

print(len(admin))

if is_admin:
    put_success('Salam ckrip')

elif user_nikname:
    put_success(f'Hello, {user_nikname}.')

    if user_age.isdigit():
        put_success(f'I know, you are {user_age} years old XD')


else:
    put_warning('You have not entered nickname. Shame on you, pal')

toast('lol, chel ti ckrip) XD')

if is_promouter:
    put_markdown('sold')
