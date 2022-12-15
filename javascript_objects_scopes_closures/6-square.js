const subclass = require('./5-square');
class Square extends subclass {
  charPrint (c = 'X') {
    for (let i = 0; i < this.width; i++) {
      for (let j = 0; j < this.height; j++) {
        process.stdout.write(c);
      }
      console.log('');
    }
  }
}

module.exports = Square;
