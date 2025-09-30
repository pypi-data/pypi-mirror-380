from nonebot.plugin import PluginMetadata, get_plugin_config
import asyncio
import json
import os
import aiohttp
import asyncio
from urllib.parse import quote
from nonebot.adapters.onebot.v11 import Bot, MessageSegment
from .config import Config

__plugin_meta__ = PluginMetadata(
    name="group_tools",
    description=(
        "群功能增强插件：\n"
        "- 消息自动撤回（延迟撤回队列）\n"
        "- 群文件上传\n"
        "- OpenList 文件上传与直链获取\n"
        "- 合并转发消息"
    ),
    usage=(
        "本插件提供一系列群聊功能接口，供机器人调用：\n"
        "1. 自动撤回消息：recall(bot, result, delay)\n"
        "2. 上传群文件：upload_group_file(filepath, group_id)\n"
        "3. OpenList 上传：openlist_upload(filepath)\n"
        "4. 获取 OpenList 链接：openlist_fetch_url(filename)\n"
        "5. 合并转发：send_merge_msg(bot, group_id, *contents)\n"
        "（具体命令可由上层插件实现）"
    ),
    type="application",  # ✅ 必须是 application 或 library
    homepage="https://github.com/Ender-Kylin/nonebot_plugin_group_tools",
    supported_adapters={"~onebot.v11"},
)

plugin_config = get_plugin_config(Config)



# 消息撤回队列
avoid_recall_queue = []
recall_queue_processor = None

# ---------------- 工具函数：消息撤回 ----------------
async def recall(bot : Bot, result, time : int = 10):
    """将消息添加到撤回队列，避免并发撤回导致的问题"""
    if result and "message_id" in result:
        # 将撤回任务添加到队列
        recall_task = {
            "bot": bot,
            "message_id": result["message_id"],
            "delay": time
        }
        avoid_recall_queue.append(recall_task)
        
        # 确保队列处理器正在运行
        await ensure_recall_queue_processor()

async def ensure_recall_queue_processor():
    """确保队列处理器正在运行"""
    global recall_queue_processor
    if recall_queue_processor is None or recall_queue_processor.done():
        recall_queue_processor = asyncio.create_task(process_recall_queue())

async def process_recall_queue():
    """处理撤回队列中的任务，依次执行撤回操作"""
    while avoid_recall_queue:
        # 获取队列中的第一个任务
        task = avoid_recall_queue.pop(0)
        bot = task["bot"]
        message_id = task["message_id"]
        delay = task["delay"]
        
        try:
            # 等待指定的延迟时间
            await asyncio.sleep(delay)
            # 执行撤回操作
            await bot.delete_msg(message_id=message_id)
        except Exception as e:
            # 记录错误但继续处理队列中的其他任务
            print(f"撤回消息失败 (ID: {message_id}): {str(e)}")
            continue

# ================= 上传QQ文件函数 =================
async def upload_group_file(filepath, group_id, url = plugin_config.onebotv11http + "/upload_group_file"):
    if group_id == 995282768:
        folder = "/dff430ef-268a-4dfd-9d79-ee46652e3494"
    else:
        folder = "/"
    payload = json.dumps({
        "group_id": group_id,
        "file": filepath,
        "name": os.path.basename(filepath),
        "folder": folder
    })
    headers = {"Content-Type": "application/json"}
    async with aiohttp.ClientSession() as s:
        for i in range(3):
            try:
                async with s.post(url = url, headers=headers,data=payload) as res:
                    if res.status == 200:
                        return None
                    else:
                        continue
            except:
                pass

# ---------------- 工具函数：Openlist上传/链接获取 ----------------

# ---------------- 工具函数：Openlist上传/链接获取 ----------------
async def openlist_login() -> str:
    data = {
        'username': plugin_config.openlist_username,
        'password': plugin_config.openlist_password
    }
    headers = {
        'Content-Type': 'application/json',
    }
    async with aiohttp.ClientSession(headers=headers) as session:
        async with aiohttp.ClientSession() as session:
            async with session.post(
                url = plugin_config.openlist_base_url + "/api/auth/login",
                data = json.dumps(data),
                headers = headers,
            ) as response:
                result = await response.json()
                return result["data"]["token"]

async def openlist_upload(filepath : str):
    with open(filepath, 'rb') as f:
        payload = f.read()
    path = quote(f"/Book/{os.path.basename(filepath)}")
    headers = {
        'Authorization': await openlist_login(),
        'File-Path': path,
        'As-Task': 'true',
        'Content-Length': str(len(payload)),
        'Content-Type': 'application/octet-stream'
    }
    async with aiohttp.ClientSession() as session:
        async with session.put(
            url = plugin_config.openlist_base_url + "/api/fs/put",
            headers = headers,
            data = payload,
        ):
            pass

async def openlist_fetch_url(filename : str):
    MAX_RETRIES = 3
    RETRY_DELAY = 2
    headers = {
   'Authorization': await openlist_login(),
   'Content-Type': 'application/json'
    }
    data = {
        "path": f"/Book/{filename}",
        "password": ""
    }
    for i in range(MAX_RETRIES):
        try:
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    url = plugin_config.openlist_base_url + "/api/fs/get",
                    headers = headers,
                    data = json.dumps(data)
                ) as response:
                    data = await response.json()
                    return data["data"]["sign"], data["data"]["name"]
        except:
            pass
    return None

# ---------------- 合并转发工具函数 ------------
async def send_merge_msg(bot: Bot, group_id: int, *contents: str):
    """
    发送合并转发消息
    :param bot: NoneBot Bot 实例
    :param group_id: 目标群号
    :param contents: 任意数量的字符串
    """
    nodes = []
    for text in contents:
        nodes.append({
            "type": "node",
            "data": {
                "name": "机器人",              # 显示的发送者昵称
                "uin": bot.self_id,           # 发送者QQ号（机器人自己）
                "content": MessageSegment.text(text),
            },
        })

    await bot.send_group_forward_msg(group_id=group_id, messages=nodes)
