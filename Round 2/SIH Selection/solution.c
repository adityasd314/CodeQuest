#include <stdio.h>
#include <stdlib.h>

int compare(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */
    int n, p;
    scanf("%d %d", &n, &p);

    int *arr = (int *)malloc(n * sizeof(int));

    for (int i = 0; i < n; i++) {
        int temp;
        scanf("%d", &temp);
        arr[i] = temp;
    }

    qsort(arr, n, sizeof(int), compare);

    int min = arr[0] - arr[n - 1];
    min *= -1 * n;

    for (int i = p - 1; i < n; i++) {
        int *begin = arr + i - p + 1;
        int *end = begin + p - 1;
        int min_temp = 0;

        for (int j = 0; j < p; j++) {
            min_temp += (*(end) - *(begin + j));
        }

        if (min_temp < min) {
            min = min_temp;
        }
    }

    printf("%d", min);

    free(arr);
    return 0;
}