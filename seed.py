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


today_at_3pm = datetime.now().replace(hour=15, minute=0, second=0, microsecond=0)

tomorrow_at_3pm = today_at_3pm + timedelta(days=1)
next_tomorrow_at_3pm = today_at_3pm + timedelta(days=2)
next = today_at_3pm + timedelta(days=3)

res = model.Reservation.create(tomorrow_at_3pm, new_user1)
res2 = model.Reservation.create(next_tomorrow_at_3pm, new_user2)
res3 = model.Reservation.create(next, new_user3)

model.db.session.add_all([new_user1, new_user2, new_user3, res, res2, res3])
model.db.session.commit()