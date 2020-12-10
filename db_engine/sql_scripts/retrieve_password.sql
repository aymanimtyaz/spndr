SELECT hashed_password FROM users 
WHERE email = (%(email)s);