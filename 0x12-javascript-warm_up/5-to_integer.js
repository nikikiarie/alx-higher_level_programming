#!/usr/bin/node

const { argv } = require('process');
const n = parseInt(argv[2]);

console.log(Number.isInteger(n) ? `My number: ${n}` : 'Not a number');
