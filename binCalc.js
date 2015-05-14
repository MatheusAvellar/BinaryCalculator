var n1 = "100"; // Binary numbers go here
var n2 = "100"; // And here
var ex = 0;
var res = "";

(function fixNums() {
	var max = n1.length > n2.length ? 2 : n2.length > n1.length ? 1 : "";
	switch (max) {
		case 1:  n1 = "0" + n1; fixNums(); break;
		case 2:  n2 = "0" + n2; fixNums(); break;
		default: break;
	}
})();

function _1() {  res = "1" + res;  }
function _0() {  res = "0" + res;  }

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

// res now contains the result //