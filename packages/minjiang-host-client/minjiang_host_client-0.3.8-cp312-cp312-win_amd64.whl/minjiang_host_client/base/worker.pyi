from _typeshed import Incomplete
from minjiang_host_client.base.channel import Channel as Channel
from minjiang_host_client.utils.terminate import write_terminate_signal as write_terminate_signal
from multiprocessing import Process
from typing import Any

class Worker:
    name: str
    group_name: str
    input_channel: Channel
    output_channel: Channel
    running: Incomplete
    exp_id: int | None
    direct_link: bool
    direct_exp_id: int | None
    def __init__(self, name: str, group_name: str, input_channel: Channel = None, output_channel: Channel = None) -> None: ...
    def process_data(self, data: Any = None) -> bytes: ...
    def print(self, *args, sep: str = ' ', end: str = '\n', file=None) -> None: ...
    def run(self) -> None: ...
    def write_data(self, data: bytes): ...
    def make_process(self) -> Process: ...
