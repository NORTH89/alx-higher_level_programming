#!/usr/bin/node

const arg = process.argv[2];
console.log(Number.isNaN(parseInt(arg)) ? 'Not a number' : 'My number: ' + parseInt(arg))
