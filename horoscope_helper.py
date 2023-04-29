from bs4 import BeautifulSoup
import requests


def get_sign(month, day):
    """
    Given parameters month, day, returns astrological sign
    Source: https://www.w3resource.com/python-exercises/python-conditional-exercise-38.php
    """
    month = str(month)
    day = int(day)
    try:
        if month == "12":
            astro_sign = "Sagittarius" if (day < 22) else "capricorn"
        elif month == "1":
            astro_sign = "Capricorn" if (day < 20) else "aquarius"
        elif month == "2":
            astro_sign = "Aquarius" if (day < 19) else "pisces"
        elif month == "3":
            astro_sign = "Pisces" if (day < 21) else "aries"
        elif month == "4":
            astro_sign = "Aries" if (day < 20) else "taurus"
        elif month == "5":
            astro_sign = "Taurus" if (day < 21) else "gemini"
        elif month == "6":
            astro_sign = "Gemini" if (day < 21) else "cancer"
        elif month == "7":
            astro_sign = "Cancer" if (day < 23) else "leo"
        elif month == "8":
            astro_sign = "Leo" if (day < 23) else "virgo"
        elif month == "9":
            astro_sign = "Virgo" if (day < 23) else "libra"
        elif month == "10":
            astro_sign = "Libra" if (day < 23) else "scorpio"
        elif month == "11":
            astro_sign = "scorpio" if (day < 22) else "sagittarius"
        return astro_sign.lower()
    except:
        return f"Error, try again!"


def daily_horoscope(given_sign):
    """
    This function returns the daily horoscope, given the parameter entered is the sign.
    Souce: https://github.com/sameerkumar18/aztro/issues/42#issuecomment-1491602309
    """
    signs = {
        "aries": 1,
        "taurus": 2,
        "gemini": 3,
        "cancer": 4,
        "leo": 5,
        "virgo": 6,
        "libra": 7,
        "scorpio": 8,
        "sagittarius": 9,
        "capricorn": 10,
        "aquarius": 11,
        "pisces": 12,
    }

    URL = (
        "https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-today.aspx?sign="
        + str(signs[given_sign])
    )

    r = requests.get(URL)
    soup = BeautifulSoup(r.text, "html.parser")

    container = soup.find("p")

    return container.text.strip()

def horoscope_yay(month,day):
    """
    Combines the two, woopdedoo~
    """
    s=get_sign(month,day) 
    print(s)
    h=daily_horoscope(s)
    return h

def main():
    evas_sign=get_sign(9,30)
    print(evas_sign)
    evas_horoscope=daily_horoscope(evas_sign)
    print(evas_horoscope)


if __name__ == "__main__":
    main()
