
    # def add_tbl_users(self):
    #     self.table_name = 'users'
    #     with self.conn.cursor() as cursor:
    #         command = ("CREATE TABLE IF NOT EXISTS %s("
    #                    "user_id serial PRIMARY KEY,"
    #                    "record_timestamp timestamp default current_timestamp,"
    #                    "user_name text not null,"
    #                    "user_email text not null,"
    #                    "user_password  varchar(50) not null"
    #                    ");")
    #         cursor.execute(command % self.table_name)
    #         self.conn.commit()
    #         # print("Table_users created successfully")

    # def add_tbl_status(self):
    #     self.table_name = 'Status'
    #     with self.conn.cursor() as cursor:
    #         command = ("CREATE TABLE IF NOT EXISTS %s("
    #                    "status_id serial PRIMARY KEY,"
    #                    "record_timestamp timestamp default current_timestamp,"
    #                    "status_type text not null"
    #                    ");")
    #         cursor.execute(command % self.table_name)
    #         self.conn.commit()
    #         # print("Table_status created successfully")

    # def add_tbl_Orders(self):
    #     self.table_name = 'Orders'
    #     with self.conn.cursor() as cursor:
    #         command = ("CREATE TABLE IF NOT EXISTS %s("
    #                    "order_id serial PRIMARY KEY,"
    #                    "created_timestamp timestamp default current_timestamp,"
    #                    "order_type text not null,"
    #                    "user_id int REFERENCES USERS (user_id),"
    #                 #    "status_type  text not null REFERENCES status (status_type),"
    #                    "amount int not null"
    #                    ");")
    #         cursor.execute(command % self.table_name)
    #         self.conn.commit()
    #         # print("Table_orders created successfully")
    #         self.conn.close()



               # cursor.execute("SELECT * FROM users WHERE user_email = '{}'".format(user_email))

                    # if cursor.fetchone():
                    #     return jsonify({"message": "Email already in Exists"}), 409
                    # else:
                    #     cursor.execute("SELECT * FROM users WHERE user_email = '{}'".format(user_email))
                    #     return jsonify({"message": "Successfully registered"}), 201



                      # except Exception as e:
            #     logging.error(e)
            #     return jsonify({'message': str(e)}), 500


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

    # def login_user(self):
        #         try:
        #             with DBConnection() as cursor:
        #                 cursor.execute("SELECT * FROM users WHERE user_email = '{}'".format(user_email))

        #                 if cursor.fetchone():
        #                     return jsonify({"message": "Email already in Exists"}), 409
        #                 else:
        #                     cursor.execute("SELECT * FROM users WHERE user_email = '{}'".format(user_email))
        #                     return jsonify({"message": "Successfully registered"}), 201

        #                 sql = "INSERT INTO users(user_name, user_email, user_password)VALUES('{}', '{}', '{}')".format(
        #                         username,
        #                         user_email,
        #                         user_password)
                    
        #                 cursor = conn.cursor()
        #                 cursor.execute(sql)
        #                 conn.commit()
        #                 qq = cursor.execute("select * from users")
        #                 return jsonify({'message': 'account added successfully!'}), 201

        #         except Exception as e:
        #             logging.error(e)
        #             return jsonify({'message': str(e)}), 500


                # app.route('/auth/login', methods=['GET', 'POST'])

                #     def login():
                #         """
                #         Handle requests to the /login route
                #         Log an user in through the login form
                #         """
                #         form = LoginForm()
                #         if form.validate_on_submit():

                #             # check whether user exists in the database and whether
                #             # the password entered matches the password in the database
                #             user = User.query.filter_by(email=form.user_email.data).first()
                #             if user is not None and user.verify_password(
                #                     form.user_password.data):
                #                 # log user in
                #                 login_user(user)

                #                 # when login details match
                #                 return ('welcome user!!')

                #             # when login details are do not match
                #             else:
                #                 flash('Invalid email or password.')

                #         return ('please login')

                #     app.route('/auth/logout')
                #     @login_required
                #     def logout():
                #         """
                #         Logout a user
                #         """
                #         logout_user()
                #         flash('You have successfully been logged out.')




        # try:
        #     with DBConnection() as cursor:
        #         sql = "select row_to_json(row) from (SELECT * FROM orders user_name) row;"
        #         cursor.execute(sql)
        #         orderlist = cursor.fetchall()
        #         return make_response(jsonify(orderlist))

        #         # return make_response(jsonify({"message": "Successfully Added to menu"}), 201)

        # except Exception as e:
        #     logging.error(e)
        #     return make_response(jsonify({'message': str(e)}), 500)


         # if len(data['Food']) == 0:
        #     return jsonify({"error": "food should not be empty"}), 404

        # if data['Food'].isspace():
        #     return jsonify({"error": "food should not be empt spaces"}), 404
        # if not isinstance(data['amount'], int):
        #     return jsonify({"error": "amount should be integer"}), 404
    

    # def get_order_by_id(order_id):
    #     if orderlist == []:
    #         return jsonify({"error": "orders not found"}), 404

    #     orders = [order for order in orderlist
    #               if order['order_id'] == order_id]
    #     if not orders:
    #         return jsonify({"error": "no match found"}), 404

    #     return jsonify({'order': orders[0]}), 200

    # def change_order_status(order_id):

    #     data = request.get_json()
    #     order1 = {
    #         'Food': data['Food'],
    #         'amount': data['amount'],
    #         'status': data['status']
    #     }
    #     if orderlist == []:
    #         return jsonify({"Error": "No orders found"})
    #     ods = [order for order in orderlist
    #            if order['order_id'] == order_id]
    #     ods[0]['status'] = data['status']
    #     ods[0] = order1
    #     return jsonify({'orderlist': order1}), 200

    # def delete_order(order_id):

    #     od = [order for order in orderlist
    #           if order['order_id'] == order_id]
    #     if not od:
    #         return jsonify({'error': 'order does not exist'}), 404

    #     orderlist.remove(od[0])
    #     return jsonify({'orderlist': orderlist}), 200





    # @app.route("/api/v1/orders/<int:order_id>", methods=["PUT"])
    # def edit_order(order_id):

    #     response = Order.change_order_status(order_id)
    #     return response

    # @app.route("/api/v1/orders/<int:order_id>", methods=["DELETE"])
    # def remove_order(order_id):

    #     response = Order.delete_order(order_id)
    #     return response

    # @app.errorhandler(404)
    # def not_found(e):
    #     return '', 404





#     @app.route("/api/v1/orders/<int:order_id>", methods=["GET"])
#     def get_order(order_id):

#         response = Order.get_order_by_id(order_id)
#         return response