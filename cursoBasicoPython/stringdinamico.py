def greet(name):

    return f"Hello, {name} how are you doing today?"


s = "eloquent"
def remove_char(s):
    return s[1:-1]


print(remove_char(s))


name = 'Martin'


names = ['Alex', 'Jacob', 'Mark', 'Max']
names1 = ['Max', 'John', 'Mark']


def likes(names):
    print(min(4, 3))
    if not names:
        return f'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} likes this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} likes this'
    if len(names) > 3:
        return f'{names[0]}, {names[1]} and {len(names)-2} others like this'


def likes1(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this',
        2: '{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


print(likes(names))
