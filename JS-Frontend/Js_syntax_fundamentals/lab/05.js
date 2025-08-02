function solve(firstNum, secondNum, operand){
   let result;
    if (operand === '+')
        result = firstNum + secondNum
    else if (operand === '-')
        result = firstNum - secondNum
    else if (operand === '/')
        result = firstNum / secondNum
    else if (operand === '*')
        result = firstNum * secondNum
    else if (operand === '%')
        result = firstNum % secondNum
    else if (operand === '**')
        result = firstNum ** secondNum
    console.log(result)
}

solve(5, 6, '+')
solve(5, 6, '/')
