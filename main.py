import ipywidgets as widgets
from IPython.display import display

# 导入xl_jupyterlab包下的change_cuda_and_nvidia模块
from xl_jupyterlab import change_cuda_and_nvidia




def launch_ui():
    # 模拟的功能模块
    #def update_cuda_ui():
    #    return widgets.Label('更新CUDA版本的UI组件')
    def update_cuda_ui():
        # 创建CUDA版本下拉菜单
        
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
        
        
        
        
        
        
        
        # 创建安装按钮
        install_button = widgets.Button(description="安装CUDA和驱动")
        
        # 定义按钮点击事件的处理函数
        def on_install_button_clicked(b):
            # 这里是安装CUDA和驱动的逻辑
            # 例如，可以调用之前定义的install_cuda_and_driver函数
            pass
        
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
    
    def apt_install_ui():
        return widgets.Label('使用apt安装软件的UI组件')
    
    def pip_env_switch_ui():
        return widgets.Label('切换pip环境的UI组件')
    
    # 创建Tab组件
    tab = widgets.Tab()
    
    # 创建每个Tab的内容
    children = [
        update_cuda_ui(),
        connect_git_ui(),
        download_stuff_ui(),
        apt_install_ui(),
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

