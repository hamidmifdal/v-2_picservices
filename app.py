from flask import Flask , render_template, request , flash
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "it dog"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Products(db.Model):
    __tablename__ = 'Products'
    id    = db.Column(db.Integer, primary_key = True)
    img   = db.Column(db.LargeBinary)
    nm    = db.Column(db.String(999))
    title = db.Column(db.String(999))
    def __repr__(self,id,img,nm,title):
        self.id    = id
        self.img   = img
        self.nm    = nm
        self.title = title

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
    return r('dist/dashbord/admin/admin.html')

@app.route('/admin/pages_edit')
def pages():
    return r('dist/dashbord/admin/page_edit.html')

@app.route('/admin/pages_edit/carousel')
def carousel():
    return r('dist/dashbord/admin/carousel.html')

@app.route('/admin/pages_edit/cards')
def cards():
    return r('dist/dashbord/admin/cards.html')
@app.route('cards/new', methods=['GET','POST'])
def new():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description'] or not request.form['prix']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
      #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         pd = Products(title = request.form['title'], description = request.form['description'], 
            prix = request.form['prix'], filename=file.filename, date=file.read())
         db.session.add(pd)
         db.session.commit()
         return r('dist/dashbord/admin/cards.html', p = Products.query.all())
        

with app.app_context():
    db.create_all()
if __name__=="__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)

    