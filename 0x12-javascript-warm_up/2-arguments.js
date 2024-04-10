#!/usr/bin/node

const { argv } = require('process');
const ar = argv.length;

if (ar === 2) {
	console.log('No argument');
} else if (ar === 3) {
	console.log('Argument found');
} else {
	console.log('Arguments found');
}
