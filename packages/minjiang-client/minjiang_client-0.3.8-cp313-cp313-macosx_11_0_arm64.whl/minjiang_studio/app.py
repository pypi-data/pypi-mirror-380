#!/usr/bin/python3
# -*- coding: utf8 -*-
# Copyright (c) 2025 ZWDX, Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os.path
import time

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from minjiang_client.com.organization import *
from minjiang_client.com.organization import add_user_to_org, get_all_org_users
from minjiang_client.com.oss import *
from minjiang_client.com.user import get_user_info, get_user_list
from minjiang_studio.function.oss import api_get_global, api_get_oss_config
from minjiang_studio.function.utils import api_get_parameter_description
from minjiang_studio.utils.resp import Resp
from minjiang_studio.utils.wrapper import exception_wrapper
from minjiang_studio.function.log import *
from minjiang_studio.function.client import *
from minjiang_studio.function.group import *
from minjiang_studio.function.task import *
from minjiang_studio.function.plugin import *
from minjiang_studio.function.exp import *
from minjiang_studio.function.device import *
from minjiang_studio.function.plot import *
from minjiang_studio.function.download import *
from minjiang_client.utils.local import get_cache_dir

app = FastAPI()
working_path = os.path.dirname(__file__)
cache_abs_path = get_cache_dir()


@app.get("/api/get_client_status")
@exception_wrapper
def get_client_status():
    resp_config = api_get_local_config()
    resp = Resp(resp_config)
    return resp()


@app.post("/api/set_client_status")
@exception_wrapper
def set_client_status(local_config: LocalConfig):
    resp_config = api_set_local_config(local_config)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/login_config")
@exception_wrapper
def login_config():
    resp_config = api_login_config()
    resp = Resp(resp_config)
    return resp()


@app.get("/api/list_groups")
@exception_wrapper
def list_groups(page: int = 1, per_page: int = 10, org_id: int = None, show_hidden: bool = True):
    resp_config = api_list_groups(page, per_page, org_id, show_hidden)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_group_detail")
@exception_wrapper
def get_group_detail(device_group_name: str):
    resp_config = api_get_group_detail(device_group_name)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/create_group")
@exception_wrapper
def create_group(group_desc: GroupDescription):
    resp_config = api_create_group(group_desc)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/set_group_hidden")
@exception_wrapper
def set_group_hidden(group_hidden: GroupHidden):
    resp_config = api_set_group_hidden(group_hidden)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/create_space")
@exception_wrapper
def create_space(space_desc: SpaceDescription):
    resp_config = api_create_space(space_desc)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/list_spaces")
@exception_wrapper
def list_spaces(device_group_name: str, page: int = 1, per_page: int = 10, show_hidden: bool = False):
    resp_config = api_list_spaces(device_group_name, page, per_page, show_hidden)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/hide_space")
@exception_wrapper
def hide_space(device_group_name: str, space_id: int):
    resp_config = api_hide_space(device_group_name, space_id)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/show_space")
@exception_wrapper
def show_space(device_group_name: str, space_id: int):
    resp_config = api_show_space(device_group_name, space_id)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/submit_space_parameter")
@exception_wrapper
def submit_space_parameter(space_param_submit: SpaceParameterSubmit):
    resp_config = api_submit_space_parameter(space_param_submit)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/list_tasks")
@exception_wrapper
def list_tasks(device_group_name: str, status: str = None, page: int = 1, per_page: int = 10,
               show_hidden: bool = False, time_range: str = None, task_id: int = None):
    resp_config = api_list_tasks(device_group_name, status, page, per_page, show_hidden, time_range, task_id)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/list_exps")
@exception_wrapper
def list_exps(device_group_name: str, task_id: int = None, page: int = 1, per_page: int = 10):
    resp_config = api_exp_list(device_group_name, task_id, page, per_page)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/exp_fitting_img")
@exception_wrapper
def exp_fitting_img(group_name: str, exp_ids: str, create_timestamps: str):
    resp_config = api_exp_fitting_img(group_name, exp_ids, create_timestamps)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/create_task")
