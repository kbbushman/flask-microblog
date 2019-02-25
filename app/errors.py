from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
  return render_template('404.html'), 404


@app.errorhandler(500)
def internal_error(error):
  # Undo any changes to database if error accurs
  # session.rollback() is the opposite of session.commit()
  db.session.rollback()
  return render_template('500.html'), 500
