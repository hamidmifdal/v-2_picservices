from crypt import methods
from flask import Flask , render_template as r, request , flash , redirect , url_for
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
import os
basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SECRET_KEY'] = "it dog"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
UPLOAD_FOLDER='static/img/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
class Cards(db.Model):
    __tablename__ = 'Cards'
    id             = db.Column(db.Integer, primary_key = True)
    img            = db.Column(db.BLOB)
    description    = db.Column(db.String(999))
    title          = db.Column(db.String(999))
    filename       = db.Column(db.String(999))
    def __repr__(self,id,img,description,title,filename):
        self.id             = id
        self.img            = img
        self.description    = description
        self.title          = title
        self.filename       = filename

class TP(db.Model):
    __tablename__ = 'TP'
    id             = db.Column(db.Integer, primary_key = True)
    img            = db.Column(db.BLOB)
    description    = db.Column(db.String(999))
    title          = db.Column(db.String(999))
    filename       = db.Column(db.String(999))
    def __repr__(self,id,img,description,title,filename):
        self.id             = id
        self.img            = img
        self.description    = description
        self.title          = title
        self.filename       = filename

class VDT(db.Model):
    __tablename__ = 'VDT'
    id             = db.Column(db.Integer, primary_key = True)
    img            = db.Column(db.BLOB)
    description    = db.Column(db.String(999))
    title          = db.Column(db.String(999))
    filename       = db.Column(db.String(999))
    def __repr__(self,id,img,description,title,filename):
        self.id             = id
        self.img            = img
        self.description    = description
        self.title          = title
        self.filename       = filename

class AT(db.Model):
    __tablename__ = 'AT'
    id             = db.Column(db.Integer, primary_key = True)
    img            = db.Column(db.BLOB)
    description    = db.Column(db.String(999))
    title          = db.Column(db.String(999))
    filename       = db.Column(db.String(999))
    def __repr__(self,id,img,description,title,filename):
        self.id             = id
        self.img            = img
        self.description    = description
        self.title          = title
        self.filename       = filename

class GPF(db.Model):
    __tablename__ = 'GPF'
    id             = db.Column(db.Integer, primary_key = True)
    img            = db.Column(db.BLOB)
    description    = db.Column(db.String(999))
    title          = db.Column(db.String(999))
    filename       = db.Column(db.String(999))
    def __repr__(self,id,img,description,title,filename):
        self.id             = id
        self.img            = img
        self.description    = description
        self.title          = title
        self.filename       = filename

class PPL(db.Model):
    __tablename__ = 'PPL'
    id             = db.Column(db.Integer, primary_key = True)
    img            = db.Column(db.BLOB)
    description    = db.Column(db.String(999))
    title          = db.Column(db.String(999))
    filename       = db.Column(db.String(999))
    def __repr__(self,id,img,description,title,filename):
        self.id             = id
        self.img            = img
        self.description    = description
        self.title          = title
        self.filename       = filename

class UVL(db.Model):
    __tablename__ = 'UVL'
    id             = db.Column(db.Integer, primary_key = True)
    img            = db.Column(db.BLOB)
    description    = db.Column(db.String(999))
    title          = db.Column(db.String(999))
    filename       = db.Column(db.String(999))
    def __repr__(self,id,img,description,title,filename):
        self.id             = id
        self.img            = img
        self.description    = description
        self.title          = title
        self.filename       = filename

class SERIT(db.Model):
    __tablename__ = 'SERIT'
    id             = db.Column(db.Integer, primary_key = True)
    img            = db.Column(db.BLOB)
    description    = db.Column(db.String(999))
    title          = db.Column(db.String(999))
    filename       = db.Column(db.String(999))
    def __repr__(self,id,img,description,title,filename):
        self.id             = id
        self.img            = img
        self.description    = description
        self.title          = title
        self.filename       = filename

@app.route('/')
def main():
    return r('dist/index.html', p = Cards.query.all())

@app.route('/serigraphie')
def seri():
    return r('dist/page/serigraphie.html', p = SERIT.query.all())

