"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""
from collections import Counter, deque
text = 'Freedom and peace!'
# text = "Корабли лавировали, лавировали, да не вылавировали"
print(f"Кодируемая строка: {text}")

# Вариант первый через ОПП

class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def make_huffman_tree(node, code=''):
    if type(node) is str:
        return {
            node: code
        }
    l, r = node.children()

    result = {}
    result.update(make_huffman_tree(l, code + '0'))
    result.update(make_huffman_tree(r, code + '1'))

    return result


frequencies = {}
for char in text:
    if char not in frequencies:
        frequencies[char] = 0
    frequencies[char] += 1

tree = frequencies.items()

while len(tree) > 1:
    tree = sorted(tree, reverse=True, key=lambda x: x[1])
    char1, count1 = tree[-1]
    char2, count2 = tree[-2]
    tree = tree[:-2]
    tree.append(
        (Node(char1, char2), count1 + count2)
    )

code_table = make_huffman_tree(tree[0][0])

coded = []
for char in text:
    coded.append(code_table[char])

print("Закодированная строка через ОПП:\n%s" % " ".join(coded))

# Вариант второй через ОПП и коллекции


class MyNode:

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def huffman_tree(s):

    count_s = Counter(s)

    sorted_s = deque(sorted(count_s.items(), key=lambda item: item[1]))

    while len(sorted_s) > 1:

        weight = sorted_s[0][1] + sorted_s[1][1]
        node = MyNode(left=sorted_s.popleft()[0], right=sorted_s.popleft()[0])

        for i, item in enumerate(sorted_s):
            if weight > item[1]:
                continue
            else:
                sorted_s.insert(i, (node, weight))
                break
        else:
            sorted_s.append((node, weight))

    return sorted_s[0][0]


code_table = dict()


def huffman_code(tree, path=''):

    if not isinstance(tree, MyNode):
        code_table[tree] = path

    else:
        huffman_code(tree.left, path=f'{path}0')
        huffman_code(tree.right, path=f'{path}1')


huffman_code(huffman_tree(text))

print("Закодированная строка через ОПП и коллекции: ")
for i in text:
    print(code_table[i], end=' ')

"""
Из разных реализаций видно что алгоритмы по разному строят деревья,
так как даже на одной и той же фразе получаются разные кодировки,
в основном это касается элементов с низкой частотой появления
"""
