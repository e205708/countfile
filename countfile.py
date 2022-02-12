import os
import subprocess
import re

check_extension = ["java","c","py","go"]
check_path = "/Users/touyamahiroto/"

def find_file(path,_check_extension):
    number_of_lines = 0
    number_of_words = 0
    number_of_bites = 0

    output_file = open(os.getcwd() +'/result/'+ _check_extension +'.txt', 'w')

    for pathname, dirnames, filenames in os.walk(path):
        for filename in filenames:
             if filename.endswith("."+_check_extension):
                #print(os.path.join(pathname,filename))
                output_file.write(os.path.join(pathname,filename) +"\n")
                proc = subprocess.run(["wc",os.path.join(pathname,filename)],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                data = re.findall(r"\d+", proc.stdout)
                number_of_lines += int(data[0])
                number_of_words += int(data[1])
                number_of_bites += int(data[2])
    print(str(number_of_lines) + " " + str(number_of_words) + " " + str(number_of_bites) + "\n")
    output_file.write(str(number_of_lines) + " " + str(number_of_words) + " " + str(number_of_bites) + "\n")

    output_file.close()

for extn in check_extension:
    find_file(check_path,extn)


