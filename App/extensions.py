from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_talisman import Talisman

db = SQLAlchemy()
migrate = Migrate()
db = SQLAlchemy()
csrf = CSRFProtect()
limiter = Limiter(get_remote_address, default_limits=["200 per day", "50 per hour"])
bcrypt = Bcrypt()
login_manager = LoginManager()


