import datetime

import httpx


async def fetch_data():
    data = {
        'agent': {
            'tools': [],
            'llm': {
                'path': 'chatglm_llm.ZhiPuLLM',
                'configs': {
                    'name': 'glm-4'
                }
            },
            'dataset_config': {
                'knowledge_ids': []
            },
            'pre_prompt': '给我生成一篇文档字数在500字以内'
        },
        'chat': {
            'query': '你好',
            'session_id': '223311',
            'inputs': {
                'from': '中文',
                'to': '法文'
            }
        }
    }
    async with httpx.AsyncClient() as client:
        async with client.stream('POST', 'http://127.0.0.1:18000/api/v1/agent/chat/', json=data, timeout=100) as response:
            print(datetime.datetime.now())

            async for chunk in response.aiter_bytes():
                # 处理每个接收到的数据块
                print(chunk.decode(), end='')  # 这里你可以根据需要处理接收到的数据

# 运行异步函数
async def main():
    await fetch_data()

# asyncio.run(main()) 是 Python 3.7+ 提供的一种运行异步函数的方法
# 如果你使用的 Python 版本低于 3.7，你需要使用更早期的异步处理方法
# 例如 loop = asyncio.get_event_loop(); loop.run_until_complete(main())
if __name__ == '__main__':
    import asyncio
    print(datetime.datetime.now())
    asyncio.run(main())
    print(datetime.datetime.now())
