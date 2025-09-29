from upplib import *
from datetime import datetime, timezone, timedelta
from typing import Any, Optional, Union
from aliyun.log import LogClient, GetLogsRequest

from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdklts.v2.region.lts_region import LtsRegion
from huaweicloudsdklts.v2 import *
from upplib import *


def query_sls_logs(logstore_name: str = '',
                   minute: int = 600,
                   limit: int = 500,
                   query: str = '',
                   config_name: str = '',
                   country: str = '',
                   start_time: datetime | str | None = None,
                   end_time: datetime | str | None = None,
                   default_tz: str = '+07:00') -> None:
    if start_time is None and end_time is None:
        start_time, end_time = (t[0], t[1]) if (t := get_from_txt()) and t[0] is not None else (get_timestamp() - 60 * minute, get_timestamp())
    start_time = get_timestamp(start_time)
    end_time = get_timestamp(end_time)
    to_print_file(country, logstore_name, mode='w', file_path='', file_name=str(country) + '_' + logstore_name)
    to_print_file(f'start_time: {to_datetime_str(start_time, tz=default_tz)}')
    to_print_file(f'end_time  : {to_datetime_str(end_time, tz=default_tz)}')
    to_print_file(query)
    c = get_config_data(config_name)
    response = (LogClient(c.get('endpoint'), c.get('access_key_id'), c.get('access_key_secret'))
                .get_logs(GetLogsRequest(c.get('project_name'), logstore_name, start_time, end_time, line=limit, query=query)))
    to_print_file(f"共 {response.get_count()} 条日志:")
    logs = response.get_logs()
    for log in reversed(logs):
        to_print_file(get_log_msg(log.contents, default_tz=default_tz))
    to_print_file('END__END')


def search_lts_logs(keywords: str | None = '',
                    limit: int = 500,
                    minute: int = 600,
                    containerName: str = '',
                    appName: str = '',
                    config_name: str = '',
                    country: str = '',
                    default_tz: str = '-06:00',
                    start_time: datetime | str | None = None,
                    end_time: datetime | str | None = None,
                    ) -> None:
    if start_time is None and end_time is None:
        start_time, end_time = (t[0], t[1]) if (t := get_from_txt()) and t[0] is not None else (get_timestamp() - 60 * minute, get_timestamp())
    start_time = get_timestamp_ms(start_time)
    end_time = get_timestamp_ms(end_time)
    to_print_file(country, appName, mode='w', file_path='', file_name=str(country) + '_' + appName)
    to_print_file(f'start_time: {to_datetime_str(start_time, tz=default_tz)}')
    to_print_file(f'end_time  : {to_datetime_str(end_time, tz=default_tz)}')
    c = get_config_data(config_name)
    credentials = BasicCredentials(c['ak'], c['sk'])
    client = LtsClient.new_builder().with_credentials(credentials).with_region(LtsRegion.value_of(c['region'])).build()
    list_logs_req = ListLogsRequest()
    list_logs_req.log_group_id = c['group_id']
    list_logs_req.log_stream_id = c['stream_id']
    list_logs_req.body = QueryLtsLogParams(
        limit=limit,
        keywords=keywords,
        is_count=False,
        highlight=False,
        is_desc=True,
        labels={
            "containerName": containerName,
            "appName": appName
        },
        start_time=str(start_time),
        end_time=str(end_time)
    )
    to_print_file(keywords)
    to_print_file(list_logs_req.body)
    logs = client.list_logs(list_logs_req)
    front_content = None
    if logs and logs.logs:
        to_print_file(f"共找到 {len(logs.logs)} 条日志:")
        for log in logs.logs[::-1]:
            s1 = log.content.split('  ')
            this_time = to_datetime_str(s1[0], default_tz=default_tz)
            this_content = log.content[len(s1[0]) + 2:]
            if front_content != this_content and this_content:
                # 2025-09-28T19:38:41.146954-06:00 com.leo.digest.aop.ApiLogAspect - traceId: - (catTraceId:rcs-gateway-0a0f2154-488625-102) - ===>API GatewayFacadeImpl#gatewayRequest START
                SEP_S = '- traceId: -'
                if SEP_S in this_content:
                    s1 = this_content.split(SEP_S)
                    this_content = s1[0][-20:] + SEP_S + s1[1:]
                to_print_file(f'{this_time} {this_content}')
            front_content = this_content
    else:
        to_print_file("未查询到日志")
    to_print_file('END__END')


def get_rpc_context_seq_id_from_txt(file_name: str = 'a.txt') -> list[str] | None:
    # 找到所有包含 "Rpc-Context" 的行
    lines = to_list_from_txt(file_name)
    rpc_lines = [line.strip() for line in lines if line.strip().startswith('"Rpc-Context"')]
    seq_ids = set()
    if not rpc_lines:
        return None
    else:
        for i, line in enumerate(rpc_lines, start=1):
            # 提取 JSON 字符串（去掉外层引号）
            json_str = line.split(':', 1)[1].strip().strip('"')
            # 去掉内层的转义符
            clean_json_str = json_str.replace('\\"', '"')
            # 解析 JSON
            data_rpc_context = json.loads(clean_json_str)
            # 获取 seq_id
            seq_id = data_rpc_context.get('seq_id')
            if seq_id:
                seq_ids.add(seq_id)
    r_list = list(seq_ids)
    r_list.sort()
    return r_list


def get_trace_id_from_txt(file_name: str = 'a.txt',
                          str_pattern: str = r'catTraceId:([^)]+)'
                          ) -> list[str] | None:
    trace_id_lines = to_list_from_txt(file_name)
    trace_id_ids = set()
    if not trace_id_lines:
        return None
    else:
        for trace_id_line in trace_id_lines:
            trace_id_match = re.search(str_pattern, trace_id_line)
            trace_id = trace_id_match.group(1) if trace_id_match else None
            if trace_id:
                trace_id_ids.add(trace_id)
    r_list = list(trace_id_ids)
    r_list.sort()
    return r_list
