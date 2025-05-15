require 'pry'
require 'json'
require 'stringio'



def timeConversion(s)
    str = s.split(":")
    hour = str[0]  
    minute =  str[1]
    second =  str[2][0,2]
    am_pm_value = str[2][2,2]

    if am_pm_value == "AM" && hour == "12"
        hour = "00"
    end
    if am_pm_value == "PM" && hour != "12"
        hour = (12+hour.to_i).to_s    
    end
    hour<<":"<<minute<<":"<<second
end


p timeConversion("12:01:00AM") # => Return '00:01:00'.
p timeConversion("07:05:45PM") # => Return 19:05:45


def timeConversion(s)
    str = s.split(":")
    hour = str[0]  
    minute =  str[1]
    second =  str[2][0,2]
    am_pm_value = str[2][2,2]
    hour = "00" if am_pm_value == "AM" && hour == "12"
    hour = (12+hour.to_i).to_s    if am_pm_value == "PM" && hour != "12"
    hour<<":"<<minute<<":"<<second
end


def timeConversion(s)
    str = s.split(":")
    str[0] = "00" if str[2][2,2] == "AM" && str[0] == "12"
    str[0] = (12+str[0].to_i).to_s if str[2][2,2] == "PM" && str[0] != "12"
    str[0]<<":"<<str[1]<<":"<<str[2][0,2]
end








# https://www.freecodecamp.org/espanol/news/problemas-de-matematicas-con-las-horas-del-reloj/