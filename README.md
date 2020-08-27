# img2shell

******PLEASE NOTE********
This is for educational purpose only.
In all likliness these exploits has already been patched on all servers on the net.
This file is NOT to be used against any machine that you not not own or have an obligation to pen tesst
mostly this file was created for me to try out python.


Use ext_payloadencoder.py to to encode your final php exploit payload.
This can be be something like tiny file manager or a php shell.
This files will be hosted on a domain that you control. However, host providers 
do not like the idea of malware to be hosted with them, so we need to hide what it is we are hosting.
We do a simple base64 encoding, then rotate each character by 13. This then gives us something that 
looks like base64 but is in fact not.
Usage: ext_payloadencoder.py -i <Source php file> - o <some innocent looking file.bin>
The output will be an encoded file that should pass security inspection on host provider
Upload this file to a public web server, and take note of the path.

use exifTl.py to generate an image with our intermediary payload.
Bad file or image uploaders either does no checking, or only checks the headers of the uploaded file.
We can inject some script code into one of the ascii enabled exif fields such as File Comment.
Usage:  exifTl.py -i <inputimage> -o <outputimage> -p <payloadurl> -d <destinationname>"
    input image is your source jpg file. It has to be jpeg or tiff
    output image is the image that will contain the initial payload.
    payload url is where you hosted the output from ext_payloadencoder.py. 
    destination name will be an inocent looking php file. such as image_manager.php or something.


The payload embedded in the image is simply a bit of php code that will download our hidden file, then save it with the new name on the target host

Final step is to upload this image via a weak image uploader that will not check exif meta data for executable code.
If it works, the 1st payload will execute, and download the main payload from your remote hosting, decode it, and save it as a php file on your target host.
This php file can then be used as a file manager, or as a shell. Look at weevely for shell access.
Just notice that weevely shells still need to get encoded, seeing as their obfiscation is not that strong and can be detected by security software.
