import requests, json

#  code2040 API Challenge
# POST to url: a JSON dict with two keys (token & github) with my api token and c2040 repo as values
# POST to here: http://challenge.code2040.org/api/register
# My API Token: b17d06b3ed94ee326a5f76be8999da9b

registrationJSON = {'token': 'b17d06b3ed94ee326a5f76be8999da9b', 'github': 'https://github.com/noradiegwu/Code2040APIChallenge'}

response = requests.post("http://challenge.code2040.org/api/register", data=registrationJSON)

print response.status_code
