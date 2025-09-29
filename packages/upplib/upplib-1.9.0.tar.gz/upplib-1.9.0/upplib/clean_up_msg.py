from upplib import *
from datetime import datetime, timezone, timedelta
from typing import Any, Optional, Union


def clean_up_msg_1(msg: str = None) -> str:
    try:
        """
            2025-09-28T19:38:41.146954-06:00 com.leo.digest.aop.ApiLogAspect - traceId: - (catTraceId:rcs-gateway-0a0f2154-488625-102) - ===>API GatewayFacadeImpl#gatewayRequest START
            ->
            2025-09-28T20:09:52.390783-06:00 o.rcs.biz.limiter.XLimitSwitc - rcs-gateway-0a0f2154-488625-102 - xlimit No current limiter configured，key=mobilewalla_mbmultiagents

            2025-09-29T10:26:55.161489-06:00 c.c.f.a.spring.annotation.SpringValueProcessor - traceId: - Monitoring key: spring.mvc.servlet.path, beanName: swaggerWelcome, field: org.springdoc.webmvc.ui.SwaggerWelcomeWebMvc.mvcServletPath
            ->
            2025-09-29T10:26:55.161489-06:00 annotation.SpringValueProcessor - - Monitoring key: spring.mvc.servlet.path, beanName: swaggerWelcome, field: org.springdoc.webmvc.ui.SwaggerWelcomeWebMvc.mvcServletPath
        """
        SEP_S = '- traceId: -'
        sep_pos = msg.find(SEP_S)
        if sep_pos == -1:
            return msg

        # 提取时间戳
        timestamp = msg[:sep_pos].rstrip()

        # 提取方法名和剩余部分
        method_part = msg[sep_pos + len(SEP_S):]
        method_end = method_part.find(SEP_S)
        if method_end == -1:
            method = method_part.strip()
            trace_part = ''
        else:
            method = method_part[:method_end].strip()
            trace_part = method_part[method_end + len(SEP_S):]

        # 提取traceId
        trace_match = re.search(r'\(catTraceId:([^)]+)\)', trace_part)
        if trace_match:
            trace_id = trace_match.group(1)
            other = trace_part[trace_match.end():].strip()
        else:
            trace_id = ''
            other = trace_part.strip()

        return f'{timestamp} {method} - {trace_id} - {other}'

    except Exception as e:
        return msg
