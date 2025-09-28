from src.pagodaAL.zmqclass import ZmqManager
import logging
import zmq
from typing import Optional, List
from src.pagodaAL.zmqreq import ZmqReqClient
from src.pagodaAL.zmqsub import ZmqSub
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - ZmqManager - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# 测试示例
if __name__ == '__main__':
    import time
    import zmq  # 仅在测试时需要直接导入

    try:
        # 初始化管理器（IP、发送端口、接收端口、订阅主题）
        zmq_manager = ZmqManager(
            ip="10.12.6.250",
            sender_port=5557,
            receiver_port=5558,
            subscribe_topics=["<Dome>"]
        )

        # 测试发送消息
        test_message = "<Content=HelloWorld>"
        send_success = zmq_manager.send(test_message)
        print(f"Send message {'success' if send_success else 'failed'}: {test_message}")

        # 测试接收消息（循环等待5秒）
        start_time = time.time()
        while 1:
            received = zmq_manager.receive()
            if received:
                print(f"Received message - Envelope: {received[0]}, Content: {received[1]}")
            time.sleep(0.1)

    except Exception as e:
        logger.error(f"Test error: {e}")
    finally:
        # 显式删除管理器实例，触发析构函数
        del zmq_manager
        print("Test completed")