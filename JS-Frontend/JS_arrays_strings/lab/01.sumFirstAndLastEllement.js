function solve(array){
    const firstElement = array.pop()
    const lastElement = array.shift()
    const result = firstElement + lastElement

    console.log(result)
}

solve([20, 30, 40])
solve([10, 17, 22, 33])
solve([11, 58, 69])