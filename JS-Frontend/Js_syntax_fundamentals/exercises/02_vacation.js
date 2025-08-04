function solve(group, type, day) {
  let price = 0;
  if (type === "Students") {
    if (day === "Friday") {
      price = group * 8.45;
    } else if (day === "Saturday") {
      price = group * 9.8;
    } else if (day === "Sunday") {
      price = group * 10.46;
    }
    if (group >= 30) {
      price *= 0.85;
    }
  } else if (type === "Business") {
    if (day === "Friday") {
      price = group * 10.9;
    } else if (day === "Saturday") {
      price = group * 15.6;
    } else if (day === "Sunday") {
      price = group * 16;
    }
    if (group >= 100){
        price -= 10 * (price / group)
    }
  } else if (type === "Regular") {
    if (day === "Friday") {
      price = group * 15;
    } else if (day === "Saturday") {
      price = group * 20;
    } else if (day === "Sunday") {
      price = group * 22.5;
    }
    if (group >= 10 && group <= 20) {
        percentage = price * 0.05
        price -= percentage
    }
  }

  console.log(`Total price: ${price.toFixed(2)}`);
}

solve(30, "Students", "Sunday");
solve(100, "Business", "Sunday");
solve(40, "Regular", "Saturday");
