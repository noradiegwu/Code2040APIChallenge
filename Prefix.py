import requests
import json
from sys import getsizeof


token_dict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b'}

# grab prefix and array
response = requests.post("http://challenge.code2040.org/api/prefix", data = token_dict)

# turn to json dict
parsed_json = json.loads(response.text)

# grab values from prefix and array keys
prefix = parsed_json.get("prefix", "")
arr = parsed_json.get("array", [])

nofix_arr = []
for s in arr: # O(n)
    if prefix not in s:
        nofix_arr.append(s) # O(1) * n - number of strings containing prefix (worst case all strings)

# count = 0
# for i in xrange(len(arr)): # O(n)
#     a = i - count # create flexible indexer
#     print "a", id(a), "size:", getsizeof(a)
#     # though I did not need to create a new list, because integers are immutable,
#     # with every reassignment python is allocating new memory for that new integer
#     # because the memory was allocated 11 times (including the first time) and the size of this int on my machine is 24 bytes
#     # the memory savings here was actually 8 bytes. Small but still cool to see.
#     # But the time cost, with my limited googled knowledge, seems to be much bigger
#     # at O(n) + O(n^2) compared to the first one's O(n) + O(n) which I believe reduces to O(n)
#     # So comparing the time and space usage, the above algorithm is more efficient
#     if prefix in arr[a]: # if prefix in that posn
#         count+=1 # tally it
#         del arr[a] # and remove the word in that spot # O(n) run - at worst - n times --> O(n^2)

val_dict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b', 'array': nofix_arr}

# post the array
validate = requests.post("http://challenge.code2040.org/api/prefix/validate", json = val_dict)

# check response
print validate.status_code, validate.text
