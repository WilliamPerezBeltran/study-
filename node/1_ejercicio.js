// We'll pass you an array of two numbers. Return the sum of those two numbers plus the sum of all the numbers between them. The lowest number will not always come first.

// For example, sumAll([4,1]) should return 10 because sum of all the numbers between 1 and 4 (both inclusive) is 10.

function sumAll (arr) {
  var ponderado = 0
  var low; var max = 0
  newArray = createArray(arr[0], arr[1])

  for (const item in newArray) {
    console.log(newArray[item])
    ponderado += newArray[item]
  }

  return ponderado
}

function createArray (low, max) {
  var newArray = []
  if (low < max) {
    low = low
    max = max
  } else {
    low = max
    max = low
  }
  while (low <= max) {
    newArray.push(low)
    low += 1
  }
  return newArray
}
sumAll([5, 10])
