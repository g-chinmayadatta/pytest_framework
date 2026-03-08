from src.util.logger import logger


class SoftAssertion:

    def __init__(self):
        self.errors = []

    def assert_equal(self, actual, expected, message="Values are not equal"):
        if actual != expected:
            error = f"{message} | Expected: {expected}, Actual: {actual}"
            logger.error(error)
            self.errors.append(error)
        else:
            logger.info(f"Assertion Passed: {actual} == {expected}")


    def assert_not_equal(self, actual, expected, message="Values should not be equal"):
        if actual == expected:
            error = f"{message} | Both values: {actual}"
            logger.error(error)
            self.errors.append(error)
        else:
            logger.info(f"Assertion Passed: {actual} != {expected}")

    def assert_true(self, condition, message="Condition is False"):
        if not condition:
            logger.error(message)
            self.errors.append(message)
        else:
            logger.info("Assertion Passed: Condition is True")

    def assert_false(self, condition, message="Condition is True"):
        if condition:
            logger.error(message)
            self.errors.append(message)
        else:
            logger.info("Assertion Passed: Condition is False")

    def assert_in(self, item, container, message="Item not found in container"):
        if item not in container:
            error = f"{message} | Item: {item}"
            logger.error(error)
            self.errors.append(error)
        else:
            logger.info(f"Assertion Passed: {item} found")

    def assert_not_in(self, item, container, message="Item unexpectedly found in container"):
        if item in container:
            error = f"{message} | Item: {item}"
            logger.error(error)
            self.errors.append(error)
        else:
            logger.info(f"Assertion Passed: {item} not present")

    def assert_is_none(self, value, message="Value is not None"):
        if value is not None:
            error = f"{message} | Value: {value}"
            logger.error(error)
            self.errors.append(error)
        else:
            logger.info("Assertion Passed: Value is None")

    def assert_is_not_none(self, value, message="Value is None"):
        if value is None:
            logger.error(message)
            self.errors.append(message)
        else:
            logger.info("Assertion Passed: Value is not None")

    def assert_greater(self, a, b, message="First value is not greater"):
        if not a > b:
            error = f"{message} | {a} <= {b}"
            logger.error(error)
            self.errors.append(error)
        else:
            logger.info(f"Assertion Passed: {a} > {b}")

    def assert_less(self, a, b, message="First value is not less"):
        if not a < b:
            error = f"{message} | {a} >= {b}"
            logger.error(error)
            self.errors.append(error)
        else:
            logger.info(f"Assertion Passed: {a} < {b}")

    def assert_length(self, data, expected_length, message="Length mismatch"):
        actual_length = len(data)
        if actual_length != expected_length:
            error = f"{message} | Expected: {expected_length}, Actual: {actual_length}"
            logger.error(error)
            self.errors.append(error)
        else:
            logger.info(f"Assertion Passed: Length == {expected_length}")

    def assert_all(self):
        if self.errors:
            error_message = "\n".join(self.errors)
            raise AssertionError(f"\nSoft Assertion Failures:\n{error_message}")