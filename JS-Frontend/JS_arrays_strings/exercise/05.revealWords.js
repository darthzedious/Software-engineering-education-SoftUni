function solve(words, text){
    const wordArr = words.split(', ')
    let textArr = text.split(' ')

    for (let i = 0; i < textArr.length; i++){
        if (textArr[i].includes("*")){
            for (let match of wordArr){
                if (textArr[i].length === match.length){
                    textArr[i] = match
                }
            }
        }
    }
    console.log(textArr.join(' '))
}

solve('great, abc', 'softuni is ***** place for learning new programming languages')