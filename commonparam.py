import datetime

# Parameters of a request URL
JOURNEY_TYPE = 'one-way'
DEPARTURE = 'NRT'
DESTINATION = 'SGN'
LOCALE = 'en-US'
PASSENGER = 1
FROM_DATE = '12-01-2018'
REQUEST_DAYS = 30
PAGE_ADDRESS = 'https://fly.vietnamairlines.com/dx/VNDX/#/flight-selection?'

# Parameters of selenium
CURRENT_TIME = datetime.datetime.now()
WINDOWS_CHROME_DRIVER = 'chromedriver.exe'
WAITING_TIME = 20
LINUX_CHROME_DRIVER = 'chromedriver'
LINUX_CHROME_STABLE = '/usr/bin/google-chrome-stable'
