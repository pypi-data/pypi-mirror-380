from bits_aviso_python_sdk.helpers import initialize_logger
from bits_aviso_python_sdk.services.google.secretmanager import SecretManager


def test():
    """Tests the Pubsub class."""
    logger = initialize_logger()
    s = SecretManager()
    print(s.add_secret_version("", "", ""))


if __name__ == '__main__':
    test()
