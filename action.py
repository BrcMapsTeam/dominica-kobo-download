import requests

# ***********************************************************
#  CREDS / API ENDPOINT
# ***********************************************************

URL = "https://kc.humanitarianresponse.info/api/v1/forms?format=json"

# DRC_1
USER_1 = ""
PASSWORD_1 = ""

# DRC_2
USER_2 = ""
PASSWORD_2 = ""

# ***********************************************************
#  PERFORM ACTION
# ***********************************************************

response = requests.get(URL,
                        auth=(USER_2, PASSWORD_2))
data = response.json()
print data
