#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import logging
from typing import Optional, List
from src.pagodaAL.zmqreq import ZmqReqClient
from src.pagodaAL.zmqsub import ZmqSub
import zmq
# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - ZmqManager - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ZmqManager:
    """
    ZeroMQ 管理器类，整合发送者(REQ)和接收者(SUB)功能，通过多线程实现并行操作
    """

    def __init__(self, ip: str, sender_port: int, receiver_port: int, subscribe_topics: List[str]):
        """
        构造函数

        :param ip: 服务器IP地址
        :param sender_port: 发送者(REQ)端口号
        :param receiver_port: 接收者(SUB)端口号
        :param subscribe_topics: 接收者订阅主题列表
        """
        self.ip = ip
        self.sender_port = sender_port
        self.receiver_port = receiver_port
        self.subscribe_topics = subscribe_topics

        # 线程相关
        self.sender_thread: Optional[threading.Thread] = None
        self.receiver_thread: Optional[threading.Thread] = None
        self._stop_event = threading.Event()  # 用于通知线程停止

        # 消息缓存（用于接收消息的存储）
        self._received_message = None
        self._message_lock = threading.Lock()  # 保护消息缓存的锁

        # 初始化发送者和接收者
        self._init_sender()
        self._init_receiver()

        # 启动线程
        self._start_threads()

    def _init_sender(self):
        """初始化发送者客户端"""
        self.sender = ZmqReqClient(self.ip, self.sender_port)
        # 初始化连接
        self.sender.initialize()

    def _init_receiver(self):
        """初始化接收者客户端"""
        self.receiver = ZmqSub(self.ip, self.receiver_port, self.subscribe_topics)

    def _start_threads(self):
        """启动发送者和接收者线程"""
        # 发送者线程（实际发送操作在send方法中触发，线程用于保持连接）
        self.sender_thread = threading.Thread(
            target=self._sender_worker,
            daemon=True,
            name="ZmqSenderThread"
        )
        self.sender_thread.start()

        # 接收者线程（持续运行接收消息）
        self.receiver_thread = threading.Thread(
            target=self._receiver_worker,
            daemon=True,
            name="ZmqReceiverThread"
        )
        self.receiver_thread.start()

        logger.info("Both sender and receiver threads started")

    def _sender_worker(self):
        """发送者线程工作函数"""
        while not self._stop_event.is_set():
            # 发送者线程主要等待send方法的调用，此处保持线程存活
            self._stop_event.wait(0.1)

    def _receiver_worker(self):
        """接收者线程工作函数"""
        while not self._stop_event.is_set():
            try:
                # 尝试接收消息（适配ZmqSub的双帧格式）
                envelope = self.receiver.sub_socket.recv_string(flags=zmq.NOBLOCK)
                message = self.receiver.sub_socket.recv_string(flags=zmq.NOBLOCK)

                # 存储接收的消息
                with self._message_lock:
                    self._received_message = (envelope, message)
                    logger.info(f"Stored message - Envelope: {envelope}, Content: {message}")
            except zmq.Again:
                # 无消息时短暂等待
                self._stop_event.wait(0.1)
            except zmq.ZMQError as e:
                if not self._stop_event.is_set():
                    logger.error(f"Receiver error: {e}")
                break

    def send(self, message: str) -> bool:
        """
        发送消息

        :param message: 要发送的字符串消息
        :return: 发送成功返回True，否则返回False
        """
        if not isinstance(message, str):
            logger.error("Message must be a string")
            return False

        if self._stop_event.is_set():
            logger.error("Cannot send message: ZmqManager is stopping")
            return False

        return self.sender.sendData(message)

    def receive(self) -> Optional[tuple]:
        """
        获取接收的消息

        :return: 包含信封和消息内容的元组 (envelope, message)，无消息时返回None
        """
        with self._message_lock:
            if self._received_message is not None:
                # 返回当前消息并清空缓存
                msg = self._received_message
                self._received_message = None
                return msg
            return None

    def __del__(self):
        """析构函数，用于清理资源和停止线程"""
        logger.info("Destructor called, cleaning up resources...")
        self._stop_event.set()

        # 等待线程退出
        if self.sender_thread and self.sender_thread.is_alive():
            self.sender_thread.join(timeout=1.0)
            if self.sender_thread.is_alive():
                logger.warning("Sender thread did not exit properly")

        if self.receiver_thread and self.receiver_thread.is_alive():
            self.receiver_thread.join(timeout=1.0)
            if self.receiver_thread.is_alive():
                logger.warning("Receiver thread did not exit properly")

        # 清理发送者和接收者实例
        del self.sender
        del self.receiver

        logger.info("ZmqManager cleanup completed")


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