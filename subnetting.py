import math
def next_power_of_2(x):
    return 1 if x == 0 else 2**(x - 1).bit_length()
def string_to_ip(ip_addr_bin_1):
    #print(ip_addr_bin[0:8:1], ip_addr_bin[8:16:1], ip_addr_bin[16:24:1], ip_addr_bin[24:32:1])
    ip = str(int(ip_addr_bin_1[0:8:1],2))+"."+str(int(ip_addr_bin_1[8:16:1],2))+"."+str(int(ip_addr_bin_1[16:24:1],2))+"."+str(int(ip_addr_bin_1[24:32:1],2))
    return ip

prefix_length=0
ip_addr_bin = ""
while True:
    ip_address = input("Enter an IP address:")
    a = ip_address.split('.')
    ip_addr_bin = format(int(a[0]),'b').rjust(8,'0')+format(int(a[1]),'b').rjust(8,'0')+format(int(a[2]),'b').rjust(8,'0')+format(int(a[3]),'b').rjust(8,'0')

    print("IP in binary = ",ip_addr_bin)
    if(len(a) == 4):
        if(int(a[0]) <= 255 and int(a[1]) <= 255 and int(a[2]) <= 255 and int(a[3]) <= 255):

            if(int(a[0]) in range(1,127) and int(a[3]) in range(1,255)):
                print(ip_address," belongs to Class A"," with subnet 255.0.0.0")
                prefix_length = 8
            elif(int(a[0]) in range(128,192) and int(a[1]) >= 1 and int(a[3]) in range(1,255)):
                print(ip_address, " belongs to Class B", " with subnet 255.255.0.0")
                prefix_length = 16
            elif (int(a[0]) in range(192, 224) and int(a[2]) in range(1,255) and int(a[3]) in range(1, 255)):
                print(ip_address, " belongs to Class C", " with subnet 255.255.255.0")
                prefix_length = 24
            elif (int(a[0]) in range(224, 240)):
                print(ip_address, " belongs to Class D", " with subnet reserved for multicasting")
            elif (int(a[0]) in range(240, 255) and int(a[3]) in range(1, 255)):
                print(ip_address, " belongs to Class E", " reserved for research")
        break
    else:
        print("Enter a valid IPv4 address")
        continue
print("Your default prefix length is ",prefix_length)
print("Change? Y:N")
opt = input()
if opt == 'Y':
    prefix_length = int(input("Enter prefix length:"))

subnet_mask_bin = "1"*prefix_length+"0"*(32-prefix_length)
#subnet_mask_bin.ljust(32,'0')
print("Subnet Mask = ",subnet_mask_bin," ",string_to_ip(subnet_mask_bin))

number_of_addresses = 2**(32-prefix_length)
number_of_subnets = next_power_of_2(int(input("Enter number of subnets:")))
addresses_per_block = int(number_of_addresses / number_of_subnets)
print("Thus, needed addresses = ",number_of_addresses," with ",addresses_per_block," addresses per block")

n_sub = 32 - int(math.log2(addresses_per_block))
number_of_positions_cleared = int(math.log2(addresses_per_block))
start_ip = ip_addr_bin[0:(32 - number_of_positions_cleared + 1):1].ljust(32, '0')

for i in range(1,number_of_subnets+1):
    print("**********************")
    print("BLock ",i, "has ")
    print("Starting IP = ", start_ip, " ", string_to_ip(start_ip))
    print(addresses_per_block)
    last_ip = bin(int(start_ip,2)+int("{0:b}".format(addresses_per_block-1),2))
    last_ip = last_ip[2:]
    print("Last IP = ", last_ip, " ", string_to_ip(last_ip))
    start_ip = bin(int(start_ip,2)+int("{0:b}".format(addresses_per_block),2))
    start_ip = start_ip[2:]


