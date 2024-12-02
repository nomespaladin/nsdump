#import necessary modules
import requests
import ipaddress
import dns.resolver
import re
import os
import time 
import datetime

print("""
██████████████████████████████████████████
█▄─▀█▄─▄█─▄▄▄▄█▄─▄▄▀█▄─██─▄█▄─▀█▀─▄█▄─▄▄─█
██─█▄▀─██▄▄▄▄─██─██─██─██─███─█▄█─███─▄▄▄█
▀▄▄▄▀▀▄▄▀▄▄▄▄▄▀▄▄▄▄▀▀▀▄▄▄▄▀▀▄▄▄▀▄▄▄▀▄▄▄▀▀▀
██████████████████████████████████████████    
                     
~nsdump                   by : NomesPaladin
""")
print("Type '-q' to exit program.\n")

 

#validate the domain with string rules
def is_valid_domain(domain):
    regex = r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)$"
    return all(re.match(regex, part) for part in domain.split("."))

#resolve the dns given a domain and a type of ns record
def get_relations(domain):
    dns_relations = {}
    for record in ['A', 'NS', 'MX', 'SOA', 'TXT', 'PTR']:
        try:
            valid = dns.resolver.resolve(domain,record)
            for data in valid:
                if record == 'A':
                    dns_relations[data.address] = record
                else:
                    dns_relations[data.to_text()] = record
        except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
            pass
    return dns_relations

#get the IP addreess realted to ns
def get_ip(dns_relations):
    ip_addresses = []
    for relation,record in dns_relations.items():
        if record == 'A':
            ip_addresses.append(relation)
        elif record == 'PTR':
            try:
                ip_address = ipaddress.ip_address(relation)
                ip_addresses.append(str(ip_address))
            except ValueError:
                pass
    return ip_addresses
    
#error retriever if invalid domain character is entered
def process_domain(domain):
    if not is_valid_domain(domain):
        print(f"Invalid domain: {domain}")
        return None,None
    dns_relations = get_relations(domain)
    ip_addresses = get_ip(dns_relations)
    return dns_relations,ip_addresses



#main function 'menu'
def main():
    while True:
        try:
        
            domain = input("Enter Domain:")
            if len(domain) < 5:
                print(f"The following|{domain}| does not seems to be a valid domain,please try again:")
                continue
            elif domain == '-q':
                time.sleep(1)
                print("Bye....")
                time.sleep(1)

                break   
            start_time = datetime.datetime.now()
            print(f"Running|{start_time.strftime("[%H:%M:%S]|[%d/%m/%Y]")}|")
            dns_relations,ip_addresses = process_domain(domain)
            save_results = []
            if dns_relations is not None:
                print(f" --- DNS Relations for {domain} --- ")
                for relation,record in dns_relations.items():
                    for ipaddress in ip_addresses:
                        time.sleep(0.001)
                        print(f"Related Name Server : {relation} | Type: {record} | IP : {ipaddress}")
                        save_results.append(f"Related Name Server : {relation} | Type: {record} | IP : {ipaddress}")
                #user choice to save the file  
                question = input("Would you like to save the file?('yes'/'no'/'-q'[to quit]):")
                if question == 'yes':
                    user_path = os.getlogin()
                    directory_to_save = input("""Select option,type: 'Desktop' | 'Documents' | 'Downloads' |
                    Enter Directory to save the file:""")
                    full_path = f"/home/{user_path}/{directory_to_save}/" #uncomment this line to use the program on linux based systems  <<< comment this line to deactivate the linux path
                    #windows full_path = f"C:/{user_path}/{directory_to_save}/"  <<< activate this line to use the program on windows based systems 
                    with open(f"{full_path}ns_results_{domain}.txt","a") as file:
                        file.write(f"----- SCAN REPORT FOR {domain} ----- AT -- {start_time.strftime("[%H:%M:%S] [%H:%M]")} ---\n")
                        for res in save_results:
                            file.write(f"{res}\n")
                        print(f"File is was saved >> {full_path}ns_results_{domain}.txt")
                        continue
                elif question == 'no':
                    quit_program = input("Do you want to exit the program?('-N'/'-q'):")
                    if quit_program == '-q':
                        print("Program Finished")
                        break
                    elif quit_program == '-N':
                        continue
                elif question == "-q":
                    raise KeyboardInterrupt("Program Finished")
                else:
                    print("Invalid option, pleasy try again")
                    continue
        except KeyboardInterrupt as ki:
            print(ki)
            break


if __name__ == "__main__":
    main()

