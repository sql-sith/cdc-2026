
# When is My Party

Given today's date and a birthday, return the number of days until the person's next birthday.

* Today's date is given as a string in `"YYYY-MM-DD"` format, with leading zeros, for example: `"2026-07-16"`.
* The birthday is given as a string in `"M/D"` format, without leading zeros, for example: `"9/7"`.
* If today is their birthday, return the number of days until their next birthday (not `0`).
* Leap years should be accounted for.

## Tests

1. days_until_birthday("2026-07-16", "9/7") should return 53.
2. days_until_birthday("2026-07-16", "3/22") should return 249.
3. days_until_birthday("2026-07-16", "7/16") should return 365.
4. days_until_birthday("2024-02-28", "3/1") should return 2.
5. days_until_birthday("2023-04-24", "12/30") should return 250.
6. days_until_birthday("2024-03-01", "2/29") should return 1460.
