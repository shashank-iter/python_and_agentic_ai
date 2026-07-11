# Class vs Static
# recieve cls (class itself as args) vs Recieve no automatic first arguements
# use case: operate on the class, not insatance vs utility function related to the class
# Access to CLS: Yes vs NO
# Access to Self No vs NO


class ChaiOrder:
    def __init__(self, tea_type, sweetness, size) -> None:
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    # cls has the referece for the class
    def from_dict(cls, order_data):
        return cls(order_data["tea_type"], order_data["sweetness"], order_data["size"])

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split(",")
        return cls(tea_type, sweetness, size)


order_one = ChaiOrder.from_dict(
    {"tea_type": "Green", "sweetness": "Medium", "size": "Large"}
)

order_two = ChaiOrder.from_string("Green,Medium,Large")

print(order_one.tea_type, order_one.sweetness, order_one.size)
print(order_two.tea_type, order_two.sweetness, order_two.size)
