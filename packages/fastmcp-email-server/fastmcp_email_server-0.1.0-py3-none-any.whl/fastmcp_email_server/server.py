# -*- coding: utf-8 -*-
"""
基于 FastMCP 框架的邮件 MCP 服务器
提供邮件收发、附件处理等功能
"""

from mcp.server.fastmcp import FastMCP
from typing import List, Dict, Any, Union, Optional
import os

# 导入邮件处理模块（包内相对导入）
from .email_config import get_imap_server, get_smtp_server
from .receive_163 import Email
from .send_163 import EmailSender

# 创建 FastMCP 实例
mcp = FastMCP("EmailService")

# ====== 邮件接收工具组 ======

@mcp.tool()
def get_newest_email(
    account: str,
    password: str,
    imap_server: Optional[str] = None,
) -> Dict[str, Any]:
    """
    获取最新的未读邮件，包括发件人、主题、内容和附件信息
    
    Args:
        account: 邮箱账号
        password: 授权码/密码
        imap_server: 自定义IMAP服务器地址（可选，未提供时自动匹配）
        
    Returns:
        包含邮件信息的字典，包括发件人、主题、日期、内容和附件列表
    """
    if not account or not password:
        raise ValueError("account 和 password 为必填参数")
    
    email_client = Email(
        imap=imap_server or get_imap_server(account),
        account=account,
        password=password,
    )
    msg_data = email_client.get_newest()
    return {
        "from": msg_data.get('from', '未知'),
        "subject": msg_data.get('subject', '无主题'),
        "date": msg_data.get('date', '未知'),
        "content": msg_data.get('content', ''),
        "files": msg_data.get('files', [])
    }

@mcp.tool()
def check_emails(
    account: str,
    password: str,
    message_type: str = "Unseen",
    count: int = 5,
    imap_server: Optional[str] = None,
) -> List[Dict[str, Any]]:
    """
    检查指定类型和数量的邮件
    
    Args:
        account: 邮箱账号
        password: 授权码/密码
        message_type: 邮件类型，可选值包括 "All", "Unseen", "Seen", "Recent", "Answered", "Flagged"
        count: 要检索的邮件数量
        imap_server: 自定义IMAP服务器地址（可选，未提供时自动匹配）
        
    Returns:
        包含邮件信息的字典列表
    """
    if not account or not password:
        raise ValueError("account 和 password 为必填参数")
    
    email_client = Email(
        imap=imap_server or get_imap_server(account),
        account=account,
        password=password,
    )
    messages = []
    
    # 设置为False以获取多封邮件，而不仅仅是最新的一封
    for msg_data in email_client.check_email(last_message=False, message_type=message_type, count=count):
        messages.append({
            "from": msg_data.get('from', '未知'),
            "subject": msg_data.get('subject', '无主题'),
            "date": msg_data.get('date', '未知'),
            "content": msg_data.get('content', ''),
            "files": msg_data.get('files', [])
        })
    
    return messages

@mcp.tool()
def save_attachment(
    file_name: str,
    account: str,
    password: str,
    save_path: str = '',
    imap_server: Optional[str] = None,
) -> str:
    """
    保存指定的附件到指定路径
    
    Args:
        file_name: 要保存的附件文件名
        account: 邮箱账号
        password: 授权码/密码
        save_path: 保存路径，默认为空（当前目录）
        imap_server: 自定义IMAP服务器地址（可选，未提供时自动匹配）
        
    Returns:
        保存状态消息
    """
    if not account or not password:
        raise ValueError("account 和 password 为必填参数")
    
    email_client = Email(
        imap=imap_server or get_imap_server(account),
        account=account,
        password=password,
        file_save_path=save_path,
    )
    msg_data = email_client.get_newest()
    
    # 检查附件是否存在
    files = msg_data.get('files', [])
    if file_name in files:
        # 文件已经在获取邮件时被保存
        file_path = os.path.join(save_path, file_name)
        if os.path.exists(file_path):
            return f"文件已保存到 {file_path}"
        else:
            return f"文件保存失败"
    else:
        return f"未找到名为 {file_name} 的附件"

# ====== 邮件发送工具组 ======

