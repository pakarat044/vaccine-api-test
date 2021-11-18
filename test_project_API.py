"""Test project API of government group's name is Flamxby."""
import unittest
import requests


class TestApi(unittest.TestCase):
    """Class for test when Gets the specific reservations
    detail from reservation id."""

    def test_reservation_id_succeed(self):
        """This function test that the website can GET reservation id to
        succeed."""
        self.response = requests.get("https://flamxby.herokuapp.com/reservation/5")
        self.assertEqual(self.response.status_code, 200)
        self.assertEqual("application/json", self.response.headers["Content-Type"])

    def test_reservation_id_input_negative_number(self):
        """This function test that it should not found information when the input
        reservation id is a negative number."""
        self.response = requests.get("https://flamxby.herokuapp.com/reservation/-1")
        self.assertEqual(self.response.status_code, 404)
        self.assertEqual(
            self.response.json(), {"detail": "No reservation with this id"}
        )

    def test_reservation_id_input_not_exist(self):
        """This function test that it should not found information when the input
        reservation id is not exist."""
        self.response = requests.get("https://flamxby.herokuapp.com/reservation/500000")
        self.assertEqual(self.response.status_code, 404)
        self.assertEqual(
            self.response.json(), {"detail": "No reservation with this id"}
        )

    def test_reservation_id_are_get_correct_response_body(self):
        """This function test that the input reservation id and get
        information on that reservation id."""
        self.response = requests.get("https://flamxby.herokuapp.com/reservation/5")
        self.assertEqual(self.response.json()["reservation_id"], 5)

    def test_reservation_id_are_get_correct_response_headers(self):
        """This function test that the input reservation id and get
        correct response headers."""
        self.response = requests.get("https://flamxby.herokuapp.com/reservation/5")
        self.assertEqual("uvicorn", self.response.headers["server"])


if __name__ == "__main__":
    unittest.main()
