import os

def generate_file_list():
    # 1. 定义要添加的前缀
    prefix = "https://my2025.btm-m.site/"
    
    # 2. 定义输出结果的文件名
    output_filename = "url_list.txt"
    
    # 获取脚本当前所在的绝对路径
    # 这样做可以确保无论你在哪里运行脚本，它都只扫描脚本所在的目录
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # 获取当前脚本自己的文件名，以便在列表中排除它
    script_name = os.path.basename(__file__)
    
    print(f"正在扫描目录: {current_dir} ...")
    
    try:
        # 获取目录下的所有项
        all_items = os.listdir(current_dir)
        
        # 准备写入文件
        # 使用 utf-8 编码以支持中文文件名
        with open(os.path.join(current_dir, output_filename), 'w', encoding='utf-8') as f:
            count = 0
            for item in all_items:
                full_path = os.path.join(current_dir, item)
                
                # 判断是否为文件 (排除文件夹)
                if os.path.isfile(full_path):
                    # 过滤掉脚本自身和输出文件自身，不让它们出现在列表中
                    if item == script_name or item == output_filename:
                        continue
                    
                    # 拼接前缀和文件名
                    full_url = prefix + item
                    
                    # 写入文件并换行
                    f.write(full_url + '\n')
                    count += 1
                    
        print("-" * 30)
        print(f"处理完成！")
        print(f"共扫描并生成了 {count} 条链接。")
        print(f"结果已保存至同目录下的: {output_filename}")
        print("-" * 30)
        
    except Exception as e:
        print(f"发生错误: {e}")

if __name__ == "__main__":
    generate_file_list()
    # 这一行是为了防止双击运行脚本时窗口瞬间关闭，让你能看到结果
    input("按回车键退出...")