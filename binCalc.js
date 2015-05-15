/*
 * Script by Matheus Avellar
 *   Binary Calculator
 */


var n1 = "1"; // Binary numbers go here
var n2 = "110110"; // And here
var ex = 0;
var opr = "+"; // Operation ("+" or "-") goes here
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
	var n3 = n1;  // In the new JS, you could simply do
	n1 = n2;      //    [n1, n2] = [n2, n1];
	n2 = n3;      // But this ain't the new JS
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
	}else {
		throw new TypeError('Use either "+" or "-" as the opr value');
	}
})();


if (neg != " "){  invert(); res = neg + res;  }

console.log(" " + n1 + "\n" + opr + n2 + "\n" + res);
