import re

def main():
    with open("filmes.json", encoding="utf-8") as f:    
        content = f.read()
    
    # Substituir o padrão do "_id" e formatar o conteúdo
    content = re.sub(r"\"_id\":{\"\$oid\":\"(\w+)\"}", "\"id\":\"\\1\"", content)
    content = re.sub(r"}\n{", r"},\n{", content)
    content = re.sub(r"{\"id\"", "\t\t{\"id\"", content)
    
    with open("filmes_normalized.json", "w", encoding="utf-8") as nf:
        nf.write("{\n\t\"filmes\": [\n" + content + "\t]\n}")

main()