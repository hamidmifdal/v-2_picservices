from flask import Flask , render_template
from flask_sqlalchemy import SQLAlchemy

import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "it dog"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

r = render_template

@app.route('/')
def main():
    return r('dist/index.html')

@app.route('/serigraphie')
def seri():
    return r('dist/page/serigraphie.html')

@app.route('/ajonda')
def ajonda():
    return r('dist/page/ajonda.html')

@app.route('/publicitepg')
def publicitepg():
    return r('dist/page/publiciteparobjet.html')

@app.route('/uv_laser')
def machine(): 
    return r('dist/page/machine.html')

@app.route('/polos_tshirt')
def pt():
    return r('dist/page/pt.html')

@app.route('/vetements_de_travil')
def vdt():
    return r('dist/page/vdt.html')

@app.route('/Autres_textiles')
def at():
    return r('dist/page/at.html')

@app.route('/admin')
def admin():
    return r('test.html')

with app.app_context():
    db.create_all()
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

    