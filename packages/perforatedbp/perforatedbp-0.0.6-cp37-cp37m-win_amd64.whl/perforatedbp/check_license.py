from base64 import b64decode
import rsa
import yaml
import os.path
import getpass
import sys
import datetime
from datetime import datetime as dtm

entered_password = ""
entered_email = ""

compiling_date = dtm.strptime("2025-9-25", "%Y-%m-%d")
expiration_days = 90


def read_license_file(license_file):
    global entered_password
    if entered_password == "":
        p = os.environ.get("PAIPASSWORD")
        if not p:
            try:
                print(
                    "A license file was found in the working directory.  Enter your PAI password to continue"
                )
                p = getpass.getpass(prompt="Password: ")
            except Exception as error:
                print("ERROR", error)
                sys.exit(1)
        entered_password = p
    with open(license_file, "r") as f:
        output = yaml.safe_load(f)
        output["password"] = entered_password
        return output


def read_token():
    global entered_password
    global entered_email
    if entered_password == "":
        e = os.environ.get("PAIEMAIL")
        p = os.environ.get("PAITOKEN")
        if not (e and p):
            print(
                "No license file found in the working directory, enter your email address and token to continue or visit https://www.perforatedai.com/getstarted to generate a license file"
            )
            print("email:")
            e = input()
            print("token:")
            p = input()
        entered_password = p
        entered_email = e
    else:
        p = entered_password
        e = entered_email
    return e, p


def valid_license(license_file):
    """
    Verify the license key with the email address, password of the user and the
    public RSA key.

    Args:
            license_file (str): path to license file
            public_key (str): path to the public RSA key.

    Returns:
            bool: True if the license key is valid, otherwise False.
    """
    key = b64decode(
        "LS0tLS1CRUdJTiBSU0EgUFVCTElDIEtFWS0tLS0tCk1JSUJDZ0tDQVFFQWs1a2dhZU95UGJ6QmdNNTdEY3JmRXRJUk9QQjhiNDNrTHQ0VG01RCtaWGZQa2RsVTFobDIKRlZhblhBeGFmTzVLOWJnSng4Vmd6Mzhsa29XR0k0aTlmVXFsUUVJd2NGNGJBRk50RjNjMlYxaXZNM2J1a1l3UQpYTDhEZG9MclRCWjRxdnNKQ1FCTFNBNDgrUE02UEdhT3dXcWRRUzJuekRhZ2VFT2p1aXBmcGhpV1JXbDMvQWhnCkVsL0xkV0xGTW5CdXA4RDRFVkpOM0YvWWhkK3lYS2VzTUVGOU9MKzdMcTU4a1U5QnBHWFJPamFycWJNMjNpc08KUGZLVUkxZ2dVRVE3a1BseTZPWU9DdXhsY29tOUNNUWExRWlTNXZ6OThpeUp6Y2dPKzcza2FsREdMVzhGNlNIdgprdHh1UDFlbnhtQTczMEVFRFlXQURQdUJxMnh0VnQyYXhRSURBUUFCCi0tLS0tRU5EIFJTQSBQVUJMSUMgS0VZLS0tLS0K"
    )

    publicKey = rsa.PublicKey.load_pkcs1(key)

    if os.path.isfile(license_file):
        license = read_license_file(license_file)
        payload = license["email"] + license["licenseDate"] + license["password"]
        licenseString = license["license"]
        licenseDate = license["licenseDate"]
    else:
        payload, licenseString = read_token()
        licenseDate = str(compiling_date).split(" ")[0]
    try:
        rsa.verify(payload.encode(), b64decode(licenseString), publicKey)
    except Exception as e:
        print("Exception during verification")
        print("Incorrect Password or Token")  # I think this is what sends here
        return False
    now = datetime.datetime.now()
    if (now - dtm.strptime(licenseDate, "%Y-%m-%d")).days > expiration_days:
        print(
            "Your Perforated AI license or token is expired, please request a new one."
        )
        return False
    if (now - dtm.strptime(licenseDate, "%Y-%m-%d")).days > (expiration_days - 7):
        print(
            "\n\nYour Perforated AI license or token will expire in %d days, please request a new one.\n\n"
            % (expiration_days - (now - dtm.strptime(licenseDate, "%Y-%m-%d")).days)
        )
    return True
