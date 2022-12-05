/* AoC 2020
 * Day 9
 *
 * Dr Bob, Tech Team, DigitalUK
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

static int get_invalid(int *lines, int num_lines, int w_size);
static int read_file(const char *filename, int **lines);
static int valid(int x, int *lines, int w_size);
static int get_weakness(int target, int *lines, int num_lines, int *min, int *max);
static int min_max(int *lines, int count, int *min, int *max);

static const char *INPUT_FILE_TEST = "input_test.txt";
static const char *INPUT_FILE = "input.txt";

/* slurp file into a list */
static int read_file(const char *filename, int **lines)
{
    FILE *fp;
    int i = 0;
    char *line = NULL; /* signal to getline() to allocate a buffer for us. we must free it */
    size_t len = 0;
    ssize_t read;

    if ((fp = fopen(filename, "r")) != NULL)
    {
        while (getline(&line, &len, fp) != -1) /* better solution: read file once, realloc() as necessary, but cba */
            i++;
        *lines = malloc(i * sizeof(int)); /* caller must free */
        rewind(fp);
        for (i = 0; (read = getline(&line, &len, fp)) != -1; i++) /* getline will realloc() on subseqeunt calls  */
            sscanf(line, "%d", &(*lines)[i]);
    }
    else
        return 0;

    fclose(fp);
    if (line)
        free(line); /* free anything allocated by getline() */
    return i;
}

/* find first invalid number in list */
static int get_invalid(int *lines, int num_lines, int w_size)
{
    for (int i = w_size; i < num_lines; i++)
        if (!valid(i, lines, w_size))
            return i;

    return -1;
}

/* check if a number is "valid", i.e. two numbers in the preceeding "window" sum to that number */
static int valid(int x, int *lines, int w_size)
{
    for (int i = x - w_size; i < x - 1; i++)
        for (int j = i + 1; j < x; j++)
            if (lines[i] + lines[j] == lines[x])
                return 1;

    return 0;
}

/* find the "weakness": a number that is not the sum of at least two digits over the previous window */
static int get_weakness(int target, int *lines, int num_lines, int *min, int *max)
{
    int sum = 0;
    for (int i = 0; i < num_lines; i++)
    {
        sum += lines[i];
        if (sum == target)
            return min_max(lines, i, min, max); /* will return 1 */
        else if (sum > target)
            return get_weakness(target, lines + 1, num_lines - 1, min, max); /* impact on stack if num_lines big */
    }
    return 0;
}

/* find the max and min in a range of numbers */
static int min_max(int *lines, int count, int *min, int *max)
{
    *min = *max = lines[0];
    for (int i = 0; i < count; i++)
        if (lines[i] > *max)
            *max = lines[i];
        else if (lines[i] < *min)
            *min = lines[i];
    return 1;
}

int main(void)
{
    int *lines = NULL;
    int n;

    /* worked examples, with assertions */
    n = read_file(INPUT_FILE_TEST, &lines);
    if (n != 0)
    {
        /* puzzle 1 */
        int q = get_invalid(lines, n, 5);
        int target = lines[q];
        printf("(TEST) Invalid number = %d\n", target);
        assert(target == 127);

        /* puzzle 2 */
        int min, max;
        get_weakness(target, lines, n, &min, &max);
        printf("(TEST) Encryption Weakness: x=%d, y=%d, weakness=%d\n", min, max, min + max);
        assert(min + max == 62);

        free(lines);
    }

    /* real data */
    n = read_file(INPUT_FILE, &lines);
    if (n != 0)
    {
        /* puzzle 1 */
        int q = get_invalid(lines, n, 25);
        int target = lines[q];
        printf("Invalid number = %d\n", target);

        /* puzzle 2 */
        int min, max;
        get_weakness(target, lines, n, &min, &max);
        printf("Encryption Weakness: x=%d, y=%d, weakness=%d\n", min, max, min + max);

        free(lines);
    }
    return 0;
}