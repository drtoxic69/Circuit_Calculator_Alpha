from contextlib import contextmanager

@contextmanager
def file(filename, methord):
    print('Enter')
    file = open(filename, methord)
    yield file
    file.close()
    print('Exit')


with file('text.txt', 'o') as f:
    print('Middle')
    f.write('hello ke bofelo')

