from minjiang_client.utils.task_status import *
import abc
from _typeshed import Incomplete
from abc import ABC, abstractmethod
from minjiang_client.auto_cali.dag_definition import ALL_SUCCESS as ALL_SUCCESS, ANY_SUCCESS as ANY_SUCCESS, DAGDefinition as DAGDefinition, IGNORE as IGNORE, NodeConfig as NodeConfig
from minjiang_client.auto_cali.utils import load_json_file_data as load_json_file_data, upload_auto_cali_json as upload_auto_cali_json
from minjiang_client.com.log import add_cali_execution_log as add_cali_execution_log, add_cali_node_status_log as add_cali_node_status_log
from minjiang_client.com.minio import get_minio_client as get_minio_client
from minjiang_client.com.oss import add_resource as add_resource
from minjiang_client.com.task import create_cali_session as create_cali_session, create_node as create_node, create_task as create_task, save_cali_result as save_cali_result, session_heartbeat as session_heartbeat, update_cali_session_status as update_cali_session_status
from minjiang_client.group.cloud_group import CloudGroup as CloudGroup
from typing import Callable

def node_run_wrapper(func: Callable): ...

class CalibrationNode(ABC, metaclass=abc.ABCMeta):
    result: Incomplete
    device_group_name: Incomplete
    space_name: Incomplete
    node_name: Incomplete
    task_id: Incomplete
    node_id: Incomplete
    session_id: Incomplete
    node_config: Incomplete
    cloud_group: Incomplete
    index: Incomplete
    def __init__(self, device_group_name: str, space_name: str, task_id: int, session_id: int, node_config: NodeConfig, index: int, cloud_group: CloudGroup = None, auto_create: bool = False) -> None: ...
    @abstractmethod
    def run(self, *args, **kwargs) -> str: ...
    def save_cali_result(self, entity: str, res: str): ...
    def save_execution_log(self, entity: str, res: str): ...

class CalibrationDAG:
    definition: Incomplete
    node_map: Incomplete
    graph: Incomplete
    task_id: int | None
    cloud_group: CloudGroup | None
    session_id: int | None
    json_resource_id: int | None
    def __init__(self) -> None: ...
    def run(self, device_group_name: str, task_id: int | None = None, space_name: str | None = None, json_resource_id: int = None, json_path: str = None, node_class_map: dict[str, Callable] = None): ...
