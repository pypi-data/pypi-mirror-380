#!/usr/bin/env python3
"""
强化学习示例

这个示例展示了如何在GridWorldPy中实现简单的强化学习算法:
- Q学习算法
- 策略评估
- 价值迭代可视化
"""

import numpy as np
from gridworldpy import GridWorldEnv
import time


class SimpleQLearning:
    """简单的Q学习实现"""

    def __init__(self, grid_size, learning_rate=0.1, discount_factor=0.9, epsilon=0.1):
        self.grid_size = grid_size
        self.lr = learning_rate
        self.gamma = discount_factor
        self.epsilon = epsilon

        # 初始化Q表：[行][列][动作]
        self.q_table = np.zeros((grid_size[0], grid_size[1], 5))

    def get_action(self, state):
        """使用epsilon-贪心策略选择动作"""
        if np.random.random() < self.epsilon:
            return np.random.randint(0, 5)  # 随机动作
        else:
            x, y = state
            return np.argmax(self.q_table[x, y])  # 贪心动作

    def update_q_table(self, state, action, reward, next_state, done):
        """更新Q表"""
        x, y = state
        nx, ny = next_state

        current_q = self.q_table[x, y, action]

        if done:
            target_q = reward
        else:
            max_next_q = np.max(self.q_table[nx, ny])
            target_q = reward + self.gamma * max_next_q

        # Q学习更新规则
        self.q_table[x, y, action] += self.lr * (target_q - current_q)

    def get_policy(self):
        """从Q表中提取策略"""
        policy = []
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                # 获取最优动作的概率分布
                q_values = self.q_table[i, j]

                # 使用softmax将Q值转换为概率
                exp_q = np.exp(q_values - np.max(q_values))
                probs = exp_q / np.sum(exp_q)

                policy.append((i, j, probs.tolist()))

        return policy

    def get_state_values(self):
        """从Q表中提取状态价值"""
        values = []
        for i in range(self.grid_size[0]):
            for j in range(self.grid_size[1]):
                value = np.max(self.q_table[i, j])
                values.append((i, j, value))
        return values


def q_learning_example():
    """Q学习训练示例"""
    print("=== Q学习训练示例 ===")

    # 创建环境
    env = GridWorldEnv(
        grid_size=(4, 4),
        keyboard_control=False,
        terminal_condition=(3, 3),  # 目标位置
        cell_size=120
    )

    # 设置奖励：目标高奖励，陷阱负奖励
    rewards = [
        # 目标
        (3, 3, 1.0),
        # 陷阱
        (1, 1, -1.0),
        (2, 1, -0.5),
        # 其他位置小负奖励（鼓励快速到达目标）
    ]
    for i in range(4):
        for j in range(4):
            if (i, j) not in [(3, 3), (1, 1), (2, 1)]:
                rewards.append((i, j, -0.02))

    env.set_rewards(rewards)

    # 初始化Q学习算法
    q_learner = SimpleQLearning(grid_size=(4, 4))

    print("开始Q学习训练...")

    # 训练阶段
    episodes = 100
    for episode in range(episodes):
        # 重置环境
        env.state = (0, 0)  # 重置到起始位置
        env.step_count = 0

        total_reward = 0
        steps = 0

        while steps < 50:  # 最大步数限制
            state = env.state
            action = q_learner.get_action(state)

            # 执行动作
            next_state, reward, done, info = env.step(action)

            # 更新Q表
            q_learner.update_q_table(state, action, reward, next_state, done)

            total_reward += reward
            steps += 1

            if done:
                break

        # 每20轮显示一次进度
        if (episode + 1) % 20 == 0:
            print(f"轮次 {episode + 1}: 平均奖励 = {total_reward:.3f}, 步数 = {steps}")

            # 可视化学习进度
            if (episode + 1) % 40 == 0:
                print(f"显示第 {episode + 1} 轮的策略和价值...")
                env.state = (0, 0)  # 重置位置用于显示

                # 获取当前策略和状态价值
                policy = q_learner.get_policy()
                state_values = q_learner.get_state_values()

                # 渲染
                env.render(state_values=state_values, policy_config=policy)
                time.sleep(2)

    print("\nQ学习训练完成！")

    # 测试训练好的策略
    print("\n测试训练好的策略...")
    env.state = (0, 0)
    env.step_count = 0

    # 使用学习到的策略
    policy = q_learner.get_policy()
    state_values = q_learner.get_state_values()
    env.set_policy(policy)

    # 执行测试
    for step in range(20):
        state = env.state
        # 使用贪心策略（不探索）
        q_values = q_learner.q_table[state[0], state[1]]
        action = np.argmax(q_values)

        next_state, reward, done, info = env.step(action)

        print(f"测试步骤 {step+1}: {state} -> 动作{action} -> {next_state}, 奖励={reward:.3f}")

        # 渲染当前状态
        env.render(state_values=state_values)

        if done:
            print(f"成功到达目标！总步数: {info['step_count']}")
            break

        time.sleep(1)

    time.sleep(3)
    env.close()


