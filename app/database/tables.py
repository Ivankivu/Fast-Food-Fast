class CreateTables():

    def add_tbl_users(self):
        self.table_name = 'users'
        with self.conn.cursor() as cursor:
            command = ("CREATE TABLE IF NOT EXISTS %s("
                       "user_id serial PRIMARY KEY,"
                       "record_timestamp timestamp default current_timestamp,"
                       "user_name text not null,"
                       "user_email text not null,"
                       "user_password  varchar(50) not null"
                       ");")

            cursor.execute(command % self.table_name)
            self.conn.commit()
            print("Table_users created successfully")

    def add_tbl_menu(self):
        self.table_name = 'menu'
        with self.conn.cursor() as cursor:
            command = ("CREATE TABLE IF NOT EXISTS %s("
                       "menu_id serial PRIMARY KEY,"
                       "record_timestamp timestamp default current_timestamp,"
                       "status_type text not null"
                       "food_amount int not null"
                       ");")
            cursor.execute(command % self.table_name)
            self.conn.commit()
            print("Table_status created successfully")

    def add_tbl_status(self):
        self.table_name = 'Status'
        with self.conn.cursor() as cursor:
            command = ("CREATE TABLE IF NOT EXISTS %s("
                       "status_id serial PRIMARY KEY,"
                       "record_timestamp timestamp default current_timestamp,"
                       "status_type text not null"
                       ");")
            cursor.execute(command % self.table_name)
            self.conn.commit()
            print("Table_status created successfully")

    def add_tbl_Orders(self):
        self.table_name = 'Orders'
        with self.conn.cursor() as cursor:
            command = ("CREATE TABLE IF NOT EXISTS %s("
                       "order_id serial PRIMARY KEY,"
                       "created_timestamp timestamp default current_timestamp,"
                       "order_type text not null,"
                       "user_id int REFERENCES USERS (user_id),"
                       "status_type  text not null REFERENCES status (status_type),"
                       "amount int not null"
                       ");")
            cursor.execute(command % self.table_name)
            self.conn.commit()
            print("Table_status created successfully")