@mcp.tool()
def send_text_email(
    to_addr: Union[str, List[str]],
    subject: str,
    content: str,
    account: str,
    password: str,
    cc_addr: Union[str, List[str], None] = None,
    smtp_server: Optional[str] = None,
) -> Dict[str, str]:
    """
    发送纯文本邮件
    
    Args:
        to_addr: 收件人邮箱地址，可以是单个字符串或字符串列表
        subject: 邮件主题
        content: 邮件正文内容
        account: 发送者邮箱账号
        password: 授权码/密码
        cc_addr: 抄送人邮箱地址，可以是单个字符串或字符串列表（可选）
        smtp_server: 自定义SMTP服务器地址（可选，未提供时自动匹配）
        
    Returns:
        包含发送状态和消息的字典
    """
    if not account or not password:
        raise ValueError("account 和 password 为必填参数")
    
    sender = EmailSender(
        account=account,
        password=password,
        smtp_server=smtp_server or get_smtp_server(account),
    )
    return sender.send_text_email(to_addr, subject, content, cc_addr)

@mcp.tool()
def send_html_email(
    to_addr: Union[str, List[str]],
    subject: str,
    html_content: str,
    account: str,
    password: str,
    cc_addr: Union[str, List[str], None] = None,
    smtp_server: Optional[str] = None,
) -> Dict[str, str]:
    """
    发送HTML格式邮件
    
    Args:
        to_addr: 收件人邮箱地址，可以是单个字符串或字符串列表
        subject: 邮件主题
        html_content: HTML格式的邮件正文内容
        account: 发送者邮箱账号
        password: 授权码/密码
        cc_addr: 抄送人邮箱地址，可以是单个字符串或字符串列表（可选）
        smtp_server: 自定义SMTP服务器地址（可选，未提供时自动匹配）
        
    Returns:
        包含发送状态和消息的字典
    """
    if not account or not password:
        raise ValueError("account 和 password 为必填参数")
    
    sender = EmailSender(
        account=account,
        password=password,
        smtp_server=smtp_server or get_smtp_server(account),
    )
    return sender.send_html_email(to_addr, subject, html_content, cc_addr)

@mcp.tool()
def send_email_with_attachment(
    to_addr: Union[str, List[str]],
    subject: str,
    content: str,
    attachment_paths: Union[str, List[str]],
    account: str,
    password: str,
    cc_addr: Union[str, List[str], None] = None,
    is_html: bool = False,
    smtp_server: Optional[str] = None,
) -> Dict[str, str]:
    """
    发送带附件的邮件
    
    Args:
        to_addr: 收件人邮箱地址，可以是单个字符串或字符串列表
        subject: 邮件主题
        content: 邮件正文内容
        attachment_paths: 附件路径，可以是单个字符串或字符串列表
        account: 发送者邮箱账号
        password: 授权码/密码
        cc_addr: 抄送人邮箱地址，可以是单个字符串或字符串列表（可选）
        is_html: 内容是否为HTML格式，默认为False
        smtp_server: 自定义SMTP服务器地址（可选，未提供时自动匹配）
        
    Returns:
        包含发送状态和消息的字典
    """
    if not account or not password:
        raise ValueError("account 和 password 为必填参数")
    
    sender = EmailSender(
        account=account,
        password=password,
        smtp_server=smtp_server or get_smtp_server(account),
    )
    return sender.send_email_with_attachment(to_addr, subject, content, attachment_paths, cc_addr, is_html)

# ====== 服务器配置工具 ======

@mcp.tool()
def get_server_config(email: str) -> Dict[str, str]:
    """
    根据邮箱地址获取推荐的服务器配置
    
    Args:
        email: 邮箱地址
        
    Returns:
        包含SMTP和IMAP服务器地址的字典
    """
    return {
        "smtp_server": get_smtp_server(email),
        "imap_server": get_imap_server(email),
        "smtp_port": "465",
        "imap_port": "993"
    }

if __name__ == "__main__":
    # 使用 stdio 传输启动 MCP 服务器
    mcp.run(transport="stdio")

def main():
    mcp.run(transport="stdio")


