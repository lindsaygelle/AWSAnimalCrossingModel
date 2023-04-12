import random
import unittest
from datetime import datetime

from model import villager


class TestVillager(unittest.TestCase):
    def test_basic(self):
        villager_id: villager.Id = 1
        created_at = datetime.now()
        gender_choices = ["Female", "Male", "Other"]
        gender = random.choice(gender_choices)
        gender_alternative = random.choice(gender_choices)
        updated_at = datetime.now()

        villager_basic = villager.Basic(
            id=villager_id,
            created_at=created_at,
            gender=gender,
            gender_alternative=gender_alternative,
            updated_at=updated_at,
        )

        assert villager_basic["id"] == villager_id
        assert villager_basic["created_at"] == created_at
        assert villager_basic["gender"] == gender
        assert villager_basic["gender_alternative"] == gender_alternative
        assert villager_basic["updated_at"] == updated_at
