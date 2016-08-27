import requests, json

# needle in a haystack

tokenDict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b'}

response = requests.post("http://challenge.code2040.org/api/haystack", data = tokenDict) # grab needle (string) and haystack (array of strings)

parsed_json = json.loads(response.text)

needle = parsed_json.get("needle")

haystack = parsed_json.get("haystack")

needleDict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b', 'needle': haystack.index(needle)} # find the index of needle in the haystack array

validate = requests.post("http://challenge.code2040.org/api/haystack/validate", data = needleDict) # post index and token

print validate.status_code
