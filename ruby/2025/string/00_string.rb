def longitud(cadena)
  cadena.length
end

def invertir(cadena)
  cadena.reverse
end

def capitalizar(cadena)
  cadena.capitalize
end

def primeros_cinco(cadena)
  cadena[0..4]
end

def contar_vocales(cadena)
  con = 0
  cadena.each_char do |char|

    if char.downcase == "a" || char.downcase == "e" || char.downcase == "i" || char.downcase == "o" || char.downcase == "u" 
      con+=1
    end
  end
  con
end

def contar_vocales_(cadena)
  cadena.downcase.count("aeiou")
end


def iguales?(str1, str2)
  str1 == str2
  str1.casecmp(str2).zero?
end

#reemplazar perro por gato
def reemplazar(cadena)
  cadena.sub("perro","gato")
end

def contar_palabras(frase)
  frase.split(" ").count
end

#concatenar nombre y edad
def presentar(name,age)
  "Mi nombre es #{name} y tengo #{age} años."
end

def limpiar(cadena)
  cadena.strip
end




























