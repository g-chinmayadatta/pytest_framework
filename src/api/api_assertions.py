class APIAssertion:

    @staticmethod
    def assert_equal(actual, expected, message=""):
        assert actual == expected, f"{message} | Expected: {expected}, Actual: {actual}"

    @staticmethod
    def assert_status_code(response, expected):
        assert response.status_code == expected, \
            f"Expected {expected}, got {response.status_code}"

    @staticmethod
    def assert_json_key(response, key):
        assert key in response.json(), f"{key} not found in response"

    @staticmethod
    def assert_json_value(response, key, expected):
        actual = response.json().get(key)
        assert actual == expected, f"Expected {key}={expected}, got {actual}"

    @staticmethod
    def assert_in(text, response_text):
        assert text in response_text, f"{text} not found in response"

    @staticmethod
    def assert_not_empty(data):
        assert data, "Response data is empty"