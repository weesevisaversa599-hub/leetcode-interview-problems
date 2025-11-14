# LeetCode 算法题记录（面试版）

这是我在面试过程中遇到的算法题记录仓库，包含公司、岗位、题目内容和解题思路。

## 功能特性

- 📊 **公司&岗位标注**：清晰记录每个题目来自哪家公司的哪个岗位面试
- 🔢 **出现次数统计**：自动统计每个题目在所有面试中出现的总次数
- 📝 **详细解题思路**：包含问题分析、解法思路和优化方向
- 🎯 **分类清晰**：完全按照 LeetCode Hot 100 题型分类组织
- 📚 **丰富题型**：覆盖所有主流算法题型

## 目录结构（LeetCode Hot 100 分类）

```
├── problems/                          # 所有题目存储目录
│   ├── array/                        # 数组
│   ├── linkedlist/                   # 链表
│   ├── string/                       # 字符串
│   ├── dynamic_programming/          # 动态规划
│   ├── tree/                         # 树
│   ├── depth_first_search/           # 深度优先搜索
│   ├── breadth_first_search/         # 广度优先搜索
│   ├── binary_search/                # 二分查找
│   ├── backtracking/                 # 回溯算法
│   ├── hash_table/                   # 哈希表
│   ├── two_pointers/                 # 双指针
│   ├── sliding_window/               # 滑动窗口
│   ├── stack/                        # 栈
│   ├── heap/                         # 堆
│   ├── greedy/                       # 贪心算法
│   ├── bit_manipulation/             # 位运算
│   ├── graph/                        # 图
│   ├── divide_and_conquer/           # 分治算法
│   ├── sort/                         # 排序
│   └── union_find/                   # 并查集
├── stats.py                          # 出现次数统计脚本
├── CONTRIBUTING.md                   # 贡献指南
├── .gitignore                        # Git 忽略文件配置
└── README.md                         # 仓库说明文档
```

## 题目文件命名规范

每个题目文件遵循以下命名格式：
```
{problem_name}_{difficulty}.md
```
- `problem_name`: 题目名称的英文或拼音简写（如 `two_sum`, `reverse_linked_list`）
- `difficulty`: 难度级别（easy/medium/hard）

## 题目文件内容模板

```markdown
# 两数之和 (Two Sum)

## 基本信息

- 题目来源：字节跳动-后端开发、阿里-算法工程师、腾讯-客户端开发
- 难度级别：简单
- 相关标签：数组、哈希表

## 出现次数统计

- 总次数：3次（字节跳动1次、阿里1次、腾讯1次）

## 题目描述

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出 **和为目标值** 的那 **两个** 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。

你可以按任意顺序返回答案。

示例：
```
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
```

## 解题思路

1. **暴力解法**：双重循环遍历数组，寻找和为目标值的两个数。时间复杂度 O(n²)，空间复杂度 O(1)。

2. **优化解法**：使用哈希表存储已遍历过的元素及其索引。对于每个元素，检查哈希表中是否存在 `target - current` 的值。如果存在，直接返回两个索引；否则将当前元素加入哈希表。时间复杂度 O(n)，空间复杂度 O(n)。

## 代码实现

```python
def twoSum(nums, target):
    # 创建哈希表
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
```

## 总结

本题核心在于利用哈希表将查找时间从 O(n) 降低到 O(1)，从而优化整体时间复杂度。这是一个经典的哈希表应用场景，也是面试中高频出现的基础题目。
```

## 统计脚本使用方法

```bash
python stats.py
```

该脚本会自动统计所有题目出现的总次数，并按次数排序输出。

## 如何贡献

请参考 `CONTRIBUTING.md` 文件了解贡献指南。

## 许可证

MIT License
