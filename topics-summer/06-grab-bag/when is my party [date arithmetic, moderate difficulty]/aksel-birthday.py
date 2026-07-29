from datetime import datetime

def days_until_birthday(todays_date: str, birthday: str) -> int:
    """ Get days until a birthday.

    Arguments:
    - todays_date (str): The current date (YYYY-MM-DD).
    - birthday (str): The birthday to check (M/D).

    Returns:
    - int: The number of days until the birthday.
    """

    today = datetime.strptime(todays_date, "%Y-%m-%d")
    birthday2 = '3/1' if birthday in ['2/29', '02/29'] else birthday
    try:
        early_bdate = datetime.strptime(f"{todays_date[:4]}/{birthday}", "%Y/%m/%d")
    except ValueError:
        early_bdate = datetime.strptime(f"{todays_date[:4]}/{birthday2}", "%Y/%m/%d")
    try:
        late_bdate = datetime.strptime(f"{int(todays_date[:4])+1}/{birthday}", "%Y/%m/%d")
    except ValueError:
        late_bdate = datetime.strptime(f"{int(todays_date[:4])+1}/{birthday2}", "%Y/%m/%d")

    till_early = (early_bdate - today)
    till_late = (late_bdate - today)

    if till_early.days < 1:
        return till_late.days
    return min(x.days for x in [till_early, till_late])