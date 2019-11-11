import unittest
import app


class SyncTasks(unittest.TestCase):
    def test_endpoints__success(self):
        with app.test_client() as c:
            response = c.post('/calculate', json={'first_number': 3.5, 'second_number': 1.59})
            task_id = response.data.decode()

        with app.test_client() as c:
            response = c.get('/callback/{}'.format(task_id))
            self.assertEqual(float(response.data.decode()), 3.5 * 1.59)

    def test_endpoints__failure(self):
        with app.test_client() as c:
            response = c.post('/calculate', json={'first_number': "asd", 'second_number': 1.59})
            task_id = response.data.decode()

        with app.test_client() as c:
            response = c.get('/callback/{}'.format(task_id))
            with self.assertRaises(ValueError):
                # it will return error details, so converting to float will raise an error
                float(response.data.decode())


if __name__ == "__main__":
    unittest.main()
