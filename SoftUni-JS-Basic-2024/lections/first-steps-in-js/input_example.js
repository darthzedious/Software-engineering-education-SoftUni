function example(input){
    let name = input[0];
    let age = Number(input[1]);
    let town = input[3];
    let car = input[2];
    
    // display the given input data
    console.log(name);
    console.log(age);
    console.log(town);
    console.log(car);
    
    // display table of the given input data 
    console.table(input);
}

example(["name", "18", "lada", "sofia"])