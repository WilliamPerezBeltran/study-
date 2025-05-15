=begin


https://medium.com/@lcriswell/ruby-symbols-vs-strings-248842529fd9
https://www.culttt.com/2015/04/22/what-are-symbols-in-ruby/
https://www.youtube.com/watch?v=mBXGBbEbXZY&ab_channel=PeterCooper


Symbols vs. Strings
To get a better idea of how symbols 
are stored in memory, give this a whirl 
in irb or a REPL. The object_id method 
returns an integer identifier for an object. 
(And remember: in Ruby, everything is an object!)

=end


"string" == "string"  #=> true

"string".object_id == "string".object_id  #=> false

:symbol.object_id == :symbol.object_id    #=> true


