import uuid


class UUIDGenerate:
    """generates a UUID"""

    @classmethod
    def generate(cls):
        """generates a UUID"""
        return str(uuid.uuid4())
