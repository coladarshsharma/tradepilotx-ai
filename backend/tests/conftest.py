import os

os.environ.setdefault("SECRET_KEY", "test-secret-key-that-is-long-enough-for-validation")
os.environ.setdefault("DATABASE_URL", "sqlite+pysqlite:///:memory:")
