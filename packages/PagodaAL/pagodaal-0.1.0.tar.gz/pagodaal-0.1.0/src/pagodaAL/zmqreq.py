#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zmq
import logging
import threading

# 配置日志记录，用于调试和错误追踪
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ZmqReqClient:
    """
    一个使用ZeroMQ REQ模式的客户端类。

    该类负责连接到指定的ZeroMQ REP服务器，发送数据，并接收回复。
    它实现了构造函数、析构函数和初始化方法，并保证了线程安全。
    """

    def __init__(self, ip: str, port: int):
        """
        构造函数。

        :param ip: 服务器的IP地址。
        :param port: 服务器的端口号。
        """
        logger.info(f"ZmqReqClient instance created for {ip}:{port}")
        self.ip = ip
        self.port = port
        self.context = None
        self.socket = None
        self._is_connected = False
        # 使用锁来保证多线程环境下的安全操作
        self._lock = threading.Lock()

    def initialize(self):
        """
        初始化函数，用于创建和连接ZeroMQ套接字。

        此函数应在使用sendData之前调用。
        """
        with self._lock:
            if self._is_connected:
                logger.warning("Client is already connected.")
                return

            try:
                # 创建ZeroMQ上下文
                self.context = zmq.Context()
                # 创建一个REQ类型的套接字
                self.socket = self.context.socket(zmq.REQ)
                # 连接到服务器
                connect_str = f"tcp://{self.ip}:{self.port}"
                logger.info(f"Connecting to {connect_str}...")
                self.socket.connect(connect_str)
                self._is_connected = True
                logger.info("Connection successful.")
            except zmq.ZMQError as e:
                logger.error(f"Failed to initialize ZeroMQ: {e}")
                self._cleanup()

    def sendData(self, data_str: str) -> bool:
        """
        发送字符串数据到服务器。

        该函数接收一个Python字符串，**在内部自动将其编码为UTF-8字节流**进行发送。
        由于REQ-REP模式的限制，发送后会等待服务器的回复。

        :param data_str: 要发送的Python字符串。
        :return: 如果成功发送并收到回复，返回True；否则返回False。
        """
        # 1. 类型检查，确保传入的是字符串
        if not isinstance(data_str, str):
            logger.error("sendData() requires a string argument.")
            return False

        with self._lock:
            if not self._is_connected:
                logger.error("Client is not connected. Call initialize() first.")
                return False

            try:
                # 2. 发送数据：在内部自动编码字符串
                # data_str.encode('utf-8') 将字符串转换为字节
                self.socket.send(data_str.encode('utf-8'))
                logger.info(f"Sent string (encoded as UTF-8): '{data_str}'")

                # 等待接收回复
                self.socket.RCVTIMEO = 5000  # 5秒超时
                reply_bytes = self.socket.recv()
                
                # 将接收到的字节解码为字符串再进行日志记录
                reply_str = reply_bytes.decode('utf-8')
                logger.info(f"Received reply: '{reply_str}'")
                
                return True

            except zmq.Again:
                logger.error("Timeout waiting for reply from server.")
                logger.info("Resetting socket due to timeout...")
                self._cleanup()
                self.initialize()
                return False
            except zmq.ZMQError as e:
                logger.error(f"ZeroMQ error occurred during send/receive: {e}")
                self._cleanup()
                return False

    def _cleanup(self):
        """
        内部清理函数，用于安全地关闭和释放资源。
        """
        logger.info("Cleaning up ZeroMQ resources...")
        if self.socket:
            try:
                self.socket.close(0)  # 0表示立即关闭
                logger.info("Socket closed.")
            except zmq.ZMQError as e:
                logger.warning(f"Error closing socket: {e}")
            self.socket = None
        
        if self.context:
            try:
                self.context.term()
                logger.info("Context terminated.")
            except zmq.ZMQError as e:
                logger.warning(f"Error terminating context: {e}")
            self.context = None
            
        self._is_connected = False

    def __del__(self):
        """
        析构函数。
        """
        logger.info("Destructor called. Cleaning up...")
        try:
            with self._lock:
                self._cleanup()
        except Exception as e:
            logger.warning(f"Error in destructor: {e}")

# --- 使用示例 ---
if __name__ == '__main__':
    # 1. 创建客户端实例
    zmq_client = ZmqReqClient(ip="10.12.6.250", port=5557)

    try:
        # 2. 初始化连接
        zmq_client.initialize()

        # 3. 发送数据 (直接传入字符串)
        message_to_send = "<Content=HelloWorld>"
        if zmq_client.sendData(message_to_send):
            print(f"Successfully processed message: '{message_to_send}'")
        else:
            print(f"Failed to process message: '{message_to_send}'")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    finally:
        del zmq_client
        print("Client object deleted. Exiting.")