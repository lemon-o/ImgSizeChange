import os
from PIL import Image, ImageFilter, ImageEnhance

def process_all_images_in_folder(input_folder, output_folder):
    # 获取脚本所在的文件夹路径
    input_folder = os.path.dirname(os.path.realpath(__file__))
    # 遍历目录中的所有文件
    for filename in os.listdir(input_folder):
        file_path = os.path.join(input_folder, filename)
        # 筛选出图片文件（假定为常见的图片格式，可根据实际情况扩展）
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            process_image(file_path, output_folder)

def process_image(input_path, output_folder):
    # 打开图片
    img = Image.open(input_path)
    # 将图片宽度修改，高度随比例改变
    target_width = 127
    w_percent = target_width / float(img.size[0])
    target_height = int(float(img.size[1]) * float(w_percent))
    img = img.resize((target_width, target_height), Image.LANCZOS)  # 或者使用 Image.BICUBIC
    # 确保 output 文件夹存在，如果不存在则创建
    output_folder = os.path.join(os.path.dirname(os.path.realpath(__file__)), "output")
    os.makedirs(output_folder, exist_ok=True) 
    # 将图片存储为 png 格式，保存到 output 文件夹中
    output_path = os.path.join(output_folder, f"{os.path.splitext(os.path.basename(input_path))[0]}.png")
    img.save(output_path, format='PNG')
    print(f"处理完成：{os.path.basename(output_path)}")

if __name__ == "__main__":
    # 处理当前脚本所在目录中的所有图片文件，保存到 output 文件夹中
    process_all_images_in_folder(os.path.dirname(os.path.realpath(__file__)), "output")
