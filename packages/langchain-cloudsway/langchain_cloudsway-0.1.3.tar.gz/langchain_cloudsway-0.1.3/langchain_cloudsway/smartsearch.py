from typing import Optional, Type
from pydantic import BaseModel, Field, validator
import httpx
import os

from langchain_core.callbacks import CallbackManagerForToolRun
from langchain_core.tools import BaseTool

class SmartsearchToolInput(BaseModel):
    """Input schema for Cloudsway smartsearch tool."""
    query: str = Field(..., description="Search keyword or question (e.g., 'Latest advances in machine learning 2024').")
    count: Optional[int] = Field(10, description="Number of results to return (1-50, recommended 3-10).")
    offset: Optional[int] = Field(0, description="Pagination offset (e.g., offset=10 means start from result #11).")
    setLang: Optional[str] = Field("en", description="Language filter (e.g., 'zh-CN', 'en', 'ja').")
    freshness: Optional[str] = Field(None, description="Filter by time period: 'Day', 'Week', 'Month', or date range like '2023-02-01..2023-05-30'.")
    sites: Optional[str] = Field(None, description="Host address to filter results from a specific website (e.g., 'baijiahao.baidu.com').")
    enableContent: Optional[bool] = Field(False, description="Whether to return full content. Default: false.")
    mainText: Optional[bool] = Field(False, description="Whether to return long summary (mainText). Requires enableContent=true.")

class SmartsearchTool(BaseTool):
    """Cloudsway Smartsearch tool for LangChain.

    Setup:
        pip install -U langchain-cloudsway
        export CLOUDSWAY_SERVER_KEY="your-endpoint-accesskey"

    Usage:
        from langchain_cloudsway.smartsearch import SmartsearchTool
        tool = SmartsearchTool()
        tool.invoke({"query": "cloudsway.ai", "count": 5})
    """

    name: str = "cloudsway_smartsearch"
    description: str = (
        "Web search via Cloudsway API. Input should be a search query. "
        "Returns structured JSON results including title, url, content, and date."
    )
    args_schema: Type[BaseModel] = SmartsearchToolInput

    def _get_api_key(self) -> str:
        api_key = os.getenv("CLOUDSWAY_SERVER_KEY")
        if not api_key:
            raise ValueError("CLOUDSWAY_SERVER_KEY environment variable not set.")
        return api_key

    def _run(
        self,
        query: str,
        count: int = 10,
        offset: int = 0,
        setLang: str = "en",
        freshness: Optional[str] = None,
        sites: Optional[str] = None,
        enableContent: Optional[bool] = False,
        mainText: Optional[bool] = False,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> dict:
        """
        Perform a synchronous search request to Cloudsway Smart API.

        Returns the parsed JSON response as a Python dict.
        """
        server_key = self._get_api_key()
        if "-" not in server_key:
            raise ValueError("CLOUDSWAY_SERVER_KEY format is invalid. Expected 'endpoint-accesskey'.")
        endpoint, api_key = server_key.split("-", 1)
        url = f"https://searchapi.cloudsway.net/search/{endpoint}/smart"

        # Basic validation (also enforced by pydantic when using args_schema)
        if not query or not query.strip():
            raise ValueError("query must be a non-empty string")
        if not (1 <= count <= 50):
            raise ValueError("count must be between 1 and 50")
        if offset < 0:
            raise ValueError("offset must be >= 0")
        # mainText requires enableContent
        if mainText and not enableContent:
            # ignore mainText if enableContent is False
            mainText = False

        params = {
            "q": query,
            "count": count,
            "offset": offset,
            "setLang": setLang,
        }
        if freshness:
            params["freshness"] = freshness
        if sites:
            params["sites"] = sites
        # include enableContent/mainText only when explicitly requested
        if enableContent:
            params["enableContent"] = "true"
            if mainText:
                params["mainText"] = "true"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "pragma": "no-cache",
        }

        try:
            with httpx.Client(timeout=60) as client:
                response = client.get(url, params=params, headers=headers)
                response.raise_for_status()
            # return parsed JSON for easier consumption by callers/tests
            return response.json()
        except httpx.HTTPStatusError as e:
            # preserve status and message
            raise RuntimeError(f"API Error [{e.response.status_code}]: {e.response.text}") from e
        except Exception as e:
            raise RuntimeError(f"API Error: {e}") from e