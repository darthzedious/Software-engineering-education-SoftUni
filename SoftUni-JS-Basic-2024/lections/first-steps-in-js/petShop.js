function petShop(array){
    let dogFoodPrice = 2.50
    let catFoodPrice = 4

    let dogFoodPack = Number(array[0]);
    let catFoodPack = Number(array[1]);

    let totalAmount = (dogFoodPack * dogFoodPrice) + (catFoodPack * catFoodPrice)

    console.log(totalAmount + ' lv.')
}

petShop(['5', '4'])