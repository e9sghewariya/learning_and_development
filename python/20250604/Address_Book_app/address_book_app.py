"""Address Book Assignment
This assignment focuses on creating an
address book application that reads and writes data in JSON format.
"""

# ## Questions

# **1. `read_file(filename)`**

# Input file is address_file if provided and $HOME/addressbook.json if not provided.

# Assume that all data is stored in the input file as JSON.

# Return a list of dictionaries where each dictionary is one address record.

# ```
# def read_file(json_file: str = None):
#     """
#     Read in a json file and return a list of dictionaries in address_book format
#     """
#     return
# ```

# ```python
# data = read_file()
# ```
import json
import os


def read_file(json_file: str = None):
    """
    Read a JSON file and return address_book list
    """
    if json_file is None:
        json_file = os.path.join(os.environ["HOME"], "addressbook.json")
    try:
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []


# **2. `write_file(data, filename)`**

# Write the contents of address_book to a json file.

# Use the file specified in json_file if provided and in $HOME/addressbook.json if not.

# Output format of the file must be JSON.

# Return the number of records written if successful. Return None if not successful.

# ```
# def write_file(address_book, json_file):
#     return -1
# ```

# ```python
# number_of_records = write_file(data)
# ```

# ```python
# number_of_records = write_file(data, "fubar.json")
# ```


def write_file(address_book, json_file: str = None):
    """
    Write address_book data to a JSON file
    """
    if json_file is None:
        json_file = os.path.join(os.environ["HOME"], "addressbook.json")
    try:
        with open(json_file, "w", encoding="utf-8") as f:
            json.dump(address_book, f, indent=4)
        return len(address_book)
    except (OSError, TypeError, json.JSONDecodeError):
        return None


# **3. `list_names(data)`**

# Retun a list of names in address_book.

# ```
# In [1]: list_names(data)
# Out[1]: ["Bugs Bunny", "Bruce Wayne"]
# ```


def list_names(data):
    """
    Return a list of names from the address_book data
    """
    return [entry["name"].title() for entry in data]


# **4. `add_name()`**

# Add the name to `address_data` if and
# only if there is no existing record with
# the same name, email, and dob.

# Return a tuple of (data, boolean) where `data`
# is address_book format of data and boolean is
# True if record was created and False if record already existed.

# ```
# def add_name(data, name, email, dob):
#     return (data, False)
# ```


# ```
# In [1]: data, created = add_name(data, "Superman", "kal-el@krypton.com", "1938-04-18")
# ```
def add_name(data, name, email, dob):
    """
    Add a new name to the address_book data if it does not already exist
    """
    for entry in data:
        if (
            entry["name"].lower() == name.lower()
            and entry["email"].lower() == email.lower()
            and entry["dob"] == dob
        ):
            return data, False

    data.append({"name": name, "email": email, "dob": dob})
    return data, True


# **5. `search_name()`**

# Return a list of names that are a superset of the provided name to be searched.

# Searches must be case insensitive.

# ```
# def search_name(data, name):
#     return List
# ```

# ```
# In [1]: search_name(data, "vish")
# Out[1]: ["Vishal Apte", "Dhruv Vishveshwar", "Avishka Menon"]
# ```


def search_name(data, name="vish"):
    """
    Search for names in the address_book data that contain the given name
    """
    name = name.lower()
    return [entry["name"].title() for entry in data if name in entry["name"].lower()]


# **6. `update_name(data)`**

# Update email and dob for the record for
# the given name if there is only one record
# with that name regardless of capitalization.

# Return a tuple of (data, boolean) where `data`
# is address_book format of data boolean is True
# if record was updated and False if not


# ```
# def update_name(data, name, email, dob):
#     return data, True
# ```
def update_name(data, name, email, dob):
    """
    Update the email and dob for a name in the
    address_book data if there is only one record with that name
    """
    matches = [entry for entry in data if entry["name"].lower() == name.lower()]
    if len(matches) == 1:
        matches[0]["email"] = email
        matches[0]["dob"] = dob
        return data, True
    return data, False


# **7. `delete_name(data, name)`**

# Delete the dict entry in the list for
# the record for the given name if there
# is only one record with that name regardless of capitalization.

# Return a tuple of (data, boolean) where `data`
# is address_book format of data and boolean is
# True if record was deleted and False if not

# ```
# def delete_name(data, name):
#     return data, True
# ```


def delete_name(data, name):
    """
    Delete a name from the address_book
    data if there is only one record with that name
    """
    count = 0
    idx_to_remove = -1
    for idx, entry in enumerate(data):
        if entry["name"].lower() == name.lower():
            count += 1
            idx_to_remove = idx
    if count == 1:
        del data[idx_to_remove]
        return data, True
    return data, False


# **8. `print_names(data)`**

# Print a formatted list of all names in `address_data`.

# Data should be sorted by DOB in ascending order.

# Date should be in the exact format shown.

# Column widths must be as specified exactly:
# - Name: 24
# - Email: 36
# - DOB: 12

# ```
# In [1]: print_names(data)
# Out[1]:
# Name                    Email                              DOB
# Superman                kal-el@krypton.com                 1938-04-18
# Bruce Wayne             bruce@wayne.com                    1939-03-30
# Bugs Bunny              bugs@warnerbros.com                1940-07-27
# ```


def print_names(data):
    """
    Print a formatted list of names
    from the address_book data sorted by DOB
    """
    sorted_data = sorted(data, key=lambda x: x["dob"])
    print(f"{'Name':24}{'Email':36}{'DOB':12}")
    for entry in sorted_data:
        name = entry["name"].title()
        email = entry["email"]
        dob = entry["dob"]
        print(f"{name:24}{email:36}{dob:12}")
