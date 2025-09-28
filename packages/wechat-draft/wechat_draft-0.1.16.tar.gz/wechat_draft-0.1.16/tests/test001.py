# 开发人员： Xiaoqiang
# 微信公众号: XiaoqiangClub
# 创建时间： 2025-09-28T06:46:20.189Z
# 文件描述： 微信 Access Token 接口模拟请求测试
# 文件路径： tests/test_wechat_access_token.py

import asyncio
import httpx  # 导入 httpx


PASSWORD = "czq087405"

TEST_PORT = 8000


async def run_test():

    async with httpx.AsyncClient() as client:
        print("模拟发送 POST 请求到 /wechat/access_token...")
        url = f"https://fastapi.xiaoqiangclub.qzz.io/wechat/access_token"
        headers = {'Content-Type': 'application/json'}
        data = {"token": PASSWORD}

        response = await client.post(url, headers=headers, json=data)
        print(response.text)
        response_data = response.json()

        print(f"响应状态码: {response.status_code}")
        print(f"响应体: {response_data}")




if __name__ == "__main__":
    asyncio.run(run_test())
