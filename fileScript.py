# write content inside a .txt file

def readFile(file):

    try:
        assert(file.readable)
        print(file.read())
        # file.write('hello, stranger \n')
        # file.close()
        # print(file.read())
    except Exception as e:
        print(f'file error --> {e}')


def createAndOpenFile():

    try:
        f = open('file.txt', 'r+')
        readFile(f)
    except FileExistsError:
        f = open('file.txt', 'r+')
        readFile(f)


createAndOpenFile()
