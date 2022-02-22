#!/usr/bin/env python

import optparse
import subprocess

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-r", "--roothome", dest="roothome", help="Root home directory as destination")
    parser.add_option("-u", "--usrhome", dest="usrhome", help="User home directory as destination")
    parser.add_option("-c", "--config", dest="config", help="Config directory as destination")
    parser.add_option("--desktop", dest="desktop", help="Desktop directory as destination")
    parser.add_option("--downloads", dest="downloads", help="Dowloads directory as destination")

    (options, arguments) = parser.parse_args()

    if (not options.roothome) \
        and (not options.usrhome) \
        and (not options.config) \
        and (not options.desktop) \
        and (not options.downloads):
        parser.error("[!] No options indicated, use --help for more information")
    
    return options

def get_path(arguments):
    path_list = []
    path = ""

    for char in str(arguments):
        if char != " ":
            path += char 
        else:
            path_list.append(path)
            path = ""

    path_list.append(path)

    return(path_list)
        
def copy(arguments, dest):
    src_list = get_path(arguments)

    for src in src_list:
        if src != 'None':
            subprocess.call(["cp", "-R", src, dest])

options = get_arguments()
usr = subprocess.check_output(['whoami']).decode('utf8')
usr = usr.replace('\n', "")

roothome = "/root"
usrhome = "/home/" + str(usr)
config = usrhome + "/.config"
downloads = usrhome + "/Descargas"
desktop = usrhome + "/Desktop"

for i in range(5):
    switch = {
        "roothome": copy(options.roothome, roothome),
        "usrhome": copy(options.usrhome, usrhome),
        "config": copy(options.config, config),
        "downloads": copy(options.downloads, downloads),
        "desktop": copy(options.desktop, desktop),
    }
