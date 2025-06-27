def batch_upsert_table(self, table_name, data, unique_key='id', update_on_duplicate=True):
    """
    批量插入或更新表数据（支持任意表结构）。

    :param table_name: 表名
    :param data: list of dict, 每个字典代表一行数据[{'column1': value, 'column2': value}]
    :param unique_key: 唯一键字段名（用于 ON DUPLICATE KEY UPDATE）
    :param update_on_duplicate: 是否在唯一键冲突时更新，默认为 True
    :return:  受影响行数
    """
    if not data:
        return 0

    # 提取所有字段名（排除 unique_key）
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())
    all_fields.discard(unique_key)

    if not all_fields:
        logging.error("fields is null")
        return 0

    fields = list(all_fields)
    field_placeholders = ', '.join(["`{}` = VALUES(`{}`)".format(f, f) for f in fields])
    value_placeholders = ', '.join(['%s'] * (len(fields) + 1))  # unique_key + other fields

    # 构造 SQL 语句
    insert_sql = """
            INSERT INTO `{table}` (`{unique_key}`, `{fields}`)
            VALUES ({value_placeholders})
        """.format(
        table=table_name,
        unique_key=unique_key,
        fields='`, `'.join(fields),
        value_placeholders=value_placeholders
    )

    if update_on_duplicate:
        insert_sql += " ON DUPLICATE KEY UPDATE {}".format(field_placeholders)

    # 构造参数列表
    parameters = []
    for row in data:
        values = [row.get(unique_key)]
        for field in fields:
            values.append(row.get(field))
        parameters.append(tuple(values))  # 每一行数据作为元组添加进列表

    # 执行 SQL
    try:
        self.cursor.executemany(insert_sql, parameters)
        self.db.commit()
        return self.cursor.rowcount
    except MySQLdb.Error, e:
        logging.error("batch_upsert_table db error:%s" % e)
        return 0