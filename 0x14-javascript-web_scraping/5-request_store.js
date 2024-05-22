#!/usr/bin/node

const fileSys = require('fs');
const req = require('request');
req(process.argv[2]).pipe(fileSys.createWriteStream(process.argv[3]));
