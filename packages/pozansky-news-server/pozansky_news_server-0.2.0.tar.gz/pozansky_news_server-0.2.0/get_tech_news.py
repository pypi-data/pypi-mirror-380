#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
获取科技新闻的脚本
"""
import asyncio
import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import NewsFetcher

async def main():
    """主函数：获取并显示科技新闻"""
    print("正在获取科技新闻...")
    print("=" * 50)
    
    # 创建新闻获取器实例
    fetcher = NewsFetcher()
    
    try:
        # 获取科技新闻（使用tech分类）
        print("开始获取科技新闻...")
        tech_news = await fetcher.fetch_hot_news(category="tech", limit=10)
        print(f"获取完成，共 {len(tech_news)} 条新闻")
        
        if not tech_news:
            print("暂时没有获取到科技新闻")
            # 尝试获取通用新闻
            print("尝试获取通用新闻...")
            general_news = await fetcher.fetch_hot_news(category="general", limit=5)
            if general_news:
                print(f"获取到 {len(general_news)} 条通用新闻：\n")
                for i, news in enumerate(general_news, 1):
                    print(f"{i}. {news.get('title', '无标题')}")
                    print(f"   来源: {news.get('source', '未知来源')}")
                    print(f"   时间: {news.get('time', '未知时间')}")
                    print(f"   链接: {news.get('url', '无链接')}")
                    print("-" * 40)
            return
        
        print(f"共获取到 {len(tech_news)} 条科技新闻：\n")
        
        # 格式化显示新闻
        for i, news in enumerate(tech_news, 1):
            print(f"{i}. {news.get('title', '无标题')}")
            print(f"   来源: {news.get('source', '未知来源')}")
            print(f"   时间: {news.get('time', '未知时间')}")
            if news.get('summary'):
                summary = news['summary'][:100] + "..." if len(news['summary']) > 100 else news['summary']
                print(f"   摘要: {summary}")
            print(f"   链接: {news.get('url', '无链接')}")
            print("-" * 40)
        
    except Exception as e:
        print(f"获取新闻时出错: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # 关闭HTTP客户端
        await fetcher.close()
        print("程序执行完成")

if __name__ == "__main__":
    # 运行异步主函数
    asyncio.run(main())
