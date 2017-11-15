import requests

# ****************************************************************************************
#  GLOBALS
# ****************************************************************************************
DOMINICA_PSS_BENEFICIARY_REGISTRAION = "180708"  # FORMS TO DOWNLOAD
DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING = "177644"  # ...............................
DOMINICA_CTP_BENEFICIARY_REGISTRATION = "175621"  # ......................................
URL = "https://kc.humanitarianresponse.info/api/v1/forms/"  # API ENDPOINT


# *****************************************************************************************
#  PERFORM ACTION
# *****************************************************************************************
def _perform(user, password):
    response = requests.get(URL + DOMINICA_PSS_BENEFICIARY_REGISTRAION, auth=(user, password))
    data = response.json()
    print "====================================================="
    print " "

    print "==> " + data['title'] + " =="
    print "==> " + data['date_modified'] + " =="
    print "==> Downloading [  =========  ] "
    response = requests.get(URL + DOMINICA_PSS_BENEFICIARY_REGISTRAION + ".csv",  auth=(user, password))
    with open("C:/Users/g-sta/Desktop/test1.csv", "wb") as code:
        code.write(response.content)

    response = requests.get(URL + DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING,  auth=(user, password))
    data = response.json()
    print " "
    print "==> " + data['title'] + " =="
    print "==> " + data['date_modified'] + " =="
    print "==> Downloading [  =========  ] "
    response = requests.get(URL + DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING + ".csv",  auth=(user, password))
    with open("C:/Users/g-sta/Desktop/test2.csv", "wb") as code:
        code.write(response.content)

    response = requests.get(URL + DOMINICA_CTP_BENEFICIARY_REGISTRATION,  auth=(user, password))
    data = response.json()
    print " "
    print "==> " + data['title'] + " =="
    print "==> " + data['date_modified'] + " =="
    print "==> Downloading [  =========  ] "
    response = requests.get(URL + DOMINICA_CTP_BENEFICIARY_REGISTRATION + ".csv",  auth=(user, password))
    with open("C:/Users/g-sta/Desktop/test3.csv", "wb") as code:
        code.write(response.content)

    print " "
    print "====================================================="


# *****************************************************************************************
#  ADD CREDS TO RUN
# *****************************************************************************************
_perform("", "")