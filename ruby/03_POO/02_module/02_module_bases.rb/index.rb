require "./animal"

include Animals

p Animals::NUMBER_OF_ANIMALS
p Animals::hello

# I can get access with :: to constants and methods
# I can get access to constants  only with ::
# I can get access to methods with :: and .

p Animals::NUMBER_OF_ANIMALS
p Animals.hello