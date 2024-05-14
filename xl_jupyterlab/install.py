
import ipywidgets as widgets

def apt_install_ui():
    # 分类1的内容
    category1_content = widgets.VBox([
        widgets.Label('这里是第一个分类的内容。'),
        widgets.Button(description='安装软件1')
    ])
    
    # 分类2的内容
    category2_content = widgets.VBox([
        widgets.Label('这里是第二个分类的内容。'),
        widgets.Button(description='安装软件2')
    ])
    
    # 创建Accordion
    accordion = widgets.Accordion(children=[category1_content, category2_content])
    
    # 为每个分类设置标题
    accordion.set_title(0, '分类1')
    accordion.set_title(1, '分类2')
    
    # 返回Accordion小部件
    return accordion

