from flask import Flask
from v1.views.orders import restuarant


restuarant.run(debug=True)
