function solve(array){
    const sorted = array.slice().sort((a, b) => a - b);
    const result = [];

    let start = 0;
    let end = sorted.length - 1;
    let counter = 0;

    while (start <= end){
        if (counter % 2 === 0){
            result.push(sorted[start]);
            start += 1
        } else {
            result.push(sorted[end]);
            end -= 1
        }
        counter++; 
    }
    return result


    // let sortedArr = array.toSorted()
    // let counter = 0
    // let result = []

    // while (sortedArr.length > 0){
    //     if (counter % 2 === 0){
    //         let smallest = sortedArr.shift()
    //         result.push(smallest)
    //     } else {
    //         let biggest = sortedArr.pop()
    //         result.push(biggest)
    //     }
    //     counter += 1
    // }
    // console.log(result)
}

console.log(solve([1, 65, 3, 52, 48, 63, 31, -3, 18, 56]))