from flask import Flask, request, jsonify
import re
app = Flask(__name__)
def validate_password(password):
    errors = []
    if len(password) < 8:
         errors.append("A senha deve ter pelo menos 8 caracteres.")
         if not re.search(r"[A-Z]", password):
             errors.append("A senha deve conter pelo menos uma letra maiúscula.")
         if not re.search(r"[a-z]", password):
             errors.append("A senha deve conter pelo menos uma letra minúscula.")
         if not re.search(r"[0-9]", password):
             errors.append("A senha deve conter pelo menos um dígito numérico.")
         if not re.search(r"[!@#$%]", password):
            errors.append("A senha deve conter pelo menos um caractere especial (!@#$%).")

    return errors

@app.route('/validate-password', methods=['POST'])
def validate():
    data = request.get_json()
    password = data.get('password')

    if not password:
        return jsonify({"error": "Senha não fornecida."}), 400

    errors = validate_password(password)

    if errors:
        return jsonify({"errors": errors}), 400
    else:
        return '', 204

if __name__ == '__main__':
    app.run(debug=True)