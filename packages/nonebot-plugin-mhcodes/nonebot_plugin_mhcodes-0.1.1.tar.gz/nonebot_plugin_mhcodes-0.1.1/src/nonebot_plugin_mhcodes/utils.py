import json
from pathlib import Path
from nonebot import logger, require

require("nonebot_plugin_localstore")
import nonebot_plugin_localstore as store

plugin_cache_file: Path = store.get_plugin_cache_file("mh_codes.json")

def load_data() -> dict:
    if plugin_cache_file.exists():
        try:
            with open(plugin_cache_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            logger.error("缓存文件损坏，创建新数据")
    return {"groups": {}}

def save_data(data: dict):
    with open(plugin_cache_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def _ensure_group_data_exists(data: dict, group_id: str):
    if "groups" not in data:
        data["groups"] = {}
    if group_id not in data["groups"]:
        data["groups"][group_id] = {"codes": []}
    elif "codes" not in data["groups"][group_id]:
        data["groups"][group_id]["codes"] = []

def code_added(group_id: str, code: str) -> bool:
    data = load_data()
    _ensure_group_data_exists(data, group_id)
    codes = data["groups"][group_id]["codes"]

    if code not in codes:
        codes.append(code)
        save_data(data)
        logger.info(f"群组 {group_id} 添加了集会码: {code}")
        return True
    return False

def code_removed(group_id: str, code: str) -> bool:
    data = load_data()
    _ensure_group_data_exists(data, group_id)
    codes = data["groups"][group_id]["codes"]

    if code in codes:
        codes.remove(code)
        save_data(data)
        logger.info(f"群组 {group_id} 移除了集会码: {code}")
        return True
    return False

def get_group_codes(group_id: str) -> list:
    data = load_data()
    return data.get("groups", {}).get(group_id, {}).get("codes", [])

def reset_all_codes_for_group(group_id: str) -> bool:
    data = load_data()
    _ensure_group_data_exists(data, group_id)
    codes = data["groups"][group_id]["codes"]

    if codes:
        data["groups"][group_id]["codes"] = []
        save_data(data)
        logger.info(f"群组 {group_id} 的集会码已通过命令重置")
        return True
    return False

def reset_all_codes_daily() -> None:
    data = load_data()
    if "groups" in data:
        codes_reset_count = 0
        for group_id in list(data["groups"].keys()):
            if "codes" in data["groups"][group_id] and data["groups"][group_id]["codes"]:
                data["groups"][group_id]["codes"] = []
                logger.info(f"每日重置: 群组 {group_id} 的集会码已重置")
                codes_reset_count += 1

        if codes_reset_count > 0:
            save_data(data)
            logger.info(f"每日集会码重置任务完成。共 {codes_reset_count} 个群组的集会码被重置")
        else:
            logger.info("每日集会码重置任务完成。没有群组有活跃的集会码需要重置")
    else:
        logger.info("每日集会码重置任务完成。未找到群组数据")
