import re
import aiohttp
import asyncio
from nonebot import get_plugin_config
from nonebot.plugin import PluginMetadata
from .config import Config
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.params import CommandArg
from nonebot.adapters.onebot.v11 import Bot


__plugin_meta__ = PluginMetadata(
    name="tcping",
    description="TCP端口连通性测试工具，支持域名和IP地址测试",
    usage=".tcping 域名:端口 或 .tcping IP:端口",
    type="server",
    homepage="https://github.com/Ender-Kylin/nonebot_plugin_tcping",
    config=Config,
    supported_adapters={"~onebot.v11"},
)


config = get_plugin_config(Config)


# 定义命令匹配规则
tcping_cmd = on_command("tcping", priority=10, block=True)

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

@tcping_cmd.handle()
async def handle_tcping(bot: Bot, args: Message = CommandArg()):
    text = args.extract_plain_text().strip()
    
    # 输入验证
    if not text:
        await tcping_cmd.send("用法：.tcping 域名:端口 或 .tcping IP:端口")
        await tcping_cmd.finish()
        
    # 检查输入格式
    if ":" not in text:
        await tcping_cmd.send("格式错误，请使用：.tcping 域名:端口 或 .tcping IP:端口")
        await tcping_cmd.finish()
        
    try:
        domain, port = text.split(":")
        
        # 验证端口格式
        if not port.isdigit() or not (0 <= int(port) <= 65535):
            await tcping_cmd.send("端口号必须是0-65535之间的整数")
            await tcping_cmd.finish()
            
        params = {
            "address": domain,
            "port": port
        }
        
        message = []
        success_count = 0
        total_ping = 0
        
        # 异步请求，连续测试3次
        async with aiohttp.ClientSession() as session:
            for i in range(3):
                try:
                    async with session.get(config.tcping_url, params=params, timeout=10) as resp:
                        if resp.status == 200:
                            res = await resp.json()
                            # 兼容code=0和code=200的情况
                            if (res.get("code") == 200 or res.get("code") == 0) and "data" in res and "ping" in res["data"]:
                                ping_value_str = res["data"]["ping"]
                                # 处理ping值，提取数字部分
                                try:
                                    # 提取所有数字（包括小数）
                                    ping_match = re.search(r'\d+\.?\d*', str(ping_value_str))
                                    if ping_match:
                                        ping_value = float(ping_match.group())
                                        # 检查是否已经包含ms单位
                                        if 'ms' in str(ping_value_str).lower():
                                            display_ping = f"{ping_value}ms"
                                        else:
                                            display_ping = f"{ping_value:.2f}ms"
                                        message.append(f'第{i+1}次延迟 {display_ping}')
                                        success_count += 1
                                        total_ping += ping_value
                                    else:
                                        message.append(f'第{i+1}次解析失败：无法识别延迟值')
                                except (ValueError, TypeError):
                                    message.append(f'第{i+1}次解析失败：无效的延迟值')
                            else:
                                message.append(f'第{i+1}次请求失败：响应数据格式不正确')
                        else:
                            message.append(f'第{i+1}次请求失败：HTTP状态码 {resp.status}')
                except asyncio.TimeoutError:
                    message.append(f'第{i+1}次请求超时')
                except Exception as e:
                    message.append(f'第{i+1}次请求异常：{str(e)}')
                
                # 每次请求间隔1秒
                if i < 2:
                    await asyncio.sleep(1)
        
        # 添加统计信息
        if success_count > 0:
            avg_ping = total_ping / success_count
            message.append(f'\n测试统计：成功{success_count}/3次，平均延迟 {avg_ping:.2f}ms')
        else:
            message.append('\n测试统计：全部请求失败')
        
        # 发送结果
        res = await tcping_cmd.send("\n".join(message))
        # 延迟撤回消息
        if config.recal_time > 0:
            await recall(bot, res, config.recal_time)
        
    except Exception as e:
        await tcping_cmd.send(f"处理请求时发生错误：{str(e)}")
        
    await tcping_cmd.finish()

