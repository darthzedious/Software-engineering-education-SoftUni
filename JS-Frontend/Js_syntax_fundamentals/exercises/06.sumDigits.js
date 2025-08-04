function solve(number) {
    let sum = 0;
    let digitAsStr = number.toString();
    for (let i = 0; i < digitAsStr.length; i++) {
        sum += Number(digitAsStr[i])
    }
    console.log(sum)
}

solve(123)