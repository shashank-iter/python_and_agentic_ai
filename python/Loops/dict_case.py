# example to use loops on dict

users = [
    {"id": 1, "total": 100, "coupon": "P20"},
    {"id": 2, "total": 150, "coupon": "F20"},
    {"id": 3, "total": 250, "coupon": "M20"},
]

discounts = {"P20": (0.2, 0), "F20": (0.5, 0), "M20": (0, 10)}

for user in users:
    percent, fixed = discounts.get(user["coupon"], (0, 0))
    discount = user["total"] * percent + fixed
    print(
        f"User: {user['id']} paid {user['total']} and got next visit discount of {discount}"
    )
