import networkx as nx
import matplotlib.pyplot as plt

# 定义数据
course_data = {
    'case': 'Python编程',
    'chapters': [
        {
            'chapter': '第一章',
            'chapter_name': 'Python基础',
            'contents': [
                {
                    'knowledge': '变量、数据类型',
                    'teaching_method': '演示、练习',
                    'blend': '代码规范',
                    'ideological_element': '开源、自由'
                },
                {
                    'knowledge': '流程控制、函数',
                    'teaching_method': '演示、练习',
                    'blend': '代码规范',
                    'ideological_element': '协作、分享'
                }
            ]
        },
        {
            'chapter': '第二章',
            'chapter_name': 'Python高级',
            'contents': [
                {
                    'knowledge': '面向对象编程',
                    'teaching_method': '演示、练习',
                    'blend': '设计模式',
                    'ideological_element': '创新、创业'
                },
                {
                    'knowledge': '网络编程、多线程',
                    'teaching_method': '演示、练习',
                    'blend': '实践案例',
                    'ideological_element': '服务、奉献'
                }
            ]
        }
    ]
}


# 定义绘制思维导图的函数
def draw_course_map(course_data, save_path):
    # 创建有向无环图
    G = nx.DiGraph()

    # 添加根节点
    G.add_node(course_data['case'], layer=0)

    # 遍历章节信息
    for chapter in course_data['chapters']:
        # 添加章节节点
        G.add_node(chapter['chapter'], layer=1)
        # 添加章节到根节点的有向边
        G.add_edge(course_data['case'], chapter['chapter'])

        # 遍历章节内容
        for content in chapter['contents']:
            # 添加内容节点
            G.add_node(content['knowledge'], layer=2)
            # 添加内容到章节的有向边
            G.add_edge(chapter['chapter'], content['knowledge'])

    # 定义不同层级的节点样式和布局
    node_styles = [
        {'node_shape': 'o', 'node_color': 'red'},  # 根节点
        {'node_shape': 's', 'node_color': 'blue'},  # 章节节点
        {'node_shape': 'd', 'node_color': 'green'}  # 内容节点
    ]
    node_layouts = [
        nx.multipartite_layout(G, subset_key="layer"),  # 多层级布局
        nx.shell_layout(G),  # 圆形布局
        nx.spring_layout(G),  # 弹簧布局
    ]

    # 绘制节点和边
    plt.figure(figsize=(15, 10))
    for i, (style, layout) in enumerate(zip(node_styles, node_layouts)):
        nodes = [n for n in G.nodes if G.nodes[n]['layer'] == i]
        nx.draw_networkx_nodes(G, layout, nodelist=nodes, node_shape=style['node_shape'],
                               node_color=style['node_color'])
        nx.draw_networkx_labels(G, layout, labels={n: n for n in nodes}, font_size=12)
    nx.draw_networkx_edges(G, nx.shell_layout(G), edgelist=G.edges(), edge_color='black', arrowsize=10)

    # 设置图像样式
    plt.axis('off')
    plt.title(course_data['case'], fontdict={'fontsize': 20})

    # 保存图片
    plt.savefig(save_path)

draw_course_map(course_data,'思维导图.png')