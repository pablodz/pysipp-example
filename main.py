import pysipp

pysipp.utils.log_to_stderr("DEBUG")

uac = pysipp.client(destaddr=("domain.example", 5060))
uac.uri_username = "username"
uac.auth_usernmame = "username"
uac.auth_password = "password"
uac()
