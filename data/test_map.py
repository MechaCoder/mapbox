from unittest import TestCase

from faker import Faker

from .map import Map

class TestMap(TestCase):

    def test_create(self):
        
        obj = Map()

        doc_id = obj.create(
            title=Faker().name(),
            background=Faker().url(),
            screensaver=Faker().url()
        )

        self.assertIsInstance(
            doc_id,
            int
        )