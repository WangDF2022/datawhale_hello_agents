#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import os
from dotenv import load_dotenv

# 加载 .env 文件中的环境变量
load_dotenv()

def get_env():
    # 现在可以直接使用
    api_key = os.getenv('OPENAI_API_KEY')
    tavily_key = os.getenv('TAVILY_API_KEY')
    base_url = os.getenv('OPENAI_BASE_URL')

    print(f"OPENAI_API_KEY: {api_key}")
    print(f"TAVILY_API_KEY: {tavily_key}")
    print(f"OPENAI_BASE_URL: {base_url}")