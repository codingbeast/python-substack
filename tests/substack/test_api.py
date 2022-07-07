import os
import unittest

from dotenv import load_dotenv

from substack import Api
from substack.exceptions import SubstackAPIException

load_dotenv()


class ApiTest(unittest.TestCase):
    def test_api_exception(self):
        with self.assertRaises(SubstackAPIException):
            Api(email="", password="")

    def test_login(self):
        api = Api(
            email=os.getenv("EMAIL"),
            password=os.getenv("PASSWORD"),
            publication_url=os.getenv("PUBLICATION_URL"),
        )
        self.assertIsNotNone(api)

    def test_get_posts(self):
        api = Api(email=os.getenv("EMAIL"), password=os.getenv("PASSWORD"))
        posts = api.get_posts()
        self.assertIsNotNone(posts)

    def test_get_drafts(self):
        api = Api(
            email=os.getenv("EMAIL"),
            password=os.getenv("PASSWORD"),
            publication_url=os.getenv("PUBLICATION_URL"),
        )
        drafts = api.get_drafts()
        self.assertIsNotNone(drafts)

    def test_post_draft(self):
        api = Api(
            email=os.getenv("EMAIL"),
            password=os.getenv("PASSWORD"),
            publication_url=os.getenv("PUBLICATION_URL"),
        )
        posted_draft = api.post_draft([{"id": os.getenv("USER_ID"), "is_guest": False}])
        self.assertIsNotNone(posted_draft)

    def test_publication_users(self):
        api = Api(
            email=os.getenv("EMAIL"),
            password=os.getenv("PASSWORD"),
            publication_url=os.getenv("PUBLICATION_URL"),
        )
        users = api.get_publication_users()
        self.assertIsNotNone(users)

    def test_put_draft(self):
        api = Api(
            email=os.getenv("EMAIL"),
            password=os.getenv("PASSWORD"),
            publication_url=os.getenv("PUBLICATION_URL"),
        )
        posted_draft = api.put_draft("")
        self.assertIsNotNone(posted_draft)