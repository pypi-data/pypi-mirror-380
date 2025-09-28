import time
import os
import socket


class NameCache4:

    def __init__(self, filename=None):
        if filename != None:
            self._filename = filename
        else:
            self._filename = "/tmp/name-cache-%s.tsv" % int(time.time())
        self.load()

    def load(self):
        self._address_to_name = {}
        self._name_to_address = {}
        if os.path.isfile(self._filename):
            with open(self._filename, 'r') as f:
                for line in f:
                    if line.strip() == "":
                        continue
                    else:
                        cols = line.strip().split("\t")
                        if len(cols) >= 2:
                            self._address_to_name[cols[0]] = cols[1]
                            self._name_to_address[cols[1]] = cols[0]
                        else:
                            self._address_to_name[cols[0]] = ""

    def save(self):
        with open(self._filename, 'w') as f:
            for ip in self._address_to_name.keys():
                        f.write("%s\t%s\n" % (ip, self._address_to_name[ip]))

    def get_name(self, ip):
        if not ip in self._address_to_name.keys():
            try:
                h, al, ad = socket.gethostbyaddr(ip)
                self._address_to_name[ip] = h
                self._name_to_address[h] = ip
            except:
                self._address_to_name[ip] = ""
                self._name_to_address[""] = ip
        return self._address_to_name[ip]
              




import subprocess

def application_memory_mb(top_n:int=100):
    lines = subprocess.check_output("""/bin/bash -c 'ps -eo rss,cmd --sort=-rss | head -%d | cut -d " " -f 1,2'""" % top_n, shell=True, universal_newlines=True).strip().split("\n")
    apps = {}
    for line in lines:
        cols = [ x.strip() for x in line.split(" ") if len(x.strip()) > 0]
        if len(cols) > 1:
            kb = int(cols[0])
            name = cols[1]
            if not name in apps.keys():
                apps[name] = 0
            apps[name] = apps[name] + kb

    for name in apps.keys():
        apps[name] = int(apps[name]/1024)

    return apps
