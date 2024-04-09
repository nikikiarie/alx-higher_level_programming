#!/usr/bin/node

const fs = require('fs');


const oneArg = fs.readFileSync(process.argv[2]).toString();
const twoArg = fs.readFileSync(process.argv[3]).toString();
fs.writeFileSync(process.argv[4], oneArg + twoArg);
