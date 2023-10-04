from flask import Flask, request, redirect, url_for, render_template, jsonify
import psycopg2
from flask_jwt_extended import JWTManager, create_access_token, jwt_required


#a senha deve ser gerado pessoalmente
app = Flask(__name__, template_folder='templates')
app.config['JWT_SECRET_KEY'] = '54d2d2df568ceb7d5262c72bc2f4e0e1'
jwt = JWTManager(app)

#informações devem ser compativeis com o dockerfile geral
db_conn = psycopg2.connect(
            dbname="postgres",
            user="alysson",
            password="1984",
            host="localhost",
            port="5432")


#rota de login
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/validar', methods=['GET'])
@jwt_required()
def validate_token():
    print('teste')
    return jsonify({'success': True}), 200


#rota para a pagina de inicio: page
@app.route('/page')
def inicio():
    return render_template('page.html')


@app.route('/login', methods=["POST"])
def protected():
    data = request.get_json()
    usuario = data.get('username')
    senha = data.get('password')
    
    cursor = db_conn.cursor()
    cursor.execute('SELECT cliente, senha FROM cadastro WHERE cliente = %s AND senha = %s', (usuario, senha))
    db_conn.commit()
    result = cursor.fetchone()
    
    if result is not None:
        access_token = create_access_token(identity=usuario)
        response_data = {'access_token': access_token, 'success': True}
        print('Login realizado com sucesso!')
    else:
        cursor.close()
        db_conn.close()
        
    
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
