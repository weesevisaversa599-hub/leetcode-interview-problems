#!/usr/bin/env python3
import os
import re

def count_problem_occurrences():
    """
    统计所有题目出现的总次数，并按次数排序输出
    """
    # 定义题目类型目录
    problem_types = [
        'array',
        'linkedlist',
        'string',
        'dynamic_programming',
        'tree',
        'depth_first_search',
        'breadth_first_search',
        'binary_search',
        'backtracking',
        'hash_table',
        'two_pointers',
        'sliding_window',
        'stack',
        'heap',
        'greedy',
        'bit_manipulation',
        'graph',
        'divide_and_conquer',
        'sort',
        'union_find'
    ]

    # 统计结果字典
    stats = {}

    # 遍历所有题目类型目录
    for problem_type in problem_types:
        dir_path = os.path.join('problems', problem_type)
        if not os.path.exists(dir_path):
            continue

        # 遍历目录下的所有 MD 文件
        for filename in os.listdir(dir_path):
            if not filename.endswith('.md'):
                continue

            file_path = os.path.join(dir_path, filename)

            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                # 提取出现次数
                occurrence_match = re.search(r'总次数：(\d+)次', content)
                if occurrence_match:
                    count = int(occurrence_match.group(1))
                    # 提取题目名称
                    title_match = re.search(r'# (.+?)\s*\(', content)
                    if title_match:
                        problem_title = title_match.group(1).strip()
                    else:
                        # 如果没有匹配到标题，使用文件名
                        problem_title = filename.replace('_', ' ').replace('.md', '').title()

                    stats[problem_title] = {
                        'count': count,
                        'type': problem_type,
                        'file': os.path.join(problem_type, filename)
                    }

            except Exception as e:
                print(f"处理文件 {file_path} 时出错: {e}")

    # 按出现次数排序
    sorted_problems = sorted(stats.items(), key=lambda x: x[1]['count'], reverse=True)

    # 输出统计结果
    print("=" * 80)
    print("LeetCode 面试题出现次数统计 (按次数降序)")
    print("=" * 80)

    if not sorted_problems:
        print("暂无统计数据，请先创建题目文件。")
        return

    # 调整列宽
    for problem_title, info in sorted_problems:
        print(f"{problem_title:<25} | 次数: {info['count']:<4} | 类型: {info['type']:<25} | 文件: {info['file']}")

    print("\n" + "=" * 80)
    print(f"总计: {len(sorted_problems)} 道题目")
    print(f"平均出现次数: {sum(info['count'] for _, info in stats.items()) / len(stats):.1f} 次")
    print("=" * 80)

if __name__ == "__main__":
    count_problem_occurrences()
