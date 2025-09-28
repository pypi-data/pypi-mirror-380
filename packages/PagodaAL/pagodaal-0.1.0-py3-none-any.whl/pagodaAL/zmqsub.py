#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import zmq
import logging
from typing import List, Optional
import time

# 配置日志（匹配Qt的调试输出风格）
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - ZmqSub - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

class ZmqSub:
    """
    ZeroMQ SUB 模式订阅者类（适配发送端“信封+内容”双帧格式）
    发送端逻辑：s_sendmore(信封标签) → s_send(消息内容)
    接收端逻辑：先收信封标签 → 再收消息内容
    """

    def __init__(self, ip: str, port: int, scribe: List[str]):
        """
        构造函数（对应Qt的ZmqSub构造函数）
        :param ip: 发布者IP地址（如"10.12.6.250"）
        :param port: 发布者端口（如5557）
        :param scribe: 订阅主题列表（对应Qt的QStringList scribe，如["Dome", "Camera"]）
        """
        logger.info(f"ZmqSub instance created: IP={ip}, Port={port}, Scribe={scribe}")
        self.quit_flag = False  # 退出标志（对应Qt的quitFlag）
        self.context: Optional[zmq.Context] = None  # ZMQ上下文（对应Qt的m_context）
        self.sub_socket: Optional[zmq.Socket] = None  # SUB套接字（对应Qt的m_sub）
        self.init_zmq(ip, port, scribe)  # 初始化ZMQ（构造时自动调用）

    def __del__(self):
        """
        析构函数（对应Qt的~ZmqSub）
        关闭套接字、终止上下文，释放ZeroMQ资源
        """
        logger.info("Destructor called: Cleaning up ZeroMQ resources...")
        # 关闭SUB套接字（对应Qt的zmq_close(m_sub)）
        if self.sub_socket:
            try:
                self.sub_socket.close(linger=0)  # linger=0：立即关闭，不等待未处理数据
                logger.info("SUB socket closed successfully")
            except zmq.ZMQError as e:
                logger.warning(f"Error closing SUB socket: {e} (Errno={e.errno})")
        # 终止ZMQ上下文（对应Qt的zmq_ctx_destroy(m_context)）
        if self.context:
            try:
                self.context.term()
                logger.info("ZMQ context terminated successfully")
            except zmq.ZMQError as e:
                logger.warning(f"Error terminating ZMQ context: {e} (Errno={e.errno})")

    def init_zmq(self, ip: str, port: int, scribe: List[str]):
        """
        初始化ZMQ（对应Qt的initZMQ函数）
        1. 创建上下文和SUB套接字 2. 连接发布者 3. 订阅指定主题
        """
        try:
            # 1. 创建ZMQ上下文（单例模式，避免资源泄漏）
            self.context = zmq.Context.instance()
            # 2. 创建SUB类型套接字（对应Qt的zmq_socket(m_context, ZMQ_SUB)）
            self.sub_socket = self.context.socket(zmq.SUB)
            # 3. 设置接收超时（1秒，避免无限阻塞，提升鲁棒性）
            self.sub_socket.RCVTIMEO = 1000  # 单位：毫秒

            # 4. 拼接连接地址（对应Qt的"tcp://" + ip + ":" + port）
            connect_addr = f"tcp://{ip}:{port}"
            logger.info(f"Connecting to publisher: {connect_addr}")
            self.sub_socket.connect(connect_addr)
            logger.info(f"Connected to publisher successfully: {connect_addr}")

            # 5. 订阅指定主题（对应Qt的循环zmq_setsockopt(ZMQ_SUBSCRIBE)）
            for topic in scribe:
                if not isinstance(topic, str) or not topic.strip():
                    logger.warning(f"Skipping invalid topic: {topic} (must be non-empty string)")
                    continue
                # 订阅主题（ZeroMQ SUB通过前缀匹配，此处完全匹配发送端的msgReceiver标签）
                self.sub_socket.setsockopt_string(zmq.SUBSCRIBE, topic.strip())
                logger.info(f"Subscribed to envelope topic: '{topic.strip()}'")

        except zmq.ZMQError as e:
            logger.error(f"ZMQ initialization failed: {e} (Errno={e.errno})", exc_info=True)
            self.__del__()  # 初始化失败时主动清理资源
            raise  # 抛出异常，让调用者感知初始化失败
        except Exception as e:
            logger.error(f"Unexpected error in init_zmq: {e}", exc_info=True)
            self.__del__()
            raise

    def receive_message(self):
        """
        持续接收消息（对应Qt的receiveMessage函数）
        适配发送端格式：先收"信封标签"（msgReceiver）→ 再收"消息内容"（reply）
        主线程阻塞运行，通过quit_flag控制退出
        """
        logger.info("Entering receive_message loop (blocking mode). Press Ctrl+C to stop.")
        while not self.quit_flag:
            try:
                # -------------------------- 关键适配：匹配发送端双帧格式 --------------------------
                # 1. 接收第一帧：信封标签（对应发送端的s_sendmore(msgReceiver)）
                envelope = self.sub_socket.recv_string()  # 接收msgReceiver（如"Dome"）
                logger.info(f"Received envelope (msgReceiver): '{envelope}'")

                # 2. 接收第二帧：实际消息内容（对应发送端的s_send(reply)）
                message = self.sub_socket.recv_string()  # 接收reply（如"<Uid=Dome.TurnOff.0.0>..."）
                logger.info(f"Received message content: '{message}'")
                # --------------------------------------------------------------------------------

                # （可选）此处可添加业务逻辑：如解析message、触发回调等
                # 示例：打印完整的“信封-内容”配对
                logger.info(f"[Complete Message] Envelope: {envelope} | Content: {message}\n")

            except zmq.Again:
                # 接收超时（正常情况，每1秒触发一次，用于检查quit_flag）
                time.sleep(0.1)  # 短暂休眠，降低CPU占用
                continue
            except zmq.ZMQError as e:
                # ZMQ错误处理（如上下文终止、套接字关闭）
                if e.errno == zmq.ETERM:
                    logger.info(f"ZMQ context terminated: {e} (Exiting receive loop)")
                    break
                elif e.errno == zmq.ENOTSOCK:
                    logger.error(f"SUB socket is invalid: {e} (Exiting receive loop)")
                    break
                else:
                    logger.error(f"ZMQ receive error: {e} (Errno={e.errno})", exc_info=True)
                    break
            except KeyboardInterrupt:
                # 捕获Ctrl+C，优雅退出
                logger.info("KeyboardInterrupt received: Stopping receive loop...")
                self.close_server()
                break
            except Exception as e:
                # 未知异常处理（避免程序崩溃）
                logger.error(f"Unexpected error in receive_message: {e}", exc_info=True)
                time.sleep(1)  # 异常后休眠1秒，防止日志刷屏

        logger.info("Exited receive_message loop")

    def close_server(self):
        """
        关闭服务（对应Qt的closeServer函数）
        设置quit_flag，触发receive_message循环退出
        """
        logger.info("close_server called: Setting quit_flag to True")
        self.quit_flag = True


