# strings are immutable
chai_type = "Ginger Chai"
print(f"{chai_type}")

# last number is not inclusive while slicing

chai_des = "Aromatic and Bold"
print(f"First Word: {chai_des[0:8]}")
print(f"Each Character: {chai_des[0:8:1]}")
print(f"Every Second Character: {chai_des[0:8:2]}")
print(f"First Word: {chai_des[:8]}")
print(f"Last Word: {chai_des[12:]}")
print(f"Reverse: {chai_des[::-1]}")

label_text = "Chai Special"
encoded_text = label_text.encode("utf-8")
print(f"Encoded-text: {encoded_text}")
decoded_text = encoded_text.decode("utf-8")
print(f"de-coded-text: {decoded_text}")
