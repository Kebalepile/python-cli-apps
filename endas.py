import pandas

file = open('./batho.txt', 'a')

data = [
    ['kebalepile', 'motshoana', 'male', 'afrikan', 23],
    ['kagisho', 'motshoana', 'male', 'afrikan', 56],
    ['phaladi', 'motshoana', 'male', 'afrikan', 17],
    ['kediemetse', 'motshoana', 'female', 'afrikan', 49],
    ['omphemetse', 'motshoana', 'male', 'afrikan', 11]
]

dataFrame = pandas.DataFrame(
    data, columns=['name', 'surname', 'gender', 'ethnic', 'age'])

# file.write(str(dataFrame))
print(dataFrame.mean().mean())
