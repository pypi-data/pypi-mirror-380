from collections import UserDict

from dyngle.error import DyngleError


class LiveData(UserDict):

    def resolve(self, key: str):
        """Given a key (which might be dot-separated), return
        the value (which might include evaluating expressions)."""

        parts = key.split('.')
        current = self.data
        for part in parts:
            if part not in current:
                raise DyngleError(
                    f"Invalid expression or data reference '{key}'")
            current = current[part]
        if callable(current):
            return current(self)
        else:
            return current
