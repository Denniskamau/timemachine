import argparse
import yaml
import re
import pickle
import sys
import subprocess
import logging

from logging.handlers import RotatingFileHandler

# Read triggers from config file
#Taken from L8 slide 6
ALERT_RECORD_FILE = "records_sent.dat"

parser = argparse.ArgumentParser(
                    description='Match files for certain matches & run program on matches')
parser.add_argument('-c', '--configfile', default="config.dat",
                    help='file to read the config from')
parser.add_argument('-a', '--alertprog', default=None,
                    help='program to call to generate alerts')

LOG_FILENAME = 'filespy.log'
rotating_handler = RotatingFileHandler(LOG_FILENAME,
				    maxBytes=10000000,
				    backupCount=3)
formatter = logging.Formatter('%(asctime)s %(levelname)-8s %(message)s')
rotating_handler.setFormatter(formatter)

logger = logging.getLogger('demoapp')
logger.setLevel(logging.DEBUG)
logger.addHandler(rotating_handler)




def read_config(filename):
    try:
        logger.debug("Reading config from {0}".format(filename))
        with open(filename,"r") as f:
            return yaml.load(f)
    except FileNotFoundError:
        logger.error("Config file {0} not found".format(filename))
        print("Config file {0} not found".format(filename), file=sys.stderr)
        sys.exit(1)


def read_records_sent():
    try:
        with open(ALERT_RECORD_FILE,"rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return set()

def send_alert(message, line):
    if alert_program is None:
        print("Alert: {1} [{0}]".format(line, message), file=sys.stderr)
    else:
        exitcode = subprocess.call([alert_program, message, line])

def make_tuple(trigger, line):
    return (trigger["file"],trigger["pattern"],trigger["message"], line)

def was_alert_sent(trigger, line):
    tpl = make_tuple(trigger, line)
    return tpl in alerts_sent

def record_alert_sent(trigger, line):
    tpl = make_tuple(trigger, line)
    alerts_sent.add(tpl)
    with open(ALERT_RECORD_FILE,"wb") as f:
        return pickle.dump(alerts_sent, f)

def check_for_matches(trigger):
    filename = trigger["file"]
    pattern = trigger["pattern"]
    message = trigger["message"]
    with open(filename, "r") as f:
        for line in f:
            if re.search(pattern,line):
                if not was_alert_sent(trigger, line):
                    send_alert(message, line)
                    record_alert_sent(trigger, line)



args =parser.parse_args()
alert_program = args.alertprog
triggers = read_config(args.configfile)
alerts_sent = read_records_sent()
#print(triggers) # And print it so we can see it - This is just some test code - remove from final program

for trigger in triggers:
    check_for_matches(trigger)




