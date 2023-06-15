#!/usr/bin/node
const { argv } = require('node:process');

if (!Number(argv[2]) || Number(argv[2]) === 0) {
  console.log('Not a number');
} else {
  console.log(Math.floor(Number(argv[2])));
}
