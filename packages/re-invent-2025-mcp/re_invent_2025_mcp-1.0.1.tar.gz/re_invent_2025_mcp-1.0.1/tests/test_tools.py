import sys
from pathlib import Path

# Add both src and tests to path
test_dir = Path(__file__).parent
sys.path.insert(0, str(test_dir.parent / "src"))
sys.path.insert(0, str(test_dir))

import pytest
from reinvent_2025_mcp.tools.session_tools import create_session_tools
from test_data import mock_sessions

class TestMCPTools:
    def setup_method(self):
        self.tools = create_session_tools(mock_sessions)

    def test_creates_all_13_tools(self):
        assert len(self.tools) == 13
        assert 'search_sessions' in self.tools
        assert 'get_session_details' in self.tools
        assert 'list_categories' in self.tools

    def test_search_sessions_tool_schema(self):
        tool = self.tools['search_sessions']
        assert tool['name'] == 'search_sessions'
        assert 'query' in tool['inputSchema']['required']

    def test_search_sessions_tool_execution(self):
        result = self.tools['search_sessions']['handler']({'query': 'AI'})
        assert len(result['items']) == 1
        assert result['items'][0]['code'] == 'AIM236-S'

    def test_get_session_details_tool_execution(self):
        result = self.tools['get_session_details']['handler']({'session_code': 'AIM236-S'})
        assert result['code'] == 'AIM236-S'
        assert result['speakers'][0]['name'] == 'John Doe'

    def test_list_categories_tool_execution(self):
        result = self.tools['list_categories']['handler']({'category': 'levels'})
        assert len(result) == 2
        assert result[0]['name'] == '300 – Advanced'

    def test_get_sessions_by_level_tool_execution(self):
        result = self.tools['get_sessions_by_level']['handler']({'level': '300'})
        assert len(result['items']) == 1
        assert result['items'][0]['code'] == 'AIM236-S'

    def test_search_sessions_by_speaker_tool_execution(self):
        result = self.tools['search_sessions_by_speaker']['handler']({'speaker_name': 'John'})
        assert len(result['items']) == 1
        assert result['items'][0]['code'] == 'AIM236-S'
