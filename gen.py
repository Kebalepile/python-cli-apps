def drawCard():
    yield "10 of diamonds"
    i = yield "Ace of Spades"
    print(i)
    yield "Seven of Hearts"
    yield card


iterator = drawCard()

card = next(iterator)

print(dir(card))
# card = iterator("5 of diamond")

print(card)
card = next(iterator)

print(card)
card = next(iterator)

print(card)
