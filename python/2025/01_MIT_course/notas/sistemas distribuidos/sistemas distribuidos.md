# Guía para estudiar Sistemas Distribuidos

## 1. Fundamentos básicos
Antes de entrar en teoría pesada, necesitas una base sólida en:
- **Redes**: TCP/IP, HTTP, RPC, sockets, latencia, ancho de banda.
- **Sistemas operativos**: procesos, hilos, concurrencia, sincronización, memoria.
- **Algoritmos y estructuras de datos**: colas, árboles, hash, grafos.
- **Bases de datos**: relacionales (SQL) y no relacionales (MongoDB, Redis, Cassandra).

Recursos:
- Libro: *Computer Networking: A Top-Down Approach* (Kurose & Ross).
- Curso gratuito: [CS50 Computer Science](https://cs50.harvard.edu/x/).

---

## 2. Teoría de sistemas distribuidos
Aquí vas a entender cómo se comunican y coordinan los nodos en un sistema:
- Modelos de comunicación: mensajes, paso de estado, Pub/Sub.
- **Algoritmos clásicos**: consenso (Paxos, Raft), relojes lógicos (Lamport), detección de fallos, elecciones de líder.
- **Teoremas clave**: CAP, Consistencia Eventual, ACID vs BASE.
- **Replicación y particionamiento**.

Recursos:
- Libro: *Distributed Systems: Principles and Paradigms* (Tanenbaum).
- Curso de MIT: [6.824 Distributed Systems](https://pdos.csail.mit.edu/6.824/).

---

## 3. Herramientas y tecnologías modernas
Empieza a tocar lo que usan las empresas:
- **Contenedores y orquestación**: Docker, Kubernetes.
- **Colas de mensajería**: Kafka, RabbitMQ.
- **Sistemas de almacenamiento distribuidos**: HDFS, Cassandra, DynamoDB.
- **Sistemas de cómputo distribuido**: Hadoop, Spark.

Recursos:
- Documentación oficial de [Kubernetes](https://kubernetes.io/docs/).
- Tutoriales de Kafka y Spark en YouTube.

---

## 4. Proyectos prácticos
La práctica es lo que realmente fija el conocimiento:
- Implementa un **chat distribuido** con sockets.
- Construye un **key-value store distribuido** estilo Redis.
- Haz un **crawler** que corra en múltiples nodos.
- Monta un cluster de **Kafka + Spark** para procesar streams de datos.

---

## 5. Avanzado / Lectura de papers
Si quieres ir al nivel senior:
- Papers clásicos: *The Google File System (GFS)*, *MapReduce*, *Bigtable*, *Dynamo*.
- Entender cómo funcionan los sistemas que usamos todos los días: Google, Amazon, Netflix, etc.

Recurso: [Papers We Love](https://paperswelove.org/).

---

## Consejos de estudio
1. Alterna teoría y práctica (lee un capítulo y luego implementa algo).
2. Usa mapas mentales para conectar conceptos (ej: Consenso ↔ Relojes lógicos ↔ Particiones).
3. Construye un **portafolio con proyectos distribuidos**, esto impresiona mucho en entrevistas.

