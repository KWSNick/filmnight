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

    let saveDelivery = Boolean($('#save_delivery').attr('checked'));
    let saveBilling = Boolean($('#save_billing').attr('checked'));
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_delivery': saveDelivery,
        'save_billing': saveBilling,
    }
    let url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function () {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.first_name.value) + $.trim(form.last_name.value),
                    phone: $.trim(form.phone_number.value),
                    email: $.trim(form.email.value),
                    address: {
                        line1: $.trim(form.billing_add1.value),
                        line2: $.trim(form.billing_add2.value),
                        city: $.trim(form.billing_town.value),
                        country: $.trim(form.billing_country.value),
                        state: $.trim(form.billing_county.value),
                    }
                }
            },
            shipping: {
                name: $.trim(form.first_name.value) + $.trim(form.last_name.value),
                phone: $.trim(form.phone_number.value),
                email: $.trim(form.email.value),
                address: {
                    line1: $.trim(form.delivery_add1.value),
                    line2: $.trim(form.delivery_add2.value),
                    city: $.trim(form.delivery_town.value),
                    country: $.trim(form.delivery_country.value),
                    postal_code: $.trim(form.delivery_postcode.value),
                    state: $.trim(form.delivery_county.value),
                }
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
    }).fail(function () {
        // If this fails reload the page so the django messages can show us the issue.
        location.reload();
    })


});