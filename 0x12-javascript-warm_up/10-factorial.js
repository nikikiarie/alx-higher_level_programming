#!/usr/bin/node

function fctl(i) {
	if (i < 0) {
		return (-1);
	}
	if (i === 0 || isNan(i)) {
		return (1);
	}
	return (i * fctl(i - 1));
}

console.log(fctl(Number(process.argv[2])));
