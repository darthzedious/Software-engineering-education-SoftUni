function solve(num1, num2, num3){
    let largestNumber;
    if (num1 > num2 && num1 > num3)
        largestNumber = num1
    else if (num2 > num1 && num2 > num3)
        largestNumber = num2
    else if (num3 > num2 && num3 > num1)
        largestNumber = num3
    console.log(`The largest number is ${largestNumber}.`)
}

solve(5, -3, 16)
solve(-3, -5, -22.5)
