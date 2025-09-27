# -*- coding: utf-8 -*-
"""
HTTP客户端 - 统一的HTTP请求处理
"""
from typing import Any, Dict, Optional
import httpx
from ..config.settings import BASE_URL, TIMEOUT


async def get_json(path: str, token: str) -> Dict[str, Any] | str:
    """发送GET请求并返回JSON数据"""
    headers = {"x-user-token": token}
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        try:
            response = await client.get(f"{BASE_URL}{path}", headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return f"Upstream {e.response.status_code}: {e.response.text}"
        except Exception as e:
            return f"Request error: {e}"


async def post_json(path: str, token: str, body: Dict[str, Any]) -> Dict[str, Any] | str:
    """发送POST请求并返回JSON数据"""
    headers = {"x-user-token": token, "Content-Type": "application/json"}
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        try:
            response = await client.post(f"{BASE_URL}{path}", json=body, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return f"Upstream {e.response.status_code}: {e.response.text}"
        except Exception as e:
            return f"Request error: {e}"


async def delete_json(path: str, token: str, body: Optional[Dict[str, Any]] = None) -> Dict[str, Any] | str:
    """发送DELETE请求并返回JSON数据"""
    headers = {"x-user-token": token, "Content-Type": "application/json"}
    async with httpx.AsyncClient(timeout=TIMEOUT) as client:
        try:
            if body:
                response = await client.delete(f"{BASE_URL}{path}", json=body, headers=headers)
            else:
                response = await client.delete(f"{BASE_URL}{path}", headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return f"Upstream {e.response.status_code}: {e.response.text}"
        except Exception as e:
            return f"Request error: {e}"
