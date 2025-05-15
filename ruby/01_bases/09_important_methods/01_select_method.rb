p """
The #select method (also called #filter) passes every item in an array 
to a block and returns a new array with only the items for which the 
condition you set in the block evaluated to true.
"""

p "with array "
friends = ['Sharon', 'Leo', 'Leila', 'Brian', 'Arun']
friends.select { |friend| friend != 'Brian' }
 #=> ["Sharon", "Leo", "Leila", "Arun"]

p "with an hash"
responses = { 'Sharon' => 'yes', 'Leo' => 'no', 'Leila' => 'no', 'Arun' => 'yes' }
# responses.select { |person, response| response == 'yes'}
responses.select { |key, value| value == 'yes'}
#=> {"Sharon"=>"yes", "Arun"=>"yes"}

