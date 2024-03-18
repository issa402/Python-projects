from collections import deque

class GridLocation:
    def __init__(self, row, col):
        self.row = row
        self.col = col

class RisingTides:
    def __init__(self, terrain):
        self.terrain = terrain.heights
        self.sources = terrain.sources

    def elevation_extrema(self):
        min_elevation = float('inf')
        max_elevation = float('-inf')

        for row in range(len(self.terrain)):
            for col in range(len(self.terrain[0])):
                current_elevation = self.terrain[row][col]

                min_elevation = min(min_elevation, current_elevation)
                max_elevation = max(max_elevation, current_elevation)

        return [min_elevation, max_elevation]

    def flooded_regions_in(self, height):
        num_rows = len(self.terrain)
        num_cols = len(self.terrain[0])

        resulting_array = [[False] * num_cols for _ in range(num_rows)]
        queue = deque()

        for source in self.sources:
            queue.append(source)
            resulting_array[source.row][source.col] = True

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        while queue:
            current = queue.popleft()

            for i in range(4):
                new_row = current.row + dx[i]
                new_col = current.col + dy[i]

                if 0 <= new_row < num_rows and 0 <= new_col < num_cols:
                    if self.terrain[new_row][new_col] <= height and not resulting_array[new_row][new_col]:
                        resulting_array[new_row][new_col] = True
                        queue.append(GridLocation(new_row, new_col))

        return resulting_array

    def is_flooded(self, height, cell):
        flooded_regions = self.flooded_regions_in(height)
        row = cell.row
        col = cell.col

        if 0 <= row < len(flooded_regions) and 0 <= col < len(flooded_regions[0]):
            return flooded_regions[row][col]
        return False

    def height_above_water(self, height, cell):
        land_height = self.terrain[cell.row][cell.col]
        height_difference = land_height - height
        absolute_height_difference = abs(height_difference)

        description = "meters above" if height_difference >= 0 else "meters below"
        print(f"The land at ({cell.row}, {cell.col}) is {absolute_height_difference} {description} the water.")

        return absolute_height_difference

    def total_visible_land(self, height):
        flooded_regions = self.flooded_regions_in(height)
        visible_land_count = sum(1 for row in flooded_regions for cell in row if not cell)

        return visible_land_count

    def land_lost(self, height, new_height):
        current_visible_land = self.total_visible_land(height)
        future_visible_land = self.total_visible_land(new_height)
        land_difference = current_visible_land - future_visible_land

        return abs(land_difference)

    def num_of_islands(self, height):
        num_rows = len(self.terrain)
        num_cols = len(self.terrain[0])
        flooded_regions = self.flooded_regions_in(height)
        unique_roots = set()

        def is_valid(row, col):
            return 0 <= row < num_rows and 0 <= col < num_cols

        class WeightedQuickUnionUF:
            def __init__(self, n, m):
                self.parent = {}
                self.size = {}
                for i in range(n):
                    for j in range(m):
                        self.parent[(i, j)] = (i, j)
                        self.size[(i, j)] = 1

            def find(self, p):
                while p != self.parent[p]:
                    self.parent[p] = self.parent[self.parent[p]]
                    p = self.parent[p]
                return p

            def union(self, p, q):
                root_p = self.find(p)
                root_q = self.find(q)

                if root_p != root_q:
                    if self.size[root_p] < self.size[root_q]:
                        self.parent[root_p] = root_q
                        self.size[root_q] += self.size[root_p]
                    else:
                        self.parent[root_q] = root_p
                        self.size[root_p] += self.size[root_q]

        uf = WeightedQuickUnionUF(num_rows, num_cols)

        for row in range(num_rows):
            for col in range(num_cols):
                if not flooded_regions[row][col]:
                    for dr in range(-1, 2):
                        for dc in range(-1, 2):
                            new_row = row + dr
                            new_col = col + dc
                            if is_valid(new_row, new_col) and not flooded_regions[new_row][new_col]:
                                uf.union((row, col), (new_row, new_col))

        for row in range(num_rows):
            for col in range(num_cols):
                if not flooded_regions[row][col]:
                    root = uf.find((row, col))
                    unique_roots.add(root)

        return len(unique_roots)