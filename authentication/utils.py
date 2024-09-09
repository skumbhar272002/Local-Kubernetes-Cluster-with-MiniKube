from django.contrib.auth.tokens import PasswordResetTokenGenerator
from six import text_type


class AppTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, User, timestamp):
        return (text_type(User.is_active)+text_type(User.pk)+text_type(timestamp))

token_generator = AppTokenGenerator()
