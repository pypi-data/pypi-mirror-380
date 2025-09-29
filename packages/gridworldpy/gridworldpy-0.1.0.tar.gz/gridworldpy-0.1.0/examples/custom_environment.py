"""
自定义环境配置示例

这个示例展示了如何创建自定义的网格世界环境，包括:
- 自定义网格大小和外观
- 设置特定的奖励分布
- 配置策略
- 禁用状态（创建障碍物）
- 状态价值可视化
"""

import numpy as np
from gridworldpy import GridWorldEnv
import time


def maze_environment():
    """创建一个迷宫环境"""
    print("=== 迷宫环境示例 ===")

    # 创建4x4的迷宫
    env = GridWorldEnv(
        grid_size=(4, 4),
        keyboard_control=False,
        terminal_condition=(3, 3),  # 目标在右下角
        cell_size=120,
        circle_radius=30,
        font_size=12
    )

    # 设置奖励：目标高奖励，其他位置小负奖励
    rewards = [
        # 路径奖励
        (0, 0, -0.1), (0, 1, -0.1), (0, 3, -0.1),
        (1, 1, -0.1), (1, 3, -0.1),
        (2, 0, -0.1), (2, 1, -0.1), (2, 2, -0.1), (2, 3, -0.1),
        (3, 0, -0.1), (3, 1, -0.1), (3, 2, -0.1),
        # 目标奖励
        (3, 3, 1.0),
        # 陷阱
        (1, 0, -1.0),
        (0, 2, -0.5),
    ]
    env.set_rewards(rewards)

    # 创建障碍物（禁用状态）
    obstacles = [(1, 2), (2, 3)]  # 在(1,2)和(2,3)位置放置障碍物
    env.disable_states(obstacles)

    # 设置智能策略：避开障碍物，朝目标移动
    policy = [
        # 起始位置：主要向右
        (0, 0, [0.1, 0.1, 0.2, 0.1, 0.5]),
        # 第一行：向右或向下
        (0, 1, [0.1, 0.1, 0.3, 0.2, 0.3]),
        (0, 3, [0.1, 0.1, 0.7, 0.1, 0.0]),
        # 第二行：避开障碍物
        (1, 1, [0.1, 0.1, 0.6, 0.1, 0.1]),  # 主要向下
        (1, 3, [0.1, 0.1, 0.6, 0.2, 0.0]),
        # 第三行：向目标移动
        (2, 0, [0.1, 0.2, 0.2, 0.0, 0.5]),
        (2, 1, [0.1, 0.1, 0.1, 0.1, 0.6]),
        (2, 2, [0.1, 0.1, 0.6, 0.1, 0.1]),
        # 最后一行：向目标
        (3, 0, [0.1, 0.3, 0.0, 0.0, 0.6]),
        (3, 1, [0.1, 0.2, 0.0, 0.1, 0.6]),
        (3, 2, [0.1, 0.1, 0.0, 0.1, 0.7]),
    ]
    env.set_policy(policy)

    print("✓ 迷宫环境已创建")
    print("  - 4x4网格")
    print("  - 障碍物在(1,2)和(2,3)")
    print("  - 目标在(3,3)")
    print("  - 智能策略：避开障碍物")

    # 渲染初始环境
    env.render()

    # 模拟智能体移动
    for step in range(15):
        # 使用当前位置的策略选择动作
        current_policy = env.get_current_policy()
        action = np.random.choice(5, p=current_policy)

        obs, reward, done, info = env.step(action)
        print(f"步骤 {step+1}: 位置={obs}, 动作={action}, 奖励={reward:.3f}")

        env.render()

        if done:
            print(f"到达目标！总步数: {info['step_count']}")
            break

        time.sleep(0.8)

    time.sleep(2)
    env.close()


