function solve(num, array){
    let arr = array.slice(0, num)
    let reversedArr = []

    while (arr.length > 0){
        let number = arr.pop()
        reversedArr.push(number)
    }
    console.log(reversedArr.join(' '))
}

solve(3, [10, 20, 30, 40, 50])