#!/usr/bin/node

const req = require('request');

req(process.arg[2], function (err, res, data) {
	if (!err) {
		const info = JSON.parse(data).results;
		console.log(info.reduce((count, movie) => {
			return movie.characters.find((character) => character.endsWith('/18/'))
			? count + 1
			: count;
		}, 0));
	}
});
