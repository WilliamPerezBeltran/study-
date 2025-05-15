# scope.rb

a = 5             # variable is initialized in the outer scope

3.times do |n|    # method invocation with a block
  puts a = 3           # is a accessible here, in an inner scope?
end
puts "--"
puts a


=begin
What is the value of a when it is printed to the screen? Try it out.

The value of a is 3. This is because a is available to the inner scope 
created by 3.times do ... end, which allowed the code to re-assign the 
value of a. In fact, it re-assigned it three times to 3. Let's try something else.
 We'll modify the same piece of code. 
=end