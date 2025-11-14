# 贡献指南

欢迎为这个 LeetCode 面试题仓库做出贡献！以下是贡献的基本流程和规范：

## 贡献类型

- 添加新的面试题记录
- 更新现有题目的出现次数
- 优化解题思路和代码
- 修复格式和语法错误
- 改进统计脚本和工具

## 贡献流程

1. Fork 仓库
2. 创建新的分支 (`git checkout -b feature/add-new-problem`)
3. 做出贡献
4. 测试你的更改（如果是代码更改）
5. 提交 PR (`git push origin feature/add-new-problem`)
6. 等待审核

## 题目文件创建规范

### 目录选择
根据题目类型将文件放入对应的目录：
- 数组：array/
- 链表：linkedlist/
- 字符串：string/
- 动态规划：dynamic_programming/
- 树：tree/
- 深度优先搜索：depth_first_search/
- 广度优先搜索：breadth_first_search/
- 二分查找：binary_search/
- 回溯算法：backtracking/
- 哈希表：hash_table/
- 双指针：two_pointers/
- 滑动窗口：sliding_window/
- 栈：stack/
- 堆：heap/
- 贪心算法：greedy/
- 位运算：bit_manipulation/
- 图：graph/
- 分治算法：divide_and_conquer/
- 排序：sort/
- 并查集：union_find/

### 文件名格式
```
{problem_name}_{difficulty}.md
```
- `problem_name`: 题目名称的英文或拼音简写，使用下划线分隔（如 `two_sum`, `reverse_linked_list`）
- `difficulty`: 难度级别，必须是 `easy`, `medium` 或 `hard`

### 文件内容模板
```markdown
# 两数之和 (Two Sum)

## 基本信息

- 题目来源：字节跳动-后端开发、阿里-算法工程师、腾讯-客户端开发
- 难度级别：简单
- 相关标签：数组、哈希表

## 出现次数统计

- 总次数：3次（字节跳动1次、阿里1次、腾讯1次）

## 题目描述

[题目内容...]

## 解题思路

[详细解题思路...]

## 代码实现

```python
# 代码实现
```

## 总结

[总结内容...]
```

### 格式要求
- 使用 Markdown 语法
- 保持内容清晰易读
- 代码块使用正确的编程语言语法高亮
- 统计信息准确无误
- 相关标签与题目类型匹配

## 统计脚本修改

如果需要修改统计脚本 `stats.py`，请确保：
- 保持原有功能
- 兼容性良好
- 代码注释清晰
- 测试通过

## 行为准则

- 尊重他人的贡献
- 提供有价值的内容
- 保持仓库的专业性
- 遵守 GitHub 社区准则

## 联系方式

如有任何问题，请在仓库中提交 Issues。

感谢你的贡献！
