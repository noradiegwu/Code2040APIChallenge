import requests, json


tokenDict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b'}

# grab prefix and array
response = requests.post("http://challenge.code2040.org/api/prefix", data = tokenDict)

# turn to json dict
parsed_json = json.loads(response.text)

# grab values from prefix and array keys
prefix = parsed_json.get("prefix", "")
arr = parsed_json.get("array", [])

# remove the strings containing the prefix
arr = [s for s in arr if prefix not in s]

valDict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b', 'array': arr}

# post the array
validate = requests.post("http://challenge.code2040.org/api/prefix/validate", json = valDict)

print validate.status_code, validate.text
