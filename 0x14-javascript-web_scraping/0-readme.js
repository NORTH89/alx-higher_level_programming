#!/usr/bin/node
// Readme.js

const fs = require("fs");

fs.readFile(process.argv[2], "utf8", function (err, data) {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});
