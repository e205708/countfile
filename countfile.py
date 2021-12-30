import os
import subprocess
import re

number_of_lines = 0
number_of_words = 0
number_of_bites = 0

check_extension = ".java"
check_path = "/Users/touyamahiroto/"

def find_file(path):
    global number_of_lines,number_of_words,number_of_bites
    for pathname, dirnames, filenames in os.walk(path):
        for filename in filenames:
             if filename.endswith(check_extension):
                proc = subprocess.run(["wc",os.path.join(pathname,filename)],stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                data = re.findall(r"\d+", proc.stdout)
                number_of_lines += int(data[0])
                number_of_words += int(data[1])
                number_of_bites += int(data[2])


find_file(check_path)
print(str(number_of_lines) + " " + str(number_of_words) + " " + str(number_of_bites) + "\n")

