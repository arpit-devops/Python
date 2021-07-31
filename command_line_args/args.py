#! /usr/bin/python3
import getopt, sys
argumentList = sys.argv[1:]

options = "hf:"   #short option  -h

temp_list=["red", "blue", "green", "black", "white"]

long_options = ["help", "filter="]   # long option --help

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)
    if arguments:
        for currentArgument, currentValue in arguments:
            try:
                if currentArgument in ("-f", "--filter"):
                    print("this element {arg} lies in = ".format(arg=str(currentValue)), end=" ")
                    print(temp_list.index(str(currentValue)))
                elif currentArgument in ("-h", "--help"):
                    print ("usage args -f|--filter")
                else: 
                    print("usage for help use --->  ./args -h|--help")
            except Exception as e:
                print(e)
    else: 
        print("usage for help use --->  ./args -h|--help")
except getopt.error as err:
    print (str(err))