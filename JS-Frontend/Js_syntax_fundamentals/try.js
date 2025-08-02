// Variables
let a = 10
let b = 20

// print()
console.log(a + b);
console.log()

const pi = 3.14159 // Constant variable


// Conditional Statements
if (a > b){
    console.log("a is > b");
} else if (a == b) {
    console.log("a is equal to b");
} else {
    console.log("a is < b");
} 


// Function declaration
function add(first_number, second_number){
    return first_number + second_number
}

// Function invocation (calling)
console.log(add(pi, b))
console.log()

//Console print
console.log('The number pi is: ' + pi.toFixed(2) + '!')

// Interpolated string (template literal)
console.log(`The number pi is: ${pi.toFixed(2)}`) // pi.toFixed(2) == pi:.2f

