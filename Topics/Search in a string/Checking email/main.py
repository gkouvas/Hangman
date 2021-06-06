def check_email(e_string):
    if (" " not in e_string) and ("." in e_string) and ("@" in e_string) and ("@." not in e_string):
        place_at = e_string.find("@")
        place_dot = e_string.rfind(".")
        if e_string.endswith('.') is False and place_dot > place_at + 1:
            return True
    return False
