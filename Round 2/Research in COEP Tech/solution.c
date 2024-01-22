#include <stdio.h>

int main() {
    // Enter your code here. Read input from STDIN. Print output to STDOUT
    int n;
    scanf("%d", &n);
    int array[n];
    
    for (int i = 0; i < n; i++) {
        array[i] = 0;
    }

    int previous = 1;
    for (int i = 0; i < n; i++) {
        int temp;
        scanf("%d", &temp);

        for (int j = 0; j < n && j < temp; j++) {
            array[j]++;
        }

        for (int j = previous; j <= i; j++) {
            if (array[j] >= j + 1) {
                previous = j + 1;
            }
        }

        printf("%d ", previous);
    }

    return 0;
}

