import asyncio

import StealthIM
from StealthIM import User
from StealthIM.apis.group import GroupInfoResult, GroupPublicInfoResult, InviteGroupResult, \
    GroupMemberType, SetMemberRoleResult, KickMemberResult, ChangeGroupNameResult, ChangeGroupPasswordResult, \
    JoinGroupResult, CreateGroupResult
from StealthIM.apis.message import SendMessageResult


class Group:
    def __init__(self, user: User, group_id: int):
        """
        Initialize a Group instance.
        :param user: User object
        :param group_id: Group ID
        """
        self.user = user
        self.group_id = group_id

    @classmethod
    async def create(cls, user: User, group_name: str) -> CreateGroupResult:
        """
        Create a new group.
        :param user: User object
        :param group_name: Name of the group
        :return: CreateGroupResult

        Raises:
            RuntimeError: If the request failed.
        """
        return await StealthIM.apis.group.create_group(user.server.url, user.session, group_name)

    async def join(self, password: str) -> JoinGroupResult:
        """
        Join a group.
        :param password: Group password
        :return: JoinGroupResult

        Raises:
            RuntimeError: If the request failed.
        """
        return await StealthIM.apis.group.join_group(self.user.server.url, self.user.session, self.group_id, password)

    async def get_members(self) -> GroupInfoResult:
        """
        Get the list of group members.
        :return: GroupInfoResult
        """
        return await StealthIM.apis.group.get_group_info(self.user.server.url, self.user.session, self.group_id)

    async def get_info(self) -> GroupPublicInfoResult:
        """
        Get public information of the group.
        :return: GroupPublicInfoResult
        """
        return await StealthIM.apis.group.get_group_public_info(self.user.server.url, self.user.session, self.group_id)

    async def invite(self, username: str) -> InviteGroupResult:
        """
        Invite a user to the group.
        :param username: Username to invite
        :return: InviteGroupResult

        Raises:
            RuntimeError: If the request failed.
        """
        return await StealthIM.apis.group.invite_group(self.user.server.url, self.user.session, self.group_id, username)

    async def set_member_role(self, username: str, role: GroupMemberType) -> SetMemberRoleResult:
        """
        Set the role of a group member.
        :param username: Username
        :param role: Role type
        :return: SetMemberRoleResult

        Raises:
            RuntimeError: If the request failed.
        """
        return await StealthIM.apis.group.set_user_role(self.user.server.url, self.user.session, self.group_id,
                                                        username, role)

    async def kick(self, username: str) -> KickMemberResult:
        """
        Remove a member from the group.
        :param username: Username
        :return: KickMemberResult

        Raises:
            RuntimeError: If the request failed.
        """
        return await StealthIM.apis.group.kick_user(self.user.server.url, self.user.session, self.group_id, username)

    async def change_name(self, new_name: str) -> ChangeGroupNameResult:
        """
        Change the group name.
        :param new_name: New group name
        :return: ChangeGroupNameResult

        Raises:
            RuntimeError: If the request failed.
        """
        return await StealthIM.apis.group.change_group_name(self.user.server.url, self.user.session, self.group_id,
                                                            new_name)

    async def change_password(self, new_password: str) -> ChangeGroupPasswordResult:
        """
        Change the group password.
        :param new_password: New password
        :return: ChangeGroupPasswordResult

        Raises:
            RuntimeError: If the request failed.
        """
        return await StealthIM.apis.group.change_group_password(self.user.server.url, self.user.session, self.group_id,
                                                                new_password)

    async def send_text(self, message: str) -> SendMessageResult:
        """
        Send a text message to the group.
        :param message: Message content
        :return: SendMessageResult
        """
        return await StealthIM.apis.message.send_message(
            self.user.server.url,
            self.user.session,
            self.group_id,
            message,
            StealthIM.apis.message.MessageType.Text
        )

    async def receive_text(self, from_id: int = 0, sync: bool = True, limit: int = 128):
        """
        Receive text messages from the group.
        :param from_id: Start message ID
        :param sync: Whether to sync
        :param limit: Maximum number of messages
        :yield: Message data
        """
        gen = StealthIM.apis.message.get_message(
            self.user.server.url,
            self.user.session,
            self.group_id,
            from_id,
            sync,
            limit
        )
        async for data in gen:
            yield data

    async def receive_latest_text(self, limit: int = 128):
        async for data in self.receive_text(from_id=0, sync=False, limit=limit):
            yield data

    async def receive_new_text(self, limit: int = 128):
        async for data in self.receive_text(from_id=-1, limit=limit):
            yield data

    async def recall_message(self, message_id: int):
        return await StealthIM.apis.message.recall_message(self.user.server.url, self.user.session, self.group_id, message_id)

    async def get_file_info(self, file_hash: str):
        """
        Get file information.
        :param file_hash: File hash value
        :return: File information result
        """
        return await StealthIM.apis.file.get_file_info(self.user.server.url, self.user.session, file_hash)

    async def send_file(self, filename: str, file_path: str):
        """
        Upload a file to the group.
        :param filename: File name
        :param file_path: File path
        :return: Upload result
        """
        return await StealthIM.apis.file.upload_file(
            self.user.server.url,
            self.user.session,
            self.group_id,
            filename,
            file_path
        )

    async def download_file(self, file_hash: str, output_path: str, threads: int = 1):
        """
        Download a file from the group using single or multi-thread (async) mode.
        :param file_hash: File hash value
        :param output_path: Path to save the file
        :param threads: Number of concurrent download tasks
        """
        file_info = await self.get_file_info(file_hash)
        if not file_info or not file_info.size:
            raise RuntimeError("Failed to get file size.")
        file_size = file_info.size

        async def fetch_chunk(range_tuple):
            start, end = range_tuple
            range_header = f"bytes={start}-{end}"
            results = []
            async for offset, data in StealthIM.apis.file.download_file(
                self.user.server.url,
                self.user.session,
                file_hash,
                range_header=range_header
            ):
                results.append((offset, data))
            return results

        if threads == 1:
            # Single thread: download all blocks and write by offset
            with open(output_path, 'wb') as f:
                async for offset, data in StealthIM.apis.file.download_file(
                    self.user.server.url,
                    self.user.session,
                    file_hash
                ):
                    f.seek(offset)
                    f.write(data)
        else:
            # Multi-thread: download chunks concurrently
            chunk_size = file_size // threads
            chunk_ranges = []
            for i in range(threads):
                start = i * chunk_size
                end = (i + 1) * chunk_size - 1 if i < threads - 1 else file_size - 1
                chunk_ranges.append((start, end))
            tasks = [fetch_chunk(r) for r in chunk_ranges]
            results = await asyncio.gather(*tasks)
            with open(output_path, 'wb') as f:
                for chunk in results:
                    for offset, data in chunk:
                        f.seek(offset)
                        f.write(data)

    async def download_files(self, file_hash_list, filename_list, output_dir, max_concurrent=1, threads_per_file=1):
        """
        批量下载多个文件，支持顺序/并行下载。
        :param file_hash_list: List of file_hash
        :param filename_list: List of output filenames
        :param output_dir: Directory to save files
        :param max_concurrent: 最大并发下载文件数
        :param threads_per_file: 单文件下载线程数
        :return: List of (file_hash, output_path, success, error)
        """
        import os
        results = []
        semaphore = asyncio.Semaphore(max_concurrent)

        async def download_one(file_hash: str, filename: str):
            output_path = os.path.join(output_dir, filename)
            try:
                async with semaphore:
                    await self.download_file(file_hash, output_path, threads=threads_per_file)
                results.append((file_hash, output_path, True, None))
            except Exception as e:
                results.append((file_hash, output_path, False, str(e)))

        tasks = [download_one(fh, fn) for fh, fn in zip(file_hash_list, filename_list)]
        await asyncio.gather(*tasks)
        return results
