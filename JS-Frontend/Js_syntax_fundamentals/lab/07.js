function theatrePromotions(day, age){
    let price;
    if (day === 'Weekday' && 0 <= age <= 18)
        price = 12
    else if(day === 'Weekday' && 18 <= age <= 64)
        price = 18
    else if(day === 'Weekday' && 64 <= age <= 122)
        price = 12
    else if(day === 'Weekend' && 0 <= age <= 18)
        price = 15
    else if(day === 'Weekend' && 18 <= age <= 64)
        price = 20
    else if(day === 'Weekend' && 64 <= age <= 122)
        price = 15
    else if(day === 'Holiday' && 0 <= age <= 18)
        price = 5
    else if(day === 'Holiday' && 18 <= age <= 64)
        price = 12
    else if(day === 'Holiday' && 64 <= age <= 122)
        price = 10
    else
        return "Error"
    console.log(`${price}$`)
}

theatrePromotions('Weekday', 18)