# --- 测试代码（仅接收端，无发送端、无多线程）---
if __name__ == '__main__':
    # -------------------------- 测试配置（需根据实际环境修改）--------------------------
    PUBLISHER_IP = "10.12.6.250"    # 发布者IP（如实际地址为10.12.6.250则修改）
    PUBLISHER_PORT = 5558         # 发布者端口（需与发送端一致）
    # 订阅主题列表（需与发送端的msgReceiver标签完全匹配，如["Dome", "Camera"]）
    SUBSCRIBE_ENVELOPES = ["<Dome>"]
    # --------------------------------------------------------------------------------

    print("=" * 60)
    print("ZeroMQ SUB Subscriber Test (Adapted to Envelope+Content Format)")
    print(f"Publisher Address: tcp://{PUBLISHER_IP}:{PUBLISHER_PORT}")
    print(f"Subscribed Envelopes (msgReceiver): {SUBSCRIBE_ENVELOPES}")
    print("Note: This script runs in blocking mode. Press Ctrl+C to exit.")
    print("=" * 60)

    try:
        # 1. 创建ZmqSub实例（自动连接发布者并订阅主题）
        subscriber = ZmqSub(
            ip=PUBLISHER_IP,
            port=PUBLISHER_PORT,
            scribe=SUBSCRIBE_ENVELOPES
        )

        # 2. 启动接收（阻塞主线程，直到Ctrl+C或调用close_server）
        subscriber.receive_message()

    except zmq.ZMQError as e:
        print(f"\nInitialization Failed! ZMQ Error: {e} (Errno={e.errno})")
        print("Please check:")
        print("1. Publisher is running at tcp://{PUBLISHER_IP}:{PUBLISHER_PORT}")
        print("2. Port is not occupied by other programs")
        print("3. Network connection between subscriber and publisher is normal")
    except Exception as e:
        print(f"\nUnexpected Error: {e}")
    finally:
        print("\nTest finished. Resources are cleaned up by destructor.")