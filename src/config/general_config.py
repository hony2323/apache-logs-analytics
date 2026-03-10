from os import environ

LOGS_FILE_PATH = environ.get("LOGS_FILE_PATH", "src/data/apache_log.txt")
GEO2_DB_FILE_PATH = environ.get("GEO2_DB_FILE_PATH", "src/data/GeoLite2-Country.mmdb")
NUM_OF_LINES_TO_READ = int(environ.get("NUM_OF_LINES_TO_READ", 100))
