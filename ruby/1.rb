require "json"

# hash to json 
datos = {nombre:"ralph", age:23}
to_json = JSON.generate(datos)
p to_json

# convert JSON to hash
hash = JSON.parse(to_json)
p hash
# entonces tenemos JSON.generate() y JSON.parse()






require "date"

puts Time.now 
puts Date.today
puts Date.parse("2025-05-15").strftime("%d/%m/%y")






require "digest"
contraseña = "secreto3215"
hash = Digest::SHA256.hexdigest(contraseña)
puts hash







require "net/http"
require "uri"

uri = URI("https://jsonplaceholder.typicode.com/todos/1")
respuesta = Net::HTTP.get(uri)
puts respuesta
