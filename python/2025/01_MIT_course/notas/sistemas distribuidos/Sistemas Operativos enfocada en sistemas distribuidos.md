# Sistemas Operativos (enfocado en Sistemas Distribuidos)

## 1. Procesos
- Unidad básica de ejecución en un sistema operativo.
- Tienen su propio espacio de memoria y recursos.
- Conceptos clave: PID, estados de un proceso (nuevo, listo, ejecutando, bloqueado, terminado).
- Comunicación entre procesos (IPC): pipes, colas de mensajes, memoria compartida.

---

## 2. Hilos (Threads)
- Ejecución más ligera dentro de un proceso.
- Comparten el mismo espacio de memoria pero tienen su propio contador de programa y pila.
- Tipos: 
  - **Hilos a nivel de usuario** (User-level threads).
  - **Hilos a nivel de kernel** (Kernel-level threads).
- Ventaja: permiten paralelismo y mejor utilización de CPUs multicore.

---

## 3. Concurrencia
- Ejecución de múltiples tareas de manera intercalada.
- Problemas típicos: **condiciones de carrera**, **deadlocks**, **starvation**.
- Técnicas de programación concurrente:
  - Bloqueos (locks).
  - Monitores.
  - Semáforos.

---

## 4. Sincronización
- Coordinar la ejecución de procesos/hilos para acceder a recursos compartidos.
- Mecanismos clásicos:
  - **Semáforos** (contador de acceso).
  - **Mutex (mutual exclusion)**.
  - **Monitores** (estructuras que encapsulan datos + mecanismos de sincronización).
- Ejemplo típico: *problema de los filósofos comiendo*.

---

## 5. Memoria
- **Gestión de memoria**: cómo el sistema asigna y organiza el espacio para procesos e hilos.
- Conceptos importantes:
  - Memoria física vs memoria virtual.
  - Paginación y segmentación.
  - Swapping.
  - Caché.
- En sistemas distribuidos, se conecta con:
  - **Memoria distribuida compartida**.
  - Manejo de consistencia entre nodos.

