from datetime import datetime, timedelta
import random
import string
import model

new_user1 = model.User.create("inna@inna.com", "inna")
new_user2 = model.User.create("alex@alex.com", "alex")
new_user3 = model.User.create("kate@kate.com", "kate")

model.db.session.add([new_user1, new_user2, new_user3])
model.db.session.commit()