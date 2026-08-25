package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func mergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	mid := len(arr) / 2

	left := mergeSort(arr[:mid])
	right := mergeSort(arr[mid:])

	return merge(left, right)
}

func merge(left, right []int) []int {
	result := make([]int, 0, len(left)+len(right))

	i, j := 0, 0

	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			result = append(result, left[i])
			i++
		} else {
			result = append(result, right[j])
			j++
		}
	}

	result = append(result, left[i:]...)
	result = append(result, right[j:]...)

	return result
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()

	input := strings.TrimSpace(scanner.Text())

	input = strings.TrimPrefix(input, "[")
	input = strings.TrimSuffix(input, "]")

	if input == "" {
		fmt.Println("[]")
		return
	}

	parts := strings.Split(input, ",")

	arr := make([]int, 0, len(parts))

	for _, part := range parts {
		num, err := strconv.Atoi(strings.TrimSpace(part))
		if err != nil {
			return
		}

		arr = append(arr, num)
	}

	sorted := mergeSort(arr)

	fmt.Print("[")

	for i, value := range sorted {
		if i > 0 {
			fmt.Print(",")
		}
		fmt.Print(value)
	}

	fmt.Println("]")
}