import string
from multiprocessing import connection
import mysql.connector
from flask import Blueprint, Flask, jsonify, render_template, request
from flask_cors import CORS, cross_origin

# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASSWORD'] = 'password'            import mysql.connector
# app.config['MYSQL_DB'] = 'countrycounty'          from flask_mysqldb import MySQL
# mysql = MySQL(app)
# cursor = mysql.connector.cursor()
# print(mysql)

app = Flask(__name__)
CORS(app, origins="*", support_credentials=True)
angular = Blueprint("angular", __name__, template_folder="src")
app.register_blueprint(angular)


@app.route('/')
@cross_origin()
def Index():
    return render_template("index.html")


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="countrycounty"
)
mycursor = mydb.cursor()


class Test():
    CountryName: string
    CapitalName: string
    Continent: string


@app.route("/Search", methods=['GET', 'POST'])  # /<string:data>
def getData():
    data = request.get_data()
    # print(data)
    # data = 'Asia'
    mycursor = mydb.cursor()
    mycursor.execute("select * from countrycapitals where  CountryName = %s or CapitalName = %s  or ContinentName = %s",
                     (data, data, data), multi=True)
    y = mycursor.fetchall()
    Arr = []
    for i in y:
        x = {
            "CountryName": i[0],
            "Capital": i[1],
            "Continent": i[2]
        }
        Arr.append(x)
    return Arr


if __name__ == '__main__':
    app.run(debug=True, port=5000)
