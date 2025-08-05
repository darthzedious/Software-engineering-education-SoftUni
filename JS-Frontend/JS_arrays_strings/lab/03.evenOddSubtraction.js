function solve(array){
    let evenSum = 0;
    let oddSum = 0;
    let resut = 0;

    for (let i = 0; i < array.length; i++){
        if (array[i] % 2 === 0){
            evenSum += array[i]
        } else{oddSum += array[i]}
    }
    resut = evenSum - oddSum

    console.log(resut)
}

solve([3,5,7,9])