import requests
import sys

# Đọc file
sub_list = open('subdomains.lst.txt').read()
#Cắt từng dòng trong file thành list
sub_doms = sub_list.splitlines()

#Duyệt qua toàn bộ list sub
for sub in sub_doms:
    # Công chuỗi để được 1 URL hoàn chỉnh
    sub_domains = f"http://{sub}.{sys.argv[1]}" #sys.argv[1] và đọc Input từ terminal
    
    try:
        # Thực hiện request tới URL đó
        requests.get(sub_domains)
        
        # Nếu có lỗi thì ngắt kết nối và
    except requests.ConnectionError:
        #bắt đầu vòng lặp tiếp theo
        pass
    
    #Nếu không có lỗi trg try/except thì sẽ vào Else
    else:
        print('Valid domain: ', sub_domains)