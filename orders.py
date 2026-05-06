def get_order_status(order_id: str) -> str:  # 定义订单查询函数，传入订单号，返回订单状态文本
    orders = {  # 创建一个字典，用来模拟订单数据库
        "1001": {  # 订单号 1001 的订单信息
            "status": "已发货",  # 订单状态
            "tracking": "顺丰快递 SF123456789",  # 物流信息
            "eta": "预计 2 天内送达"  # 预计送达时间
        },
        "1002": {  # 订单号 1002 的订单信息
            "status": "待发货",  # 订单状态
            "tracking": "暂无物流单号",  # 物流信息
            "eta": "预计 24 小时内发货"  # 预计发货时间
        },
        "1003": {  # 订单号 1003 的订单信息
            "status": "已签收",  # 订单状态
            "tracking": "中通快递 ZT987654321",  # 物流信息
            "eta": "已于昨天签收"  # 签收情况
        }
    }

    order = orders.get(order_id)  # 根据订单号查询订单

    if not order:  # 如果没有查到订单
        return f"没有查询到订单号 {order_id}，请确认订单号是否正确。"  # 返回错误提示

    return (  # 返回订单查询结果
        f"订单号：{order_id}\n"
        f"订单状态：{order['status']}\n"
        f"物流信息：{order['tracking']}\n"
        f"预计情况：{order['eta']}"
    )