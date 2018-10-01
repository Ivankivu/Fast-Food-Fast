from flask import Flask, request, make_response, jsonify
from app.database.server import DBConnection
from app.validate import validate_user


class User(DBConnection):

    def __init__(self, username, user_email, user_password):
        DBConnection.__init__(self)
        data = request.get_json()
        self.username = data['user_name']
        self.user_email = data['user_email']
        self.user_password = data['user_password']
        self.cursor = self.conn.cursor()

    def adduser(self):
        sql = "INSERT INTO users(user_name, user_email, user_password)VALUES('{}', '{}', '{}')".format(
                    self.username,
                    self.user_email,
                    self.user_password)
        self.cursor.execute(sql)
        self.conn.commit()
        with DBConnection() as cursor:
            cursor.execute("SELECT * FROM users WHERE user_email = '{}'"
                           .format(self.user_email))

            if cursor.fetchone():
                return make_response(jsonify({
                    "message": "Email already in Exists"}), 409)
            else:
                cursor.execute("SELECT * FROM users WHERE user_email = '{}'"
                               .format(self.user_email))
                return make_response(jsonify({
                    "message": "Successfully registered"}), 201)
        qq = self.cursor.execute("select * from users")
        return make_response(jsonify({'message': 'account added successfully!'}), 201)

    # app.route('/auth/login', methods=['GET', 'POST'])
    # def login():
    #     """
    #     Handle requests to the /login route
    #     Log an user in through the login form
    #     """
    #     form = LoginForm()
    #     if form.validate_on_submit():

    #         # check whether user exists in the database and whether
    #         # the password entered matches the password in the database
    #         user = User.query.filter_by(email=form.user_email.data).first()
    #         if user is not None and user.verify_password(
    #                 form.user_password.data):
    #             # log user in
    #             login_user(user)

    #             # when login details match
    #             return ('welcome user!!')

    #         # when login details are do not match
    #         else:
    #             flash('Invalid email or password.')

    #     return ('please login')

    # app.route('/auth/logout')
    # @login_required
    # def logout():
    #     """
    #     Logout a user
    #     """
    #     logout_user()
    #     flash('You have successfully been logged out.')
