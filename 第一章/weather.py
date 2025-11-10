#!/usr/bin/env Python
# -*- coding: utf-8 -*-
import requests
import json

def get_weather(city):
    """
    获取指定城市的天气信息
    这里使用模拟数据，实际应用中可以接入真实的天气API
    """
    # 模拟天气数据
    weather_data = {
        "北京": {"temperature": 25, "condition": "晴", "wind": "微风"},
        "上海": {"temperature": 28, "condition": "多云", "wind": "东南风"},
        "广州": {"temperature": 32, "condition": "雷阵雨", "wind": "南风"},
        "深圳": {"temperature": 30, "condition": "阴", "wind": "无风"}
    }

    if city in weather_data:
        data = weather_data[city]
        return f"{city}当前天气：{data['condition']}，气温{data['temperature']}°C，{data['wind']}"
    else:
        return f"抱歉，暂时无法获取{city}的天气信息"