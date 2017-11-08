"use strict";
var page = require('webpage').create();



var fs = require('fs');
var stream = fs.open('/Users/zhoufengting/Desktop/possession2.txt', 'r');


var line = stream.readLine();




page.onConsoleMessage = function(msg) {
 console.log(msg);
};
var fs = require('fs');
var path = '/Users/zhoufengting/Desktop/possession1.txt';
var content;



function fun1(argument) {

    console.log("argument: " + argument)

    page.open(argument, function(status) {
        console.log("success");
        if (status === "success") {
            //var name = document.querySelectionAll("div.mobile-player");
            var possession = page.evaluate(function(){
                
                return $("[data-bind='text: stats.penaltiesScored.away']").text();
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
        } else {
            console.log("Error")
            phantom.exit();
        }
    });
}

fun1(line);