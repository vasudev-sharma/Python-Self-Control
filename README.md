# Python-Self-Control
A productivity based python script to keep one away from social media distractions

## Install 
1. ` git clone https://github.com/vs74/Python-Self-Control.git`
2. `cd Python-Self-Control`


## How to use?

`python script.py --websites "twitter.com, youtube.com, facebook.com"`

## (Optional) If you wish to automate blocking the websites, set up a cron job:- 

**NOTE:-** You can set up a cron job only  in Linux / Mac operating system

- **STEP 1:** In terminal, type `crontab -e` # This will allow you add a cron job in vim editor
- **STEP 2:** Add a cron job: `* * * * * <path_to_python_bin> <path_to_script.py> -w "twitter.com, youtube.com, facebook.com"` 

**TODO**
- [ ] Allow the user to pass the end time of day using CLI