@app.route('/ajonda')
def ajonda():
    return r('dist/page/ajonda.html', p = GPF.query.all())

@app.route('/publicitepg')
def publicitepg():
    return r('dist/page/publiciteparobjet.html', p = PPL.query.all())

@app.route('/uv_laser')
def machine(): 
    return r('dist/page/machine.html', p = UVL.query.all())

@app.route('/polos_tshirt')
def pt():
    return r('dist/page/pt.html', p = TP.query.all())

@app.route('/vetements_de_travil')
def vdt():
    return r('dist/page/vdt.html', p = VDT.query.all())

@app.route('/Autres_textiles')
def at():
    return r('dist/page/at.html', p = AT.query.all())

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

@app.route('/cards/new', methods=['GET','POST'])
def Card():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
         #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         pd = Cards(title = request.form['title'], description = request.form['description'], filename=file.filename, img=file.read())
         db.session.add(pd)
         db.session.commit()
         return redirect('/admin')
    return r('dist/dashbord/admin/cards.html', p = Cards.query.all())

@app.route('/page_serit/new', methods=['GET','POST'])
def Serit():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
         #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         fire = SERIT(title = request.form['title'], description = request.form['description'], filename=file.filename, img=file.read())
         db.session.add(fire)
         db.session.commit()
         return redirect(url_for('main'))
    #return r('dist/dashbord/admin/cards.html', p = TP.query.all())
@app.route('/page_vdt/new', methods=['GET','POST'])
def Vdt():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
         #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         pd = VDT(title = request.form['title'], description = request.form['description'], filename=file.filename, img=file.read())
         db.session.add(pd)
         db.session.commit()
         return redirect(url_for('main'))

@app.route('/page_at/new', methods=['GET','POST'])
def At():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
         #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         pd = AT(title = request.form['title'], description = request.form['description'], filename=file.filename, img=file.read())
         db.session.add(pd)
         db.session.commit()
         return redirect(url_for('main'))

@app.route('/page_gpf/new', methods=['GET','POST'])
def Gpf():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
         #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         pd = GPF(title = request.form['title'], description = request.form['description'], filename=file.filename, img=file.read())
         db.session.add(pd)
         db.session.commit()
         return redirect(url_for('main'))

@app.route('/page_ppl/new', methods=['GET','POST'])
def Ppl():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
         #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         ppl = PPL(title = request.form['title'], description = request.form['description'], filename=file.filename, img=file.read())
         db.session.add(ppl)
         db.session.commit()
         return redirect(url_for('main'))
    return r('dist/dashbord/admin/cards.html', p = PPL.query.all())

@app.route('/page_uvl/new', methods=['GET','POST'])
def Uvl():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
         #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         uvl = UVL(title = request.form['title'], description = request.form['description'], filename=file.filename, img=file.read())
         db.session.add(uvl)
         db.session.commit()
         return redirect(url_for('main'))

@app.route('/page_tp/new', methods=['GET','POST'])
def Tp():
    if request.method == 'POST':
      if not request.form['title'] or not request.form['description']:
         flash('Please enter all the fields', 'error')
      else:
         file = request.files['file']
         #file.save(file.filename)
         file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
         #file.save(os.path.join(app.config['UPLOAD_FOLDER']))
         tp = TP(title = request.form['title'], description = request.form['description'], filename=file.filename, img=file.read())
         db.session.add(tp)
         db.session.commit()
         return redirect(url_for('main'))
#card rm
@app.route('/cards/rm/<int:id>',methods=['GET','POST'])
def rmcard(id):
    rm_card = Cards.query.filter_by(id=id).first()
    if request.method=='POST':
        if rm_card:
            db.session.delete(rm_card)
            db.session.commit() 
    return redirect(url_for('main'))

        

with app.app_context():
    db.create_all()
if __name__=="__main__":
    os.system('git add .')
    os.system('git commit -m "it is server"')
    app.run(debug=True, host='0.0.0.0', port=5000)

    