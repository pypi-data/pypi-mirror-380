# -*- coding: utf-8 -*-
"""
@项目名称 : yhfin-data-agent
@文件名称 : sql_checker.py
@创建人   : zhongbinjie
@创建时间 : 2025/9/10 14:08
@文件说明 : 
@企业名称 : 深圳市赢和信息技术有限公司
@Copyright:2025-2035, 深圳市赢和信息技术有限公司. All rights Reserved.
"""

import re
from ..utils import logger

def is_valid_sql_statement(sql, statement_type):
    """校验SQL是否为合法的指定类型语句
    :param sql: SQL语句
    :param statement_type: 语句类型(SELECT/UPDATE/DELETE/INSERT)
    """
    # 移除注释和空白字符
    sql_clean = re.sub(r'--.*$', '', sql, flags=re.MULTILINE)
    sql_clean = re.sub(r'/\*.*?\*/', '', sql_clean, flags=re.DOTALL)
    sql_stripped = sql_clean.strip().upper()

    # 基础校验: 语句类型匹配且无分号
    if ';' in sql_stripped.split('\n')[0]:
        return False

    # 特殊处理SELECT语句，允许WITH AS语法
    if statement_type == 'SELECT':
        # 允许以WITH开头的SELECT语句
        if sql_stripped.startswith('WITH'):
            if 'SELECT' not in sql_stripped:
                return False
        else:
            if not sql_stripped.startswith('SELECT'):
                return False
    else:
        if not sql_stripped.startswith(statement_type):
            return False

    # 针对不同类型的额外校验
    if statement_type == 'DELETE' and 'WHERE' not in sql_stripped:
        logger.warning("DELETE语句缺少WHERE子句，可能导致全表删除")
        # return False  # 可选：强制要求WHERE子句

    if statement_type == 'UPDATE' and 'WHERE' not in sql_stripped:
        logger.warning("UPDATE语句缺少WHERE子句，可能导致全表更新")
        # return False  # 可选：强制要求WHERE子句

    return True


def test():
    print()


if __name__ == '__main__':
    None
