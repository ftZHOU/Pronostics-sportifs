"use strict";
var page = require('webpage').create();


var fs = require('fs');
var stream = fs.open('/Users/zhoufengting/Desktop/href_2014.txt', 'r');


var line = stream.readLine();


page.onConsoleMessage = function(msg) {
   console.log(msg);
};

function fun1(argument) {
    
    console.log("argument: " + argument)

    page.open(argument, function(status) {
        console.log("success");
        if (status === "success") {
            page.includeJs("http://libs.useso.com/js/jquery/1.6.4/jquery.min.js", function() {
                page.evaluate(function() {
                    console.log("evalute")
                    // console.log($("[data-bind='text: stats.possession.home']").text());
                });
            });
        } else {
            console.log("Error")
        }

        if (!stream.atEnd()) {
            var line = stream.readLine();
            console.log("readLine: " + line);
            fun1(stream.readLine(line));
        } else {
            phantom.exit();
        }

    });
}

fun1(line);