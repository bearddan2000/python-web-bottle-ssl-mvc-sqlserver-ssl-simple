import bottle
from bottle import (
    route,
    response,
    run,
    redirect,
    request,
    static_file,
    ServerAdapter,
    default_app,
)
from beaker.middleware import SessionMiddleware
from bottle.ext.sqlalchemy import SQLAlchemyPlugin

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import settings
from model import Base, DogModel

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = engine = create_engine(
    '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.SQLSERVER
    ),
    echo=settings.SQLALCHEMY['debug']
)
session_local = sessionmaker(
    bind=engine,
    autoflush=settings.SQLALCHEMY['autoflush'],
    autocommit=settings.SQLALCHEMY['autocommit']
)

@route('/')
def index():
	return static_file('index.html', root='./templates')

@route('/dogs')
def get_all_dog(db):
    dogs = db.query(DogModel)
    results = [
        {
            "id": dog.id,
            "breed": dog.breed,
            "color": dog.color
        } for dog in dogs]

    return {"results": results}

bottle.install(SQLAlchemyPlugin(engine, Base.metadata, create=False, create_session = session_local))
class SSLCherootAdapter(ServerAdapter):
    def run(self, handler):
        from cheroot import wsgi
        from cheroot.ssl.builtin import BuiltinSSLAdapter
        import ssl

        server = wsgi.Server((self.host, self.port), handler)
        server.ssl_adapter = BuiltinSSLAdapter("./server.crt", "./server.key")

        try:
            server.start()
        finally:
            server.stop()


# define beaker options
# -Each session data is stored inside a file located inside a
#  folder called data that is relative to the working directory
# -The cookie expires at the end of the browser session
# -The session will save itself when accessed during a request
#  so save() method doesn't need to be called
session_opts = {
    "session.type": "file",
    "session.cookie_expires": True,
    "session.data_dir": "./data",
    "session.auto": True,
}

# Create the default bottle app and then wrap it around
# a beaker middleware and send it back to bottle to run
app = SessionMiddleware(default_app(), session_opts)

if __name__ == "__main__":
    run(app=app, host="0.0.0.0", port=443, server=SSLCherootAdapter)


