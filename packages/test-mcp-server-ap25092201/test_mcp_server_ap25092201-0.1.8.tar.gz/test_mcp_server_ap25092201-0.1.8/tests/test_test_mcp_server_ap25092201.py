"""Basic tests for test-mcp-server-ap25092201."""


def test_import() -> None:
    """Test that the package can be imported."""
    import test_mcp_server_ap25092201

    assert hasattr(test_mcp_server_ap25092201, "__version__")


def test_version() -> None:
    """Test that version is defined."""
    from test_mcp_server_ap25092201 import __version__

    assert __version__ is not None
    assert isinstance(__version__, str)
