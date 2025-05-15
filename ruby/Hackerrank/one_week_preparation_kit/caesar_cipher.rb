def caesarCipher(s, k)
    factor = k
    if factor > 26
        factor = ((k/26)*26-k).abs()
    end
    alphabet_minusculas = "a".upto("z").map(&:to_s)
    alphabet_mayusculas = "A".upto("Z").map(&:to_s)
    rta = s.split("").map do |x| 
        if alphabet_minusculas.include?(x)
            alphabet_minusculas[alphabet_minusculas.index(x)+factor-26]
        elsif  alphabet_mayusculas.include?(x)
            alphabet_mayusculas[alphabet_mayusculas.index(x)+factor-26]
        else
             x
        end
    end
    rta.join("")

end

p caesarCipher("middle-Outz", 3)