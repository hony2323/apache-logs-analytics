# from apachelogs import LogParser
#
# parser = LogParser('%h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i"') # type: ignore
#
# line = '83.149.9.216 - - [17/May/2015:10:05:43 +0000] "GET /presentations/logstash-monitorama-2013/images/kibana-dashboard3.png HTTP/1.1" 200 171717 "http://semicomplete.com/presentations/logstash-monitorama-2013/" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.77 Safari/537.36"'
#
#
with open("data/apache_log.txt", "r") as f:
    logs = f.readlines()
from user_agents import parse

#
# entry = parser.parse(logs[0])
#
# print(entry)
# print(entry.remote_host)   # IP
# print(entry.request_line)
# print(entry.final_status)
# print(entry.bytes_sent)
# print(logs[:1])

import geoip2.database
from apachelogs import LogParser

parser = LogParser(
    '%h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i"'
)

reader = geoip2.database.Reader("data/GeoLite2-Country.mmdb")
line = logs[0]
entry = parser.parse(line)
ip = entry.remote_host

geo = reader.country(ip)
ua_string = entry.headers_in["User-Agent"]
print(ip, geo.country.name, geo.country.name)

ua = parse(ua_string)

print({
    "browser": ua.browser.family,
    "browser_version": ua.browser.version_string,
    "os": ua.os.family,
    "os_version": ua.os.version_string,
    "device": ua.device.family
})
