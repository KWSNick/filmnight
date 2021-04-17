from django.http import HttpResponse

class StripeWH_Handler:
    """Handle stripe webhooks"""

    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        """Handle an unknown event"""
        return HttpResponse(
            content=f'Stripe Webhook Received {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle an unknown event"""
        intent = event.data.object
        print(intent)
        pid = intent.id 
        basket = intent.metadata.basket
        save_delivery = intent.metadata.save_delivery
        save_billing = intent.metadata.save_billing
        billing_details = intent.charges.data[0].billing_details
        shipping_details = intent.shipping
        grand_total = round(intent.charges.data[0].amount /100, 2)

        for field, value in  shipping_details.address.items:
            if value == "":
                shipping_details.address[field] = None
        for field, value in  billing_details.address.items:
            if value == "":
                billing_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    billing_country__iexact=billing_details.address.country,
                    billing_town__iexact=billing_details.address.city,
                    billing_add1__iexact=billing_details.address.line1,
                    billing_add2__iexact=billing_details.address.line2,
                    billing_county__iexact=billing_details.address.state,
                    grand_total=grand_total,
                    basket=basket,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'{event["type"]} | SUCCESS: Order already exists',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    email__iexact=billing_details.email,
                    phone_number__iexact=billing_details.phone,
                    billing_country__iexact=billing_details.address.country,
                    billing_town__iexact=billing_details.address.city,
                    billing_add1__iexact=billing_details.address.line1,
                    billing_add2__iexact=billing_details.address.line2,
                    billing_county__iexact=billing_details.address.state,
                    grand_total=grand_total,
                    basket=basket,
                    stripe_pid=pid,
                )
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'{event["type"]} | ERROR: {e}',
                    status=500)
        return HttpResponse(
                content=f'{event["type"]} | SUCCESS: Created order in webhook',
                status=200)

            
    
    def handle_payment_intent_payment_failed(self, event):
        """Handle an unknown event"""
        return HttpResponse(
            content=f'Stripe Webhook Received {event["type"]}',
            status=200)
