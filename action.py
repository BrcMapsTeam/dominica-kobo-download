import requests
import datetime

# ****************************************************************************************
#  GLOBALS
# ****************************************************************************************
DOMINICA_PSS_BENEFICIARY_REGISTRAION = "180708"  # FORMS TO DOWNLOAD
DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING = "177644"  # ...............................
DOMINICA_CTP_BENEFICIARY_REGISTRATION = "175621"  # ......................................
URL = "https://kc.humanitarianresponse.info/api/v1/forms/"  # API ENDPOINT
# ........................................................................................
# START HERE -- ENTER CREDS .ETC
USER = ""
PASSWORD = ""
DOWNLOAD_HERE = ""
# ........................................................................................


# *****************************************************************************************
#  PERFORM ACTION
# *****************************************************************************************
def _perform(user, password, download_here):

    print "[ Performing acton ======================================= ]"
    log_time = str(datetime.datetime.utcnow())
    log = open(download_here + 'log.txt', 'a')
    log.write("=====================================================\n")
    log.write("New log entry: " + log_time + "\n")
    log.write("=====================================================\n")

    response = requests.get(URL + DOMINICA_PSS_BENEFICIARY_REGISTRAION, auth=(user, password))
    data = response.json()
    log.write("=====================================================\n")
    log.write(" ")

    log.write("==> " + data['title'] + " ==\n")
    log.write("==> " + data['date_modified'] + " ==\n")
    log.write("==> Downloading [ 0%  =========  ] \n")
    log.write("==> " + "Done.\n")
    response = requests.get(URL + DOMINICA_PSS_BENEFICIARY_REGISTRAION + ".csv",  auth=(user, password))
    with open(download_here + "dominica_pss_beneficiary_registration" + ".csv", "wb") as code:
        code.write(response.content)

    response = requests.get(URL + DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING,  auth=(user, password))
    data = response.json()
    log.write("==> " + data['title'] + " ==\n")
    log.write("==> " + data['date_modified'] + " ==\n")
    log.write("==> Downloading [ 0%  =========  ] \n")
    log.write("==> " + "Done.\n")
    response = requests.get(URL + DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING + ".csv",  auth=(user, password))
    with open(download_here + "dominica_relief_post_distribution_monitoring" + ".csv", "wb") as code:
        code.write(response.content)

    response = requests.get(URL + DOMINICA_CTP_BENEFICIARY_REGISTRATION,  auth=(user, password))
    data = response.json()
    log.write("==> " + data['title'] + " ==\n")
    log.write("==> " + data['date_modified'] + " ==\n")
    log.write("==> Downloading [ 0%  =========  ] \n")
    log.write("==> " + "Done.\n")
    response = requests.get(URL + DOMINICA_CTP_BENEFICIARY_REGISTRATION + ".csv",  auth=(user, password))
    with open(download_here + "dominica_ctp_beneficiary_registration" + ".csv", "wb") as code:
        code.write(response.content)

    log.write("=====================================================\n")
    print "[ Done =================================================== ]"


# *****************************************************************************************
#  ADD CREDS TO RUN
# *****************************************************************************************
_perform(USER, PASSWORD, DOWNLOAD_HERE)