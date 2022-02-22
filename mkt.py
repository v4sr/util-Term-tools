#!/usr/bin/env python

import optparse
import subprocess

def get_arguments():
    Plab_help = "Directory structure for pentesting lab"
    Proj_help = "Directory structure for common program project"

    # Parser
    parser = optparse.OptionParser()
    parser.add_option("-l", "--pent_lab", dest="pent_lab", help=Plab_help)
    parser.add_option("-p", "--pro_proj", dest="pro_proj", help=Proj_help)

    (options, arguments) = parser.parse_args()
    
    if (not options.pent_lab) and (not options.pro_proj):
        parser.error("[!] No options indicated, use --help for more information")

    return options

def get_dir(arguments):
    dir_list = []
    dir = ""

    for char in str(arguments):
        if char != " ":
            dir += char
        else:
            dir_list.append(dir)
            dir = ""

    dir_list.append(dir)

    return (dir_list)

def mkdir(arguments, struct):
    dir_list = get_dir(arguments)
    dir_struct = []

    for dir in dir_list:
        if dir != 'None':
            if (struct == "pent_lab"):
                dir_struct = [
                    (str(dir)+"/nmap"), 
                    (str(dir)+"/exploits"), 
                    (str(dir)+"/content")
                ]
            elif (struct == "pro_proj"):
                dir_struct = [
                    (str(dir)+"/bin"),
                    (str(dir)+"/src"),
                    (str(dir)+"/inc"),
                    (str(dir)+"/doc")
                ]
 
            for i in range(len(dir_struct)):
                print(dir_struct)
                subprocess.call(["mkdir", "-p", dir_struct[i]])

options = get_arguments()

mkdir(options.pent_lab, "pent_lab")
mkdir(options.pro_proj, "pro_proj")



