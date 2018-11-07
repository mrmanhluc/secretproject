from selenium import webdriver
import urllib
import pandas as pd
import logging
import commond

# general a arange date
def general_date(from_date, to_date):
    return [date.strftime('%m-%d-%Y') for date in pd.date_range(from_date, to_date)]

# general csv file name. Like 20183011_1830.csv
def csv_file_name():
    return str(commond.CURRENT_TIME.year) + str(commond.CURRENT_TIME.month) + str(commond.CURRENT_TIME.day) + \
           str('_') + str(commond.CURRENT_TIME.hour) + str(commond.CURRENT_TIME.minute) + str('.csv')

# insert a values into array
def insert(col_name, value):
    collected_data[col_name].append(value)


collected_data = {
        'journeyType': [],
        'departure': [],
        'destination': [],
        'search_date': [],
        'departure_datetime': [],
        'arrival_datetime': [],
        'stops': [],
        'passenger': [],
        'prices': [],
        'flight_number': [],
    }


class Util:
    def __init__(self):
        # Set varience for url link. Define in commond.py
        self.current = commond.CURRENT_TIME
        self.journey_type = commond.JOURNEY_TYPE
        self.locale = commond.LOCALE
        self.origin = commond.DEPARTURE
        self.adt = commond.PASSENGER
        self.destination = commond.DESTINATION
        self.from_date = commond.FROM_DATE
        self.to_date = commond.TO_DATE

    def get_urls(self):
        date_range = general_date(self.from_date, self.to_date)
        urls = []
        # General n urls. Each url has same parameters except date
        for search_date in date_range:
            urls.append(self.request_url(search_date))
        return urls

    # join all parameter and general complete URL to request
    def request_url(self, departure_date):
        url_variances = {
            'domain': 'https://fly.vietnamairlines.com/dx/VNDX/#/flight-selection?',
            'variances': {
                'journeyType': self.journey_type,
                'locale': self.locale,
                'origin': self.origin,
                'destination': self.destination,
                'ADT': self.adt,  # Adult numbers
                'CHD': 0,
                'INT': 0,
                'date': departure_date,
            }
        }
        return url_variances['domain'] + urllib.parse.urlencode(url_variances['variances'])


def crawling_data():
    urls = Util().get_urls()

    for url in urls:
        driver = webdriver.Chrome(commond.CHROME_DRIVER)
        driver.implicitly_wait(commond.WAITING_TIME)
        driver.get(url)

        try:
            # Step 1. Get main price table
            flights_main = driver.find_element_by_class_name('flights-table')

            # Step 2. Get each children from main table has class name 'dxp-flight'
            flights = flights_main.find_elements_by_class_name('dxp-flight')

            for flight in flights:
                insert('journeyType', commond.JOURNEY_TYPE)
                insert('departure', commond.DEPARTURE)
                insert('destination', commond.DESTINATION)
                insert('search_date', commond.CURRENT_TIME)

                depart_arrival_time = flight.find_elements_by_class_name('dxp-time')
                insert('departure_datetime', depart_arrival_time[0].get_attribute('datetime'))
                insert('arrival_datetime', depart_arrival_time[1].get_attribute('datetime'))

                insert('stops', flight.find_element_by_xpath("//td[@class='column flight-stops']").text)
                insert('passenger', commond.PASSENGER)

                prices = []
                for price in flight.find_elements_by_class_name("price-container"):
                    prices.append(price.text)
                insert('prices', prices)

                flight_number = flight.find_element_by_class_name("flight-number").text
                insert('flight_number', flight_number)

        except ValueError:
            logging.basicConfig(format='%(asctime)s %(message)s')
            logging.warning('Elements is not founded.')
        driver.quit()


def __main__():
    crawling_data()
    pd.DataFrame(collected_data).to_csv(csv_file_name(), index=False)


__main__()
