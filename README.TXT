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

Example Output:

apache referrer statistics for 21. Nov

top 10 hosts by number of requests

    879 hits ->  78.32.62.221    -> www.somedomain.org
    968 hits ->  188.232.41.23  -> static-ip-x-x-41-x.inaddr.ip-pool.com
   1008 hits ->  33.194.80.22   -> xxxxxxxxxxx.access.telenet.be
   1335 hits ->  44.22.201.22  -> x-x-x-x.adsl.highway.telekom.at
   1730 hits ->  188.44.116.154  -> ERR: hostname not found
   1730 hits ->  77.44.130.4    -> x.x.x.x.wireless.dyn.drei.com
   2898 hits ->  120.100.221.82  -> ERR: hostname not found
   3301 hits ->  62.178.132.122  -> chelloxxxxxxxxxx.1.x.vie.surfer.at
   3705 hits ->  81.111.250.90   -> chelloxxxxxxxxx.x.14.vie.surfer.at
  40828 hits ->  200.111.11.113 -> chelloxxxxxxxxx.14.vie.surfer.at

last updated: 21.11.2015 23:00

truly yours paperboy

<3

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
