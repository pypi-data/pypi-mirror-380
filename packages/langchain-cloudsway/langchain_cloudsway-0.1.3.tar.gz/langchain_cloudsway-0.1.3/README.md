# langchain-cloudsway

LangChain integration for the Cloudsway SmartSearch API.

## Installation

```bash
pip install -U langchain-cloudsway
```

## Configuration

The tool expects a single environment variable containing both the endpoint and access key in the format:
endpoint-accesskey

Examples:

```bash
# POSIX / Git Bash
export CLOUDSWAY_SERVER_KEY="endpoint-accesskey"

# Windows (cmd.exe / PowerShell)
set CLOUDSWAY_SERVER_KEY=endpoint-accesskey
# or in PowerShell:
$env:CLOUDSWAY_SERVER_KEY="endpoint-accesskey"
```

- endpoint: the random path segment generated for your account (used in the request URL).
- accesskey (AK): the AccessKey used for Authorization Bearer.

Register and get credentials at: https://console.cloudsway.ai/

## Tool

SmartsearchTool — web search using Cloudsway Smart API.

### Basic Python usage

```python
from langchain_cloudsway.smartsearch import SmartsearchTool

tool = SmartsearchTool()
result = tool.invoke({
    "query": "cloudsway.ai",
    "count": 5,
    "setLang": "en"
})
print(result)
```

## Parameters

Notes:
- q (query) is required and must be non-empty.
- count default: 10. Maximum: 50. Accepted values (recommended page sizes): 10, 20, 30, 40, 50.
- offset is zero-based.
- freshness supports Day, Week, Month or a date range like 2019-02-01..2019-05-30 (source support may vary).
- setLang accepts 2- or 4-letter codes (recommend 4-letter like en-US). If invalid, server may default to en.
- enableContent and mainText control long/full content fetching. mainText only applies when enableContent=true.

| Parameter     | Required | Type    | Description |
|---------------|----------|---------|-------------|
| q / query     | Yes      | String  | Search query text. Cannot be empty. |
| count         | No       | Short   | Number of results to return. Default 10. Max 50. (Allowed: 10,20,30,40,50) |
| offset        | No       | Short   | Zero-based offset for paging. Default 0. |
| freshness     | No       | String  | Time filter: Day, Week, Month, or date-range `YYYY-MM-DD..YYYY-MM-DD`. |
| setLang       | No       | String  | UI language code (ISO 639-1 or ISO639-1-ISO3166, e.g., en-US). |
| sites         | No       | String  | Host filter (host format, e.g., `baijiahao.baidu.com`). |
| enableContent | No       | Boolean | Return full content / long summary. Default false. |
| mainText      | No       | Boolean | When enableContent=true, request long summary (key fragment). Default false. |

## Advanced examples

```python
# freshness + language
tool.invoke({"query": "latest AI research", "count": 20, "freshness": "Week", "setLang": "en-US"})

# site filter + full content + mainText
tool.invoke({"query": "machine learning tutorial", "sites": "github.com", "enableContent": True, "mainText": True})

# pagination
tool.invoke({"query": "climate change", "count": 10, "offset": 10})
```

## Response structure

Typical response:

```json
{
  "queryContext": {
    "originalQuery": "cat"
  },
  "webPages": {
    "value": [
      {
        "name": "cat - 搜狗百科",
        "url": "http://baike.sogou.com/...",
        "displayUrl": "http://baike.sogou.com/...",
        "thumbnailUrl": "http://img02.sogoucdn.com/...",
        "snippet": "Short description... (first 200 characters)",
        "datePublished": "2024-07-31T06:25:29.0000000",
        "datePublishedDisplayText": "Jul 31, 2024",
        "dateLastCrawled": "2024-09-08T23:18:00.0000000Z",
        "siteName": "搜狗百科",
        "score": 0.67,
        "mainText": "Longer extracted summary or full page content (present when enableContent=true)"
      }
    ]
  }
}
```

Response field notes:
- queryContext.originalQuery — original query string.
- webPages.value — array of WebPage objects.
- WebPage fields:
  - name (String): page title.
  - snippet (String): short text snippet (first ~200 chars).
  - url (String): canonical URL.
  - displayUrl (String): display-friendly URL.
  - thumbnailUrl (String): thumbnail image URL when available.
  - datePublished / datePublishedDisplayText (String): publish time and display text.
  - dateLastCrawled (String): last crawl time (when available).
  - siteName (String): source site name.
  - score (Float): relevance score.
  - mainText (String): long summary .
  - content: extracted main content (only when enableContent requested)

## Status codes / Error handling

- 200: Success
- 429: QPS (rate) limit exceeded — contact Cloudsway to request higher QPS.

If you encounter any problems, reach out to info@cloudsway.com.

## License

MIT — See [LICENSE](./LICENSE) for details.
