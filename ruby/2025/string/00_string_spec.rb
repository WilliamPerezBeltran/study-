# string_utils_spec.rb
require_relative '00_string'

RSpec.describe 'Funciones de String en Ruby' do
  it 'longitud devuelve el tamaño de la cadena' do
    expect(longitud("Hola")).to eq(4)
  end

  it 'invierte una cadena' do
    expect(invertir("ruby")).to eq("ybur")
  end

  it 'capitaliza una cadena' do
    expect(capitalizar("hola")).to eq("Hola")
  end

  it 'extrae los primeros cinco caracteres' do
    expect(primeros_cinco("programador")).to eq("progr")
  end

  it 'cuenta las vocales' do
    expect(contar_vocales("ingeniero")).to eq(5)
  end

  it 'compara dos strings sin importar mayúsculas' do
    expect(iguales?("Ruby", "ruby")).to be true
  end

  it 'reemplaza perro por gato' do
    expect(reemplazar("El perro corre")).to eq("El gato corre")
  end

  it 'cuenta cuántas palabras hay' do
    expect(contar_palabras("Hola mundo Ruby")).to eq(3)
  end

  it 'presenta nombre y edad' do
    expect(presentar("William", 30)).to eq("Mi nombre es William y tengo 30 años.")
  end

  it 'elimina espacios en los extremos' do
    expect(limpiar("   hola   ")).to eq("hola")
  end
end
