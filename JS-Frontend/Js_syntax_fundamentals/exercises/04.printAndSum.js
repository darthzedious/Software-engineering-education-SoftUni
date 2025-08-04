function solve(start, end) {
    let resultStr = '';
    let sum = 0;
    for (let i = start; i <= end; i++){
        sum += i
        resultStr += `${i} `
    }
    console.log(resultStr);
    console.log(`Sum: ${sum}`);
}

solve(0, 26)