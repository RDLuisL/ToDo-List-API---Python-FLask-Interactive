from flask import Flask, jsonify, json, request
# Importamos el componente de Flask como framework para crear al API
# Importamos jsonify para convertir Python en lenguaje Json 
# Importamos json que es util para manejar base de datos
# Importamos request para que nos de acceso a los datos enviados por el cliente, como URL y/o formulario.



app = Flask(__name__)
#creamos la APP

todos= [{ "label": "My first task", "done": False },
        { "label": "My first task", "done": False }]
#Creamos el objeto del ToDo List, de atributos label: es la tarea y done: es el checkbox


@app.route('/todos', methods=['GET'])
def hello_world():
    request_body = request.data
    return jsonify(todos)
#Ruta GET para obtener las tareas


@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body =request.get_json(force=True)
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)
#Ruta POST para agregar nueva tareas

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)
#Ruta DELETE para eliminar la tarea y devuelve la liustan actualizada


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)

#La APP se inicia en el host 0.0.0.0 y el puerto 3245