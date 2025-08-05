function solve(text, word){
    // let counter = 0;
    // let textAsStr = text.split(' ')

    // textAsStr.forEach(element => { 
    //     if (element === word){
    //         counter += 1
    //     }
    // });

    // console.log(counter)

    // second try:
    let counter = text.split(' ').filter(w => w === word).length

    console.log(counter)
}

solve('This is a word and it also is a sentence', 'is')