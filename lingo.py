class Lingo:
    def __init__(self):
        self.woord = "appel"  # Kies hier zelf een woord van vijf letters!

    def validate_input(self, woord):
        if len(woord) != len(self.woord):
            return "Ongeldige invoer. Het woord moet vijf letters bevatten."
        elif woord == self.woord:
            return "Gefeliciteerd! Je hebt het woord geraden."
        else:
            resultaat = ""
            for i in range(len(woord)):
                if woord[i] == self.woord[i]:
                    resultaat += woord[i]
                else:
                    resultaat += "*"
            return resultaat