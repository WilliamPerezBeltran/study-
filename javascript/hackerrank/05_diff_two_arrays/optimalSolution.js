function diffArray(arr1, arr2) {
  let difference = arr1
    .filter((item) => !arr2.includes(item))
    .concat(arr2.filter((item) => !arr1.includes(item)));
  return difference;
}
