#BD LOCAL
# class Config(object):
#     SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Qualitas@localhost:5432/bdcarsales"
#     SQLALCHEMY_TRACK_MODIFICATIONS = True

#BD EN LA NUBE
class Config(object):
    SQLALCHEMY_DATABASE_URI = "postgresql://bdcarsales_jsgu_user:FRlmmzUARdU02Jr2eYpc4U2z52Wx90TW@dpg-cka5e3ns0fgc73ah792g-a.oregon-postgres.render.com:5432/bdcarsales_jsgu"
    SQLALCHEMY_TRACK_MODIFICATIONS = True