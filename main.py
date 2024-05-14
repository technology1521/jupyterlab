import ipywidgets as widgets
from IPython.display import display

# 导入xl_jupyterlab包下的change_cuda_and_nvidia模块
from xl_jupyterlab import change_cuda_and_nvidia
from xl_jupyterlab.install import apt_install_ui

base_url = "http://mirrors.chukk.cc:8866/cuda/"
file_path = "/root/.bashrc"  # 文件路径



def launch_ui():
    def update_cuda_ui():
        result = change_cuda_and_nvidia.create_cuda_ui_components()
        if result is None:
        # 处理None返回值的情况，例如通过显示错误消息或返回一个空的UI组件
            return widgets.Label('无法创建CUDA UI组件，可能是因为缺少必要的配置或数据。')
          # 调用函数并接收返回的组件
        cuda_version_dropdown, nvidia_driver_dropdown, download_rule_dropdown = change_cuda_and_nvidia.create_cuda_ui_components()
        # 创建安装按钮
        install_button = widgets.Button(description="安装CUDA和驱动")

        # 定义按钮点击事件的处理函数
        def on_install_button_clicked(b):
            # 这里是安装CUDA和驱动的逻辑
            cuda_version = cuda_version_dropdown.value
            nvidia_driver = nvidia_driver_dropdown.value
            download_rule = download_rule_dropdown.value
            global base_url, file_path
            # 注意：确保install_cuda_and_driver函数的定义与这里的参数匹配
            change_cuda_and_nvidia.install_cuda_and_driver(cuda_version, nvidia_driver, download_rule, base_url, file_path)

        # 绑定事件处理函数到按钮
        install_button.on_click(on_install_button_clicked)
        
        # 使用VBox或其他布局组件来垂直排列或以其他方式组织这些控件
        ui_components = widgets.VBox([cuda_version_dropdown, nvidia_driver_dropdown, download_rule_dropdown, install_button])
        
        # 返回包含所有UI组件的容器，而不是单个Label
        return ui_components
    
    def connect_git_ui():
        return widgets.Label('连接到Git的UI组件')
    
    def download_stuff_ui():
        return widgets.Label('下载特定链接内容的UI组件')
    
    def apt_install_ui_wrapper():
        return apt_install_ui()
    
    def pip_env_switch_ui():
        return widgets.Label('切换pip环境的UI组件')
    
    # 创建Tab组件
    tab = widgets.Tab()
    
    # 创建每个Tab的内容
    children = [
        update_cuda_ui(),
        connect_git_ui(),
        download_stuff_ui(),
        apt_install_ui_wrapper(),
        pip_env_switch_ui()
    ]
    
    # 设置Tab的子组件
    
    tab.children = children
    
    # 为每个Tab设置标题
    titles = ['更新CUDA', '连接Git', '下载内容', '安装软件', '切换环境']
    for i, title in enumerate(titles):
        tab.set_title(i, title)
    
    # 显示Tab UI
    display(tab)

