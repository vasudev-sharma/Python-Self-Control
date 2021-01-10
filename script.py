from datetime import datetime, date
import logging
import os

import argparse


def self_control(list_sites):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_name = os.path.join(dir_path, "self_control_log.log")


    #logger to log the files
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    


    #create a file handler

    file_handler = logging.FileHandler(file_name)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
    logger.addHandler(file_handler)

    #reference  - 2021, 01, 04, 19 

    redirect = "127.0.0.1" 
    endtime =  list(map(int, str(date.today()).split("-")))


    YYYY, MM, DD = endtime
    HH = 19
    endtime = datetime(YYYY, MM, DD, HH)
    sites_to_block = list_sites.split(",")
    print(sites_to_block)

    #sites_to_block = ["youtube.com, www.youtube.com, facebook.com, www.facebook.com, gradcafe.com, www.gradcafe.com, voot.com, www.voot.com, twitter.com, www.twitter.com, gmail.com, www.gmail.com, yahoo.com, www.yahoo.com"]
  
    #The list of sites to block 
    print(sites_to_block)

    if datetime.now() < endtime:
        with open('/etc/hosts', "r+") as file:
            file_content = file.read()
            for site_name in sites_to_block:
                if site_name not in file_content:
                    file.write(redirect + " "+ site_name + "\n")
            #print(file.read())
        logger.info("SITES BLOCKED")

    else:
        with open('/etc/hosts', "r+") as file:
            file_content = file.readlines()
            for site_name in sites_to_block:
                if (redirect + " " + site_name + '\n') in file_content:
                    file_content.remove(redirect + " " + site_name + '\n')
            file.truncate(0)
            print(file_content)
            for content in file_content: 
                file.write(content)  
            print(file.readlines())
        logger.info("SITES UNBLOCKED")  

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--WEBSITES', required = True,
                    help='Enter the site names separated by comma')
    args = parser.parse_args()
    print(args)
    self_control(args.WEBSITES)
