def longitud(cadena)
  cadena.length
end
puts longitud("asdf")

def invertir(cadena)
  cadena.reverse
end
puts invertir("william")

def capitalizar(cadena)
  cadena.capitalize
end
puts capitalizar("ruby")

def primeros_cinco(cadena)
  cadena[0..4]
end
puts primeros_cinco("programador")

def contar_vocales(cadena)
  con = 0
  cadena.each_char do |char|

    if char.downcase == "a" || char.downcase == "e" || char.downcase == "i" || char.downcase == "o" || char.downcase == "u" 
      con+=1
    end
  end
  con
end
puts contar_vocales("ingeniero")

def iguales?(str1, str2)
  str1 == str2
end
puts iguales?("ruby","Ruby")

#reemplazar perro por gato
def reemplazar(cadena)
  cadena.sub("perro","gato")
end
puts reemplazar("El perro corre")

def contar_palabras(frase)
  frase.split(" ").count
end
puts contar_palabras("hola mundo ruby")

#concatenar nombre y edad
def presentar(name,age)
  "#{name} #{age}"
end
puts presentar("raul",23)

def limpiar(cadena)
  cadena.strip
end
puts limpiar("      ruby        " ) 




























