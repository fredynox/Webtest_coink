from flask import Flask, jsonify, request, render_template
from Models import Users, db
from logging import exception

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database\\oink.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

#acá empieza la web ;)
@app.route("/")
def home():
    return render_template("index.html")
  

@app.route("/api/users", methods=["GET"])
def gtUsers():
    try:
        
        list_users = Users.query.all()
        toReturn = [users.__str__() for users in list_users]
        
        return jsonify(toReturn), 200
    except Exception:
        exception("[SERVER]: Error")
        return jsonify({"msg": " Ha ocrrurrido un error"}), 500
    
@app.route("/api/searchuser", methods=["POST"])
def searchUserFrom():
    try:
        nameUser = request.form["name"]

        list_user = Users.query.filter(Users.name.like(f"%{nameUser}%")).first()
        if not list_user:
            return jsonify({"msg": " Este usuario no existe"}), 200
        else:
            return jsonify(list_user.serialize()), 200 
    
    except Exception:
        exception("[SERVER]: Error in route /api/searchuser ->")
        return jsonify({"msg": " Ha ocrrurrido un error"}), 500    

@app.route("/api/finduser", methods=["GET"])
def getUser():
    try:
        fields = {}
        if "name" in request.args:
            fields["name"] = request.args["name"]

        if "email" in request.args:
            fields["email"] = request.args["email"]    

        if "phone" in request.args:
            fields["phone"] = request.args["phone"]

        
        list_user = Users.query.filter_by(**fields).first()

        if not list_user:
            return jsonify({"msg": " Este usuario no existe"}), 200
        else:
            return jsonify(list_user.serialize()), 200 
    except Exception:
        exception("[SERVER]: Error")
        return jsonify({"msg": " Ha ocrrurrido un error"}), 500    

#formulario HTML creado 
# @app.route("/")
# def home():
#    return render_template("index.html")

@app.route("/api/adduser", methods=["POST"])
def adduser():
    try:
        name = request.form["name"]
        email = request.form["email"]
        phone = request.form["phone"]

        Newuser = Users(name, email, int(phone))
        db.session.add(Newuser)
        db.session.commit()

        return jsonify(Newuser.serialize()), 200
    except Exception:
        exception("\n[SERVER]: Error in route /api/adduser. Log: \n")
        return jsonify({"msg": "algo no va bien"}), 500

headings = ("Nombre", "E-Mail", "Teléfono")

@app.route('/VistaUsuarios', methods=['GET', 'POST'])
def table():
    res = Users.query.all()
    for temp in res:
        print (temp) 
    return render_template('VistaUsuarios.html', res=res, headings=headings)

    

if __name__ == "__main__":
    app.run(debug=False, port=5000)

