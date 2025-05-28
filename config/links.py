import os



class Links:
    HOST = os.environ.get("HOST", "http://www.msp.lan")
    LOGIN_PAGE = f"{HOST}/msp/auth"
    MSP_PAGE = f"{HOST}/msp"
  