@exception_wrapper
def create_task(task_desc: CreateTask):
    resp_config = api_create_task(task_desc.device_group_name, task_desc.space_name,
                                  task_desc.title, task_desc.description)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_exp_template_groups")
@exception_wrapper
def get_exp_template_groups():
    resp_config = api_get_exp_template_groups()
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_exp_templates")
@exception_wrapper
def get_exp_templates(template_group_name: str):
    resp_config = api_get_exp_templates(template_group_name)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_exp_template_setup")
@exception_wrapper
def get_exp_template_setup(template_group_name: str, template_name: str, group_name: str, space_id: int):
    resp_config = api_get_exp_template_setup(template_group_name, template_name, group_name, space_id)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/generate_exp")
@exception_wrapper
def generate_exp(generate_exp: GenerateExp):
    resp_config = api_generate_exp(generate_exp.group_name, generate_exp.space_id, generate_exp.task_id,
                                   generate_exp.template_group, generate_exp.template_name, generate_exp.setting)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_fitter_groups")
@exception_wrapper
def get_fitter_groups():
    resp_config = api_get_fitter_groups()
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_fitters")
@exception_wrapper
def get_fitters(fitter_group_name: str):
    resp_config = api_get_fitters(fitter_group_name)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_fitter_setup")
@exception_wrapper
def get_fitter_setup(fitter_group_name: str, fitter_name: str, group_name: str, space_id: int):
    resp_config = api_get_fitter_setup(fitter_group_name, fitter_name, group_name, space_id)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/fitter_fit")
@exception_wrapper
def fitter_fit(fitter_fit: FitterFit):
    resp_config = api_fitter_fit(fitter_fit.fitter_group, fitter_fit.fitter_name, fitter_fit.group_name,
                                 fitter_fit.space_id, fitter_fit.setting)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/submit_fitting_result")
@exception_wrapper
def submit_fitting_result(submit_fit: SubmitFittingResult):
    resp_config = api_submit_fitting_result(
        submit_fit.group_name, submit_fit.space_id, submit_fit.task_id, submit_fit.exp_id, submit_fit.img_file,
        submit_fit.table_file, submit_fit.space_parameters, submit_fit.update_space_parameters
    )
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_cloud_fitting_result")
@exception_wrapper
def get_cloud_fitting_result(device_group_name: str, space_id: int, exp_id: int):
    resp_config = api_get_cloud_fitting_result(device_group_name, space_id, exp_id)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/open_cloud_plotter")
async def open_cloud_plotter(device_group_name: str, exp_id: int):
    api_open_cloud_plotter(device_group_name, exp_id)
    resp = Resp("ok")
    return resp()


@app.get("/api/get_exp_detail")
@exception_wrapper
def get_exp_detail(device_group_name: str, exp_id: int):
    resp_config = api_load_exp(device_group_name, exp_id)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_exp_attachment")
@exception_wrapper
def get_exp_attachment(device_group_name: str, exp_id: int):
    resp_config = api_get_exp_attachment(device_group_name, exp_id)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/preview_exp_attachment")
@exception_wrapper
def preview_exp_attachment(absolute_path: str, in_zip_path: str = None):
    resp_config = api_preview_exp_attachment(absolute_path, in_zip_path)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_exp_status")
@exception_wrapper
def get_exp_status(device_group_name: str, exp_id: int):
    resp_config = api_get_exp_status(device_group_name, exp_id)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/get_parameter_by_tree")
@exception_wrapper
def get_parameter_by_tree(parameter: GetParameterByTree):
    resp_config = api_get_parameter_by_tree(parameter.device_group_name, parameter.space_id, parameter.parent_tree,
                                            parameter.version)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_history_space_parameter")
@exception_wrapper
def get_history_space_parameter(device_group_name: str, space_id: int, version: str):
    resp_config = api_get_history_space_parameter(device_group_name, space_id, version)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_parameter_history")
