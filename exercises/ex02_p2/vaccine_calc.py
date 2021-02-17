"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730394055"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    elaps_days: int = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    date_of_salv: str = future_date(elaps_days)
    # TODO 5: Print the expected output using the variables above.
    elaps_str: str = str(elaps_days)
    tar_str: str = str(target)
    print("We will reach " + tar_str + "% vaccination in " + elaps_str + " days, which falls on " + date_of_salv + ".")


# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Returns number of days until population has reached a certain percent vaccinated."""
    total_doses_desired: int = round(2 * population * target / 100)
    remaining_doses_needed: int = total_doses_desired - doses
    elaps_int: int = round(remaining_doses_needed / doses_per_day)
    return elaps_int


# TODO 3: Define future_date function
def future_date(elaps_int: int) -> str:
    """Turns integer of time to reach desire vaccine % into a string stating the day the vaccine % will be reached."""
    elaps_days: timedelta = timedelta(elaps_int)
    today: datetime = datetime.today()
    end_date: datetime = today + elaps_days
    return end_date.strftime("%B %d, %Y")


if __name__ == "__main__":
    main()