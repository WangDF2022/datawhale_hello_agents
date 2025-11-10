#!/usr/bin/env Python
# -*- coding: utf-8 -*-
from openai import OpenAI
from loguru import logger
import re
import os



class OpenAICompatibleClient:
    def __init__(self):
        self.client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY"),
            base_url=os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
        )

    # def chat_completion(self, messages, model="gpt-3.5-turbo"):  # 在魔搭该模型无效
    def chat_completion(self, messages, model="Qwen/Qwen3-VL-8B-Instruct"):
        """调用LLM进行对话"""
        try:
            response = self.client.chat.completions.create(
                model=model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"调用LLM时出现错误：{str(e)}"

    def parse_action(self, response):
        """解析LLM响应中的Action"""
        # 使用正则表达式提取Action
        action_pattern = r'Action:\s*([a-zA-Z_]+)\((.*?)\)'
        match = re.search(action_pattern, response)

        if match:
            function_name = match.group(1)
            # 简单解析参数（实际应用中需要更robust的解析）
            params_str = match.group(2).strip('"\'')
            params = [p.strip().strip('"\'') for p in params_str.split(',') if p.strip()]
            print("===========:",params[0])
            print("===========:",function_name)
            print("===========:",response)
            return function_name, params

        return None, None