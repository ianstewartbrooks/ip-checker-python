# -*- coding: utf-8 -*-
from check_ip import CheckIP

check_ip = CheckIP()

current_ip_info = check_ip.get_saved_ip_info()
success, latest_ip = check_ip.get_latest_ip()

# If get_latest_ip successfully returned an IP then lets compare it to see if it's the
# same as the stored one
if success:
    if check_ip.ip_has_changed():
        check_ip.save_new_ip_info()
        check_ip.show_ip_changed_info()
