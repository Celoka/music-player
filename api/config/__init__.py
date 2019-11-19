import os


def get_env(key):
    try:
        return os.environ[key]
    except Exception as e:
        print(f'{type(e).__name__}: {e}')
