import dataclasses
import aiohttp
import json
import struct
import blake3
import os

from markdown_it.common.html_blocks import block_names
from mdit_py_plugins.myst_blocks.index import block_break

from StealthIM import logger

from .common import request, Result, NoValResult


BLOCK_SIZE = 2048 * 1024  # 2MB


@dataclasses.dataclass
class FileInfoResult:
    size: int
    result: Result


async def get_file_info(
        url: str,
        session: str,
        file_hash: str,
) -> FileInfoResult:
    api_address = f"{url}/api/v1/file/{file_hash}"
    logger.debug(f"Called API get_file_info with url: {api_address}")
    header = {
        "Authorization": f"Bearer {session}"
    }

    response_data = await request(api_address, "POST", headers=header)
    logger.debug(f"Response data: {response_data}")

    success = response_data["result"]["code"] == 800

    return FileInfoResult(
        size=response_data["size"] if success else None,
        result=Result(
            code=response_data["result"]["code"],
            msg=response_data["result"]["msg"]
        )
    )


async def upload_file(
    url: str,
    session: str,
    groupid: int,
    filename: str,
    file_path: str
) -> dict:
    api_address = f"{url}/api/v1/file/"
    api_address = api_address.replace("https", "wss").replace("http", "ws")
    logger.debug(f"Called API upload_file with url: {api_address}")
    header = {
        "Authorization": f"Bearer {session}"
    }

    file_size = os.path.getsize(file_path)
    block_hashes = []
    with open(file_path, 'rb') as f:
        while True:
            block = f.read(BLOCK_SIZE)
            if not block:
                break
            h = blake3.blake3(block).digest()
            block_hashes.append(h)
    final_hash = blake3.blake3(b''.join(block_hashes)).hexdigest()
    async with aiohttp.ClientSession() as client:
        async with client.ws_connect(api_address, headers=header) as ws:
            meta = {
                "size": str(file_size),
                "groupid": str(groupid),
                "hash": final_hash,
                "filename": filename[:30]
            }
            await ws.send_str(json.dumps(meta))
            meta_resp = await ws.receive()
            meta_resp = json.loads(meta_resp.data)
            if meta_resp.get("result", {}).get("code") != 0:
                return meta_resp
            with open(file_path, 'rb') as f:
                block_id = 0
                while True:
                    block = f.read(BLOCK_SIZE)
                    if not block:
                        break
                    block_id_bytes = struct.pack('<I', block_id)
                    data = block_id_bytes + block
                    await ws.send_bytes(data)
                    block_resp = await ws.receive()
                    block_resp = json.loads(block_resp.data)
                    if block_resp.get("result", {}).get("code") != 0:
                        return block_resp
                    block_id += 1
            complete_resp = await ws.receive()
            complete_resp = json.loads(complete_resp.data)
            return complete_resp


async def download_file(
    url: str,
    session: str,
    file_hash: str,
    range_header: str = None
):
    """
    下载文件，按协议 yield (offset, binary_data)。
    offset = BlockID * BLOCK_SIZE
    BlockID == 0xffffffff 时结束。
    """
    api_address = f"{url}/api/v1/file/{file_hash}"
    logger.debug(f"Called API download_file with url: {api_address}")
    headers = {
        "Authorization": f"Bearer {session}"
    }
    if range_header:
        headers["Range"] = range_header
    async with aiohttp.ClientSession() as client:
        async with client.get(api_address, headers=headers) as resp:
            while True:
                block_id_bytes = await resp.content.read(4)
                if not block_id_bytes or len(block_id_bytes) < 4:
                    logger.debug("No more block_id bytes, breaking.")
                    break
                block_id = struct.unpack('<I', block_id_bytes)[0]
                length_bytes = await resp.content.read(4)
                if not length_bytes or len(length_bytes) < 4:
                    logger.debug("No more length bytes, breaking.")
                    break
                length = struct.unpack('<I', length_bytes)[0]
                data = await resp.content.read(length)
                if block_id == 0xffffffff:
                    logger.debug("Received end block, stopping download.")
                    break
                offset = block_id * BLOCK_SIZE
                logger.debug(f"Yield block: id={block_id}, offset={offset}, length={length}")
                yield offset, data
