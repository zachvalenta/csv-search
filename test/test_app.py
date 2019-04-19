from src.app import create_query_container


def test_create_containers():
    assert isinstance(create_query_container(), list)
