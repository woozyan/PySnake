import math


def dist(snake, egg):
    head = snake.head
    return math.sqrt(math.pow(head.x - egg.x, 2) + math.pow(head.y - egg.y, 2))


def min_dist(snake, egg):
    node = snake.head
    min_dist = float("inf")
    while node:
        this_dist = math.sqrt(math.pow(node.x - egg.x, 2) + math.pow(node.y - egg.y, 2))
        if this_dist < min_dist:
            min_dist = this_dist
        node = node.next
    return min_dist
