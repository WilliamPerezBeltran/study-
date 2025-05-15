const removeFromArray = function(array,...parameters) {
	let result = []
	for (element of array ){
		if(!parameters.includes(element)){
			result.push(element)
		}

	}
	return result

};

// Do not edit below this line
module.exports = removeFromArray;
