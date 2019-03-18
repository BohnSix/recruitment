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


class User(db.model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_id = db.Column(db.String(32), unique=True, index=True)
    logo = db.Column(db.String(255), unique=True)

    name = db.Column(db.String(32), index=True)
    pswd = db.Column(db.String(32))
    email = db.Column(db.String(100), unique=True, index=True)
    phone = db.Column(db.String(11), unique=True, index=True)

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
    user_id = db.Column(db.String(32), db.ForeignKey('user.id'))
    sex = db.Column(db.String(10), )
