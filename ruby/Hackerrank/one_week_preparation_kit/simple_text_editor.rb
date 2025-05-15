require 'pry'
require 'json'
require 'stringio'

Q = gets.to_i
puts "ole: #{Q}"
S = ""
lastState = [S]

for x in (0..Q)
    input = gets.chomp.split(" ")
    puts "x: #{input[0]}- #{input[1]}"
    
    if input[0] == "1"
        S<<input[1]
    elsif input[0] == "2"
        #S = (S.chars - S.chars.last(input[1])).join() 
        S = S[0..S.size-1-input[1]] 
    elsif input[0] == "3"
        puts S[input[1]]
    else
        S = lastState[0]
    end
end







Q = gets.to_i
puts "ole: #{Q}"
S = ""
lastState = [S]

for x in (0..Q)
    input = gets.chomp.split(" ")
    puts "x: #{input[0]}- #{input[1]}"
    
    if input[0] == "1"
        S<<input[1]
    elsif input[0] == "2"
        #S = (S.chars - S.chars.last(input[1])).join() 
        S = S[0..S.size-1-input[1]] 
    elsif input[0] == "3"
        puts S[input[1]]
    else
        S = lastState[0]
    end
end


Q = gets.to_i
S = ""
lastState = []
n = S.length-1

for x in (0..Q)
    input = gets.split(" ")
    
    if input[0] == "1"
        lastState<<S
        S<<input[1]
    elsif input[0] == "2"
        lastState<<S
        k = input[1].to_i
        S = S[0..n-k] 
    elsif input[0] == "3"
        k = input[1].to_i
        puts S[k]
    else
        previous_state = lastState.pop
        S = previous_state
    end
end