@exception_wrapper
def get_parameter_history(device_group_name: str, space_id: int, key: str = None, page: int = 1, per_page: int = 10):
    resp_config = api_get_parameter_history(device_group_name, space_id, key, page, per_page)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/remove_space_parameter")
@exception_wrapper
def remove_space_parameter(get_parameter: GetParameter):
    resp_config = api_remove_space_parameter(get_parameter.device_group_name,
                                             get_parameter.space_id, get_parameter.key)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/create_plugin")
@exception_wrapper
def create_plugin(create_plugin: CreatePlugin):
    resp_config = api_create_plugin(create_plugin)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/modify_plugin")
@exception_wrapper
def modify_plugin(modify_plugin: ModifyPlugin):
    resp_config = api_modify_plugin(modify_plugin)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_plugin_config")
@exception_wrapper
def plugin_config(plugin_id: int):
    resp_config = api_get_plugin_config(plugin_id)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/set_plugin_global_visibility")
@exception_wrapper
def set_plugin_global_visibility(plugin_visible: PluginVisible):
    resp_config = api_set_plugin_global_visibility(plugin_visible)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/list_plugins")
@exception_wrapper
def list_plugins(page: int = 1, per_page: int = 10):
    resp_config = api_list_plugins(page, per_page)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/list_local_plugins")
@exception_wrapper
def list_local_plugins():
    resp_config = api_list_local_plugins()
    resp = Resp(resp_config)
    return resp()


@app.get("/api/list_plugin_versions")
@exception_wrapper
def list_plugin_versions(plugin_id: int, page: int = 1, per_page: int = 10):
    resp_config = api_list_plugin_versions(plugin_id, page, per_page)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/install_plugin")
@exception_wrapper
def install_plugin(plugin_id: int):
    resp_config = api_install_plugin(plugin_id)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/install_plugin_via_file")
async def install_plugin_via_file(plugin_file: UploadFile = File(...)):
    file_path = None
    try:
        file_path = os.path.join(get_cache_dir(), "upload_" + str(time.time()) + "_" + plugin_file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await plugin_file.read())
        resp_config = api_install_plugin_via_file(file_path)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Cannot remove file {file_path}:", e)
        resp = Resp(resp_config)
        return resp()
    except Exception as e:
        resp = Resp({}, msg=f"Upload plugin failed: {e}", status=1)
        try:
            os.remove(file_path)
        except Exception:
            pass
        return resp()


@app.get("/api/uninstall_plugin")
@exception_wrapper
def uninstall_plugin(plugin_name: str):
    resp_config = api_uninstall_plugin(plugin_name)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/package_plugin_version")
@exception_wrapper
def package_plugin_version(plugin_dir: PluginDir):
    resp_config = api_package_plugin_version(plugin_dir.plugin_dir)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/submit_plugin_version")
async def submit_plugin_version(plugin_id=Form(...), plugin_file=File(...)):
    file_path = None
    try:
        if isinstance(plugin_id, str):
            if plugin_id.isdigit():
                plugin_id = int(plugin_id)
            else:
                raise TypeError("Plugin id must be an integer")
        file_path = os.path.join(get_cache_dir(), "upload_" + str(time.time()) + "_" + plugin_file.filename)
        with open(file_path, "wb") as buffer:
            buffer.write(await plugin_file.read())
        resp_config = await api_submit_plugin_version(plugin_id, file_path)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Cannot remove file {file_path}:", e)
        resp = Resp(resp_config)
        return resp()
    except Exception as e:
        resp = Resp({}, msg=f"Upload plugin failed: {e}", status=1)
        try:
            os.remove(file_path)
        except Exception:
            pass
        return resp()


@app.get("/api/exp_edit_get_entities")
@exception_wrapper
def exp_edit_get_entities(device_group_name: str, space_id: int):
    resp_config = api_exp_edit_get_entities(device_group_name, space_id)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/exp_edit_get_gates")
@exception_wrapper
def exp_edit_get_gates(device_group_name: str, space_id: int):
    resp_config = api_exp_edit_get_gates(device_group_name, space_id)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/exp_edit_get_script_templates")
