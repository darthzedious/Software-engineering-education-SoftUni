function solve(number) {
    let areSame = true;
    let sum = 0;

    numberToStr = number.toString()
    let first = numberToStr[0];

    for (let i = 0; i < numberToStr.length; i++){
        if (numberToStr[i] === first){
            areSame = true
        }else {
            areSame = false
        }

        sum += Number(numberToStr[i])
    }

    console.log(areSame)
    console.log(sum)

}


solve(2222222)
solve(1234)