#!/usr/bin/node

//function that returns the number of occurrences in a list
exports.nbOccurences = function (list, searchElement) {
    let i = 0;
    list.forEach(myFunction);

    function myFunction(item) {
	if (item === searchElement) {
	    i += 1;
	}
    }
    return i;
}
