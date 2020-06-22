import mongodb
from utils import web_scraping
import datetime


def insert():
    soup = web_scraping.scraping()

    for i in soup.findAll('div', class_='views-row'):

        state = i.find('span', class_='st_name').text

        active = i.find('div', class_='tick-active').small.text

        cured = i.find('div', class_='tick-discharged').small.text

        death = i.find('div', class_='tick-death').small.text

        confirmed = i.find('div', class_='tick-confirmed').small.text

        mydict = {"time": datetime.datetime.now(), "state": state, "active": int(
            active), "cured": int(cured), "death": int(death), "confirmed": int(confirmed)}

        myStatedict = {"state": state}

        mongodb.insert(mydict, myStatedict)
