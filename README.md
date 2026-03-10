# apache-logs-analytics

A tool for parsing and analyzing Apache access logs, with GeoIP country lookup and user-agent parsing.

## Requirements

- Python 3.x
- A GeoLite2-Country database file (`.mmdb`) from [MaxMind](https://dev.maxmind.com/geoip/geolite2-free-geolocation-data)

## Setup

1. **Clone the repository**

   ```bash
   git clone <repo-url>
   cd apache-logs-analytics
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv venv
   source venv/bin/activate       # Linux/macOS
   venv\Scripts\activate.bat      # Windows
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Add required data files**

   Place the following files in `src/data/`:
   - `apache_log.txt` — your Apache access log file
   - `GeoLite2-Country.mmdb` — the MaxMind GeoLite2 Country database

## Running

```bash
python main.py
```

## Configuration

The following settings can be overridden via environment variables:

| Variable | Default | Description |
|---|---|---|
| `LOGS_FILE_PATH` | `src/data/apache_log.txt` | Path to the Apache log file |
| `GEO2_DB_FILE_PATH` | `src/data/GeoLite2-Country.mmdb` | Path to the GeoLite2 database |
| `NUM_OF_LINES_TO_READ` | `100` | Number of log lines to process |

Example:

```bash
NUM_OF_LINES_TO_READ=500 LOGS_FILE_PATH=/path/to/access.log python main.py
```
