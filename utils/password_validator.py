
class PasswordValidator:
    min_length = 6
    length_error = f'Password must be at least {min_length} characters'

    def __init__(self):
        self.checks = [
            self._min_length_requirement
        ]

    def _min_length_requirement(self, password):
        if len(password) >= self.min_length:
            return None

        return self.length_error

    def validation_errors(self, password):
        return [error for error in self.checks if error is not None]

