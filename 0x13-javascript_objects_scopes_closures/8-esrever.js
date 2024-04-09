#!/usr/bin/node
exports.esrever = function (list) {
	let l = list.length - 1;
	let j = 0;
	while ((l - j) > 0) {
		const b = list[l];
		list[l] = list[j];
		list[j] = b;
		j++;
		l--;
	}
	return list;
