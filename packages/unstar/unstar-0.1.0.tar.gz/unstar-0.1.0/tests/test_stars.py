from unittest.mock import Mock, patch

import pytest

from unstar.exceptions import GitStarsException
from unstar.stars import GitStars


class TestGitStars:
    def setup_method(self):
        self.git_stars = GitStars("https://api.github.com", "test_token")

    @patch('unstar.stars.requests.get')
    def test_get_all_star_repos_empty(self, mock_get):
        """Test getting starred repos when there are none."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = []
        mock_get.return_value = mock_response

        result = self.git_stars.get_all_star_repos(0)

        assert result == []
        mock_get.assert_called_once()

    @patch('unstar.stars.requests.get')
    def test_get_all_star_repos_with_data(self, mock_get):
        """Test getting starred repos with data."""
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.side_effect = [
            [{'full_name': 'user/repo1'}, {'full_name': 'user/repo2'}],
            []  # Second call returns empty to stop pagination
        ]
        mock_get.return_value = mock_response

        result = self.git_stars.get_all_star_repos(0)

        assert result == ['user/repo1', 'user/repo2']
        assert mock_get.call_count == 2

    @patch('unstar.stars.requests.delete')
    def test_delete_star_success(self, mock_delete):
        """Test successful star deletion."""
        mock_response = Mock()
        mock_response.status_code = 204
        mock_delete.return_value = mock_response

        result = self.git_stars.delete_star('user/repo')

        assert result is True
        mock_delete.assert_called_once()

    @patch('unstar.stars.requests.delete')
    def test_delete_star_not_found(self, mock_delete):
        """Test star deletion when repo not found."""
        mock_response = Mock()
        mock_response.status_code = 404
        mock_delete.return_value = mock_response

        result = self.git_stars.delete_star('user/repo')

        assert result is False
        mock_delete.assert_called_once()

    @patch('unstar.stars.requests.delete')
    def test_delete_star_error(self, mock_delete):
        """Test star deletion with error response."""
        mock_response = Mock()
        mock_response.status_code = 500
        mock_response.json.return_value = {'message': 'Server Error'}
        mock_delete.return_value = mock_response

        with pytest.raises(GitStarsException):
            self.git_stars.delete_star('user/repo')
