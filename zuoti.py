#!/usr/bin/env python
import argparse
import sys
import wget
import os

def getOptions(args=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Parses command.")
    #parser.add_argument("-i", "--input", help="Your input file.")
    #parser.add_argument("-o", "--output", help="Your destination output file.")
    #parser.add_argument("-n", "--number", type=int, help="A number.")
    #parser.add_argument("-v", "--verbose",dest='verbose',action='store_true', help="Verbose mode.")
    parser.add_argument("-u", "--url", help="file url")
    parser.add_argument("-n", "--name", help="absolute file path/name")
    options = parser.parse_args(args)
    return options

def wgetfile(url,name=None):
    if name:
        file = name
    else:
        file = url.split('/')[-1]

    if  not os.path.exists(file):
        wget.download(url,out=file)
    else:
        print('***********'+file+' exists!***********')
    print('***********chmod +x '+file+'***********')
    os.system('chmod +x '+file)
    print('***********checksec '+file+'***********')
    os.system('checksec '+file)
    if  not os.path.exists(file+'.py'):
        print('***********touch '+file+'.py'+'***********')
        os.system('touch '+file+'.py')
    else:
        print('***********'+file+'.py exists!***********')

options = getOptions(sys.argv[1:])
print(options)
if options.name:
    wgetfile(options.url,name=options.name)
else:
    wgetfile(options.url)


