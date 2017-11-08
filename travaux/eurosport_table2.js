"use strict";
var page = require('webpage').create();
var fs = require('fs');
// consulting a link list of all 380 matches which I've caught by python
var stream = fs.open('/Users/zhoufengting/Desktop/herf_2013_2014.txt', 'r');
var line = stream.readLine();
page.onConsoleMessage = function(msg) {
 console.log(msg);
};
var fs = require('fs');
// stock all the data in a file of txt
var path = '/Users/zhoufengting/Desktop/performance.txt';
var content;
function fun1(argument) {
    console.log("argument: " + argument)
    page.open(argument, function(status) {
        console.log("success");
        if (status === "success") {
        	page.includeJs("http://ajax.googleapis.com/ajax/libs/jquery/1.6.1/jquery.min.js", function() {
            	var possession = page.evaluate(function(){
                	return $("[data-bind='text: highlights.good.player.name']").text();
            	});
            	console.log(possession);
            	content = '\n'+possession;
            	fs.write(path, content, 'a');
            	if (!stream.atEnd()) {
                	//var line= stream.readLine();
                	//console.log("readLine: " + line);
                	fun1(stream.readLine(line));
            	} else {
                	phantom.exit();
            	}
        	});
            } else {
            console.log("Error")
            phantom.exit();
        }
    });
}

fun1(line);