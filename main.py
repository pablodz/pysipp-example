import pysipp

pysipp.utils.log_to_stderr("DEBUG")

uac = pysipp.client(destaddr=("pip.sip.vozy.co", 5060))
uac.uri_username = "pdiaz"
uac.auth_password = "BcCR2vW2ajSC"
uac()
