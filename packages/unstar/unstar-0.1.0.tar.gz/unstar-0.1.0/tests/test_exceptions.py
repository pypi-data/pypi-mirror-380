from unstar.exceptions import GitStarsException


def test_git_stars_exception():
    """Test GitStarsException creation and string representation."""
    exception = GitStarsException(404, "Not Found")

    assert str(exception) == "status: 404 | message: Not Found"

    # Test with additional args
    exception_with_args = GitStarsException(500, "Server Error", "extra", "args")
    assert str(exception_with_args) == "status: 500 | message: Server Error"
