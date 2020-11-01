import os


class Config:

    env = 'prod'

    if env == 'dev':
        SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
        SECRET_KEY = os.environ.get('SECRET_KEY')
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        MAIL_SERVER = 'smtp.gmail.com'
        MAIL_PORT = 465
        MAIL_USE_SSL = True
        MAIL_USERNAME = os.environ.get('EMAIL_USER')
        MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
    else:
        SQLALCHEMY_DATABASE_URI = 'postgres://unqmjvhjpmzquq:9531e778bb5abc2fa677335ae1445b6de1ace8fd0c2be1bbd0e7fc26d202a24e@ec2-3-208-224-152.compute-1.amazonaws.com:5432/d6854u8oh6u03g'
        SECRET_KEY = 'a1e824f498ef42682a1e81bce53cbd2db3'
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        MAIL_SERVER = 'smtp.gmail.com'
        MAIL_PORT = 465
        MAIL_USE_SSL = True
        MAIL_USERNAME = 'dasavishek1995@gmail.com'
        MAIL_PASSWORD = 'Bubai@1995'
