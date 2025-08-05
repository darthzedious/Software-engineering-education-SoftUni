function solve(speed, road) {
    const limits = {
        motorway: 130,
        interstate: 90,
        city: 50,
        residential: 20
    };

    const limit = limits[road];
    const speedAsInt = Number(speed);
    const difference = speedAsInt - limit;

    if (difference <= 0) {
        console.log(`Driving ${speedAsInt} km/h in a ${limit} zone`);
    } else {
        const status = speedStatus(difference);
        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${limit} - ${status}`);
    }
}

function speedStatus(difference) {
    if (difference <= 20) {
        return 'speeding';
    } else if (difference <= 40) {
        return 'excessive speeding';
    } else {
        return 'reckless driving';
    }
}

solve(40, 'city');


solve(21, 'residential');


solve(120, 'interstate');


solve(200, 'motorway');

