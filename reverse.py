import requests

# token: b17d06b3ed94ee326a5f76be8999da9b

token_dict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b'}

response = requests.post("http://challenge.code2040.org/api/reverse", data = token_dict) # grab the string

string = response.text[::-1] # reverse it

val_dict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b', 'string': string}

validate = requests.post("http://challenge.code2040.org/api/reverse/validate", data = val_dict) # post the reversed string

print validate.status_code, validate.text # check status code and text
