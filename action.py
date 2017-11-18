'''
    Author: Austin Lazarus
    Email: austin.lazarus@gmail.com
    Tel: +1 (767) - 614 - 4347
'''
import requests
import datetime

# ****************************************************************************************
#  GLOBALS
# ****************************************************************************************
DOMINICA_PSS_BENEFICIARY_REGISTRAION = "180708"  # FORMS TO DOWNLOAD
DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING = "177644"  # ...............................
DOMINICA_CTP_BENEFICIARY_REGISTRATION = "175621"  # ......................................
DOMINICA_WASH_HYGIENE_PROMOTION_REGISTRATION = "183099"
URL = "https://kc.humanitarianresponse.info/api/v1/forms/"  # API ENDPOINT
# ........................................................................................
# START HERE -- ENTER CREDS .ETC
USER = ""
PASSWORD = ""
USER_2 = ""
PASSWORD_2 = ""
DOWNLOAD_HERE_LOGS = r'\\192.168.88.190\im_rcd\00______DATABASE______'
DOWNLOAD_HERE_DPBR = r'\\192.168.88.190\im_rcd\00______DATABASE______\02____PSS_Beneficiary_Data'
DOWNLOAD_HERE_RPDM = r'\\192.168.88.190\im_rcd\00______DATABASE______\04____RELIEF_Post_Distribution_Monitoring'
DOWNLOAD_HERE_CBR = r'\\192.168.88.190\im_rcd\00______DATABASE______\01____CTP_Beneficiary_Data'
DOWNLOAD_HERE_DWHPR = r'\\192.168.88.190\im_rcd\00______DATABASE______\03____WASH'


# ........................................................................................


# *****************************************************************************************
#  PERFORM ACTION
# *****************************************************************************************
def _perform_1(user, password, download_here_logs, download_here_dpbr, download_here_rpdm, download_here_cbr):
    print "WARNING! OFFICIAL DRC SCRIPT IN-PROGRESS\n"
    print "[ Performing acton ======================================= ]"
    time = str(datetime.datetime.utcnow())
    log = open(download_here_logs + '\kobo_download_logs.txt', 'a')
    log.write("=====================================================\n")
    log.write("New log entry #1: " + time + "\n")
    log.write("=====================================================\n")

    response = requests.get(URL + DOMINICA_PSS_BENEFICIARY_REGISTRAION, auth=(user, password))
    data = response.json()
    log.write("=====================================================\n")
    log.write(" ")

    log.write("==> " + data['title'] + " ==\n")
    log.write("==> " + data['date_modified'] + " ==\n")
    log.write("==> Downloading [ 0%  =========  ] \n")
    log.write("==> " + "Done.\n")
    response = requests.get(URL + DOMINICA_PSS_BENEFICIARY_REGISTRAION + ".xlsx", auth=(user, password))
    with open(download_here_dpbr + "/Dominica-PSS-Beneficiary-Demographics - labels" + ".xlsx", "wb") as code:
        code.write(response.content)

    response = requests.get(URL + DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING, auth=(user, password))
    data = response.json()
    log.write("==> " + data['title'] + " ==\n")
    log.write("==> " + data['date_modified'] + " ==\n")
    log.write("==> Downloading [ 0%  =========  ] \n")
    log.write("==> " + "Done.\n")
    response = requests.get(URL + DOMINICA_RELIEF_POST_DISTRIBUTION_MONITORING + ".xlsx", auth=(user, password))
    with open(download_here_rpdm + "/Dominica-Relief-Post-Distribution-Monitoring-Form - labels" + ".xlsx",
              "wb") as code:
        code.write(response.content)

    response = requests.get(URL + DOMINICA_CTP_BENEFICIARY_REGISTRATION, auth=(user, password))
    data = response.json()
    log.write("==> " + data['title'] + " ==\n")
    log.write("==> " + data['date_modified'] + " ==\n")
    log.write("==> Downloading [ 0%  =========  ] \n")
    log.write("==> " + "Done.\n")
    response = requests.get(URL + DOMINICA_CTP_BENEFICIARY_REGISTRATION + ".xlsx", auth=(user, password))
    with open(download_here_cbr + "/Dominica-CTP-Beneficiary-Registration-Form - labels" + ".xlsx", "wb") as code:
        code.write(response.content)

    log.write("=====================================================\n")
    print "[ Done =================================================== ]\n"


def _perform_2(user_2, password_2, download_here_logs, download_here_dwhpr):
    print "[ Performing acton ======================================= ]"
    time = str(datetime.datetime.utcnow())
    log = open(download_here_logs + '/kobo_download_logs.txt', 'a')
    log.write("=====================================================\n")
    log.write("New log entry #2: " + time + "\n")
    log.write("=====================================================\n")

    response = requests.get(URL + DOMINICA_WASH_HYGIENE_PROMOTION_REGISTRATION, auth=(user_2, password_2))
    data = response.json()
    log.write("=====================================================\n")
    log.write(" ")

    log.write("==> " + data['title'] + " ==\n")
    log.write("==> " + data['date_modified'] + " ==\n")
    log.write("==> Downloading [ 0%  =========  ] \n")
    log.write("==> " + "Done.\n")
    response = requests.get(URL + DOMINICA_WASH_HYGIENE_PROMOTION_REGISTRATION + ".xlsx", auth=(user_2, password_2))
    with open(download_here_dwhpr + "/Dominica-WASH-Hygiene-Promotion-Registration - labels" + ".xlsx", "wb") as code:
        code.write(response.content)

    log.write("=====================================================\n")
    print "[ Done =================================================== ]"


# *****************************************************************************************
#  RUN SCRIPT
# *****************************************************************************************
_perform_1(USER, PASSWORD, DOWNLOAD_HERE_LOGS, DOWNLOAD_HERE_DPBR, DOWNLOAD_HERE_RPDM, DOWNLOAD_HERE_CBR)
_perform_2(USER_2, PASSWORD_2, DOWNLOAD_HERE_LOGS, DOWNLOAD_HERE_DWHPR)
