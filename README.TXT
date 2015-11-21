    ___ _______           ___ __    __       __ __ __
   |.  |   _   .--.--.--.'  _|__.--|  .-----|  |__|  |_.--.--.
    |  |.  |   |  |  |  |   _|  |  _  |  -__|  |  |   _|  |  |
    |__|.  |   |________|__| |__|_____|_____|__|__|____|___  |
       |:  1   |                                       |_____|
       |::.. . |                        electric.larry 04-2015
       '-------'

topaccess - scans apache access.log and shows the 10 hosts
with the most accesses to the site.

I use this script to identify bruteforce attacks, exploit
scans or hosts with an unusual number of hits on the server.

-----------------------------------------------------------------------

USAGE Help!!111

If used without commands, it will show stats for todaywithout hostnames resolved from /var/log/apache2/access.log

-d, --day	define day to parse
-m, --month	month to parse as short string (eg. Jan, Feb)
-y, --year	year to parse
-f, --logfile	logfile to read from
-n, --hostnames	resolve hostnames for ip addies

Examples:

All available options set. Getting stats for 4th May 2015. Resolving hostnames enabled
python brutewatcher.py -f /var/log/apache2/access.log -d 04 -m May -y 2015 -n

Get statistics for today from defined apache log file, no hostnames resolved
python brutewatcher.py --logfile /var/log/apache2/access.log

lofi <3 u!
bye
