import requests
import json


token_dict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b'}

# grab needle (string) and haystack (array of strings)
response = requests.post("http://challenge.code2040.org/api/haystack", data = token_dict)
parsed_json = json.loads(response.text)

needle = parsed_json.get("needle")
haystack = parsed_json.get("haystack")

# find the index of needle in the haystack array
needle_dict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b', 'needle': haystack.index(needle)}

# post index and token
validate = requests.post("http://challenge.code2040.org/api/haystack/validate", data = needle_dict)

print validate.status_code, validate.text
