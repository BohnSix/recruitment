from recruitment.app.init import db


class Admin(db.model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, autoincrement=True)
    name = db.Column(db.String(32), unique=True)
    pswd = db.Column(db.String(32))

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pswd(self, pswd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pswd, pswd)


class Freshman(db.model):
    __tablename__ = "freshman"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_id = db.Column(db.String(32), unique=True, index=True)
    logo = db.Column(db.String(255), unique=True)

    name = db.Column(db.String(32), index=True)
    pswd = db.Column(db.String(32))
    email = db.Column(db.String(100), unique=True, index=True)
    phone = db.Column(db.String(11), unique=True, index=True)
    info = db.Column(db.Text)

    def __repr__(self):
        return "<Freshman %r>" % self.name
