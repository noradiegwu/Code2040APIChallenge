import requests

# token: b17d06b3ed94ee326a5f76be8999da9b

tokenDict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b'}

response = requests.post("http://challenge.code2040.org/api/reverse", data = tokenDict) # grab the string

string = response.text[::-1] # reverse it

valDict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b', 'string': string}

validate = requests.post("http://challenge.code2040.org/api/reverse/validate", data = valDict) # post the reversed string

print validate.status_code # check status code
