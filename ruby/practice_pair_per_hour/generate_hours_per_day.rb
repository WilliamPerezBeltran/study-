# t=Time.new(2012,01,01,0,0,0) #start time
# max_time=Time.new(2012,01,31,23,59,59) #end time
# step=60*60 #1hour
# array = []
# while t<=max_time
#      p t #your code here
#      t += step
# end




# t=Time.new(2012,01,01,0,0,0) #start time
# max_time=Time.new(2012,01,31,23,59,59) #end time
# step=60*60 #1hour
# array = []
# while t<=max_time
#      array << {
#           "time"=> t,
#           # "time"=> (now-n*one_hour).to_s,
#           "reading"=> rand(0.0..1.3).round(4)
#         }
#      t += step
# end

# p array


t=Time.new(2012,01,01,0,0,0) #start time
max_time=Time.new(2012,01,31,23,59,59) #end time
t=Time.new(2012,01,01,0,0,0) #start time
step=60*60 #1hour
array = []
while t<=max_time
     array << {
          "time"=> t,
          # "time"=> (now-n*one_hour).to_s,
          "reading"=> rand(0.0..1.3).round(4)
        }
     t += step
end

p array

