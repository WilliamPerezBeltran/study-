const repeatString = function(word, times) {
	if(times=== -1) return 'ERROR'
	let count  = 0
	let result = ""
	while(count < times){
		result +=word
		count++
	}

	return result

};

// Do not edit below this line
module.exports = repeatString;
