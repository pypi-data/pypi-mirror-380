"""
基本使用示例

这个示例展示了GridWorldPy的基本功能，包括:
- 创建环境
- 设置奖励和策略
- 执行动作和渲染
"""

import numpy as np
from gridworldpy import GridWorldEnv
import time


def basic_example():
    """基本使用示例"""
    print("=== GridWorldPy 基本使用示例 ===")

    # 创建一个5x5的网格世界
    env = GridWorldEnv(
        grid_size=(5, 5),
        keyboard_control=False,  # 自动模式
        terminal_condition=(4, 4)  # 目标位置为右下角
    )

    # 设置随机奖励
    env.set_rewards('random')
    print("✓ 已设置随机奖励")

    # 设置随机策略
    env.set_policy('random')
    print("✓ 已设置随机策略")

    # 渲染初始环境
    env.render()
    print("✓ 初始环境已渲染")

    # 执行一些随机步骤
    for step in range(10):
        action = np.random.randint(0, 5)  # 随机选择动作
        obs, reward, done, info = env.step(action)

        print(f"步骤 {step+1}: 动作={action}, 奖励={reward:.3f}, 完成={done}")

        # 渲染当前状态
        env.render()

        if done:
            print(f"环境已完成！总步数: {info['step_count']}")
            break

        time.sleep(1)  # 暂停1秒便于观察

    # 保持窗口打开几秒钟
    time.sleep(3)
    env.close()
    print("示例完成！")


def interactive_example():
    """交互式示例（需要键盘控制）"""
    print("\n=== 交互式示例 ===")
    print("按空格键控制执行...")

    # 创建带键盘控制的环境
    env = GridWorldEnv(
        grid_size=(3, 3),
        keyboard_control=True,  # 启用键盘控制
        terminal_condition=10   # 最大10步
    )

    # 设置特定奖励
    rewards = [
        (0, 0, 0.0),   # 起始位置
        (1, 1, -1.0),  # 陷阱
        (2, 2, 1.0),   # 目标
    ]
    env.set_rewards(rewards)

    # 设置倾向于向右下移动的策略
    policy = [
        (0, 0, [0.1, 0.1, 0.4, 0.1, 0.3]),  # 偏向下和右
        (0, 1, [0.1, 0.1, 0.3, 0.1, 0.4]),  # 偏向右
        (1, 0, [0.1, 0.1, 0.3, 0.1, 0.4]),  # 偏向下
    ]
    env.set_policy(policy)

    # 初始渲染
    env.render()

    # 交互式执行
    for step in range(10):
        action = np.random.choice(5, p=env.get_current_policy())
        obs, reward, done, info = env.step(action)

        print(f"步骤 {step+1}: 位置={obs}, 奖励={reward:.3f}")

        # 渲染并等待用户输入
        env.render()

        if done:
            print(f"完成！原因: {info['exit_reason']}")
            break

    env.close()


if __name__ == "__main__":
    # 运行基本示例
    basic_example()

    # 询问是否运行交互式示例
    response = input("\n是否运行交互式示例？(y/n): ")
    if response.lower() == 'y':
        interactive_example()