@exception_wrapper
def exp_edit_get_script_templates():
    resp_config = api_exp_edit_get_script_templates()
    resp = Resp(resp_config)
    return resp()


@app.get("/api/exp_edit_get_wave_functions")
@exception_wrapper
def exp_edit_get_wave_functions():
    resp_config = api_exp_edit_get_wave_functions()
    resp = Resp(resp_config)
    return resp()


@app.get("/api/exp_edit_get_wave_compiler_setup")
@exception_wrapper
def exp_edit_get_wave_compiler_setup():
    resp_config = api_exp_edit_get_wave_compiler_setup()
    resp = Resp(resp_config)
    return resp()


@app.get("/api/exp_edit_get_default_gates")
@exception_wrapper
def exp_edit_get_default_gates():
    resp_config = api_exp_edit_get_default_gates()
    resp = Resp(resp_config)
    return resp()


@app.get("/api/exp_edit_get_gate_default_waveforms")
@exception_wrapper
def exp_edit_get_gate_default_waveforms(device_group_name: str, space_id: int, entities: str, gate_name: str):
    resp_config = api_exp_edit_get_gate_default_waveforms(device_group_name, space_id, entities, gate_name)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/exp_edit_get_wave_sequence")
@exception_wrapper
def exp_edit_get_wave_sequence(get_sequence: GetSequence):
    resp_config = api_exp_edit_get_wave_sequence(get_sequence.device_group_name, get_sequence.space_id,
                                                 get_sequence.waves, get_sequence.use_carrier)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/exp_edit_get_full_wave_sequence")
@exception_wrapper
def exp_edit_get_full_wave_sequence(submit_exp: SubmitExperiment):
    resp_config = api_exp_edit_get_full_wave_sequence(submit_exp)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/exp_edit_get_exp_options")
@exception_wrapper
def exp_edit_get_exp_options():
    resp_config = api_exp_edit_get_exp_options()
    resp = Resp(resp_config)
    return resp()


@app.post("/api/exp_edit_submit_experiment")
@exception_wrapper
def exp_edit_submit_experiment(submit_exp: SubmitExperiment):
    resp_config = api_exp_edit_submit_experiment(submit_exp)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/terminate_exp")
@exception_wrapper
def terminate_exp(exp_id: int):
    data = api_terminate_exp(exp_id)
    resp = Resp(data)
    return resp()


@app.get("/api/scan_devices")
@exception_wrapper
def scan_devices(group_name: str):
    data = api_scan_devices(group_name)
    resp = Resp(data)
    return resp()


@app.post("/api/add_device")
@exception_wrapper
def add_device(device_data: DeviceData):
    data = api_add_device(device_data)
    resp = Resp(data)
    return resp()


@app.post("/api/delete_device")
@exception_wrapper
def delete_device(device_data: DeviceData):
    data = api_delete_device(device_data.sn, device_data.group_name)
    resp = Resp(data)
    return resp()


@app.post("/api/update_device")
@exception_wrapper
def update_device(device_data: DeviceData):
    data = api_update_device(device_data.sn, device_data.parameters, device_data.group_name)
    resp = Resp(data)
    return resp()


@app.post("/api/select_devices")
@exception_wrapper
def select_devices(device_data: DeviceData):
    data = api_select_devices(device_data.group_name, device_data.sn_list)
    resp = Resp(data)
    return resp()


@app.get("/api/get_device_parameters")
@exception_wrapper
def get_device_parameters(model: str, group_name: str):
    data = api_get_device_parameters(model, group_name)
    resp = Resp(data)
    return resp()


@app.get("/api/query_devices_by_group")
@exception_wrapper
def query_devices_by_group(group_name: str):
    data = api_query_devices_by_group(group_name)
    resp = Resp(data)
    return resp()


@app.get("/api/query_devices_by_sn")
@exception_wrapper
def query_devices_by_sn(sn: str, group_name: str):
    data = api_query_devices_by_sn(sn, group_name)
    resp = Resp(data)
    return resp()


