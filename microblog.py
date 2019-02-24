from app import app, db
from app.models import User, Post

# Adds db, User, and Post to flask shell
@app.shell_context_processor
def make_shell_context():
  return {'db': db, 'User': User, 'Post': Post}
