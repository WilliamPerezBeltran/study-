# https://stackoverflow.com/questions/28319759/how-get-the-last-week-start-date-and-end-date-based-on-date-in-current-week-ruby?rq=1
# https://stackoverflow.com/questions/28319759/how-get-the-last-week-start-date-and-end-date-based-on-date-in-current-week-ruby?rq=1
# https://stackoverflow.com/questions/28319759/how-get-the-last-week-start-date-and-end-date-based-on-date-in-current-week-ruby?rq=1
# https://stackoverflow.com/questions/28319759/how-get-the-last-week-start-date-and-end-date-based-on-date-in-current-week-ruby?rq=1
# https://stackoverflow.com/questions/28319759/how-get-the-last-week-start-date-and-end-date-based-on-date-in-current-week-ruby?rq=1


require 'date'
=> true

date = Date.today
=> #<Date: 2015-02-04 ((2457058j,0s,0n),+0s,2299161j)>

# date.wday return week day
end_date = date-date.wday
=> #<Date: 2015-02-01 ((2457055j,0s,0n),+0s,2299161j)>

start_date = date-date.wday-6
=> #<Date: 2015-01-26 ((2457049j,0s,0n),+0s,2299161j)>





=================================
=================================
=================================

You could use DateTime.parse

 d1 = DateTime.parse("20141024_142440","%Y%m%d_%H%M%S")
 d2 = DateTime.parse("20141024_133641","%Y%m%d_%H%M%S")
and compare them as usual

 if d1 > d2 ...
or like @kroky said

[d1,d2].min.to_s #=> "2014-10-24T13:36:41+00:00"
[d1,d2].max.to_s #=> "2014-10-24T14:24:40+00:00"