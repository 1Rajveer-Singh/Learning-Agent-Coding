use std::io::{self, Read};

#[allow(non_snake_case)]
fn sortArray(arr: Vec<i32>) -> Vec<i32> {
    if arr.len() <= 1 {
        return arr;
    }

    let mid = arr.len() / 2;

    let left = sortArray(arr[..mid].to_vec());
    let right = sortArray(arr[mid..].to_vec());

    let mut result = Vec::with_capacity(arr.len());

    let mut i = 0;
    let mut j = 0;

    while i < left.len() && j < right.len() {
        if left[i] <= right[j] {
            result.push(left[i]);
            i += 1;
        } else {
            result.push(right[j]);
            j += 1;
        }
    }

    while i < left.len() {
        result.push(left[i]);
        i += 1;
    }

    while j < right.len() {
        result.push(right[j]);
        j += 1;
    }

    result
}

fn main() {
    // Read input from Custom Input window
    let mut input = String::new();
    io::stdin()
        .read_to_string(&mut input)
        .unwrap();

    // Remove brackets and commas
    let input = input
        .replace('[', "")
        .replace(']', "")
        .replace(',', " ");

    // Convert input into Vec<i32>
    let arr: Vec<i32> = input
        .split_whitespace()
        .map(|x| x.parse::<i32>().unwrap())
        .collect();

    // Call challenge function
    let result = sortArray(arr);

    // Print result
    println!("{:?}", result);
}