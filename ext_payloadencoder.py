#!/usr/bin/python3

import sys, getopt, codecs, os
def main(argv):
    inputfile = ''
    encodedfile = ''

    try:
        opts, args = getopt.getopt(argv,"i:o:h",["ifile=","ofile="])
    except getopt.GetoptError:
        print(sys.argv[0] + " -i <inputfile> -o <encodedfile>")
        sys.exit(2)
    for opt, arg in opts:
        if opt == "-h":
            print(sys.argv[0] + " -i <inputfile> -o <encodedfile>") 
            sys.exit(0)
        elif opt in ("-i", "--ifile"):
            inputfile = arg
        elif opt in ("-o", "--ofile"):
            encodedfile = arg

    print(os.getcwd())

    with open(inputfile, 'r') as file:
        data = codecs.encode(file.read().encode('utf8'), "base_64")
        encodedstring = codecs.encode(data.decode('utf8'), "rot_13")
        open(encodedfile, 'w').write(encodedstring) 

    print("Input file: " + inputfile)
    print("Encoded output: " + encodedfile)
if __name__ == "__main__":
    main(sys.argv[1:])