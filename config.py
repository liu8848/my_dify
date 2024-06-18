import os
import dotenv

dotenv.load_dotenv()

DEFAULTS = {
    'DB_USERNAME': 'postgres',
    'DB_PASSWORD': 'sudalu929',
    'DB_HOST': 'localhost',
    'DB_PORT': '5432',
    'DB_DATABASE': 'flask_test',
    'SQLALCHEMY_DATABASE_URI_SCHEME': 'postgresql',
    'SQLALCHEMY_POOL_SIZE': 30,
    'SQLALCHEMY_MAX_OVERFLOW': 10,
    'SQLALCHEMY_POOL_RECYCLE': 3600,
    'SQLALCHEMY_POOL_PRE_PING': 'False',
    'SQLALCHEMY_ECHO': 'False',
}


# 根据key获取环境变量
def get_env(key):
    return os.environ.get(key, DEFAULTS.get(key))


def get_bool_env(key):
    value = get_env(key)
    return value.lower() == 'true' if value is not None else False


class Config:
    def __init__(self):
        # ----------------------
        # 数据库配置
        # ----------------------
        db_credentials = {
            key: get_env(key) for key in
            ['DB_USERNAME', 'DB_PASSWORD', 'DB_HOST', 'DB_PORT', 'DB_DATABASE', 'DB_CHARSET']
        }
        self.SQLALCHEMY_DATABASE_URI_SCHEME = get_env('SQLALCHEMY_DATABASE_URI_SCHEME')
        db_extras = f"?client_encoding={db_credentials['DB_CHARSET']}" if db_credentials['DB_CHARSET'] else ""

        self.SQLALCHEMY_DATABASE_URI \
            = f"{self.SQLALCHEMY_DATABASE_URI_SCHEME}://{db_credentials['DB_USERNAME']}:{db_credentials['DB_PASSWORD']}@{db_credentials['DB_HOST']}:{db_credentials['DB_PORT']}/{db_credentials['DB_DATABASE']}{db_extras}"

        self.SQLALCHEMY_ENGINE_OPTIONS = {
            'pool_size': int(get_env('SQLALCHEMY_POOL_SIZE')),
            'max_overflow': int(get_env('SQLALCHEMY_MAX_OVERFLOW')),
            'pool_recycle': int(get_env('SQLALCHEMY_POOL_RECYCLE')),
            'pool_pre_ping': get_bool_env('SQLALCHEMY_POOL_PRE_PING'),
            'connect_args': {'options': '-c timezone=utc'}
        }

        self.SQLALCHEMY_ECHO = get_bool_env('SQLALCHEMY_ECHO')
