function solve(array, num) {
    for (let i = 0; i < num; i ++){
        let elem = array.shift()
        array.push(elem)
    }
    console.log(array.join(' '))
}

solve([51, 47, 32, 61, 21], 2)