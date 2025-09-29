# walitool: 差分进化优化工具库

`walitool` 是一个轻量级的差分进化（Differential Evolution, DE）优化算法工具库，基于 NumPy 和 Numba 实现，专注于提供高效、易用的全局优化解决方案，适用于科学计算、工程优化等场景。


## 核心特性

- **高效计算**：使用 Numba 进行 JIT 编译加速，大幅提升算法运行效率
- **简洁接口**：封装完整的差分进化流程，提供直观的 API 接口
- **灵活配置**：支持自定义参数（种群大小、迭代次数、交叉概率等）
- **边界处理**：内置变量边界约束处理机制
- **轻量依赖**：仅依赖 NumPy 和 Numba，易于部署


## 安装方法

### 从源码安装
```bash
git clone https://github.com/waliwuao/walitool.git
cd walitool
pip install .
```

### 开发模式安装（用于本地开发）
```bash
pip install -e .[dev]
```


## 快速开始

以下是使用 `walitool` 求解函数最小值的简单示例：

```python
import numpy as np
from walitool import DE

# 定义目标函数（以Sphere函数为例）
def sphere(x):
    return np.sum(x**2)

# 初始化差分进化优化器
de = DE(
    func=sphere,          # 目标函数
    dim=30,               # 变量维度
    popsize=50,           # 种群大小
    lower_bound=-100,     # 变量下界（标量或数组）
    upper_bound=100,      # 变量上界（标量或数组）
    f1=0.8,               # 差分权重1
    f2=0.2,               # 差分权重2
    cr=0.9,               # 交叉概率
    maxiter=1000,         # 最大迭代次数
    logging=True          # 打印日志
)

# 执行优化
best_position, best_fitness = de.optimize()

# 输出结果
print(f"最优解: {best_position}")
print(f"最优适应度: {best_fitness}")
```


## 核心组件说明

`walitool` 的差分进化算法由以下核心组件构成：

1.** 种群生成器（Generator）**- 负责初始化种群，支持根据变量边界生成均匀分布的初始解

2.** 变异操作（Mutate）**- 实现差分变异策略，生成变异向量
   - 支持自定义变异权重（f1, f2）

3.** 交叉操作（Crossover）**- 对父代和变异向量进行交叉，生成试验向量
   - 支持交叉概率（cr）配置，确保种群多样性

4.** 选择操作（Selection）**- 基于适应度值选择更优个体保留到下一代
   - 采用贪婪选择策略，保留更优解

5.** 优化器（DE）**- 整合上述组件，提供完整的差分进化流程
   - 支持迭代过程日志记录，便于监控优化进度


## 参数说明

| 参数名        | 类型          | 描述                          | 默认值       |
|---------------|---------------|-------------------------------|--------------|
| `func`        | 函数          | 待优化的目标函数（求最小值）  | 无           |
| `dim`         | int           | 变量维度                      | 无           |
| `popsize`     | int           | 种群大小                      | 50           |
| `lower_bound` | 标量/数组     | 变量下界                      | 0（全维度）  |
| `upper_bound` | 标量/数组     | 变量上界                      | 1（全维度）  |
| `f1`          | float         | 差分变异权重1                 | 1.0          |
| `f2`          | float         | 差分变异权重2                 | 0.01         |
| `cr`          | float         | 交叉概率（0-1）               | 0.95         |
| `maxiter`     | int           | 最大迭代次数                  | 100          |
| `logging`     | bool          | 是否打印迭代日志              | False        |
| `dtype`       | numpy dtype   | 数值类型                      | np.float64   |


## 注意事项

- 目标函数需接收 NumPy 数组作为输入，并返回标量适应度值
- 若变量各维度边界不同，可传入与维度相同长度的数组作为 `lower_bound`/`upper_bound`
- 对于复杂优化问题，建议调整 `popsize`、`f1`、`f2`、`cr` 等参数以获得更好性能
- 日志打印频率为每100代一次（可在源码中修改）


## 开发与贡献

克隆仓库并安装开发依赖：
   ```bash
   git clone https://github.com/waliwuao/walitool.git
   cd walitool
   pip install -e .[dev]
   ```
欢迎提交 Issue 和 Pull Request 帮助改进本项目！


## 许可证

本项目基于 MIT 许可证开源，详情参见 [LICENSE](LICENSE) 文件。
