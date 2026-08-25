import java.util.*;

public class Main {

    public static int aStar(int[][] grid) {
        int n = grid.length;
        int m = grid[0].length;

        if (grid[0][0] == 1 || grid[n - 1][m - 1] == 1)
            return -1;

        int[][] dist = new int[n][m];

        for (int[] row : dist)
            Arrays.fill(row, Integer.MAX_VALUE);

        PriorityQueue<int[]> pq = new PriorityQueue<>(
            Comparator.comparingInt(a -> a[0])
        );

        dist[0][0] = 0;

        int h = Math.abs(n - 1) + Math.abs(m - 1);
        pq.offer(new int[]{h, 0, 0, 0});

        int[] dr = {-1, 1, 0, 0};
        int[] dc = {0, 0, -1, 1};

        while (!pq.isEmpty()) {
            int[] cur = pq.poll();

            int g = cur[1];
            int r = cur[2];
            int c = cur[3];

            if (g != dist[r][c])
                continue;

            if (r == n - 1 && c == m - 1)
                return g;

            for (int i = 0; i < 4; i++) {
                int nr = r + dr[i];
                int nc = c + dc[i];

                if (nr < 0 || nr >= n || nc < 0 || nc >= m)
                    continue;

                if (grid[nr][nc] == 1)
                    continue;

                int newG = g + 1;

                if (newG < dist[nr][nc]) {
                    dist[nr][nc] = newG;

                    int heuristic =
                        Math.abs(n - 1 - nr) +
                        Math.abs(m - 1 - nc);

                    pq.offer(new int[]{
                        newG + heuristic,
                        newG,
                        nr,
                        nc
                    });
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();

        int[][] grid = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                grid[i][j] = sc.nextInt();
            }
        }

        System.out.println(aStar(grid));

        sc.close();
    }
}