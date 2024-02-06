import os
import xml.etree.ElementTree as ET

html = '''
<!DOCTYPE html>
<html>
<head>
    <title>EngWeb2023</title>
    <meta charset="UTF-8">
</head>
<body>
'''

template = html

def percorrer_pastaXML(directory):
    ruas = set() # usei set para não haver ruas duplicadas
    
    for filename in os.listdir(directory):
        if filename.endswith('.xml'): 
            tree = ET.parse(os.path.join(directory, filename))
            root = tree.getroot()
            
            rua_nome = None
            imagens = []
            
            for rua in root.iter('nome'):
                rua_nome = rua.text
                
            for figura in root.iter('figura'):
                imagem_path = figura.find('imagem').attrib['path']
                imagens.append(imagem_path)
                
            if rua_nome:
                html_rua = template
                html_rua += f"<h1>{rua_nome}</h1>"

                html_rua += "<div>"
                
                for imagem in imagens:
                    html_rua += f"<img src='{imagem}' alt='Imagem'>"
                html_rua += "</div>"    
                
                    
                html_rua += "</body>"
                html_rua += "</html>"

                if not os.path.exists('html'):
                    os.mkdir('html')
                
                with open(f"html/{rua_nome}.html", "w", encoding="utf-8") as file:
                    file.write(html_rua)
                    
                ruas.add(rua_nome)

    return sorted(ruas)


pasta_xmlInfo = './MapaRuas-materialBase/texto'

ruas = percorrer_pastaXML(pasta_xmlInfo)

html += "<ul>"

print(f"Número de ruas encontrado: {len(ruas)}")
for rua in ruas:
    print(rua)
    
    html += f"<li><a href='html/{rua}.html'>{rua}</a></li>"
    
html += "</ul>"
html += "</body>"
html += "</html>"

file = open("ruas.html", "w", encoding="utf-8")
file.write(html)
file.close()

    
    
    