@app.get("/api/query_devices_by_sn")
@exception_wrapper
def query_devices_by_sn(sn: str, group_name: str):
    data = api_query_devices_by_sn(sn, group_name)
    resp = Resp(data)
    return resp()


@app.get("/api/query_host_client_status")
@exception_wrapper
def query_host_client_status(group_name: str):
    data = api_query_host_client_status(group_name)
    resp = Resp(data)
    return resp()


@app.get("/api/get_mapping_by_group")
@exception_wrapper
def get_mapping_by_group(group_name: str):
    data = api_get_mapping_by_group(group_name)
    resp = Resp(data)
    return resp()


@app.get("/api/switch_device_snapshot")
@exception_wrapper
def switch_device_snapshot(group_name: str, sn: str, snapshot: str):
    data = api_switch_device_snapshot(group_name, sn, snapshot)
    resp = Resp(data)
    return resp()


@app.get("/api/get_device_snapshot_status")
@exception_wrapper
def get_device_snapshot_status(group_name: str, sn: str):
    data = api_get_device_snapshot_status(group_name, sn)
    resp = Resp(data)
    return resp()


@app.get("/api/get_device_snapshot")
@exception_wrapper
def get_device_snapshot(group_name: str, sn: str):
    data = api_get_device_snapshot(group_name, sn)
    resp = Resp(data)
    return resp()


@app.get("/api/get_space_initializer_list")
@exception_wrapper
def get_space_initializer_list():
    data = api_get_space_initializer_list()
    resp = Resp(data)
    return resp()


@app.get("/api/get_space_initializer_setup")
@exception_wrapper
def get_space_initializer_setup(initializer_name: str):
    resp_config = api_get_space_initializer_setup(initializer_name)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/space_initializer_preview")
@exception_wrapper
def space_initializer_preview(initializer_data: SpaceInitializer):
    resp_config = api_space_initializer_preview(initializer_data)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/space_initializer_submit")
@exception_wrapper
def space_initializer_submit(initializer_data: SpaceInitializer):
    resp_config = api_space_initializer_submit(initializer_data)
    resp = Resp(resp_config)
    return resp()


@app.post("/api/exp_query_plot")
@exception_wrapper
def exp_query_plot(plot_query: PlotQuery):
    resp_config = api_exp_query_plot(
        plot_query.device_group_name,
        plot_query.space_id,
        plot_query.exp_id,
        plot_query.fields,
        plot_query.latest_step
    )
    resp = Resp(resp_config)
    return resp()


@app.get("/api/exp_debug_plot")
@exception_wrapper
def exp_debug_plot():
    resp_config = api_exp_plot_debug()
    resp = Resp(resp_config)
    return resp()


@app.get("/api/list_sessions")
@exception_wrapper
def list_sessions(device_group_name: str, page: int = 1, per_page: int = 10):
    data = api_get_cali_session_list(device_group_name, page, per_page)
    resp = Resp(data)
    return resp()


@app.get("/api/search_space_parameters")
@exception_wrapper
def search_space_parameters(device_group_name: str, space_id: int, search_word: str):
    data = api_search_space_parameters(device_group_name, space_id, search_word)
    resp = Resp(data)
    return resp()


@app.get("/api/get_node_log")
@exception_wrapper
def get_node_log(node_id: int, session_id: int, last_record_id: Optional[int] = None):
    data = api_get_node_log(node_id, session_id, last_record_id)
    resp = Resp(data)
    return resp()


@app.get("/api/get_session_entities")
@exception_wrapper
def get_session_entities(device_group_name: str, space_id: int):
    data = api_get_session_entities(device_group_name, space_id)
    resp = Resp(data)
    return resp()


@app.get("/api/get_entity_log")
@exception_wrapper
def get_entity_result_log(session_id: int, entity: str, last_record_id: Optional[int] = None):
    data = api_get_entity_log(session_id, entity, last_record_id)
    resp = Resp(data)
    return resp()


