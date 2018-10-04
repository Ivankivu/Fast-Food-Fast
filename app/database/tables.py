class MyTables():

    def create_tables(self):
            """method for creating all tables"""
            commands = (
                """CREATE TABLE IF NOT EXISTS users(
                    user_id SERIAL PRIMARY KEY,
                    user_name varchar NOT NULL,
                    user_password varchar NOT NULL,
                    admin BOOLEAN DEFAULT FALSE
                )""",

                """CREATE TABLE IF NOT EXISTS status(
                    status_id SERIAL PRIMARY KEY,
                    status_type varchar NOT NULL,
                    CREATED_TIMESTAMP TEXT NOT NULL DEFAULT TO_CHAR(CURRENT_TIMESTAMP,
                                                        'YYYY-MM-DD HH:MI:pm')""",

                """CREATE TABLE IF NOT EXISTS menu(
                    menu_id SERIAL PRIMARY KEY,
                    food_type varchar NOT NULL,
                    food_price INTEGER NOT NULL,
                    FOREIGN KEY (user_name) REFERENCES users(user_name) ON DELETE CASCADE ON UPDATE CASCADE)""",

                """CREATE TABLE IF NOT EXISTS orders(
                    order_id SERIAL PRIMARY KEY,
                    user_name TEXT NOT NULL,
                    food_type TEXT NOT NULL,
                    qty INTEGER NOT NULL,
                    status varchar NOT NULL,
                    CREATED_TIMESTAMP TEXT NOT NULL DEFAULT TO_CHAR(CURRENT_TIMESTAMP,
                                                        'YYYY-MM-DD HH:MI:pm'), 
                    FOREIGN KEY (user_name) REFERENCES users(user_name) ON DELETE CASCADE ON UPDATE CASCADE,
                    FOREIGN KEY (food_type) REFERENCES menu(food_type) ON DELETE CASCADE ON UPDATE CASCADE)"""
            )

            for command in commands:
                print('tables created succesfully')
                self.cursor.execute(command)