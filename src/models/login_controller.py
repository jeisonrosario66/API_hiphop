from src.database.db_connect import create_db_connection
from src.database.db_connect import close_db_connection
from src.errors_handling.msg_exception import msg_exception
from passlib.hash import pbkdf2_sha256


class LoginController:
    def __init__(self):
        pass

    def login_verify(self, user_input, passw_input):
        """This will verify if exist username and password

        Args:
            user_input (str): The username input from fronted (client)
            passw_input (str): The password input from fronted (client)

        Returns:
            bool: If the username exist then "retun=1" otherwise "retunr=0
        """
        user_input = user_input.lower()
        try:
            db_connection = create_db_connection()
            if db_connection:
                with db_connection.cursor() as cursor:
                    sql = "SELECT * FROM user_admin WHERE user_admin = (%s)"
                    cursor.execute(sql, (user_input,))
                    
                    data_got = cursor.fetchone()

                    if not data_got == None:
                        user = data_got[1]
                        passw = data_got[2]
                        # print("data_got: ",data_got[2]," - Type: ", type(data_got[2]))
                        if user_input == user and pbkdf2_sha256.verify(passw_input, passw):
                            return 1
                        else:
                            return 0
                    else:
                        return 0

        except Exception as ex:
            return msg_exception(self.login_verify, ex)
        finally:
            close_db_connection(db_connection)
            
        