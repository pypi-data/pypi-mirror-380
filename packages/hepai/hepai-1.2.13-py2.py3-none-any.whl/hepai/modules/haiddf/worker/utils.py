
def get_uuid(lenth, prefix=None):
    import uuid
    if prefix:
        return prefix + str(uuid.uuid4())[:lenth-len(prefix)]
    return str(uuid.uuid4())[:lenth]

def get_hostname():
    import socket
    return socket.gethostname()


def get_used_ports(start=1, end=65535):
    import socket
    ports = []
    for port in range(start, end):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.bind(('0.0.0.0', port))
        except:
            ports.append(port)
        finally:
            s.close()
    return ports


def auto_port(port=None, start=42901, **kwargs):
    """
    自动获取端口，返回数字端口号
    """
    if port == 'auto':
        # 获取所有被占用的端口号
        used_ports = get_used_ports(start=start, **kwargs)
        for i in range(start, 65535):
            if i not in used_ports:
                return int(i)
        raise ValueError('No available port')
    else:
        return port
    

def auto_worker_address(worker_address, host, port):
    import socket
    if worker_address != 'auto':
        return worker_address
    if host in ['localhost', '127.0.0.1']:
        return f'http://{host}:{port}'
    elif host == '0.0.0.0':
        ## TODO，此处需要改进，获取本机ip
        # 获取本机的外部 IP 地址是使用一个与外部世界的连接
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("10.255.255.255", 1))
            ip = s.getsockname()[0]
        return f'http://{ip}:{port}'
    else:
        raise ValueError(f'host {host} is not supported')


def extract_worker_id(text: str) -> str:
    import re
    # 使用正则表达式来匹配格式形如 'wk-xxxx-xxxx' 的 worker_id
    # match = re.search(r'worker_id: `(\w+-\w+)`', text)
    match = re.search(r'worker_id:\s*`([^`]*)`', text)
    if match:
        return match.group(1)
    return None

def wait_for_worker(worker_id, timeout=10):
    # 向服务发起请求
    import os, time
    from haiddf import HaiDDF
    from haiddf._types import WorkerInfo
    client = HaiDDF(api_key=os.getenv("DDF_API_KEY"))

    start_time = time.time()
    while time.time() - start_time < timeout:
        wk_info = client.get_worker_info(worker_id=worker_id)
        if isinstance(wk_info, WorkerInfo):
            return wk_info
        time.sleep(0.5)
    return False

def run_standlone_worker_demo(logger=None):
    import os, sys
    import time
    from pathlib import Path
    here = Path(__file__).parent

    class PrintLogger:
        def info(self, *args, **kwargs):
            print(*args, **kwargs)

    logger = logger or PrintLogger()
    
    current_dir = os.getcwd()

    import subprocess
    from datetime import datetime

    os.chdir(str(here))
    try:
        print(f"Run standalone worker demo in `{here}` ...", end="")
        # logger.info(f"Run standalone worker demo in `{here}` ...")
        ct = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_file = f"nohup.out.demo.{ct}"
        cmd = f"nohup python demo_worker.py >{log_file} 2>&1 &"
        result = subprocess.run(
            cmd,
            shell=True,  
            check=True,  # 如果命令失败，抛出 CalledProcessError
            capture_output=True,  # 捕获标准输出和标准错误
            text=True  # 将输出作为字符串处理，而不是字节
        )
        print(", succeeded.", end="")
        # print(result.stdout)
    except subprocess.CalledProcessError as e:
        print(", failed.")
        print("Error message:")
        print(e.stderr)
        raise e

    os.chdir(current_dir)

    # 从logfile读取worker_id
    # 等待worker启动
    time.sleep(0.5)

    # 等待文件被创建和写入
    file_path = f"{here}/{log_file}"
    timeout = 5
    t0 = time.time() 
    while True:
        ct = time.time() - t0
        if ct > timeout:
            raise TimeoutError(f"Wait for worker start timeout. {ct}s")
        if not os.path.exists(file_path):
            time.sleep(0.5)
            # print(f"Waiting for file `{file_path}` to be created ... {ct}s")
            logger.info(f"Waiting for log_file `{log_file}` to be created ... {ct:.2f}s")
            continue
        
        with open(f'{here}/{log_file}', 'r') as f:
            text = f.read()
            if text == "":
                time.sleep(0.5)
                logger.info(f"Waiting for log_file `{log_file}` to be written ... {ct}s")
                # print(f"Waiting for file `{file_path}` to be written ... {ct}s")
                continue
        worker_id = extract_worker_id(text)
        # print(f" Worker_id: `{worker_id}`")
        if worker_id:
            return wait_for_worker(worker_id, timeout=10)
        else:
            if "Traceback" in text:
                chunks = text.split("Traceback")
                error_msg = f"Traceback{chunks[-1]}"
                raise ProcessLookupError(f"Worker started failed. {error_msg}")
            # print(" Worker started, but worker_id not found.")
            # return
            raise ValueError("Worker started, but worker_id not found.")
        