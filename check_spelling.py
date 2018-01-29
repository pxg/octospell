import enchant


d = enchant.Dict("en_UK")
print(d.check("Hello"))
print(d.check("Helo"))
print(d.suggest("Helo"))
