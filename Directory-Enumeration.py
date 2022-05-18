from msilib.schema import Directory
import requests
import sys

sub_list = open('wordlist2.txt').read()
directory = sub_list.splitlines()

for dir in directory:
    dir_enum = f"http://{sys.argv[1]}/{dir}.html"
    r = requests.get(dir_enum)
    
    # Khác code enum sub 1 tí, là chỗ này luôn trả về kết quả, chỉ khác là code res là 200, 300 hay 400
    if r.status_code==404:
        pass
    else:
        print('Valid directory: ', dir_enum)