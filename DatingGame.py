import requests
import json
from datetime import datetime, timedelta


token_dict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b'}

# grab the date dict
response = requests.post("http://challenge.code2040.org/api/dating", data = token_dict)

# turn to json dict
parsed_json = json.loads(response.text)

# grab values from json
datestamp = parsed_json.get("datestamp", "")
interval = parsed_json.get("interval", 0)
# datestamp: 2016-09-24T10:14:42Z interval: 161717

# convert to datetime for simple adding
datetime_obj = datetime.strptime(datestamp, "%Y-%m-%dT%H:%M:%SZ")

# add interval
new_date = datetime_obj + timedelta(0, interval)

# put new_date obj into correct string format
new_datestamp = "%02d-%02d-%02dT%02d:%02d:%02dZ" % (new_date.year, new_date.month,
new_date.day, new_date.hour, new_date.minute, new_date.second)

val_dict = tokenDict = {'token': 'b17d06b3ed94ee326a5f76be8999da9b', 'datestamp': new_datestamp}

validate = requests.post("http://challenge.code2040.org/api/dating/validate", data = val_dict)

print validate.status_code, validate.text
