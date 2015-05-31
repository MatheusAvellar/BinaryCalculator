/*
 * Script by Matheus Avellar
 *   Binary Calculator
 */

var n1 = "1101001";       // Binary numbers go here
var n2 = "1011110";  // And here
var ex = 0;
var opr = "+";      // Operation ("+" or "-") goes here
var neg = " ";
var res = "";

(function fixNums() {
    var max = n1.length > n2.length ? 2 : n2.length > n1.length ? 1 : 3;
    switch (max) {
        case 1:  n1 = "0" + n1; fixNums(); break;
        case 2:  n2 = "0" + n2; fixNums(); break;
        case 3:  if (opr == "-" && parseInt(n1) < parseInt(n2)){  invert(); neg = "-"  } break;
        default: break;
    }
})();

function _1() {  res = "1" + res;  }
function _0() {  res = "0" + res;  }

function invert() {
    var n3 = n1;    // In the new JS, you could simply do
    n1 = n2;        //    [n1, n2] = [n2, n1];
    n2 = n3;        // But this ain't the new JS
}

(function result() {
    if (opr == "+") {
        for (var i = n1.length - 1; i >= 0; i--) {
            var e = parseInt(n1[i]) + parseInt(n2[i]) + ex;
            switch (e) {
                case 3:   _1(); ex = 1; break;
                case 2:   _0(); ex = 1; break;
                case 1:   _1(); ex = 0; break;
                default:  _0(); ex = 0; break;
            }
            if (!i && ex) {  _1();  }
        };
    }else if (opr == "-") {
        for (var i = n1.length - 1; i >= 0; i--) {
            var e = parseInt(n1[i]) - parseInt(n2[i]) - ex;
            switch (e) {
                case -2:  _0(); ex = 1; break;
                case -1:  _1(); ex = 1; break;
                case 0:   _0(); ex = 0; break;
                case 1:   _1(); ex = 0; break;
                default: break;
            }
            if (!i && ex) {  _1();  }
        };
    }else if (opr == "*") {
        var results = [];
        for (var i = n2.length - 1; i >= 0; i--) {
            for (var k = 1; k < n2.length - i; k++) {
                if (typeof results[i] == "undefined") {  results[i] = "";  }
                results[i] = "0" + results[i];
                console.log("#1 " + results);
            };

            for (var j = n1.length - 1; j >= 0; j--) {
                if (typeof results[i] == "undefined") {  results[i] = "";  }
                var e = parseInt(n1[j]) * parseInt(n2[i]);

                if (e == 1) {  results[i] = "1" + results[i];  }
                else        {  results[i] = "0" + results[i];  }

                if (!i && ex) {  _1();  }
                console.log("#2 " + results);
            };
        };
        console.log("#3 " + results);

        var resultsBackup = results;

        for (var l = 0; l < results.length; l++) {
            for (var i = results[l].length - 1; i >= 0; i--) {
                if (typeof results[l+1] != "undefined") {
                    if (typeof results[l+1][i] != "undefined"){
                        var e = parseInt(results[l][i]) + parseInt(results[l+1][i]) + ex;
                        switch (e) {
                            case 3:   results[l] = "1" + results[l]; ex = 1; break;
                            case 2:   results[l] = "0" + results[l]; ex = 1; break;
                            case 1:   results[l] = "1" + results[l]; ex = 0; break;
                            default:  results[l] = "0" + results[l]; ex = 0; break;
                        }
                        if (!i && ex) {  _1();  }
                    } else {
                        results[l] = "1" + results[l];
                    }
                }
            };
        };
        console.log("#4 " + results);
        // Well crap, I got this array with a bunch of values I gotta add :l
    } else {
        throw new TypeError('Use either "+" or "-" as the opr value');
    }
})();


if (neg != " "){  invert(); res = neg + res;  }
function c(number, baseFrom, baseTo) {
    return parseInt(number, baseFrom).toString(baseTo);
}

 /*
console.log(n1 + "\n" + opr + n2 + "\n" + res);                               // Binary result
console.log(c(n1, 2, 10) + "\n" + opr + c(n2, 2, 10) + "\n" + c(res, 2, 10)); // Decimal result
console.log(c(n1, 2, 16) + "\n" + opr + c(n2, 2, 16) + "\n" + c(res, 2, 16)); // Hexadecimal result
 */