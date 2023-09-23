a = int(input())
b = int(input())
def before():
    print(f'Before:')
    print(f'a = {a}')
    print(f'b = {b}')

def after():
    print(f'After:')
    print(f'a = {b}')
    print(f'b = {a}')
before()
after()
