from datetime import datetime


redirect = "127.0.0.1" 
string_endtime = map(int, input("Enter the end time in the format YYYY, MM, DD, HH: - ").split(','))
YYYY, MM, DD, HH = string_endtime
print(type(YYYY), type(MM), type(DD), type(HH) )
endtime = datetime(YYYY, MM, DD, HH)
print(endtime)

sites_to_block = ["youtube.com", "www.youtube.com", "facebook.com", "www.facebook.com", "gradcafe.com", "www.gradcafe.com", "voot.com", "www.voot.com"]
reply = input("Do you wish to enter more websites to block: Y/N -  ")
if reply == "Y":
    while(True):
        site = input("Enter the site name: - ")
        sites_to_block.append(site)
        sites_to_block.append("www."+site)
        reply = input("Do you wish to enter more websites to block: Y/N -  ")
        if reply == "N":
            break

#The list of sites to block 
print(sites_to_block)

if datetime.now() < endtime:
    with open('/etc/hosts', "r+") as file:
        file_content = file.read()
        print(file_content)
        for site_name in sites_to_block:
            if site_name not in file_content:
                file.write(redirect + " "+ site_name + "\n")

else:
    with open('/etc/hosts', "r+") as file:
        file_content = file.readlines()
        for site_name in sites_to_block:
            if (redirect + " " + site_name + '\n') in file_content:
                file_content.remove(redirect + " " + site_name + '\n')
        file.truncate(0)
        for content in file_content: 
          file.write(content)  
      