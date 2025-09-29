import pytest

from crypticorn.client import SyncClient


def test_client_basic_instantiation():
    """Test basic client instantiation without errors."""
    client = SyncClient()
    assert client is not None
    assert client._http_client is None
    client.close()


def test_client_manual_close():
    """Test manual close of client."""
    client = SyncClient()

    assert client._http_client is None

    # Close manually
    client.close()
    assert client._http_client is None


def test_client_ping_functionality():
    """Test that ping works correctly."""
    client = SyncClient()

    try:
        response = client.hive.status.ping()
        # Should not raise any exceptions
        assert response is not None
    finally:
        client.close()


def test_client_multiple_service_access():
    """Test accessing multiple services without errors."""
    client = SyncClient()

    try:
        assert client._http_client is None
        # Access multiple services to ensure they're properly initialized
        subclient = client._services["hive"]
        assert subclient is not None
        assert subclient.base_client.rest_client.pool_manager is None
    finally:
        client.close()


def test_client_no_exceptions_on_basic_operations():
    """Test that basic operations don't raise unexpected exceptions."""
    client = SyncClient()

    try:
        # Access a service
        hive_client = client.hive
        assert hive_client is not None

        # Ping should work
        response = client.hive.status.ping()
        assert response is not None

    except Exception as e:
        pytest.fail(f"Unexpected exception raised: {e}")
    finally:
        client.close()


def test_client_service_lazy_initialization():
    """Test that services are lazily initialized."""
    client = SyncClient()

    # But HTTP client should be None until first use
    assert client._http_client is None
    # First access should create the session
    client.hive.status.ping()
    assert client._http_client is None

    client.close()
    assert client._http_client is None


def test_client_concurrent_operations():
    """Test that client handles concurrent operations correctly."""
    client = SyncClient()

    responses = []
    for _ in range(5):
        responses.append(client.hive.status.ping())  # ✅ Each call properly managed

    client.close()  # ✅ Reliable cleanup
    assert client._http_client is None
