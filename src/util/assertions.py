from src.util.logger import logger

class Assertion:
    @staticmethod
    def assert_equal(actual, expected, message):
        logger.info(message)
        logger.info(f"Validating equality: {actual} == {expected}")
        assert actual == expected, f"{message} | Expected: {expected}, Actual: {actual}"

    @staticmethod
    def assert_true(condition, message):
        logger.info(message)
        logger.info("Validating condition is True")
        assert condition, message

    @staticmethod
    def assert_in(item, container, message):
        logger.info(message)
        logger.info(f"Validating {item} in {container}")
        assert item in container, message

    @staticmethod
    def assert_length(data, expected_length, message):
        logger.info(message)
        logger.info(f"Validating length == {expected_length}")
        assert len(data) == expected_length, message
