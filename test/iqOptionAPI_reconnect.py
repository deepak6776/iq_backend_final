from iqoptionapi.stable_api import IQ_Option

error_password = """
                    {"code":"invalid_credentials",
                     "message":"You entered the wrong credentials. Please check that the login/password is correct."
                     }
                """

iq_option = IQ_Option("deepak.enka@gmail.com", "aswdkl;123")

check, reason = iq_option.connect()
if check:
    print("Start your robot")
    # if see this you can close network for test
    while True:
        if iq_option.check_connect() == False: # detect the websockets is close
            print("try reconnect")
            check, reason = iq_option.connect()
            if check:
                print("Reconnect successfully")
            else:
                if reason == error_password:
                    print("Error Password")
                else:
                    print("No Network")

else:

    if reason == "[Errno -2] Name or service not known":
        print("No Network")
    elif reason == error_password:
        print("Error Password")