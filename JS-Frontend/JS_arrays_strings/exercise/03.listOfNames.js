function solve(array){
    let sortedArr = array.toSorted((a, b) => {
        if(a.toLowerCase() > b.toLowerCase()){
            return 1;
        }else if(a.toLowerCase() < b.toLowerCase()){
            return -1;
        } else{
            return 0;
        }
    })
    for (let i = 0; i < sortedArr.length; i++){
        console.log(`${i + 1}.${sortedArr[i]}`)
    }
}

solve(["John", "bob", "Christina", "Ema"])
