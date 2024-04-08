from enum import Enum
from collections import defaultdict

# Define an Enum for the possible values
class Name(Enum):
    Amr = "Amr"
    Ahmed = "Ahmed"
    Default = "Default"

# Define default values for each key
default_values = {
    "key1": Name.Default.value,
    "key2": Name.Default.value,
    "key3": Name.Default.value,
    # Add more keys and default values as needed
}

# Create a defaultdict with a lambda function that retrieves the default value from the dictionary
x = defaultdict(lambda: Name.Default.value)
x.update(default_values)

# Access keys and assign values
x["key1"] = Name.Amr.value
x["key2"] = Name.Ahmed.value

# Attempting to assign a value other than Amr, Ahmed, or Default will raise an error
try:
    x["key4"] = Name("random")
    print(x["key4"])  # Output: Default
except Exception as e:
    print("Error:", e)
    print(e)  # Output: 'random' is not a valid Name
    print(x["key4"])  # Output: Default

# Access keys that don't exist (each will use its respective default value)
print(x["key1"])  # Output: Amr
print(x["key2"])  # Output: Ahmed
print(x["key3"])  # Output: Default



"""
from enum import Enum

class Name(Enum):
    Amr = 'Amr'
    Ahmed = 'Ahmed'

# Usage
x = Name.Amr.value  # Valid
print(x)  # Output: Name.Amr

# This will raise an error when trying to access the variable through the Enum
x = 'John'
print(Name(x).value)  # Raises ValueError: 'John' is not a valid Name

# This does not raise an error because 'John' is assigned directly to the variable
x = 'John'
print(x)  # Output: John

"""