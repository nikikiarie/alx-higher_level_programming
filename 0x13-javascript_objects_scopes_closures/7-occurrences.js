#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	let ns = 0;
	for (let j = 0; j < list.length; j++) {
		if (searchElement === list[j]) {
			ns++;
		}
	}
	return ns;
