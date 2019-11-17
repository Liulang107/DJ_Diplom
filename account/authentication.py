from django.contrib.auth import get_user_model


class EmailAuthBackend(object):
    def __init__(self):
        self.UserModel = get_user_model()

    def authenticate(self, username=None, password=None):
        try:
            user = self.UserModel.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except self.UserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.UserModel.objects.get(pk=user_id)
        except self.UserModel.DoesNotExist:
            return None