@app.get("/api/get_session_json")
@exception_wrapper
def get_session_json(session_id: int, org_id: int):
    data = api_get_session_json(session_id, org_id)
    resp = Resp(data)
    return resp()


@app.get("/api/get_session_nodes")
@exception_wrapper
def get_session_nodes(session_id: int):
    data = api_get_session_nodes(session_id)
    resp = Resp(data)
    return resp()


@app.get("/api/get_session_info")
@exception_wrapper
def get_session_info(session_id: int):
    data = api_get_session_info(session_id)
    resp = Resp(data)
    return resp()


@app.get("/api/download_exp_file")
@exception_wrapper
def download_exp_file(group_name: str, exp_id: int):
    data = api_download_exp(group_name, exp_id)
    resp = Resp(data)
    return resp()


@app.get("/api/download_space_parameter_file")
@exception_wrapper
def download_space_parameter_file(group_name: str, space_id: int, version: int = None):
    if version is None:
        version = int(time.time())
    data = api_download_space_parameter_file(group_name, space_id, version)
    resp = Resp(data)
    return resp()


@app.get("/api/global_search")
@exception_wrapper
def global_search(keyword: str):
    data = api_global_search(keyword)
    resp = Resp(data)
    return resp()


@app.get("/api/space_abstract")
@exception_wrapper
def space_abstract(device_group_name: str, space_id: int, entity_type: str = None):
    data = api_space_abstract(device_group_name, space_id, entity_type)
    resp = Resp(data)
    return resp()


@app.get("/api/get_parameter_description")
@exception_wrapper
def get_parameter_description(full_key_list: str, language: str = "cn"):
    data = api_get_parameter_description(full_key_list.strip().split(","), language=language)
    resp = Resp(data)
    return resp()


@app.post("/api/generate_and_submit_experiment")
@exception_wrapper
def generate_and_submit_experiment(generate_exp: GenerateExp):
    resp_config = create_and_submit_exp(generate_exp.group_name, generate_exp.space_id, generate_exp.task_id,
                                        generate_exp.template_group, generate_exp.template_name, generate_exp.setting)
    resp = Resp(resp_config)
    return resp()


@app.get("/api/get_user_list")
@exception_wrapper
def user_list():
    data = get_user_list()
    resp = Resp(data)
    return resp()


@app.get("/api/get_user_info")
@exception_wrapper
def user_info():
    data = get_user_info()
    resp = Resp(data)
    return resp()


@app.get("/api/get_org_info")
@exception_wrapper
def org_info(org_id: int):
    data = get_org_info(org_id)
    resp = Resp(data)
    return resp()


@app.post("/api/create_organization")
@exception_wrapper
def create_org(org_data: OrgData):
    data = create_organization(org_data.name, org_data.admin_ids, org_data.user_ids)
    resp = Resp(data)
    return resp()


@app.get("/api/get_org_list")
@exception_wrapper
def org_list():
    data = get_org_list()
    resp = Resp(data)
    return resp()


@app.get("/api/get_admin_org_list")
@exception_wrapper
def admin_org_list():
    data = get_admin_org_list()
    resp = Resp(data)
    return resp()


@app.get("/api/get_all_org_users")
@exception_wrapper
def all_org_users():
    data = get_all_org_users()
    resp = Resp(data)
    return resp()


@app.get("/api/get_org_users")
@exception_wrapper
def org_users(organization_id: int):
    data = get_org_users(organization_id)
    resp = Resp(data)
    return resp()


@app.get("/api/get_org_devices")
@exception_wrapper
def org_devices(organization_id: int):
    data = get_org_devices(organization_id)
    resp = Resp(data)
    return resp()


@app.post("/api/add_org_user")
@exception_wrapper
def add_organization_user(org_user_query: AddOrgUserQuery):
    data = add_org_user(org_user_query.org_id, org_user_query.user_name, org_user_query.org_role)
    resp = Resp(data)
    return resp()


