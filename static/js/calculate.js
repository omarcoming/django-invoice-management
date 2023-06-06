

function calculateTax() {
    var subtotal = parseFloat(document.getElementById('subtotal').value);
    var taxRate = 0.0775;
    var tax = subtotal * taxRate;
    document.getElementById('tax').value = tax.toFixed(2);
    var total = subtotal + tax
    document.getElementById('total').value = total.toFixed(2)
};

function calculateBalance() {
    var total = parseFloat(document.getElementById('total').value);
    var deposit = parseFloat(document.getElementById('deposit').value);
    var balance = total - deposit;
    document.getElementById('balance').value = balance.toFixed(2);
};

function calculateSubTotal() {
    var all_total = document.getElementsByName('prod_total');
    var subtotal = 0;
    for (let i = 0; i < all_total.length; i++) {
        subtotal += parseFloat(all_total[i].value)
        document.getElementById('subtotal').value = subtotal.toFixed(2)
    }
};

function calculateProductTotal() {
    var all_qty = document.getElementsByName('qty');
    var all_price = document.getElementsByName('price');
    var all_total = document.getElementsByName('prod_total');
    var len = all_qty.length;
    console.log(all_qty)
    console.log(all_price)
    console.log(all_total)
    for (let i = 0; i < len; i++) {
        var total = parseFloat(all_qty[i].value) * parseFloat(all_price[i].value);
        all_total[i].value = total.toFixed(2)
        calculateSubTotal();
        calculateTax();
        calculateBalance();
    }
};