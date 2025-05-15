# ===================Mezclando el módulo========================
class Person
  include MyModule
end

class Person
  include MyModule1
  include MyModule2
  include MyModule4
     .
     .
     .
     n modulos
end
# ===================Anidando módulos========================
module System
  module Currency
    class Dollar
    end
  end
end

¿Cómo accedemos a la clase Dollar? De la siguiente forma:
System::Currency::Dollar.new