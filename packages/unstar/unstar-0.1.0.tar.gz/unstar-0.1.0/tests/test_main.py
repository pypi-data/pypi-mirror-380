from unittest.mock import Mock, patch

import pytest

from unstar import main


class TestMain:
    @patch('sys.argv', ['unstar'])
    @patch('builtins.print')
    def test_main_no_args(self, mock_print):
        """Test main function with no arguments."""
        with pytest.raises(SystemExit) as exc_info:
            main()

        assert exc_info.value.code == 1
        mock_print.assert_any_call("Usage: unstar <access_token>")

    @patch('sys.argv', ['unstar', 'test_token'])
    @patch('unstar.GitStars')
    @patch('builtins.print')
    def test_main_success(self, mock_print, mock_git_stars_class):
        """Test successful main execution."""
        mock_git_stars = Mock()
        mock_git_stars.get_all_star_repos.return_value = ['user/repo1', 'user/repo2']
        mock_git_stars.delete_star.return_value = True
        mock_git_stars_class.return_value = mock_git_stars

        with patch('time.sleep'):  # Mock sleep to speed up test
            main()

        mock_print.assert_any_call("user/repo1 is unstarred")
        mock_print.assert_any_call("user/repo2 is unstarred")
