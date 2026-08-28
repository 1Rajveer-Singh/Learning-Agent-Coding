function search(data) {
  const { arr, X } = data;
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === X) {
      return i;
    }
  }
  return -1;
}