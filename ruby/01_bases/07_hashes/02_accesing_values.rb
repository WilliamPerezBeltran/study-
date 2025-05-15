shoes = {
  "summer" => "sandals",
  "winter" => "boots"
}

shoes["summer"]   #=> "sandals"


# Sometimes, this behavior can be problematic for you if silently returning a nil value could potentially wreck havoc in your program. Luckily, hashes have a fetch method that will raise an error when you try to access a key that is not in your hash.

shoes.fetch("hiking")   #=> KeyError: key not found: "hiking"
# Alternatively, this method can return a default value instead of raising an error if the given key is not found.

shoes.fetch("hiking", "hiking boots") #=> "hiking boots"