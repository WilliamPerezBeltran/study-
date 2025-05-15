shoes = {
  "summer" => "sandals",
  "winter" => "boots",
  "fall"=>"sneakers"
}



shoes.delete("summer")    #=> "flip-flops"
shoes                     #=> {"winter"=>"boots", "fall"=>"sneakers"}