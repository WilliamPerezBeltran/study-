
p "Ruby: Find a hash key given it's value"
Hash#key(value) → key
# => Returns the key of the first occurrence of a given value.
     If the value is not found, returns nil.

hash = { "a" => 100, "b" => 200, "c" => 300, "d" => 300 }
hash.key(200)   #=> "b"
hash.key(300)   #=> "c"
hash.key(999)   #=> nil
