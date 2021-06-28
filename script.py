from datetime import datetime, date
import logging
import os

import argparse


def self_control(list_sites, hour):
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
    HH = hour
    endtime = datetime(YYYY, MM, DD, HH)

    # The list of sites to block
    sites_to_block = list_sites.split(",")

  

    if datetime.now() < endtime:
        with open('/etc/hosts', "r+") as file:
            file.seek(0)
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
            # file.truncate(0)
            # print(file_content)
            # file.writelines(file_content)
            # print(file.readlines())
            # file.seek(0)
        logger.info("SITES UNBLOCKED") 
        print(file_content)
        with open('/etc/hosts', "w") as file:
            file.writelines(file_content)
            print(file_content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--websites', default="youtube.com,www.youtube.com,facebook.com,www.facebook.com,gradcafe.com,www.gradcafe.com,voot.com,www.voot.com,twitter.com,www.twitter.com,gmail.com,www.gmail.com,yahoo.com,www.yahoo.com,linkedin.com,www.linkedin.com,twitter.com,www.twitter.com",
                    type=str, help='Enter the site names separated by comma')
    parser.add_argument('--hour', default=19, type=int, help='Enter the hour of the day (24-hour format) until which you wish to block the website')
    args = parser.parse_args()
    self_control(args.websites, args.hour)