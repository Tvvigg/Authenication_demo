from app import app
from models import *


db.drop_all()
db.create_all()

db.session.commit()