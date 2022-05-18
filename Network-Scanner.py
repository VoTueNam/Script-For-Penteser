from scapy.all import *

# Tùy chọn cấu hình
interface = "eth0"
ip_range = "10.10.X.X/24"
broadcastMac = "ff:ff:ff:ff:ff:ff"

#câu lệnh khởi tạo package
packet = Ether(dst=broadcastMac)/ARP(pdst = ip_range)

ans, unans = srp(packet, timeout = 2, iface = interface, inter = 0.1)

for send, receive in ans:
    print(receive.print(r"%Ether.src% - %ARP.psrc%"))