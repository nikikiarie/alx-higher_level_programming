#!/usr/bin/node
let ar = 0;

exports.logMe = function (item) {
	console.log(ar + ': ' + item);
	ar++;
}
