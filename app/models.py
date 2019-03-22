from recruitment.app.exts import db


class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    pswd = db.Column(db.String(32))

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pswd(self, pswd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pswd, pswd)


class Super(Admin):
    __tablename__ = "super"

    def __repr__(self):
        return "<Super %r>" % self.name

    def check_pswd(self, pswd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pswd, pswd)


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_id = db.Column(db.String(32), unique=True, index=True)
    name = db.Column(db.String(32), index=True)
    pswd = db.Column(db.String(32))

    create_time = db.Column(db.DateTime)
    update_time = db.Column(db.DateTime)

    userinfo = db.relationship("UserInfo", backref="user")

    def __repr__(self):
        return "<User %r>" % self.name

    def check_pswd(self, pswd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pswd, pswd)


class UserInfo(db.Model):
    __tablename__ = "userinfo"
    user_id = db.Column(db.String(32), db.ForeignKey('user.id'), primary_key=True)
    sex = db.Column(db.String(10), )
    logo = db.Column(db.String(255), unique=True)

    department = db.Column(db.String(11), index=True)
    department2 = db.Column(db.String(11), index=True)
    intro = db.Column(db.Text)
    school = db.Column(db.String(11), index=True)
    classnum = db.Column(db.String(11), index=True)

    email = db.Column(db.String(100), unique=True, index=True)
    phone = db.Column(db.String(11), unique=True, index=True)

    first_impression = db.Column(db.Text)
    second_impression = db.Column(db.Text)
