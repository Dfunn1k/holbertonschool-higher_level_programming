#!/usr/bin/node
exports.logMe = ((count = 0) => function (item) {
  console.log(`${count++}: ${item}`);
})();
