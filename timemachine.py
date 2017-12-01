import yaml
import argparse
import logging
import subprocess


from logging.handlers import RotatingFileHandler


parser = argparse.ArgumentParser(description="Create copies of specified files and watch for changes ")
parser.add_argument('-a' ,'--add', default=None, action="store_true",
                    help='Add a file to the list of files to be observed')

parser.add_argument('-r' , '--remove',default=None,action="store_true",
                    help='Remove a file from the list of files to be observed')

parser.add_argument('-l','--list', action="store_true",
                    help='Print a list of the file being observed')


config = './config.dat'
copies = './copiesDir'
log = './logfile.log'
rotating_handler = RotatingFileHandler(log,
				    maxBytes=10000000,
				    backupCount=3)

logger = logging.getLogger('dante')
logger.setLevel(logging.DEBUG)
logger.addHandler(rotating_handler)

"""
-function to read the config file data
-Gives the user an option to give the location of the config file if none is provided then the default value of 
config file in ./config.dat
-Gives the user an option to give the location of where the files are to be copied to ,if none is given then the
default location will be in the copies Directory

-Copies the content of the file given in the config.dat to a file in the copies Directory
"""
def copy_files():
    config_Location = input('Please input the location of the config file to read from? ')

    if config_Location == '':
        logger.debug('Config location is ./config.dat')

    else:
        logger.debug('Config location is '+ config_Location)

    copies_Location = input('Please input the location of the file to store the copies of file? ')

    if copies_Location == '':
        logger.debug('Copies location is /copiesDir/data.txt')
    else:
        logger.debug('Copies location is '+ copies_Location)

    
    #Check the location before starting to copy files
    if config_Location == '' and copies_Location == '':
        try:
            logger.debug('copying files from '+config +' to ' +copies)
            with open(config,'r') as f:
                file = yaml.load(f)
                for i in file:
                    for data in file[i]:
                        subprocess.call(['cp','-r',data,copies])
        except FileNotFoundError:
            logger.debug('Files not found')
            print("Specified file {0} not found".format(filename), file=sys.stderr)
            sys.exit(1)

    elif config_Location != '' and copies_Location != '':
        try:
            logger.debug('copying files from '+ config_Location +' to'+ copies_Location)
            with open(config_Location,'r') as f:
                file = yaml.load(f)
                for i in file:
                    for data in file[i]:
                        subprocess.call(['cp','-r',data,copies_Location])
        except FileNotFoundError:
            logger.debug('file not found')
            print("Specified file {0} not found".format(filename), file=sys.stderr)

    elif config_Location == '' and copies_Location != '':
        try:
            logger.debug('copying files from '+config +' to '+ copies_Location)
            with open(config,'r') as f:
                file = yaml.load(f)
                for i in file:
                    for data in file[i]:
                        subprocess.call(['cp','-r',data,copies_Location])
        except FileNotFoundError:
            logger.debug('FIle not found')
            print("Specified file {0} not found".format(filename), file=sys.stderr)

    elif config_Location != '' and copies_Location == '':
        try:
            logger.debug('copying files from '+config_Location + ' to ' + copies)
            with open(config_Location,'r') as f:
                file = yaml.load(f)
                for i in file:
                    for data in file[i]:
                        subprocess.call(['cp','-r',data,copies])
        except FileNotFoundError:
            logger.debug('FIles not found')
            print("Specified file {0} not found".format(filename), file=sys.stderr)

    
"""
-A function to watch for changes in the original file and compare them to the copies created.
"""
   

def check_for_change():
    with open (config,'r') as f:
        file = yaml.load(f)
        
    with open('./copiesDir/data.txt', 'w') as c:
        file2 = yaml.load(c)
        print(file2)


# Check for all the files in config.dat
def list_all_files():
    print('checking for files')
    try:
        with open(config, 'r') as f:
            files = yaml.load(f)
            print (files)
    except FileNotFoundError:
        print("Config file {0} not found".format(filename), file=sys.stderr)
        sys.exit(1)

#Add a file to config.dat
def add_file_to_config(filename):
    print('adding file to list of observable files')
    
    try:
        with open(config, 'w') as f:
            new_file = yaml.dump(filename,f.files,default_flow_style=False)
            print(file+ "has been added to the list of observable files")
    except FileNotFoundError:
        print("Specified file {0} not found".format(filename), file=sys.stderr)
        sys.exit(1)


#Delete a file from config.dat
def delete_file_from_config():
     print('removing file from list of observable files')
    




        
        

        

    
   
                
            

       
        

def main():
    args =parser.parse_args() 
    if args.list:
        list_all_files()
    elif args.add:
        add_file_to_config()
    elif args.remove:
        delete_file_from_config()
    else:
        #execute = read_config_file_and_copy()
        execute=copy_files()


    



run=main()
