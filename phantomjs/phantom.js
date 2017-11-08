var fs = require('fs');
 
var path = '/Users/zhoufengting/Desktop/possession.txt';
var content = 'Hello World 200% !';
fs.write(path, content, 'a');
var ap = 3;
content = '\n'+ap;
fs.write(path, content, 'a');
phantom.exit();