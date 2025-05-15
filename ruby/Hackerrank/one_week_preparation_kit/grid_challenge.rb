#!/usr/bin/env ruby

=begin

Pasos:
	1. Recorro la matriz por cada fila guardando el primer elemento que va ser el punto de comparacion, lo llamaremos ref 
	2. En la segunda iteración comparo el elemento con la variable ref para determinar si está en ascendente o descendente  
		(element.ord < ref.ord) => me va determinar su comportamiento descendente o ascendente
	3.  si element.ord < ref.ord es verdadero, retorna NO 
	4. Recorro la matriz por cada columna y repito el paso 2 y 3

=end


require "pry"




def gridChallenge(grid)
    matriz = []
    for x in (0..(grid.length-1))
        matriz.push(grid[x].split("").sort)
    end

    fila = grid.length-1
    columna = grid[0].length-1

    for x in 0..columna
        for y in 0..fila-1
            return "NO" if matriz[y][x]>matriz[y+1][x]
        end
    end
    return "YES"
end

p gridChallenge(["abc","ade","efg"]) # => YES








 





