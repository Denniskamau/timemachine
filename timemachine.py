import yaml
import argparse
import logging
import subprocess
import os


from logging.handlers import RotatingFileHandler


parser = argparse.ArgumentParser(description="Create copies of specified files and watch for changes ")
parser.add_argument('-a' ,'--add',  action="store", default='',
                    help='Add a file to the list of files to be observed')

parser.add_argument('-r' , '--remove',action="store",default='',
                    help='Remove a file from the list of files to be observed')

parser.add_argument('-l','--list', action="store_true",
                    help='Print a list of the file being observed')


config = '/home/dennis/Desktop/dante/config.dat'
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

    check_for_change()
"""
-A function to watch for changes in the original file and compare them to the copies created.
"""
   

def check_for_change():
    os.chdir(copies)#change directory to copiesDir
    suffix = '.txt' 
    fnames = os.listdir('.') #looks for all files

    files =[] #an empty array to hold the names of the copy files
    for fname in fnames:
        if fname.endswith(suffix):
            pname= os.path.abspath(fname)
            files.append(pname) #add the files to our array

    for i in files:
        compare(i)

   
   

         
def compare(filename):
    with open (config, 'r') as f:
        file = yaml.load(f)
        for i in file:
            for data in file[i]:
                logger.debug('Running comparison of files')
                comparison = subprocess.call(['diff','-c', data ,filename])




# Check for all the files in config.dat
def list_all_files():
    print('checking for files')
    try:
        logger.debug('listing all files in config file')
        with open(config, 'r') as f:
            files = yaml.load(f)
            print (files)
    except FileNotFoundError:
        print("Config file {0} not found".format(filename), file=sys.stderr)
        sys.exit(1)

#Add a file to config.dat
def add_file_to_config(filename):
    
    print('adding file to list of observable files')
    pname= os.path.abspath(filename)
    with open (config,'a') as f:
        logger.debug('adding '+pname +' to config file')
        file = yaml.dump(pname, f)
        


#Delete a file from config.dat
def delete_file_from_config(filename):
    print('removing file from list of observable files')
    pname=os.path.abspath(filename)
    with open (config, 'r') as f:
        file = yaml.load(f)
        for i in file:
            for data in file[i]:
                try:
                    logger.debug('deleting '+pname+ ' from config file')
                    subprocess.call(['rm','-rf', pname])
                except FileNotFoundError: 
                    print('file not found!!')              


       
    


        

def main():
    args =parser.parse_args() 
    if args.list:
        list_all_files()
    elif args.add:
        add_file_to_config(args.add)
    elif args.remove:
        delete_file_from_config(args.remove)
    else:
        execute=copy_files()


    



run=main()
