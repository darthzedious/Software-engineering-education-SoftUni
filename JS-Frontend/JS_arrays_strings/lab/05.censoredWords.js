function solve(text, word){
    const censor = '*'.repeat(word.length)
    let textAsArr = text.split(' ').map(w => w === word ? censor: w).join(' ')
    console.log(textAsArr)
}

solve('A small sentence with some words', 'small')
solve('Find the hidden word', 'hidden')