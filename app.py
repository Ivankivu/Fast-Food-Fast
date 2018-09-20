from flask import Flask
from v1.views.orders import app

app.run(debug=True)
