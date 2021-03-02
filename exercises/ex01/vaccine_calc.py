"""A vaccination calculator."""

__author__ = "730394055"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...
population: int = int(input("Population: "))
compl_dose: int = int(input("Doses administered: "))
daily_dose: int = int(input("Doses per day: "))
target_pct: int = int(input("Target percent vaccinated: "))
today: datetime = datetime.today()

total_doses_desired: int = round(2 * population * target_pct / 100)
remaining_doses_needed: int = total_doses_desired - compl_dose
elaps_int: int = round(remaining_doses_needed / daily_dose)
elaps_days: timedelta = timedelta(elaps_int)
end_date: datetime = today + elaps_days

print("We will reach " + str(target_pct) + "% vaccination in " + str(elaps_int) + " days, which falls on " + 
    end_date.strftime("%B %d, %Y") + ".")