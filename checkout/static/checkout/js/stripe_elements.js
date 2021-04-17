// Create stripe instance and card element
let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

let cardStyle = {
    base: {
        color: '#CCCCCC',
        fontFamily: '"Barlow Semi Condensed", sans-serif',
    },
    invalid: {
        color: '#ff1919',
    }
};

let card = elements.create('card', {
    style: cardStyle
});
card.mount('#stripe_card');
$('#stripe_card').addClass('form-control');

// Handle card validation errors
// Based on Ci Boutique Ado script
card.addEventListener('change', function (event) {
    let errorDiv = $('#card_messages');
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

// Handle billing same as delivery address checkbox
$('#same_as_delivery').change(function () {
    if ($('#same_as_delivery').prop('checked') == true) {
        $('#id_billing_add1').val($('#id_delivery_add1').val());
        $('#id_billing_add2').val($('#id_delivery_add2').val());
        $('#id_billing_town').val($('#id_delivery_town').val());
        $('#id_billing_county').val($('#id_delivery_county').val());
        $('#id_billing_postcode').val($('#id_delivery_postcode').val());
        $('#id_billing_country').val($('#id_delivery_country').val());
    } else {
        $('#id_billing_add1').val('');
        $('#id_billing_add2').val('');
        $('#id_billing_town').val('');
        $('#id_billing_county').val('');
        $('#id_billing_postcode').val('');
        $('#id_billing_country').val('');
    }
});

// Handle Form Submission
let form = $('#checkout_form');

form.submit(function (event) {
    event.preventDefault();
    card.update({
        'disabled': true
    });
    $('#submit_checkout').attr('disabled', true);
    stripe.confirmCardPayment(clientSecret, {
        payment_method: {
            card: card,
        }
    }).then(function (result) {
        if (result.error) {
            let errorDiv = $('#card_messages');
            let html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>`

            $(errorDiv).html(html);
            card.update({
                'disabled': false
            });
            $('#submit_checkout').attr('disabled', false);
        } else {
            if (result.paymentIntent.status === 'succeeded') {
                form.submit();
            }
        }
    });
});