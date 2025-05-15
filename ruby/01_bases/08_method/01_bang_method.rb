
whisper = "HELLO EVERYBODY"

puts whisper.downcase #=> "hello everybody"
puts whisper #=> "HELLO EVERYBODY"

# and now 


puts whisper.downcase! #=> "hello everybody"
puts whisper #=> "hello everybody"

# the original string is converter to downcase