function solve(string, text){
    let txt = text.split(' ')

    for (word of txt){
        if (string.toLowerCase() === word.toLowerCase()){
            console.log(word.toLowerCase())
            return
        }
    }
    console.log(`${string} not found!`)
}


solve('javascript','JavaScript is the best programming language')