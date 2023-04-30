from ser import Ser
import time

with Ser() as bot:
    bot.land_first_page()
    bot.login("Email", "Password")
    bot.dailyserve()
    time.sleep(5000)





