# javascript-warm_up

# Files

### 0. First constant, first print
### [0-javascript_is_amazing.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/0-javascript_is_amazing.js)

```JavaScript
$ curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
$ sudo apt-get install -y nodejs

```

### 1. 3 languages
### [1-multi_languages.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/1-multi_languages.js)

```JavaScript
$ sudo npm install semistandard --global

```

### 2. Arguments
### [2-arguments.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/2-arguments.js)

```JavaScript
guillaume@ubuntu:~/$ ./0-javascript_is_amazing.js 
JavaScript is amazing
guillaume@ubuntu:~/$ 
guillaume@ubuntu:~/$ semistandard ./0-javascript_is_amazing.js 
guillaume@ubuntu:~/$ 

```

### 3. Value of my argument
### [3-value_argument.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/3-value_argument.js)

```JavaScript
guillaume@ubuntu:~/$ ./1-multi_languages.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/$ 

```

### 4. Create a sentence
### [4-concat.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/4-concat.js)

```JavaScript
guillaume@ubuntu:~/$ ./2-arguments.js 
No argument
guillaume@ubuntu:~/$ ./2-arguments.js Best
Argument found
guillaume@ubuntu:~/$ ./2-arguments.js Best School
Arguments found
guillaume@ubuntu:~/$ 

```

### 5. An Integer
### [5-to_integer.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/5-to_integer.js)

```JavaScript
guillaume@ubuntu:~/$ ./3-value_argument.js 
No argument
guillaume@ubuntu:~/$ ./3-value_argument.js School
School
guillaume@ubuntu:~/$ 

```

### 6. Loop to languages
### [6-multi_languages_loop.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/6-multi_languages_loop.js)

```JavaScript
guillaume@ubuntu:~/$ ./4-concat.js c cool
c is cool
guillaume@ubuntu:~/$ ./4-concat.js c 
c is undefined
guillaume@ubuntu:~/$ ./4-concat.js
undefined is undefined
guillaume@ubuntu:~/$ 

```

### 7. I love C
### [7-multi_c.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/7-multi_c.js)

```JavaScript
guillaume@ubuntu:~/$ ./5-to_integer.js 
Not a number
guillaume@ubuntu:~/$ ./5-to_integer.js 89
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js "89"
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js 89.89
My number: 89
guillaume@ubuntu:~/$ ./5-to_integer.js School
Not a number
guillaume@ubuntu:~/$ 

```

### 8. Square
### [8-square.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/8-square.js)

```JavaScript
guillaume@ubuntu:~/$ ./6-multi_languages_loop.js 
C is fun
Python is cool
JavaScript is amazing
guillaume@ubuntu:~/$ 

```

### 9. Add
### [9-add.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/9-add.js)

```JavaScript
guillaume@ubuntu:~/$ ./7-multi_c.js 2
C is fun
C is fun
guillaume@ubuntu:~/$ ./7-multi_c.js 5
C is fun
C is fun
C is fun
C is fun
C is fun
guillaume@ubuntu:~/$ ./7-multi_c.js 
Missing number of occurrences
guillaume@ubuntu:~/$ ./7-multi_c.js -3
guillaume@ubuntu:~/$ 

```

### 10. Factorial
### [10-factorial.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/10-factorial.js)

```JavaScript
guillaume@ubuntu:~/$ ./8-square.js
Missing size
guillaume@ubuntu:~/$ ./8-square.js School
Missing size
guillaume@ubuntu:~/$ ./8-square.js 2
XX
XX
guillaume@ubuntu:~/$ ./8-square.js 6
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
XXXXXX
guillaume@ubuntu:~/$ ./8-square.js -3
guillaume@ubuntu:~/$ 

```

### 11. Second biggest!
### [11-second_biggest.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/11-second_biggest.js)

```JavaScript
guillaume@ubuntu:~/$ ./9-add.js 
NaN
guillaume@ubuntu:~/$ ./9-add.js 1
NaN
guillaume@ubuntu:~/$ ./9-add.js 1 7
8
guillaume@ubuntu:~/$ ./9-add.js 13 89
102
guillaume@ubuntu:~/$ 

```

### 12. Object
### [12-object.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/12-object.js)

```JavaScript
guillaume@ubuntu:~/$ ./10-factorial.js 
1
guillaume@ubuntu:~/$ ./10-factorial.js 3
6
guillaume@ubuntu:~/$ ./10-factorial.js 89
1.6507955160908452e+136
guillaume@ubuntu:~/$ ./10-factorial.js 333
Infinity
guillaume@ubuntu:~/$ 

```

### 13. Add file
### [13-add.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/13-add.js)

```JavaScript
guillaume@ubuntu:~/$ ./11-second_biggest.js 
0
guillaume@ubuntu:~/$ ./11-second_biggest.js 1
0
guillaume@ubuntu:~/$ ./11-second_biggest.js 4 2 5 3 0 -3
4
guillaume@ubuntu:~/$ 

```

### 14. Const or not const
### [100-let_me_const.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/100-let_me_const.js)

```JavaScript
guillaume@ubuntu:~/$ cat 12-object.js
#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12
};
console.log(myObject);
/*
YOUR CODE HERE
*/
console.log(myObject);

guillaume@ubuntu:~/$ ./12-object.js
{ type: 'object', value: 12 }
{ type: 'object', value: 89 }
guillaume@ubuntu:~/$ 

```

### 15. Call me Moby
### [101-call_me_moby.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/101-call_me_moby.js)

```JavaScript
guillaume@ubuntu:~/$ cat 13-main.js
#!/usr/bin/node
const add = require('./13-add').add;
console.log(add(3, 5));
guillaume@ubuntu:~/$ ./13-main.js
8
guillaume@ubuntu:~/$ 

```

### 16. Add me maybe
### [102-add_me_maybe.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/102-add_me_maybe.js)

```JavaScript
guillaume@ubuntu:~/$ cat 100-main.js
#!/usr/bin/node
myVar = 89;
require('./100-let_me_const')
console.log(myVar);
guillaume@ubuntu:~/$ ./100-main.js
333
guillaume@ubuntu:~/$ 

```

### 17. Increment object
### [103-object_fct.js](https://github.com/Dfunn1k/holbertonschool-higher_level_programming/blob/main/javascript-warm_up/103-object_fct.js)

```JavaScript
guillaume@ubuntu:~/$ cat 101-main.js
#!/usr/bin/node
const callMeMoby = require('./101-call_me_moby').callMeMoby;
callMeMoby(3, function () {
  console.log('C is fun');
});
guillaume@ubuntu:~/$ ./101-main.js
C is fun
C is fun
C is fun
guillaume@ubuntu:~/$ 

```

