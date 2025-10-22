# This code demonstrates how to automate a automated a case-preserving text replacement using re.sub() with a replacement function
import re

# 1️⃣ Read text from the original file
input_path = "/Users/manishasasatte/Manisha-Portfolio/Python-Concept/temp_data_collection.py"
output_path = "/Users/manishasasatte/Manisha-Portfolio/Python-Concept/05_tuple.py"

# 1️⃣ Read the file
with open(input_path, "r") as file:
    text = file.read()

# 2️⃣ Define a dynamic replacement function that preserves case
def replace_with_case(match):
    word = match.group()
    if word.isupper():
        return "TUPLE"
    elif word[0].isupper():
        return "Tuple"
    else:
        return "tuple"

# 3️⃣ Replace *any* occurrence of “list” (even inside other words)
updated_text = re.sub(r'list', replace_with_case, text, flags=re.IGNORECASE)

# 4️⃣ Write to the new file
with open(output_path, "w") as file:
    file.write(updated_text)

print(f"✅ Automatic replacement done. File saved as:\n{output_path}")

