import requests
import yaml
import io
import pandas as pd
import json
import traceback
from .config import feishu_config

def read_config_file(file_id):

    # Obtain an access token
    auth_url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/"
    headers = {
        "Content-Type": "application/json"
    }
    payload = feishu_config.get_auth_payload()
    # Authenticate and get your access token from Feishu
    response = requests.post(auth_url, headers=headers, json=payload)
    auth_token = response.json().get("app_access_token")

    # The endpoint for downloading files from Feishu might look like this

    download_endpoint = f'https://open.feishu.cn/open-apis/drive/v1/files/{file_id}/download'

    # Make the request to download the file
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }
    response = requests.get(download_endpoint, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Assuming the response content is the binary content of the YAML file
        file_content = response.content

        # Load the YAML content
        content = yaml.safe_load(file_content)
        try:
            yaml_file_path = './cfg.yaml'
            with open(yaml_file_path, 'r') as file:
                yaml_content = yaml.safe_load(file)
            yaml_content = content
        except:
            yaml_file_path = 'cfg.yaml'
            yaml_content = content
        with open(yaml_file_path, 'w') as file:
            yaml.safe_dump(yaml_content, file)

    else:
        return 'Failed to download the file:'+response.text
def get_tidb_config(file_id,table_name, config_name,charset="utf8mb4",connect_timeout=10,write_timeout=30):
    """
    返回TiDB连接配置，从本地cfg.yaml文件读取配置信息
    支持SSL和其他通用配置，参考tablemaster实现
    
    参数:
        table_name: 要操作的表名，默认为'ods_pet_profile_detail_di'
        config_name: 配置名称，默认为'aiot_internal'
        charset: 字符集，默认为'utf8mb4'
        connect_timeout: 连接超时时间，默认为10秒
        write_timeout: 写入超时时间，默认为30秒
    
    配置文件支持的SSL相关字段:
        - db_type: 数据库类型 ('tidb', 'mysql' 等)
        - use_ssl: 是否强制使用SSL (bool)
        - ssl_ca: SSL CA证书路径 (str)
        - ssl_cert: SSL客户端证书路径 (str) 
        - ssl_key: SSL客户端密钥路径 (str)
        - ssl_disabled: 是否禁用SSL (bool)
        - ssl_verify_cert: 是否验证服务器证书 (bool)
        - ssl_verify_identity: 是否验证服务器身份 (bool)
    """
    read_config_file(file_id)  # 这会在本地生成cfg.yaml文件
    
    # 从cfg.yaml文件读取配置
    with open("cfg.yaml", "r") as file:
        all_configs = yaml.safe_load(file)
    
    # 获取指定名称的配置
    if config_name not in all_configs:
        raise ValueError(f"配置名称 '{config_name}' 在cfg.yaml中不存在")
    
    db_config = all_configs[config_name]
    
    # 获取数据库类型，默认为mysql
    db_type = db_config.get("db_type", "mysql").lower()
    db_host = db_config.get("host")
    init_command = db_config.get("init_command", "SET tidb_txn_mode='optimistic'")
    # 基础配置
    config = {
        "host": db_config.get("host"),
        "port": db_config.get("port"),
        "database": db_config.get("database"),
        "user": db_config.get("user"),
        "password": db_config.get("password"),
        "table": table_name,
        "charset": charset,
        "connect_timeout": connect_timeout,
        "write_timeout": write_timeout,
        "db_type": db_type,
        "init_command": init_command
    }
    
    # SSL配置处理 - 参考tablemaster的实现
    use_ssl = db_config.get("use_ssl", False)
    ssl_disabled = db_config.get("ssl_disabled", False)
    
    # TiDB默认使用SSL，除非明确禁用
    if (db_type == 'tidb' and not ssl_disabled) or use_ssl:
        # SSL基础配置
        ssl_config = {}
        
        # CA证书路径
        ssl_ca = db_config.get("ssl_ca")
        if ssl_ca:
            ssl_config["ca"] = ssl_ca
        elif db_type == 'tidb':
            # TiDB默认证书路径
            ssl_config["ca"] = "/etc/ssl/cert.pem"
        
        # 客户端证书和密钥
        ssl_cert = db_config.get("ssl_cert")
        if ssl_cert:
            ssl_config["cert"] = ssl_cert
            
        ssl_key = db_config.get("ssl_key")
        if ssl_key:
            ssl_config["key"] = ssl_key
        
        # SSL验证选项
        ssl_config["check_hostname"] = db_config.get("ssl_verify_identity", False)
        ssl_config["verify_mode"] = db_config.get("ssl_verify_cert", True)
        
        # 将SSL配置添加到连接配置中
        config["ssl"] = ssl_config
        config["ssl_disabled"] = False
        
        print(f"SSL配置已启用 - 数据库类型: {db_type}")
        if ssl_ca:
            print(f"SSL CA证书: {ssl_ca}")
        if ssl_cert:
            print(f"SSL客户端证书: {ssl_cert}")
    else:
        # 明确禁用SSL
        config["ssl_disabled"] = True
        print(f"SSL配置已禁用 - 数据库类型: {db_type}，使用{db_host}连接数据库")
    return config
def send_message(chat_id,content,user_id=None):
    
    """Get the access token from Feishu."""
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers = {'Content-Type': 'application/json'}
    payload = feishu_config.get_auth_payload()
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    token = data.get('tenant_access_token')
    """Send a message to a Feishu chat."""
    url = 'https://open.feishu.cn/open-apis/message/v4/send/'
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    if user_id:
        payload = {
            'chat_id': chat_id,
            'msg_type': 'text',
            'content': {
                'text': f"<at user_id = \"{user_id}\">Tom</at> {content}",
            }
        }
    else:
        payload = {
            'chat_id': chat_id,
            'msg_type': 'text',
            'content': {
                'text': f"{content}",
            }
        }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def send_message_user(user_id, content):
    """Get the access token from Feishu."""
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers = {'Content-Type': 'application/json'}
    payload = feishu_config.get_auth_payload()
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    token = data.get('tenant_access_token')
    """Send a message to a Feishu chat."""
    url = 'https://open.feishu.cn/open-apis/message/v4/send/'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    payload = {
        'user_id': user_id,
        'msg_type': 'text',
        'content': {
            'text': f"{content}",
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()
def send_card_message(chat_id,title,content, link_url='',content_2='',user_id= ''):
    """Get the access token from Feishu."""
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers = {'Content-Type': 'application/json'}
    payload = feishu_config.get_auth_payload()
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    token = data.get('tenant_access_token')
    if link_url != '':
        if content_2 != '':
            content_new = f"{content}<a href='{link_url}'></a>{content_2}"
        else:
            content_new = f"{content}<a href='{link_url}'></a>"
    else:
        content_new = content
    if user_id != '':
        user_id_length = len(user_id)
        user_id_content = ''
        for i in range(user_id_length):
            user_id_content = f"<at id=\"{user_id[i]}\"></at>" + user_id_content
    else:
        user_id_content = ''
    card_content = {
    'chat_id': chat_id,
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": True
        },
        "header": {
            "title": {
                "tag": "plain_text",
                "content": f"{title}"
            }
        },
        "elements": [
                {
            "tag": "div",
            "text": {
                "content": user_id_content, 
                "tag": "lark_md"
            }
        },
            {
                "tag": "markdown",
                "content": f"""{content_new}"""
                }
        ]
}
    }
    # 发送消息的API端点
    message_url = 'https://open.feishu.cn/open-apis/message/v4/send/'
    # 发送POST请求的headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    # 发送卡片消息
    response = requests.post(message_url, headers=headers, json=card_content)
    return response.json()
def send_card_message_user(user_id,content,title,link_url='',content_2=''):
    """Get the access token from Feishu."""
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers = {'Content-Type': 'application/json'}
    payload = feishu_config.get_auth_payload()
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    token = data.get('tenant_access_token')
    if link_url != '':
        if content_2 != '':
            content_new = f"{content}<a href='{link_url}'></a>{content_2}"
        else:
            content_new = f"{content}<a href='{link_url}'></a>"
    else:
        content_new = content
    # 卡片消息内容
    card_content = {
    'user_id': user_id,
    "msg_type": "interactive",
    "card": {
        "config": {
            "wide_screen_mode": True
        },
        "header": {
            "title": {
                "tag": "plain_text",
                "content": f"{title}"
            }
        },
        "elements": [
            {
                "tag": "markdown",
                "content": f"{content_new}"
                    
                }
                
            # 其他卡片组件，例如按钮等
        ]
    }
}
    # 发送消息的API端点
    message_url = 'https://open.feishu.cn/open-apis/message/v4/send/'

    # 发送POST请求的headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # 发送卡片消息
    response = requests.post(message_url, headers=headers, json=card_content)
    return response.json()
def read_fs_file(file_id,file_type = None):

    # Obtain an access token
    auth_url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/"
    headers = {
        "Content-Type": "application/json"
    }
    payload = feishu_config.get_auth_payload()
    # Authenticate and get your access token from Feishu
    response = requests.post(auth_url, headers=headers, json=payload)
    auth_token = response.json().get("app_access_token")

    # The endpoint for downloading files from Feishu might look like this

    download_endpoint = f'https://open.feishu.cn/open-apis/drive/v1/files/{file_id}/download'

    # Make the request to download the file
    headers = {
        'Authorization': f'Bearer {auth_token}'
    }
    response = requests.get(download_endpoint, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
        # Assuming the response content is the binary content of the YAML file
        file_content = response.content

        # Load the YAML content
        if file_type == None:
            return file_content
        elif file_type == 'yaml':
            content = yaml.safe_load(file_content)
            return content
        elif file_type == 'json':
            content = json.loads(file_content)
            return content
        elif file_type == 'text':
            content = file_content.decode('utf-8')
            return content
        elif file_type == 'xls':
            content = io.BytesIO(file_content)
            return content
    else:
        return 'Failed to download the file:'+response.text
    
def clear_fs_spreadsheet(api_token, spreadsheet_id,sheet_id, dimension='ROWS',startIndex=1, endIndex=100):
    url = f"https://open.feishu.cn/open-apis/sheet/v2/spreadsheets/{spreadsheet_id}/dimension_range"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    data = {
        "dimension":{
        "sheetId":sheet_id,
        "majorDimension":f"{dimension}",
        "startIndex":startIndex,
        "endIndex":endIndex
    }
    }
    response = requests.delete(url, headers=headers, json=data)
    if response.status_code == 200:
        print("Spreadsheet cleared successfully.")
    else:
        print("Failed to clear spreadsheet:", response.text)
def upload_data_to_feishu(table, spreadsheet_token,sheet_id,defualt_start_index = 'A1',upload_end_index='',delete_first='Yes',startIndex=1,clear_end_index=100):
    # Obtain an access token
    auth_url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/"
    headers = {
        "Content-Type": "application/json"
    }
    payload = feishu_config.get_auth_payload()
    # Authenticate and get your access token from Feishu
    response = requests.post(auth_url, headers=headers, json=payload)
    access_token = response.json().get("app_access_token")
    values = table.values.tolist()
    headers = table.columns.tolist() 
    value = [headers] + values
    url = f"https://open.feishu.cn/open-apis/sheet/v2/spreadsheets/{spreadsheet_token}/values_prepend"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    if upload_end_index == '':
        upload_end_index = f"T{len(value)+1}"
    body = {
        "valueRange": {
            "range": f"{sheet_id}!{defualt_start_index}:{upload_end_index}",
            "values": value
  
        }
    }
    try:
        if delete_first == 'Yes':
            clear_fs_spreadsheet(access_token,spreadsheet_token,sheet_id,startIndex=startIndex,endIndex=clear_end_index)
        else:
            pass
        
    except:
        return f"{traceback.format_exc()}"
    response = requests.post(url, json=body, headers=headers)
    if response.status_code == 200:
        return "Data uploaded successfully."
    else:
        return f"Failed to upload data: {response.text}"
def send_beautiful_card_message(receive_type,receive_id,template_id,template_variable,template_version=""):
    """Get the access token from Feishu."""
    url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal/'
    headers = {'Content-Type': 'application/json'}
    payload = feishu_config.get_auth_payload()
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()
    token = data.get('tenant_access_token')
    
    # 卡片消息内容
    if template_version == "":
        template = {"type":"template",
        "data":{"template_id":f"{template_id}",
                "template_variable":template_variable}}
    else:
        template = {"type":"template",
        "data":{"template_id":f"{template_id}",
                "template_version_name":f"{template_version}",
                "template_variable":template_variable}}
    template = json.dumps(template,ensure_ascii=False)
    template = template.replace('"', '\"')
    payload = json.dumps({
	"content": template,
	"msg_type": "interactive",
	"receive_id": f"{receive_id}",
})
    message_url = f"https://open.feishu.cn/open-apis/im/v1/messages?receive_id_type={receive_type}"

    # 发送POST请求的headers
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    # 发送卡片消息
    response = requests.request("POST", message_url, headers=headers, data=payload)
    return response.text
def read_fs_folder(folder_token):
    """
    从 Feishu 文件夹获取所有文件列表，支持分页。

    :param folder_token: 文件夹的 token
    :return: 文件夹内所有文件的列表
    """
    # 获取 Feishu 的访问令牌
    auth_url = "https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal/"
    headers = {"Content-Type": "application/json"}
    payload = feishu_config.get_auth_payload()

    response = requests.post(auth_url, headers=headers, json=payload)
    if response.status_code != 200:
        print(f"Failed to get auth token: {response.status_code}")
        return None

    auth_token = response.json().get("app_access_token")
    if not auth_token:
        print("Failed to retrieve access token from response.")
        return None

    # 初始化分页相关变量
    download_endpoint = "https://open.feishu.cn/open-apis/drive/v1/files/"
    headers = {'Authorization': f'Bearer {auth_token}'}
    params = {
        "direction": "DESC",
        "folder_token": folder_token,
        "page_size": 200,
        "order_by": "EditedTime"
    }

    all_files = []
    next_page_token = None

    while True:
        if next_page_token:
            params["page_token"] = next_page_token

        response = requests.get(download_endpoint, headers=headers, params=params)
        if response.status_code != 200:
            print(f"Failed to fetch files: {response.status_code}")
            break

        # 解析响应内容
        data = response.json().get('data')
        if not data:
            print("No data found in the response.")
            break

        files = data.get('files', [])
        all_files.extend(files)

        # 检查是否有下一页
        next_page_token = data.get('next_page_token')
        if not next_page_token:
            break

    return all_files