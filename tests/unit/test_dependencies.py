from easymoney.verify_dependencies import verify_dependencies


def test_should_execute_a_select_to_check_the_db_connection():
    assert verify_dependencies() is None
