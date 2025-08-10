# Configuración de la base de datos, claves secretas, etc.
DATABASE_URL = "sqlite:///./users.db"
SECRET_KEY = "user-secret-key"
# Configuración de JWT
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
