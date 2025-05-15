puts """
Calling the #methods method on an array will also yield a long list of the available methods.

num_array.methods       #=> A very long list of methods
[].methods       #=> A very long list of methods
"""


[].empty?               #=> true
[[]].empty?             #=> false
[1, 2].empty?           #=> false

[1, 2, 3].length        #=> 3

[1, 2, 3].reverse       #=> [3, 2, 1]

[1, 2, 3].include?(3)   #=> true
[1, 2, 3].include?("3") #=> false

[1, 2, 3].join          #=> "123"
[1, 2, 3].join("-")     #=> "1-2-3"

print [1,2,3].map{ |num| num*2}
puts ""
print [1,2,3].collect{ |num| num*2}
puts ""

[1,2,3].delete_at(1)

["run", "jump", "stay","hit"].delete("run")

irb :010 > b = [1, 1, 2, 2, 3, 3, 4, 4]
=> [1, 1, 2, 2, 3, 3, 4, 4]
irb :011 > b.uniq
=> [1, 2, 3, 4]
irb :012 > b
=> [1, 1, 2, 2, 3, 3, 4, 4]

If you add the bang suffix (!) to this method, you can perform the uniq function destructively. Much like the way the delete method works.

Copy Code
irb :013 > b = [1, 1, 2, 2, 3, 3, 4, 4]
=> [1, 1, 2, 2, 3, 3, 4, 4]
irb :014 > b.uniq!
=> [1, 2, 3, 4]
irb :015 > b
=> [1, 2, 3, 4]