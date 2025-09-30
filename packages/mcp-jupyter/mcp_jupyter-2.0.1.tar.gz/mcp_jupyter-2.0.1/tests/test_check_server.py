"""Test that check_server query type doesn't try to access notebooks."""

import pytest

from mcp_jupyter.rest_client import NotebookClient
from mcp_jupyter.server import query_notebook


def test_check_server_without_notebook(jupyter_server):
    """Test that check_server works without a notebook path."""
    # check_server should work even with a non-existent notebook path
    # because it doesn't actually access the notebook
    result = query_notebook(
        "non_existent_notebook",  # This notebook doesn't exist
        "check_server",
        server_url=jupyter_server,
    )
    assert result == "Jupyter server is running"


def test_list_sessions_without_notebook(jupyter_server):
    """Test that list_sessions works without accessing a specific notebook."""
    # list_sessions should work with any notebook path
    # because it doesn't actually access the notebook
    result = query_notebook(
        "any_notebook_name",  # This notebook doesn't need to exist
        "list_sessions",
        server_url=jupyter_server,
    )
    assert isinstance(result, list)


def test_get_default_kernel_info(jupyter_server):
    """Test that kernel info can be retrieved from the server."""
    # Create a client to test kernel info retrieval
    client = NotebookClient(
        server_url=jupyter_server,
        notebook_path="test_kernel.ipynb",  # Doesn't need to exist for this test
        token="BLOCK",
    )

    # Test getting kernel info
    kernelspec, language_info = client._get_default_kernel_info()

    # Verify kernelspec structure
    assert isinstance(kernelspec, dict)
    assert "display_name" in kernelspec
    assert "language" in kernelspec
    assert "name" in kernelspec

    # Verify language_info structure
    assert isinstance(language_info, dict)
    assert "name" in language_info

    # Verify content makes sense for a typical Jupyter setup
    assert kernelspec["language"] == "python"
    assert language_info["name"] == "python"
    assert "python" in kernelspec["display_name"].lower()
