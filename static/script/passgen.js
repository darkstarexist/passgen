let gen_btn = document.getElementById("gen-pass");
let passbox = document.getElementById("pass-box");


/* Function to generate combination of password */
function generatePass() {
	let pass = '';
	let str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' +
		'abcdefghijklmnopqrstuvwxyz0123456789@#$';

	for (let i = 1; i <= 12; i++) {
		let char = Math.floor(Math.random()
			* str.length + 1);

		pass += str.charAt(char)
	}
    // console.log(pass)
    passbox.value = pass;
    
    
	return pass;
}

gen_btn.addEventListener('click',generatePass)



// gen_pass()