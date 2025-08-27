
========================== Linked list: ===========================

- Las listas enlazadas es un tipo de estructura de dato lineal en los cuales los
elementos llamados nodos estan conectados mediante referencias o punteros. 

Partes de una lista enlazada: 

1.  NODO:
	( unidad básica ) Cada NODO contiene:
		1. DATO => El valor que almacena  
		2. PUNTERO => La dirección al siguiente nodo.
	
	Ejemplo visual:

				[ data | next ] => 

2.  CABEZA:
	- Es el primer nodo de la lista
	- Este nos permite entrar a toda la lista desde ahí podemos recorrer nodo por nodo 
	- Si la lista esta vacia el head es null 
	
	Ejemplo visual:
	
			Head =>  [ 10 | next ] => [ 20 | next ] =>  [ 30 | Null ] 

3.  TAIL ( cola ):
	- Es el ultimo nodo de la lista
	- Su puntero Next siempre apunta a null ( porque no hay mas elementos después )

	Ejemplo visual:

			Head =>  [ 10 | next ] => [ 20 | next ] =>  Tail

4.  LINKS ( enlaces ):
	- Son las conexiones entre los nodos ( el next que apunta al siguiente nodo )
	- Son los que permiten recorrer la lista de principio a fin 

	Ejemplo visual:

			Head =>  [ 10 | next ] => [ 20 | next ] =>  Tail

	Resumen 
	- Head
	- Tail 
	- Nodo 
	- Next 
	- Null 


	Ejemplo visual:

			Head =>  [ 10 | next ] => [ 20 | next ] =>  Tail
			
			↓	         ↓           ↓          ↓          ↓ 
			Cabeza    data       Enlace    puntero     Cola

Tipos de listas enlazadas:

1. listas enladas simples:
- Cada nodo tiene un dato y un puntero al siguiente nodo 

			Head =>  [ 10 | next ] => [ 20 | next ] => null 

2. LIstas doblemente enlazadas:
- Cada nodo tiene puntero al siguiente y al alterior nodo.

			head <=> [ prev | data| next ] <=> [ prev | data | next ] <=> null


3. Listas enlazadas ciruclares:
- El ultimo nodo apunta nuevamente al head 
- Se puede recorrer ambas direcciones 

			head <=> [prev|data|next] <=> [prev|data|next] <=> head 
			head => [prev|data|next] => [prev|data|next] => head 

Aplicaciones reales de software para cada una:

1. Lista enlazada simple

 Aplicación real: Implementación de historial de navegación web.
Cada página visitada se agrega como un nodo, y es fácil avanzar (next) en el historial. No necesitas retroceder muchas veces, por eso basta con un puntero hacia adelante.

2. Lista doblemente enlazada

 Aplicación real: Implementación de editor de texto (undo/redo).
Cuando editas un documento (Word, Google Docs, VS Code), cada cambio es un nodo en la lista. Puedes moverte hacia atrás (undo) o hacia adelante (redo) gracias a los punteros prev y next.

3. Lista circular simple

 Aplicación real: Round-robin scheduling en sistemas operativos.
En un sistema multitarea, cada proceso tiene un tiempo en CPU. La lista circular permite recorrer los procesos en bucle y asignar turno de manera equitativa.

4. Lista circular doble

 Aplicación real: Playlist de un reproductor de música.
Las canciones están conectadas en ambas direcciones y de forma circular. Puedes avanzar o retroceder infinitamente sin preocuparte por un final.


