import ipywidgets as widgets
import subprocess
import os


def create_cuda_ui_components():
    cuda_version_dropdown = widgets.Dropdown(
    options=[
        ('11.5.0', 'cuda_11.5.0_495.29.05_linux.run'),
        ('11.5.1', 'cuda_11.5.1_495.29.05_linux.run'),
        ('11.5.2', 'cuda_11.5.2_495.29.05_linux.run'),
        ('11.6.0', 'cuda_11.6.0_510.39.01_linux.run'),
        ('11.6.1', 'cuda_11.6.1_510.47.03_linux.run'),
        ('11.6.2', 'cuda_11.6.2_510.47.03_linux.run'),
        ('11.7.0', 'cuda_11.7.0_515.43.04_linux.run'),
        ('11.7.1', 'cuda_11.7.1_515.65.01_linux.run'),
        ('11.8.0', 'cuda_11.8.0_520.61.05_linux.run'),
        ('12.0.0', 'cuda_12.0.0_525.60.13_linux.run'),
        ('12.0.1', 'cuda_12.0.1_525.85.12_linux.run'),
        ('12.1.0', 'cuda_12.1.0_530.30.02_linux.run'),
        ('12.1.1', 'cuda_12.1.1_530.30.02_linux.run'),
        ('12.2.0', 'cuda_12.2.0_535.54.03_linux.run'),
        ('12.2.1', 'cuda_12.2.1_535.86.10_linux.run'),
        ('12.2.2', 'cuda_12.2.2_535.104.05_linux.run'),
        ('12.3.1', 'cuda_12.3.1_545.23.08_linux.run'),
        ('12.3.2', 'cuda_12.3.2_545.23.08_linux.run'),
        ('12.4.1', 'cuda_12.4.1_550.54.15_linux.run')
    ],
    value='cuda_11.5.0_495.29.05_linux.run',
    description='CUDA版本:',
    )

    # 创建一个下拉菜单让用户选择是否安装NVIDIA驱动
    nvidia_driver_dropdown = widgets.Dropdown(
        options=[
            ('不安装', None),
            ('NVIDIA 535.154.05', 'NVIDIA-Linux-x86_64-535.154.05.run'),
            ('NVIDIA 550.54.14', 'NVIDIA-Linux-x86_64-550.54.14.run')
        ],
        value=None,
        description='NVIDIA驱动:',
    )
    
    # 创建下载驱动规则的下拉菜单
    download_rule_dropdown = widgets.Dropdown(
        options=[
            ('总是', 'Always'),
            ('本地', 'IfNotPresent')
           
        ],
        value='IfNotPresent',  # 默认值
        description='下载规则:',
    )
    return cuda_version_dropdown, nvidia_driver_dropdown, download_rule_dropdown
def update_cuda_version(file_path, cuda_version):
    # 定义要替换或追加的行
    path_line = f"export PATH=/usr/local/cuda-{cuda_version}/bin:$PATH  \n\
"
    ld_line = f"export LD_LIBRARY_PATH=/usr/local/cuda-{cuda_version}/lib64:$LD_LIBRARY_PATH  \n\
"
    
    # 尝试读取文件内容
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print(f"文件 {file_path} 未找到。")
        return

    # 检查文件是否已包含相关行
    path_exists = any("export PATH=/usr/local/cuda-" in line for line in lines)
    ld_exists = any("export LD_LIBRARY_PATH=/usr/local/cuda-" in line for line in lines)

    # 替换或追加内容
    with open(file_path, 'w') as file:
        for line in lines:
            # 替换现有行
            if "export PATH=/usr/local/cuda-" in line:
                file.write(path_line)
            elif "export LD_LIBRARY_PATH=/usr/local/cuda-" in line:
                file.write(ld_line)
            else:
                file.write(line)
                
        # 如果不存在，则追加
        if not path_exists:
            file.write(path_line)
        if not ld_exists:
            file.write(ld_line)

def check_driver_present(driver_name):
    """
    检查指定的NVIDIA驱动文件是否存在于本地文件系统中。
    :param driver_name: 驱动文件名称，例如 'NVIDIA-Linux-x86_64-550.54.14.run'
    :return: 如果文件存在返回True，否则返回False
    """
    # 假设驱动文件存放在某个特定的目录下，例如 "/usr/local/drivers"
    # 你可以根据实际情况修改这个路径
    driver_path = os.path.join("./", driver_name)
    
    # 使用os.path.exists检查文件是否存在
    if os.path.exists(driver_path):
        print(f"驱动文件 {driver_name} 存在于 {driver_path}。")
        return True
    else:
        print(f"驱动文件 {driver_name} 不存在于 {driver_path}。")
        return False

def install_cuda_and_driver(cuda_version, nvidia_driver, download_rule, base_url, file_path):
    version_number_string = cuda_version.split('_')[1]  # 结果是 '12.2.1'
    major_minor_version = '.'.join(version_number_string.split('.')[:2])  # 结果是 '12.2'
    if download_rule == 'Always' or (download_rule == 'IfNotPresent' and not check_driver_present(cuda_version)):
        #print(f"开始下载CUDA {cuda_version_dropdown.label}...")
        cuda_install_command = f"wget {base_url}{cuda_version}"
        subprocess.run(cuda_install_command, shell=True, check=True)
    
    chmod_command = f"chmod +x {cuda_version}"
    subprocess.run(chmod_command, shell=True, check=True)
    #print(f"开始安装CUDA {cuda_version_dropdown.label}...")
    install_command = f"./{cuda_version} --silent --toolkit"
    subprocess.run(install_command, shell=True, check=True)
    #print(f"CUDA {cuda_version_dropdown.label} 安装完成。")
                         
    update_cuda_version(file_path, major_minor_version)
    #source_command = f"source /root/.bashrc"
    #subprocess.run(source_command, shell=True, check=True)
   
	# Source ~/.bashrc to apply changes immediately
    #subprocess.run(["source", f"/root/.bashrc"], shell=True, executable="/bin/bash")

    # 如果用户选择了安装NVIDIA驱动
    if nvidia_driver:
        if download_rule == 'Always' or (download_rule == 'IfNotPresent' and not check_driver_present(nvidia_driver)):
            #print(f"开始下载NVIDIA驱动 {nvidia_driver_dropdown.label}...")
            driver_install_command = f"wget {base_url}{nvidia_driver}"
            subprocess.run(driver_install_command, shell=True, check=True)
        chmod_command = f"chmod +x {nvidia_driver}"
        subprocess.run(chmod_command, shell=True, check=True)
        #print(f"开始安装NVIDIA驱动 {cuda_version_dropdown.label}...")
        install_command = f"./{nvidia_driver} --no-questions --ui=none --dkms"
        subprocess.run(install_command, shell=True, check=True)
        #print(f"NVIDIA驱动 {nvidia_driver_dropdown.label} 安装完成。")
    print(f"请在自己的ssh界面上执行 source /root/.bashrc，或者打开新的ssh界面")
