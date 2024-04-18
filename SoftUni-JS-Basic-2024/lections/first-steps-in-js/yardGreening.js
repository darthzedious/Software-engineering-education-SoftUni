function yardGreening(input){
    let pricePerMeter = 7.61
    let discount = 0.18
    let totalGround = Number(input[0])

    let brutPrice = pricePerMeter * totalGround
    let finalDiscount = discount * brutPrice
    let netPrice = brutPrice - finalDiscount

    console.log(`The final price is: ${netPrice} lv.`)
    console.log(`The discount is: ${finalDiscount} lv.`)

}

yardGreening(["550"])