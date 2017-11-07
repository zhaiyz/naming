from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/naming'
db = SQLAlchemy(app)


class Naming(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    chinese_name = db.Column(db.String(30), index=True)
    english_name = db.Column(db.String(30), index=True)

    def __init__(self, chinese_name, english_name):
        self.chinese_name = chinese_name
        self.english_name = english_name

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<%s: %s>' % (self.chinese_name, self.english_name)


if __name__ == '__main__':
    db.create_all()
    print(Naming.query.all())
