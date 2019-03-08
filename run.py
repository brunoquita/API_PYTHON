from app import app

# Importando rotas
from app.routes import *

# importando models

from app.models import vendedor
from app.models import cliente


if __name__ == '__main__':
    app.run(port=8080, debug=True)
