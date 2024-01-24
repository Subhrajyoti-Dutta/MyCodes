from flask import Flask, request
from flask import render_template
from flask import current_app as app
from application.models import *

db.create_all()
tracker_dict = dict()

for i in Trackers.query.all():
	tracker_dict[i.tracker_name] = newTrackerMaker(i.tracker_name)
	tracker_name = tracker_dict[i.tracker_name]
	db.create_all()
print(tracker_dict)
userCred = dict()

@app.route("/", methods=["GET"])
def index():
	return render_template('login.html')

@app.route("/login", methods=["POST"])
def userLogin():
	userID = request.form["user"]
	pwd = request.form["password"]

	user = Users.query.filter_by(login_id = userID).first()
	if (pwd == user.login_pwd):
		userCred['userID'] = userID
		return redirect(f'/tracker/{userID}')
	else:
		return redirect("/")


@app.route("/register", methods=["POST"])
def userRegister():
	userID = request.form["user"]
	user = Users.query.filter_by(login_id = userID).first()

	if user is None:
		pwd = request.form["pwd"]
		cpwd = request.form["cpwd"]
		if pwd == cpwd:
			newuser = Users(login_id = userID, login_pwd = pwd)
			db.session.add(newuser)
			db.session.commit()
			userCred['userID'] = userID
			return redirect(f'/tracker/{userID}')
		else:
			redirect("/")
	else:
		redirect("/")


@app.route("/tracker/<user_id>", methods=["GET"])
def trackerManager(user_id):
	trackers = Trackers.query.all()
	tracker_info = {i.tracker_no: i.tracker_name.capitalize() for i in trackers}
	user_records = Record.query.filter_by(login_id = user_id)
	user_record_info = {int(i.tracker_no): "Last Reviewed: "+i.last_review.strftime("%Y-%m-%d") for i in user_records}
	return render_template('tracker.html',user=user_id.capitalize(), num = len(tracker_info), tracker_info = tracker_info, user_record_info = user_record_info, userName = user_id)



if __name__ == "__main__":
	app.run(
    debug=True,
    host='0.0.0.0',
    port='8000'
    )