@app.post("/api/delete_org_user")
@exception_wrapper
def delete_organization_user(org_user_query: OrgUserQuery):
    data = delete_org_user(org_user_query.org_id, org_user_query.user_id)
    resp = Resp(data)
    return resp()


@app.post("/api/modify_org_user_role")
@exception_wrapper
def modify_user_role(org_user_query: OrgUserQuery):
    data = modify_org_user_role(org_user_query.org_id, org_user_query.user_id, org_user_query.org_role)
    resp = Resp(data)
    return resp()


@app.post("/api/modify_user_device_group_permission")
@exception_wrapper
def modify_group_permission(user_device_permission: UserDevicePermission):
    data = modify_user_device_group_permission(user_device_permission.org_id, user_device_permission.user_id,
                                               user_device_permission.device_group_id,
                                               user_device_permission.permission)
    resp = Resp(data)
    return resp()


@app.post("/api/batch_modify_permission_by_user")
@exception_wrapper
def batch_modify_by_user(batch_user_permission: BatchUserPermission):
    data = batch_modify_permission_by_user(batch_user_permission.org_id, batch_user_permission.user_id,
                                           batch_user_permission.permission)
    resp = Resp(data)
    return resp()


@app.post("/api/batch_modify_permission_by_device")
@exception_wrapper
def batch_modify_by_device(batch_device_permission: BatchDevicePermission):
    data = batch_modify_permission_by_device(batch_device_permission.org_id, batch_device_permission.device_group_id,
                                             batch_device_permission.permission)
    resp = Resp(data)
    return resp()


@app.get("/api/get_device_list_by_user")
@exception_wrapper
def device_list_by_user(organization_id: int, user_id: int):
    data = get_device_list_by_user(organization_id, user_id)
    resp = Resp(data)
    return resp()


@app.get("/api/get_user_list_by_device")
@exception_wrapper
def user_list_by_device(organization_id: int, device_group_id: int):
    data = get_user_list_by_device(organization_id, device_group_id)
    resp = Resp(data)
    return resp()


@app.post("/api/add_user")
@exception_wrapper
def add_user_org(user_data: UserData):
    data = add_user_to_org(user_data.user_name, user_data.org_id, user_data.org_role)
    resp = Resp(data)
    return resp()


@app.get("/api/get_global_oss")
@exception_wrapper
def get_global_oss():
    data = api_get_global()
    resp = Resp(data)
    return resp()


@app.get("/api/get_org_oss")
@exception_wrapper
def get_org_oss(organization_id: int):
    data = api_get_oss_config(organization_id)
    resp = Resp(data)
    return resp()


@app.post("/api/set_oss_auth")
@exception_wrapper
def set_oss(oss_data: OSSData):
    data = set_oss_auth(
        if_global=oss_data.if_global,
        disabled=oss_data.disabled,
        organization_id=oss_data.organization_id,
        auth_text=oss_data.auth_text,
    )
    resp = Resp(data)
    return resp()


@app.get("/cache/{full_path:path}")
async def catch_cache(full_path):
    global cache_abs_path

    if get_cache_dir() != cache_abs_path:
        cache_abs_path = get_cache_dir()
        app.mount("/", StaticFiles(directory=cache_abs_path, check_dir=True, html=False), name="cache")
        print("Mount cache dir:", cache_abs_path)

    cache_file = os.path.join(cache_abs_path, full_path)
    if os.path.isfile(cache_file):
        return FileResponse(cache_file)

    return FileResponse(os.path.dirname(__file__) + "/static/index.html")


@app.get("/{full_path:path}")
async def catch_all(full_path):
    static_file = os.path.join(os.path.dirname(__file__), "static", full_path)
    if os.path.isfile(static_file):
        return FileResponse(static_file)

    return FileResponse(os.path.dirname(__file__) + "/static/index.html")


static_abs_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "static"))
app.mount("/", StaticFiles(directory=static_abs_path, html=True), name="static")

if cache_abs_path:
    app.mount("/", StaticFiles(directory=cache_abs_path, check_dir=True, html=False), name="cache")
    print("Mount cache dir:", cache_abs_path)
