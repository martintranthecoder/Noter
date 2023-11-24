class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64),index=True,unique=True)
    email = db.Column(db.String(128),index=True,unique=True)
    password = db.Column(db.String(128))

    def __repr__(self): #not really necessary; can delete later
        return '<User {}>'.format(self.username)
    
    notes - db.relationship('Notes', backref='author', lazy='dynamic')

class Notes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(500))  #will change to whatever length needed
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) #in case you want to sort by recently updated
    user_id = db.Column(db.Integer, db.ForeignKey(user.id))
    
    def __repr__(self): #not really necessary; can delete later
        return '<Notes {}>'.format(self.body)