def value_visualization_example():
    """状态价值可视化示例"""
    print("\n=== 状态价值可视化示例 ===")

    # 创建3x3环境
    env = GridWorldEnv(
        grid_size=(3, 3),
        keyboard_control=False,
        terminal_condition=(2, 2),
        cell_size=140,
        circle_radius=40
    )

    # 简单的奖励设置
    rewards = [
        (0, 0, 0.0), (0, 1, 0.0), (0, 2, 0.0),
        (1, 0, 0.0), (1, 1, -0.5), (1, 2, 0.0),
        (2, 0, 0.0), (2, 1, 0.0), (2, 2, 1.0),
    ]
    env.set_rewards(rewards)

    # 设置均匀策略
    env.set_policy('random')

    print("\n演示状态价值的变化...")

    # 模拟价值迭代过程
    for iteration in range(5):
        print(f"\n价值迭代 {iteration + 1}:")

        # 生成模拟的状态价值（这里用简单的距离启发式）
        state_values = []
        for i in range(3):
            for j in range(3):
                # 基于到目标的距离计算价值
                distance = abs(i - 2) + abs(j - 2)
                if (i, j) == (2, 2):  # 目标状态
                    value = 1.0
                elif (i, j) == (1, 1):  # 陷阱
                    value = -0.5
                else:
                    # 距离越近价值越高
                    value = 1.0 - 0.2 * distance - 0.1 * iteration

                state_values.append((i, j, value))

        # 渲染带状态价值的环境
        env.render(state_values=state_values)
        time.sleep(1.5)

    time.sleep(2)
    env.close()


def large_environment_example():
    """大型环境示例"""
    print("\n=== 大型环境示例 ===")

    # 创建7x7的大型环境
    env = GridWorldEnv(
        grid_size=(7, 7),
        keyboard_control=False,
        terminal_condition=50,  # 最大50步
        cell_size=80,
        circle_radius=20,
        font_size=10,
        max_arrow_length=30
    )

    # 设置渐变奖励：中心高，边缘低
    rewards = []
    center = (3, 3)
    for i in range(7):
        for j in range(7):
            distance = max(abs(i - center[0]), abs(j - center[1]))
            reward = 0.5 - 0.1 * distance  # 中心0.5，边缘-0.1
            rewards.append((i, j, reward))

    env.set_rewards(rewards)

    # 设置向中心移动的策略
    policy = []
    for i in range(7):
        for j in range(7):
            # 计算到中心的方向
            di = center[0] - i  # 需要移动的行差
            dj = center[1] - j  # 需要移动的列差

            # 基础概率
            probs = [0.1, 0.1, 0.1, 0.1, 0.1]  # [保持, 上, 下, 左, 右]

            # 根据方向调整概率
            if di > 0:  # 需要向下
                probs[2] += 0.3
            elif di < 0:  # 需要向上
                probs[1] += 0.3

            if dj > 0:  # 需要向右
                probs[4] += 0.3
            elif dj < 0:  # 需要向左
                probs[3] += 0.3

            # 归一化
            total = sum(probs)
            probs = [p/total for p in probs]

            policy.append((i, j, probs))

    env.set_policy(policy)

    print("✓ 大型7x7环境已创建")
    print("  - 中心高奖励，边缘低奖励")
    print("  - 策略倾向于向中心移动")

    # 渲染并运行
    env.render()

    for step in range(20):
        current_policy = env.get_current_policy()
        action = np.random.choice(5, p=current_policy)

        obs, reward, done, info = env.step(action)

        if step % 3 == 0:  # 每3步显示一次信息
            print(f"步骤 {step+1}: 位置={obs}, 累计奖励={reward:.3f}")

        env.render()

        if done:
            print(f"达到最大步数！位置: {obs}")
            break

        time.sleep(0.5)

    time.sleep(2)
    env.close()


if __name__ == "__main__":
    # 运行迷宫示例
    maze_environment()

    # 运行状态价值可视化示例
    value_visualization_example()

    # 运行大型环境示例
    large_environment_example()

    print("\n所有自定义环境示例完成！")
