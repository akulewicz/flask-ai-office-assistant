from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sda32r4d3450ewfk-A4rejmcsd'

from aiassistant import routes