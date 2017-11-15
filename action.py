import requests

# ****************************************************************************************
#  GLOBALS
# ****************************************************************************************
DOMINICA_PSS_BENEFICIARY_REGISTRAION = "180708"                     # FORMS TO DOWNLOAD
DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING = "177644"             # ......................
DOMINICA_CTP_BENEFICIARY_REGISTRATION = "175621"                    # ......................
URL = "https://kc.humanitarianresponse.info/api/v1/forms/"          #  CREDS / API ENDPOINT
USER_1 = ""                                                         # DRC_1
PASSWORD_1 = ""                                                     # ......................
USER_2 = ""                                               # DRC_2
PASSWORD_2 = ""

# *****************************************************************************************
#  PERFORM ACTION
# *****************************************************************************************

response = requests.get(URL + DOMINICA_PSS_BENEFICIARY_REGISTRAION,
                        auth=(USER_2, PASSWORD_2 ))
data = response.json()
print "====================================================="
print "==> " + data['title'] + " =="
print "==> " + data['date_modified'] + " =="
print "====================================================="

response = requests.get(URL + DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING,
                        auth=(USER_2, PASSWORD_2 ))
data = response.json()
print "====================================================="
print "==> " + data['title'] + " =="
print "==> " + data['date_modified'] + " =="
print "====================================================="

response = requests.get(URL + DOMINICA_CTP_BENEFICIARY_REGISTRATION,
                        auth=(USER_2, PASSWORD_2 ))
data = response.json()
print "====================================================="
print "==> " + data['title'] + " =="
print "==> " + data['date_modified'] + " =="
print "====================================================="

# print "Downloading ... "
# r = requests.get(URL)
# with open("C:/Users/g-sta/Desktop/test.xls", "wb") as code:
#     code.write(r.content)