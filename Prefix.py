import requests
import json


token_dict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b'}

# grab prefix and array
response = requests.post("http://challenge.code2040.org/api/prefix", data = token_dict)

# turn to json dict
parsed_json = json.loads(response.text)

# grab values from prefix and array keys
prefix = parsed_json.get("prefix", "")
arr = parsed_json.get("array", [])

print arr, prefix
# remove the strings containing the prefix
nofix_arr = []
for s in arr:
    if prefix not in s:
        nofix_arr.append(s)

print nofix_arr

# # original idea
# for s in arr:
#     if prefix in s:
#         arr.remove(s)
# # with this i had the intention of not needing to create a new array and simply editing the existing one
# # but this created an issue because of how python interprets arrays as lists
# # when I would remove a string at that index, the list would shift down from there
# # and continue iterating while skipping over the string that shifted into the previous posn
# # so this loop would remove some strings while ignoring the strings directly after the ones removed
# # especially annoying when the prefix is in two (or three) consecutive strings
# # while googling, i found list comprehension: arr = [s for s in arr if prefix not in s] which did the trick
# # but as it turns out, python essentially creates a list of None values with comprehension
# # so considering the "zen of python", readibility conquers here
# # still in search of a solution!

val_dict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b', 'array': nofix_arr}

# post the array
validate = requests.post("http://challenge.code2040.org/api/prefix/validate", json = val_dict)

print validate.status_code, validate.text
