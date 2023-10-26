from datetime import datetime, timedelta
import os
import model, server

os.system('dropdb melon-tasting')
os.system('createdb melon-tasting')

model.connect_to_db(server.app)
model.db.create_all()

new_user1 = model.User.create("inna@inna.com", "inna")
new_user2 = model.User.create("alex@alex.com", "alex")
new_user3 = model.User.create("kate@kate.com", "kate")

model.db.session.add_all([new_user1, new_user2, new_user3])
model.db.session.commit()