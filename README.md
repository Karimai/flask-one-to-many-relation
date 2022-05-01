$ python
from app import db
db.create_all()
exit()

max = Pet(name="max", age=10, owner_id=1)
nil = Pet(name="Nil", age=5, owner_id=1)
zus = Pet(name="Zus", age=3, owner_id=2)

db.session.add_all([max, nil, zus])
db.session.commit()

db.relationship and backref.
  mel = Pet(name="Mel", age=3, owner=b)
  db.session.add(mel)
  db.session.commit()
  mel.owner
  <Owner 2>
  mel.owner.name
  Karim
  mel.owner.address
  Nijkerk 36 PS