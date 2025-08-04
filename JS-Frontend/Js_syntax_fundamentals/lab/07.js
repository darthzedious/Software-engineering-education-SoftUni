function theatrePromotions(day, age) {
    let price;

    if (age < 0 || age > 122) {
        console.log("Error!");
        return;
    }

    if (day === 'Weekday') {
        if (age <= 18) price = 12;
        else if (age <= 64) price = 18;
        else price = 12;
    } else if (day === 'Weekend') {
        if (age <= 18) price = 15;
        else if (age <= 64) price = 20;
        else price = 15;
    } else if (day === 'Holiday') {
        if (age <= 18) price = 5;
        else if (age <= 64) price = 12;
        else price = 10;
    }

    if (price !== undefined) {
        console.log(`${price}$`);
    } else {
        console.log("Error!");
    }
}

// Test cases
theatrePromotions('Weekday', 18);    // 12$
theatrePromotions('Weekend', 42);    // 20$
theatrePromotions('Holiday', -12);   // Error!
theatrePromotions('Holiday', 15);    // 5$
