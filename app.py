from logging import debug
from flask import Flask, render_template, url_for, request, redirect # render_template is use for render the html file in template folder
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime
from werkzeug.utils import redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

db= SQLAlchemy(app) #db connection

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key= True)   #Db table data
    content = db.Column(db.String(200), nullable=False)     #Db table data
    date_created = db.Column(db.DateTime, default = datetime.utcnow)    #Db table data

    def __repr__(self):
        return '<Task %r>' % self.id  

@app.route('/',methods = ['POST','GET'])

def index():
    if request.method == 'POST':
        task_content = request.form['content'] # Get the content in form
        new_task = Todo(content = task_content) # store the content in todo object

        try:
            db.session.add(new_task)    # add task in db
            db.session.commit()
            return redirect('/')
        
        except:
            return 'Some issues to adding the task'
    
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html',tasks=tasks) 

@app.route('/delete/<int:id>',methods = ['POST','GET'])
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)  #Get the task id and fetch the detail in db

    try:
        db.session.delete(task_to_delete)   # delete task in db
        db.session.commit()
        return redirect('/')
    except:
        return 'TSome issues to deleting the task'


@app.route('/update/<int:id>',methods = ['POST','GET'])
def update(id):
    task= Todo.query.get_or_404(id)     # get the task using id and update
     
    if request.method == 'POST':
        task.content = request.form['content']

        try:
            db.session.commit()     # update task in db
            return redirect('/') 
        except:
            return 'Unable to update'       
    else:
        return render_template('update.html', task= task)

if __name__ == "__main__":
    app.run(debug = True)
