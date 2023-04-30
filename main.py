from ser import Ser
import time

with Ser() as bot:
    bot.land_first_page()
    bot.login("hamza1996780@gmail.com","Hamza123")
    bot.dailyserve()
    time.sleep(5000)





