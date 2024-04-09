#!/usr/bin/node
const SquareF = require('./5-square');


class Square extends SquareF {
	charPrint (c) {
		if (c === undefined)  {
			c = 'X';
		}
		for (let i = 0; i < this.height; i++) {
			let a = '';
			for (let j = 0; j < this.width; j++) {
				a += c;
			}
			console.log(a);
		}
	}
}

module.exports = Square;
