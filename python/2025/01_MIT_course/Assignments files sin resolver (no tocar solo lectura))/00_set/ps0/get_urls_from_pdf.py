import re

# Leer el PDF como binario
with open("MIT6_0001F16_ProblemSet0.pdf", "rb") as f:
    raw_data = f.read()

# Decodificar el binario a texto ignorando errores
text = raw_data.decode(errors="ignore")

# Regex para capturar URLs
pattern = re.compile(r'https?://[^\s)<>"]+')

# Buscar todas las coincidencias en el texto completo
urls = pattern.findall(text)

# Eliminar duplicados y ordenar
unique_urls = sorted(set(urls))

# Mostrar en consola
for url in unique_urls:
    print(url)

# Guardar en TXT (una URL por línea)
with open("urls.txt", "w") as f:
    f.write("\n".join(unique_urls))
