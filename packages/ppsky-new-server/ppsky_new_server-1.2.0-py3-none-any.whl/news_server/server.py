import asyncio
import httpx
import feedparser
from datetime import datetime
from typing import List, Dict
from mcp.server.fastmcp import FastMCP

# 创建 FastMCP 实例
mcp = FastMCP("NewsServer")

class NewsFetcher:
    def __init__(self):
        self.client = None
        self.news_sources = {
            "tech": [
                "https://www.ithome.com/rss/",
            ],
            "general": [
                "http://www.people.com.cn/rss/politics.xml"
            ],
            "international": [
                "http://rss.cnn.com/rss/edition.rss",
                "https://feeds.bbci.co.uk/news/world/rss.xml"
            ]
        }

    async def initialize(self):
        """初始化HTTP客户端"""
        if self.client is None:
            self.client = httpx.AsyncClient(
                timeout=30.0,
                headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
            )
        return True

    async def fetch_hot_news(self, category: str = "general", limit: int = 20) -> List[Dict]:
        """获取热点新闻"""
        await self.initialize()
        news_list = []
        sources = self.news_sources.get(category, self.news_sources["general"])
        
        # 并发获取所有RSS源
        tasks = [self._fetch_rss_feed(source) for source in sources[:3]]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        for result in results:
            if isinstance(result, Exception):
                continue
            news_list.extend(result)

        # 去重和排序
        news_list = self._deduplicate_news(news_list)
        news_list.sort(key=lambda x: x.get('time', ''), reverse=True)
        return news_list[:limit]

    async def _fetch_rss_feed(self, rss_url: str) -> List[Dict]:
        """获取单个RSS源的内容"""
        try:
            response = await self.client.get(rss_url)
            feed = feedparser.parse(response.content)
            news_items = []
            
            for entry in feed.entries[:10]:  # 每个源最多10条
                news_item = {
                    'title': entry.title,
                    'url': entry.link,
                    'source': feed.feed.get('title', '未知来源'),
                    'time': self._parse_time(entry.get('published', '')),
                    'summary': entry.get('summary', '')[:200]
                }
                news_items.append(news_item)
            return news_items
        except Exception as e:
            print(f"获取RSS源失败 {rss_url}: {e}")
            return []

    async def search_news(self, keyword: str, limit: int = 10) -> List[Dict]:
        """搜索新闻"""
        try:
            # 先获取一些新闻，然后过滤
            all_news = await self.fetch_hot_news("general", 50)
            filtered_news = [
                news for news in all_news
                if keyword.lower() in news['title'].lower()
            ]
            return filtered_news[:limit]
        except Exception as e:
            print(f"搜索新闻失败: {e}")
            return []

    def _parse_time(self, time_str: str) -> str:
        """解析时间字符串"""
        if not time_str:
            return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        time_formats = [
            '%a, %d %b %Y %H:%M:%S %Z',
            '%a, %d %b %Y %H:%M:%S %z',
            '%Y-%m-%dT%H:%M:%S%z',
            '%Y-%m-%d %H:%M:%S'
        ]
        
        for fmt in time_formats:
            try:
                dt = datetime.strptime(time_str, fmt)
                return dt.strftime('%Y-%m-%d %H:%M:%S')
            except ValueError:
                continue
        return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def _deduplicate_news(self, news_list: List[Dict]) -> List[Dict]:
        """去重新闻"""
        seen_titles = set()
        unique_news = []
        for news in news_list:
            title = news['title'].lower().strip()
            if title not in seen_titles:
                seen_titles.add(title)
                unique_news.append(news)
        return unique_news

    async def close(self):
        """关闭客户端"""
        if self.client:
            await self.client.aclose()
            self.client = None

# 创建全局实例
news_fetcher = NewsFetcher()

def _format_news(news_list: list) -> str:
    """格式化新闻输出"""
    if not news_list:
        return "📰 没有找到相关新闻"
    
    result = ["📰 最新新闻摘要:", ""]
    for i, news in enumerate(news_list, 1):
        result.append(f"{i}. **{news.get('title', '无标题')}**")
        if news.get('source'):
            result.append(f"   📍 来源: {news['source']}")
        if news.get('time'):
            result.append(f"   ⏰ 时间: {news['time']}")
        if news.get('summary'):
            result.append(f"   📝 摘要: {news['summary']}")
        if news.get('url'):
            result.append(f"   🔗 链接: {news['url']}")
        result.append("")
    
    return "\n".join(result)

@mcp.tool()
async def get_hot_news(category: str = "general", limit: int = 10) -> str:
    """获取热点新闻
    
    Args:
        category: 新闻分类 (general-综合, tech-科技, international-国际)
        limit: 返回新闻数量 (1-20)
    """
    try:
        # 参数验证
        if limit > 20:
            limit = 20
        if limit < 1:
            limit = 5
            
        valid_categories = ["general", "tech", "international"]
        if category not in valid_categories:
            category = "general"
            
        news_list = await news_fetcher.fetch_hot_news(category, limit)
        return _format_news(news_list)
    except Exception as e:
        return f"❌ 获取新闻失败: {str(e)}"

@mcp.tool()
async def search_news(keyword: str, limit: int = 10) -> str:
    """搜索新闻
    
    Args:
        keyword: 搜索关键词
        limit: 返回结果数量 (1-10)
    """
    try:
        if limit > 10:
            limit = 10
        if limit < 1:
            limit = 5
            
        if not keyword or len(keyword.strip()) == 0:
            return "请输入有效的搜索关键词"
            
        news_list = await news_fetcher.search_news(keyword.strip(), limit)
        return _format_news(news_list)
    except Exception as e:
        return f"❌ 搜索新闻时出错: {str(e)}"

@mcp.tool()
async def list_news_categories() -> str:
    """列出可用的新闻分类"""
    categories_info = """
📊 可用的新闻分类:

1. **general** - 综合新闻 (人民网等)
2. **tech** - 科技新闻 (IT之家等)  
3. **international** - 国际新闻 (CNN、BBC等)

使用示例: get_hot_news(category="tech", limit=5)
"""
    return categories_info


# def main():
#     """主入口函数 - 这是打包的关键！"""
#     print("🚀 新闻MCP服务器启动中...")
#     print("📋 可用工具:")
#     print("   - get_hot_news: 获取热点新闻")
#     print("   - search_news: 搜索新闻") 
#     print("   - list_news_categories: 列出新闻分类")
    
#     # 使用stdio传输运行MCP服务器
#     mcp.run(transport="stdio")

if __name__ == "__main__":
    mcp.run(transport="stdio")


# # 确保脚本可以直接运行
# if __name__ == "__main__":
#     main()