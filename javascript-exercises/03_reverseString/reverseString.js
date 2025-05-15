// const reverseString = function(data) {
// 	let result = ""
// 	for (let i = data.length-1; i >= 0; i--) {
// 		result+=data[i]
// 	}
// 	return result

// };

// Do not edit below this line
const reverseString = function(data){
	return data.split("").reverse().join("")

}
module.exports = reverseString;

