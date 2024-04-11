from flask import Flask, jsonify, request
app = Flask(__name__)

todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

#@app.route('/todos') especifica el endpoint que estará disponible
@app.route('/todos', methods=['GET'])   # metodo GET para obtener info
def hello_world():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])  # metodo POST para añadir nueva tarea
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print("Incoming request with the following body", request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])  
def delete_todo(position):
    todos.pop(position)
    print ("This is the position to delete:", position)
    return jsonify(todos)




# Estas dos líneas siempre deben estar al final de tu archivo app.py
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)