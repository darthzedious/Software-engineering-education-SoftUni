// Variables
let a = 10
let b = 20
console.log(typeof a)

a = 11 // let is used only one time when the variable is declared
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
console.log()

//Data types
let number = 5 // Number; like int, float
let person = {name: 'Angel', age: 25} // Object
let array = [1, 2, 3] // List
let isTrue = true // Boolean
let name = 'Angel' // String
let empty = null // None
let unknown  // undefined

// Arithmetic operators
console.log('Arithmetic operators:')
console.log()
let z = 15;
let y = 5;
let c;

c = z + y; // Addition
console.log(`Addition: ${z} + ${y} = ${c}`)
c = z - y // Subtraction
console.log(`Subtraction: ${z} - ${y} = ${c}`)
c = z * y // Multiplication
console.log(`Multiplication: ${z} * ${y} = ${c}`)
c = z / y //Division
console.log(`Division: ${z} / ${y} = ${c}`)
c = z % y // Remainder(Module division)
console.log(`Modulo: ${z} % ${y} = ${c}`)
c = z ** y // Exponentiation
console.log(`Exponentiation: ${z} ** ${y} = ${c}`)
console.log()

// Comparasion operators
console.log('Comparasion operators:')
console.log()
console.log(1 == '1')  // true => equality
console.log(1 === '1') // false => identity like '==' in python 
console.log(1 != '1') // false
console.log(3 !== '3') // true
console.log( 5 < 5.5) // true
console.log(5 <= 4) // false
console.log((5 > 7) ? 4 : 10) // 10 => if 5 > 7 return 4 else 10
console.log()

// operators
// ! = not
// && = and
// \\ = or


if (![]) console.log("Empty array is falsy!"); // DOES NOT print (arrays are truthy!)
if (!"") console.log("Empty string is falsy!"); // prints
if (!0) console.log("Zero is falsy!");         // prints
if (!null) console.log("null is falsy!");      // prints
if (!undefined) console.log("undefined is falsy!"); // prints
if (!NaN) console.log("NaN is falsy!");        // prints
console.log()
if ([]) console.log("Empty array is truthy!");    // prints!
if ({}) console.log("Empty object is truthy!");   // prints!
if ("hello") console.log("Non-empty string is truthy!"); // prints
console.log()


// Loops
console.log('Loops:')
console.log('for loop:')

for (let i = 0; i < 10; i++){ // can be i += 1
    console.log(i)
}
console.log()

// while loop
console.log('while loop:')
let j = 0
while (j < 10){
    j += 1
    console.log(j)
}
console.log()
