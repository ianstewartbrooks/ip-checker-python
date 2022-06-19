# -*- coding: utf-8 -*-
import datetime
import json

import requests


class CheckIP(object):
    def __init__(self):
        self.latest_ip = None
        self.current_ip_data = {
            "ip": None,
            "date": None,
        }
        self.new_ip_data = {}

    def get_saved_ip_info(self):
        with open("/ip_data.json") as json_file:
            self.current_ip_data = json.load(json_file)

    def save_new_ip_info(self):
        self.new_ip_data = {
            "ip": self.latest_ip,
            "date": datetime.datetime.now().isoformat(),
        }

        with open("/ip_data.json", "w") as json_file:
            json.dump(self.new_ip_data, json_file)

    def get_latest_ip(self):
        url = "https://api.ipify.org/"
        response = requests.get(url)

        if response.status_code == 200:
            self.latest_ip = response.content.decode("utf-8")
            return True, response.content.decode("utf-8")

        # If there is an error then it is probably because my connection has dropped again
        # so Just return
        return False, None

    def ip_has_changed(self):
        if self.latest_ip != self.current_ip_data["ip"]:
            return True

        return False

    def show_ip_changed_info(self):
        print("<----- IP Changed ----->")
        print(f"New IP..... {self.new_ip_data['ip']}")
        print(f"New Date... {self.new_ip_data['date']}")
        print(f"Old IP..... {self.current_ip_data['ip']}")
        print(f"Old Date... {self.current_ip_data['date']}")
