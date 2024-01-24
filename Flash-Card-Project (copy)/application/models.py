from application.database import db
import datetime

from flask import current_app as app

engine = db.create_engine(
	app.config.get('SQLALCHEMY_DATABASE_URI'),
	app.config.get('SQLALCHEMY_ENGINE_OPTIONS')
)

class Users(db.Model):
	__tablename__ = 'users'
	user_id = db.Column(db.String, primary_key = True, unique = True, nullable = False)
	user_pwd = db.Column(db.String, nullable = False)

class Trackers(db.Model):
	__tablename__ = 'trackers'
	tracker_no = db.Column(db.Integer, primary_key=True,autoincrement=True)
	tracker_name = db.Column(db.String,  unique = True)

def newTrackerMaker(trackerName):
	class Track(db.Model):
		__tablename__ = trackerName
		card_no = db.Column(db.Integer,primary_key=True,autoincrement=True,nullable=False)
		card_word = db.Column(db.String, unique=True, nullable=False)
		card_ans = db.Column(db.String, nullable=False)
	db.create_all()
	return Track


class TrackerList:
	trackers = {tracker.tracker_name : newTrackerMaker(tracker.tracker_name) for tracker in Trackers.query.all()}

	def get(tracker_name):
		return TrackerList.trackers[tracker_name]

	def post(tracker_name):
		TrackerList.trackers[tracker_name] = newTrackerMaker(tracker_name)

	def delete(tracker_name):
		db.metadata.remove(TrackerList.trackers[tracker_name].__table__)
		TrackerList.trackers[tracker_name].__table__.drop(engine)
		del TrackerList.trackers[tracker_name]


db.create_all()

if __name__ == "__main__":
	new_tracker = Tracker(tracker_name = "Synonyms", creation_date = datetime.date.today())
	db.session.add(new_tracker)
	db.session.commit()
	# pass