collect() public
Invokes the given block once for each element of self.

Creates a new array containing the values returned by the block.

See also Enumerable#collect.

If no block is given, an Enumerator is returned instead.

a = [ "a", "b", "c", "d" ]
a.collect { |x| x + "!" }         #=> ["a!", "b!", "c!", "d!"]
a.map.with_index { |x, i| x * i } #=> ["", "b", "cc", "ddd"]
a                                 #=> ["a", "b", "c", "d"]

>> ['a', 'b', 'c'].collect{|letter| letter.capitalize}
=> ["A", "B", "C"]
But it looks so much nicer this way:

>> ['a', 'b', 'c'].collect(&:capitalize)
=> ["A", "B", "C"]
Default_avatar_30 shuber - August 20, 20094 thanks
Symbol#to_proc
@tadman - or simply defining:

require 'enumerator'

['a', 'b', 'c'].enum_for(:each_with_index).collect do |item, index| 
  "#{index}: #{item}" 
end
See also: Enumerable#each_with_index


['a', 'b', 'c'].collect(&:capitalize)
 #  => TypeError: wrong argument type Symbol (expected Proc)
 
Can operate for both key and value for Hash
If you need to process both key and value of the Hash:

>> {"a" => "aa", "b" => "bb", "c" => "cc"}.collect {|k,v| [k,k+v]}
=> [["a", "aaa"], ["b", "bbb"], ["c", "ccc"]]

# Conclusion
# In Ruby difference between collect and map does not exist.
# C level implementation of these methods shows that they both are same. Collect is an alias to Map