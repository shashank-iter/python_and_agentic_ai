class ChaiUtils:
    # its a decorator which allows to use methods without object creation
    @staticmethod
    def clean_ingedients(text):
        return [item.strip() for item in text.split(",")]


raw = "ginger "

# obj = ChaiUtils()

# cleaned = obj.clean_ingedients(raw)

cleaned = ChaiUtils.clean_ingedients(raw)

print(cleaned)
