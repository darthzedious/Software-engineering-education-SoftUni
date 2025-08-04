function solve(speed, road){
    let difference = 0;
    let speedAsInt = Number(speed)

    if (road === 'motorway'){
        if (speedAsInt <= 130){
            console.log(`Driving ${speedAsInt} km/h in a 130 zone`)
        } else {
            difference = speedAsInt - 130
            let status = speedStatus(difference)
            console.log(`The speed is ${difference} km/h faster than the allowed speed of 130 - ${status}`)
        }
    } else if (road === 'interstate'){
        if (speedAsInt <= 90){
            console.log(`Driving ${speedAsInt} km/h in a 90 zone`)
        } else {
            difference = speedAsInt - 90
            let status = speedStatus(difference)
            console.log(`The speed is ${difference} km/h faster than the allowed speed of 90 - ${status}`)
        } 
    } else if (road === 'city'){
        if (speedAsInt <= 50){
            console.log(`Driving ${speedAsInt} km/h in a 50 zone`)
        } else {
            difference = speedAsInt - 50
            let status = speedStatus(difference)
            console.log(`The speed is ${difference} km/h faster than the allowed speed of 50 - ${status}`)
        }
    } else if (road === 'residential'){
        if (speedAsInt <= 20){
            console.log(`Driving ${speedAsInt} km/h in a 20 zone`)
        } else {
            difference = speedAsInt - 20
            let status = speedStatus(difference)
            console.log(`The speed is ${difference} km/h faster than the allowed speed of 20 - ${status}`)
        }
    }
    
}


function speedStatus(difference){
    let status = '';

    if (difference <= 20){
        status = 'speeding'
    } else if (difference <= 40){
        status = 'excessive speeding'
    } else {
        status = 'reckless driving'
    }
    return status
}

solve(40, 'city')
solve(21, 'residential')
solve(120, 'interstate')
solve(200, 'motorway')
