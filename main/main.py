from flask import Flask , jsonify ,request 
import json

app = Flask(__name__)


provas = [
    {
        "id":1,
        "nome":"Karine",
        "materia":"matematica"
    },
    {
        "id":2,
        "nome":"Joao",
        "materia":"fisica"
    }
]

# Recupera prova pelo ID , também altera e exclui seus dados 

@app.route("/provas/<int:id>", methods=["GET","PUT","DELETE"]) # GET recupera dados , PUT altera dados
def prova(id):
        if request.method == "GET": #consultar dados 
            try:
                response = provas[id]
            except IndexError:
                mensagem ="Desenvolvedor de ID {} não existe ".format(id)
                response = {"status": "Erro" ,"mensagem":mensagem}
                
            except Exception:
                mensagem = "Erro desconhecido. Procure o administrador da API"
                response = {"status": "Erro" ,"mensagem":mensagem}
            return jsonify(response)
        
        elif request.method == "PUT": # alterar dados 
            dados = json.loads(request.data)
            provas[id] = dados
            return jsonify("Alterado com sucesso",dados)    
        
        elif request.method == "DELETE": # deletar dados 
           provas.pop(id)
           return jsonify({"status":"sucesso","mensagem":"Registro excluido"})

#Listar as provas e registra uma nova prova

@app.route("/provas/",methods=["POST","GET"])
def lista_provas() :
    if request.method == "POST": # criar novo cadastro
        dados = json.loads(request.data)
        posicao = len(provas)
        dados["id"] = posicao
        provas.append(dados)
        return jsonify(provas[posicao]) 
    
    elif request.method == "GET":
        return jsonify(provas)



if __name__ == '__main__':
    app.run(debug=True)