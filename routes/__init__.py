

def register_blueprints(app):
    from routes import index
    app.register_blueprint(index.bp)
    app.add_url_rule('/', endpoint='index')

    from routes import auth
    app.register_blueprint(auth.bp)
