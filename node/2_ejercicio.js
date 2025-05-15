// Compare two arrays and return a new array with any
// items only found in one of the two given arrays, but not both.
// In other words, return the symmetric difference of the two arrays.

function diffArray (arr1, arr2) {
  var newArr = []
  var ar1 = []
  var ar2 = []
  if (arr1.length > arr2.length) {
    ar1 = arr1
    ar2 = arr2
  } else {
    ar1 = arr2
    ar2 = arr1
  }

  var test = false

  for (const item in ar1) {
    for (const item2 in ar2) {
      if (ar1[item] == ar2[item2]) {
      	test = true
      }
    }

    if (!test) {
    	newArr.push(ar1[item])
    }
    test = false
  }
}

diffArray([1, 2, 3, 5], [1, 2, 3, 4, 5])