def policy_evaluation_example():
    """策略评估示例"""
    print("\n=== 策略评估示例 ===")

    # 创建小型环境便于观察
    env = GridWorldEnv(
        grid_size=(3, 3),
        keyboard_control=False,
        terminal_condition=(2, 2),
        cell_size=150
    )

    # 简单奖励设置
    rewards = [
        (0, 0, 0.0), (0, 1, 0.0), (0, 2, 0.0),
        (1, 0, 0.0), (1, 1, -0.5), (1, 2, 0.0),
        (2, 0, 0.0), (2, 1, 0.0), (2, 2, 1.0),
    ]
    env.set_rewards(rewards)

    # 定义一个简单策略：倾向于向右下移动
    fixed_policy = [
        (0, 0, [0.1, 0.1, 0.3, 0.1, 0.4]),  # 向下和向右
        (0, 1, [0.1, 0.1, 0.4, 0.1, 0.3]),
        (0, 2, [0.1, 0.1, 0.7, 0.1, 0.0]),
        (1, 0, [0.1, 0.1, 0.3, 0.1, 0.4]),
        (1, 1, [0.2, 0.2, 0.2, 0.2, 0.2]),  # 陷阱：均匀分布
        (1, 2, [0.1, 0.1, 0.6, 0.2, 0.0]),
        (2, 0, [0.1, 0.2, 0.0, 0.1, 0.6]),
        (2, 1, [0.1, 0.2, 0.0, 0.1, 0.6]),
        (2, 2, [1.0, 0.0, 0.0, 0.0, 0.0]),  # 目标：停留
    ]

    env.set_policy(fixed_policy)

    print("使用固定策略进行价值评估...")

    # 模拟价值迭代过程
    values = np.zeros((3, 3))
    gamma = 0.9  # 折扣因子

    for iteration in range(10):
        new_values = np.zeros((3, 3))

        for i in range(3):
            for j in range(3):
                if (i, j) == (2, 2):  # 终止状态
                    new_values[i, j] = 1.0
                    continue

                # 获取当前状态的策略
                policy_probs = None
                for pi, pj, probs in fixed_policy:
                    if pi == i and pj == j:
                        policy_probs = probs
                        break

                if policy_probs is None:
                    continue

                # 计算期望价值
                expected_value = 0.0
                actions = [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]  # 保持,上,下,左,右

                for action_idx, (di, dj) in enumerate(actions):
                    prob = policy_probs[action_idx]

                    # 计算下一状态
                    ni, nj = i + di, j + dj
                    ni = max(0, min(2, ni))  # 边界限制
                    nj = max(0, min(2, nj))

                    # 获取奖励
                    reward = 0
                    for ri, rj, r in rewards:
                        if ri == i and rj == j:
                            reward = r
                            break

                    expected_value += prob * (reward + gamma * values[ni, nj])

                new_values[i, j] = expected_value

        values = new_values

        # 每2次迭代显示一次
        if iteration % 2 == 0:
            print(f"\n价值迭代 {iteration + 1}:")
            state_values = [(i, j, values[i, j]) for i in range(3) for j in range(3)]
            env.render(state_values=state_values)
            time.sleep(1.5)

    print("\n策略评估完成！")
    time.sleep(3)
    env.close()


if __name__ == "__main__":
    # 运行Q学习示例
    q_learning_example()

    # 运行策略评估示例
    policy_evaluation_example()

    print("\n强化学习示例完成！")
