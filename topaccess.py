#!/usr/bin/python

import re
import socket
import sys
import time
import getopt


#run a commandline operation. allows long ones with pipes, fuck yeah!
def run(cmd):
    from subprocess import Popen, PIPE
    import shlex
    
    """Runs the given command locally and returns the output, err and exit_code."""
    if "|" in cmd:    
        cmd_parts = cmd.split('|')
    else:
        cmd_parts = []
        cmd_parts.append(cmd)
      
    i = 0
    p = {}
    
    for cmd_part in cmd_parts:
        cmd_part = cmd_part.strip()
        if i == 0:
            p[i]=Popen(shlex.split(cmd_part),stdin=None, stdout=PIPE, stderr=PIPE)
        else:
            p[i]=Popen(shlex.split(cmd_part),stdin=p[i-1].stdout, stdout=PIPE, stderr=PIPE)
        i = i +1
    
    (output, err) = p[i-1].communicate()
    exit_code = p[0].wait()
    
    return str(output), str(err), exit_code
    


""" usage explaination """
def usage():
    print ("lofi bruteforce watcher :(\n\nUSAGE Help!!111\n"
           "\nIf used without commands, it will show stats for today"
           "without hostnames resolved from /var/log/apache2/access.log\n")
    
    print ("-d, --day\tdefine day to parse\n"
        "-m, --month\tmonth to parse as short string (eg. Jan, Feb)\n"
        "-y, --year\tyear to parse\n"
        "-f, --logfile\tlogfile to read from\n"
        "-n, --hostnames\tresolve hostnames for ip addies\n"
        "\nExamples:\n\n"
        "All available options set. Getting stats for 4th May 2015. Resolving hostnames enabled\n"
        "python brutewatcher.py -f /var/log/apache2/access.log -d 04 -m May -y 2015 -n\n"
        "\nGet statistics for today from defined apache log file, no hostnames resolved\n"
        "python brutewatcher.py --logfile /var/log/apache2/access.log"
        "\n\nlofi <3 u!")



""" programm entry point """
def main(argv):
    

    #get commandline options or show help on commandline    
    try:                                
        opts, args = getopt.getopt(argv, "hf:d:m:y:n", ["help", "logfile=", "day=", "month=", "year=", "hostnames"]) 
    except getopt.GetoptError:           
        usage()                          
        sys.exit(2)  
        
    #default path for logfile to parse. can be changed with -f flag from commandline    
    logfile = "/var/log/apache2/access.log"
    
    #defaultsettings for date to parse
    day = time.strftime("%d")
    month = time.strftime("%b")
    year = time.strftime("%Y")
    
    #resolve hostnames for top 10 ip addresses. could take more time to run the script with those enables
    bHostnames = False
    
    #get settings from commandline
    for opt, arg in opts:                
        #show quick help
        if opt in ("-h", "--help"):      
            usage()                     
            sys.exit()         
        #set day to parse
        elif opt in ("-d", "--day"):                
            day = arg     
        #set month to parse
        elif opt in ("-m", "--month"):                
            month = arg  
        #set year to parse
        elif opt in ("-y", "--year"):                
            year = arg                                
        #define logfile we're parsing
        elif opt in ("-f", "--logfile"): 
            logfile = arg
        #resolve hostnames for ip addresses
        elif opt in ("-n", "--hostnames"):
            bHostnames = True
            
            
    
    print "Apache referrer statistics for %s. %s %s\n" % (day, month, year)
    print "Top 10 hosts by number of requests\n" 
    
    command = "cat %s | grep '%s\/%s\/%s' | grep -Eo '^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | sort | uniq -c | sort -n | tail -10" % (logfile, day, month, year)
    #the command that gets a list of top ten penetration hosts from commandline
    #cat /var/log/apache2/access.log | grep 28\/Apr\/2015 | grep -Eo '[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | sort | uniq -c | sort -n | tail -10
     	
    
    #run the above command and fetch return value
    output, err, exit_code = run(command)
    #if we get an error, lets break here
    if exit_code != 0:
        #print "Output:"
        #print output
        print "Error fetching list of hosts from %s:" % logfile
        print err
        #die here
        sys.exit()
        
    
    
    #commandline operation successfully finished
    #show the top 10 accessing hosts with corresponding hostname
    #each line would be something like: 123 192.168.1.1, where 123 is the number of hits    
    for line in re.split('\n', output):    
        #split the line into two groups: number of hits and ip address
        m = re.search("([\s0-9]*?) ([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})", line)    
        if m:
            #accessing ip addy        
            strIP = m.group(2)
            #number of hits
            strNumHits = m.group(1)
            
            #resolve hostnames if necessary
            if bHostnames == True:
                try:
                    #try getting the hostname
                    strHostname, lstAlias, lstAddress = socket.gethostbyaddr(strIP)
                except: 
                    #or show only ip addy and error message
                    strHostname = "ERR: hostname not found"       
                
                #output shows also the hostname if resolvable
                #append whitespaces to short ip address for pretty printing
                print "%s hits ->  %s -> %s" % (strNumHits, strIP.ljust(15, ' '), strHostname)              

            else:
                #no hostname appended in output             
                #append whitespaces to short ip address for pretty printing
                print "%s hits ->  %s" % (strNumHits, strIP.ljust(15, ' ')) 
        
                  
    
    
    print time.strftime("\nlast updated: %d.%m.%Y %H:%M")
    print "logfile: %s" % logfile
    
    print "\ntruly yours paperboy\n\n<3"

""" eof main """




if __name__ == "__main__":
    
    try:
        #main program entry point
        main(sys.argv[1:])

    #if user forces to quit before we finish
    except SystemExit as e:
        print "bye"
    
    #if user hits CTRL + C
    except KeyboardInterrupt as e:
        print "\nbye"
        sys.exit()