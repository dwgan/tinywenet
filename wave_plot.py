import matplotlib
import numpy as np
import matplotlib.pyplot as plt

# 切换到非交互式后端
matplotlib.use('Agg')

def plot_tensor(tensor, save_path='tensor_plot.png'):
    """
    绘制一个 tensor 并保存为图像文件

    参数:
    - tensor: 要绘制的 tensor (可以是 NumPy 数组或 PyTorch tensor)
    - save_path: 保存图像的路径 (默认: 'tensor_plot.png')
    """
    # 确保输入的 tensor 是一维数组
    if isinstance(tensor, np.ndarray):
        tensor = tensor.flatten()
    else:
        tensor = tensor.numpy().flatten()  # 如果是 PyTorch tensor 转换为 NumPy 数组

    # 绘制图像
    plt.plot(tensor)
    plt.title('Tensor Plot')
    plt.xlabel('Index')
    plt.ylabel('Value')

    # 保存图像到指定路径
    plt.savefig(save_path)
    print(f"图像已保存到 {save_path}")