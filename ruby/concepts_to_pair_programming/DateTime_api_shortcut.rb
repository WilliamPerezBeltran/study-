https://www.shortcutfoo.com/app/dojos/ruby-dates/cheatsheet
https://www.shortcutfoo.com/app/dojos/ruby-dates/cheatsheet
https://www.shortcutfoo.com/app/dojos/ruby-dates/cheatsheet

Date & Time Parts I
d.cwday		Return the day of calendar week of date d (1-7, Monday is 1)
d.cweek		Return the calendar week number of date d (1-53)
d.day		Return the day of the month of date d (1-31)
d.month		Return the month (1-12) of date d (option 2)
d.wday		Return the day of week of date d (0-6, Sunday is zero)
d.yday		Return the day of year of date d (1-366)
d.year		Return the year of date d

Addition / Subtraction I
d + integer		Return a date object with integer days added to date d
d - integer		Return a date object with integer days subtracted from date d
d1 - d2		Return the difference between date d1 and date d2
d << integer		Return a date object with integer months subtracted from date d
d >> integer		Return a date object with integer months added to date d
d.nextReturn a date object denoting the following date of date d (option 1)

Addition / Subtraction II
d.next_dayDate d + 1 day (long form)
d.next_monthDate d + 1 month (long form)
d.next_yearDate d + 1 year (long form)
d.prev_dayDate d - 1 day (long form)
d.prev_monthDate d - 1 month (long form)
d.prev_yearDate d - 1 year (long form)
d.succReturn a date object denoting the following date of date d (option 2)

Constants I
Date::ABBR_DAYNAMES	Array of abbreviated day names
Date::ABBR_MONTHNAMES   Array of abbreviated month names
Date::DAYNAMES   Array of full names of days of the week
Date::ENGLAND    The Julian day number of the day of calendar reform for England and her colonies
Date::GREGORIAN   The Julian day number of the day of calendar reform for the proleptic Gregorian calendar
Date::ITALYThe Julian day number of the day of calendar reform for Italy
Date::JULIANThe Julian day number of the day of calendar reform for the proleptic Julian calendar
Date::MONTHNAMES   Array of full month names

Conversion I
d.to_date    Return self of date d
d.to_datetime   Convert date d to DateTime
d.to_s   Return a string of date d in ISO 8601 format
d.to_time    Convert date d to Time

Iteration I
d1.downto(d2)   Iterate down from dates d1 to d2 one day at a time passing date to block
d1.step(d2, integer)   Iterate integer steps at a time from dates d1 to d2
d1.upto(d2)    Iterate up from dates d1 to d2 one day at a time passing date to block

Inspection I
d.friday?   Return true if date d is Friday
d.monday?   Return true if the date is Monday
d.saturday?  Return true if the date is Saturday
d.sunday?   Return true if date d is Sunday
d.thursday?   Return true if date d is Thursday
d.tuesday?   Return true if date d is Tuesday
d.wednesday?   Return true if date d is Wednesday

Inspection II
d.inspect   Return the value as a string for inspection of date d
d.gregorian?  Return true if date d is on or after the day of calendar reform
d.julian?   Return true if date d is before the day of calendar reform
d.leap?    Return true if the year is a leap year of date d

General I
d1 <=> d2    Compare two dates d1 and d2 and return -1, 0, 1, or nil.
d1 === d2    Return true if d1 and d2 are the same day
d.asctime    Return a string in asctime format. Equivalent to strftime('%c') (option 1)
d.ctime     Return a string in asctime format. Equivalent to strftime('%c') (option 2)
d.httpdate    Format date d as http date (equivalent to strftime('%a, %d %b %Y %T GMT')

Date & Time Parts II
d.ajd   Return the astronomical Julian day number of date d
d.amjd   Return the astronomical modified Julian day number of date d
d.cwyear   Return the calendar week based year of date d
d.day_fraction   Return the fractional part of the day of date d
d.jd   Return the Julian day number of date d
d.mon   Return the month (1-12) of date d (option 1)
d.start   Return the Julian day number denoting the day of calendar reform
