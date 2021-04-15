// Create stripe instance and card element
let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

let cardStyle = {
    base = {
        color: '#CCCCCC',
        fontFamily: '"Barlow Semi Condensed", sans-serif',
    }
    invalid = {
        color: '#ff1919',
    }
}

let card = elements.create('card', {
    style: cardStyle
});
card.mount('#stripe_card');

// Handle card validation errors
// Based on Ci Boutique Ado script
card.addEventListener('change', function (event) {
    let errorDiv = document.getElementById('card_messages');
    if (event.error) {
        let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>`

        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});