function solve(text){
    const pattern = /^[a-zA-Z]+$/
    let textArr = text
    .split(' ')
    .filter(word => word.startsWith('#') && word.length > 1 && pattern.test(word.slice(1)))
    .map(word => word.slice(1))
    .join('\n')

    console.log(textArr)
}


solve('Nowadays everyone uses # to tag a #special word in #socialMedia')
console.log()
solve('The symbol # is known #variously in English-speaking #regions as the #number sign')
