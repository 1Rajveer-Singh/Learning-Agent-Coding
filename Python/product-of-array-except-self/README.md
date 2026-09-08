# Product of Array Except Self

## 💡 Overview & Approach
The problem requires calculating the product of all elements in an array except the one at the current index without using the division operator. A naive approach would involve calculating the total product and dividing by each element, but this fails when zeros are present in the input array.

The optimal approach utilizes the concept of **Prefix and Suffix products**. We perform two passes over the array:
1. **Forward Pass**: We compute the prefix product for every index `i` and store it in the result array. At any index `i`, `res[i]` contains the product of all elements from `0` to `i-1`.
2. **Backward Pass**: We maintain a running suffix product variable. As we iterate backwards, we multiply the current `res[i]` by the suffix product. This effectively combines the prefix product (already in `res[i]`) with the suffix product (calculated on the fly), resulting in the product of all elements except `nums[i]`.

## 📊 Complexity Analysis
- **Time Complexity**: O(N), where N is the length of the input array. We perform two linear passes over the array.
- **Space Complexity**: O(1) auxiliary space (excluding the output array), as we only use a few integer variables to track the running products.

## 🏢 Top Companies Asking This Problem
- Meta (Facebook)
- Amazon
- Google
- Microsoft
- Apple
- Bloomberg

## 🚀 Key Features & Edge Cases Handled
- **Zeros in Input**: The algorithm naturally handles zeros because it relies on multiplication rather than division. If one zero exists, the result will be zero everywhere except at the index of the zero. If two or more zeros exist, the result array will be all zeros.
- **Empty/Single Element Arrays**: The logic handles small arrays gracefully, though the problem constraints typically guarantee at least two elements.
- **No Division**: The solution strictly adheres to the constraint of not using the division operator, ensuring robustness against division-by-zero errors.