function solve(array, step) {
    // let newElements = array.filter((value, index) => index % step === 0 ?
    // value : null).join('\n')
    // console.log(newElements)
    const newElements = array.filter((value, index) => index % step === 0)
    return newElements
}

console.log(solve(['5', '20', '31', '4', '20'], 2))
