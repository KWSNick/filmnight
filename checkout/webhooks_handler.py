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

        return HttpResponse(
            content=f'Stripe Webhook Received {event["type"]}',
            status=200)
    
    def handle_payment_intent_failed(self, event):
        """Handle an unknown event"""
        return HttpResponse(
            content=f'Stripe Webhook Received {event["type"]}',
            status=200)
