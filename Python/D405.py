def find_path(maze, H, W):
    def is_valid_move(r, c):
        return 0 <= r < H and 0 <= c < W and maze[r][c] == "."

    def dfs(r, c, path):
        if r == H - 1 and c == W - 1:
            return path
        if is_valid_move(r + 1, c):
            new_path = dfs(r + 1, c, path + "S")
            if new_path:
                return new_path
        if is_valid_move(r, c + 1):
            new_path = dfs(r, c + 1, path + "E")
            if new_path:
                return new_path
        return None

    return dfs(0, 0, "")


H, W = map(int, input().strip().split())
maze = [input().strip() for _ in range(H)]

shortest_path = find_path(maze, H, W)
print(shortest_path)
