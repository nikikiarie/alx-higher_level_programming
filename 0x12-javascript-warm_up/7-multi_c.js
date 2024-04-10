#!/usr/bin/node

if (process.argv[2] === undefined || isNan(process.argv[2])) {
	console.log('Missing number of occurrences');
} else {
	const b = Number(process.argv[2]);
	let a = 0;
	while (a < b) {
		console.log('C is fun');
		a++;
	}
}
