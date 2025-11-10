#!/usr/bin/env Python
# -*- coding: utf-8 -*-
from tavily import TavilyClient
import os


def search_attraction(city, weather):
    """
    根据城市和天气条件搜索合适的旅游景点
    """
    try:
        # 初始化Tavily客户端
        tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

        # 构建搜索查询
        query = f"{city} {weather} 适合的旅游景点推荐"

        # 执行搜索
        response = tavily.search(query=query, max_results=3)

        # 处理搜索结果
        attractions = []
        for result in response.get('results', []):
            attractions.append({
                'title': result.get('title', ''),
                'content': result.get('content', '')[:200] + '...'
            })

        return f"根据{city}的{weather}天气，推荐以下景点：" + \
            "\n".join([f"- {attr['title']}: {attr['content']}" for attr in attractions])

    except Exception as e:
        return f"搜索景点时出现错误：{str(e)}"