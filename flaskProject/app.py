from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import text

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://ejc:1Bringitback@localhost/db_name'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)

@app.route('/')
def testdb():
    try:
        db.session.query(text('1')).from_statement(text('SELECT 1')).all()
        return '<h1>It works.</h1>'
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text

if __name__ == '__main__':
    app.run(debug=True)

# Pass the required route to the decorator.
@app.route("/coursesbygrade")
def coursesbygrade(grade):
    courses = db.query.filter_by(db.grade=grade).order_by(db.abbreviation).all()
    return courses

@app.route("/coursebyccn")
def coursebyccn(ccn):
    courses = db.query.filter_by(db.ccn=ccn).order_by(db.abbreviation).all()
    return courses

@app.route("/ppn")
def pnp(semester):
    courses = db.query.filter_by(db.grade=ppn).order_by(db.abbreviation).all()

@app.route("/grades")
def grades(course):
    grade = db.query.filter_by(db.name=course).order_by(db.abbreviation).all()
    return grade

@app.route("/coursesbysectionnumber")
def coursesbysectionnumber(sectionnumber):
    courses = db.query.filter_by(db.section_num=sectionnumber).order_by(db.abbreviation).all()

@app.route("/coursesbylevel")
def levels(level):
    courses = db.query.filter_by(db.level=level).order_by(db.abbreviation).all()
    return courses

@app.route("/semesteroffered")
def semesteroffered(course):
    semesters = db.query.filter_by(db.abbreviation=course).order_by(db.semester).all()
    return semesters

@app.route("/gradebysemester")
def gradebysemester(course, semester):
    grade = db.query.filter_by(db.abbreviation=course, db.semester=semester).all()
    return grade

@app.route("/gradebyyear")
def gradebyyear(course, year):
    grade = db.query.filter_by(db.abbreviation=course, db.semester=year).all()
    return grade

@app.route("/coursebyinstructor")
def coursebyinstructor(instructor):
    courses = db.query.filter_by(db.instructor=instructor).order_by(db.abbreviation).all()
    return courses

@app.route("/")
def index():
    return "Homepage of ESC-Mobile-App"