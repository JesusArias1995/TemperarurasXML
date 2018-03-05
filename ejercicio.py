from lxml import etree
import time

doc = etree.parse('sevilla.xml')

codigos=doc.findall("municipio")

nombre=input("Dime el nombre de un municipio: ")

for i in codigos:
	if nombre.upper()==i.text.upper():
		codigo=i.attrib["value"][-5:]

url="http://www.aemet.es/xml/municipios/localidad_"+codigo+".xml"

arbol=etree.parse(url)

for i in arbol.findall("prediccion/dia"):
	if i.attrib["fecha"]==time.strftime("%Y-%m-%d"):
		maxima=i.find("temperatura/maxima")
		minima=i.find("temperatura/minima")
print("Temperatura máxima:", maxima.text)
print("Temperatura mínima:", minima.text)
