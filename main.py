from lingo import Lingo

lingo = Lingo()
ingevoerd_woord = input("Voer een woord in van vijf letters: ")
resultaat = lingo.validate_input(ingevoerd_woord)
print("Resultaat: " + resultaat)