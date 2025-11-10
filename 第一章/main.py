#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import config
from 第一章.weather import *
from 第一章.attraction import *
from 第一章.openapi_client import OpenAICompatibleClient

AGENT_SYSTEM_PROMPT = """
你是一个智能旅行助手，能够帮助用户规划旅行并提供相关信息。

你有以下工具可以使用：
1. get_weather(city): 获取指定城市的天气信息
2. search_attraction(city, weather): 根据城市和天气搜索合适的旅游景点

请按照以下格式回复：
Thought: [你的思考过程]
Action: [要执行的动作，格式为函数调用]

如果不需要使用工具，请直接回复用户。
"""

# 可用工具字典
available_tools = {
    "get_weather": get_weather,
    "search_attraction": search_attraction
}



def run_agent():
    """运行智能体主循环"""
    client = OpenAICompatibleClient()

    # 初始化对话历史
    messages = [{"role": "system", "content": AGENT_SYSTEM_PROMPT}]

    print("🤖 智能旅行助手已启动！输入 'quit' 退出。\n")

    while True:
        # 获取用户输入
        user_input = input("👤 用户: ").strip()
        if user_input.lower() == 'quit':
            print("👋 再见！")
            break

        # 添加用户消息到历史
        messages.append({"role": "user", "content": user_input})

        # 开始智能体循环
        max_iterations = 5  # 防止无限循环
        for iteration in range(max_iterations):
            print(f"\n🔄 循环 {iteration + 1}:")

            # 1. 思考阶段：调用LLM
            response = client.chat_completion(messages)
            print(f"🧠 智能体响应:\n{response}")

            # 2. 解析行动
            function_name, params = client.parse_action(response)

            if function_name and function_name in available_tools:
                # 3. 执行行动
                print(f"⚡ 执行工具: {function_name}({', '.join(params)})")

                try:
                    tool_result = available_tools[function_name](*params)
                    observation = f"Observation: {tool_result}"
                    print(f"👁️ 观察结果: {tool_result}")

                    # 4. 将观察结果添加到对话历史
                    messages.append({"role": "assistant", "content": response})
                    messages.append({"role": "user", "content": observation})

                except Exception as e:
                    error_msg = f"Observation: 工具执行出错 - {str(e)}"
                    print(f"❌ 错误: {str(e)}")
                    messages.append({"role": "assistant", "content": response})
                    messages.append({"role": "user", "content": error_msg})
            else:
                # 没有工具调用，直接结束循环
                messages.append({"role": "assistant", "content": response})
                print("✅ 任务完成！")
                break

        print("\n" + "=" * 50 + "\n")


# 运行智能体
if __name__ == "__main__":
    config.get_env()
    run_agent()