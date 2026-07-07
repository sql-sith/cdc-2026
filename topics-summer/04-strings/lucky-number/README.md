# Lucky Number

Given a string of a person's first and last name, calculate their lucky number using the following rules:

* First and last names are separated by a space
* Find the vowel and consonant count for each name
* Multiply the smaller vowel and consonant counts by each other and then by the length of the smaller name
* Do the same for the two larger counts and the larger name
* Subtract the smaller value from the larger one to get their lucky number
* If the final value is zero (0), return 13.

Tests:

1. get_lucky_number("John Doe") should return 21.
2. get_lucky_number("Olivia Lewis") should return 52.
3. get_lucky_number("James Wilson") should return 18.
4. get_lucky_number("Elizabeth Hernandez") should return 81.
5. get_lucky_number("Mike Walker") should return 32.
6. get_lucky_number("Chloe Perez") should return 13.
