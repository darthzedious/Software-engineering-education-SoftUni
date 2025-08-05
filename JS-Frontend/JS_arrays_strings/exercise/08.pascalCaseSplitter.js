function solve(text){
    let startIndex = -1;
    const words = []

    for (let i = 0; i < text.length; i++){
        if (text[i] === text[i].toUpperCase()){
            if (startIndex < 0){
                startIndex = i
            }else{
                let word = text.substring(startIndex, i)
                words.push(word)
                startIndex = i
            }
        }
    }

    words.push(text.substring(startIndex))
    console.log(words.join(', '))
}

solve('SplitMeIfYouCanHaHaYouCantOrYouCan')
