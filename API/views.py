from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Vendor, Purchase
from .forms import VendorForm, PurchaseForm
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.db.models import Avg, Count
from django.views.decorators.http import require_http_methods
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated


@csrf_exempt
@permission_classes([IsAuthenticated])
def create_vendor(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        form = VendorForm(data)
        if form.is_valid():
            vendor = form.save()
            response_data = {'success': True, 'vendor_id': vendor.id}
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            response_data = {'success': False, 'errors': errors}

        return JsonResponse(response_data)

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
@permission_classes([IsAuthenticated])
def get_all_vendors(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        vendor_list = [{'id': vendor.id, 'name': vendor.name, 'vendor_code': vendor.vendor_code} for vendor in vendors]
        return JsonResponse({'vendors': vendor_list})

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
@permission_classes([IsAuthenticated])
def get_vendor_by_id(request, vendor_id):
    if request.method == 'GET':
        vendor = get_object_or_404(Vendor, id=vendor_id)
        vendor_info = {
            'id': vendor.id,
            'name': vendor.name,
            'contact_details': vendor.contact_details,
            'address': vendor.address,
            'vendor_code': vendor.vendor_code,
            'on_time_delivery_rate': vendor.on_time_delivery_rate,
            'quality_rating_avg': vendor.quality_rating_avg,
            'average_response_time': vendor.average_response_time,
            'fulfillment_rate': vendor.fulfillment_rate,
        }
        return JsonResponse({'vendor': vendor_info})

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
@permission_classes([IsAuthenticated])
def update_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)

    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        form = VendorForm(data, instance=vendor)
        
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True, 'message': f'Vendor with ID {vendor_id} updated successfully'})
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'success': False, 'errors': errors}, status=400)

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)



@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_vendor(request, vendor_id):
    vendor = get_object_or_404(Vendor, id=vendor_id)

    if request.method == 'DELETE':
        vendor.delete()
        return JsonResponse({'success': True, 'message': f'Vendor with ID {vendor_id} deleted successfully'})

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)



# working on purchase stuffs

@csrf_exempt
@permission_classes([IsAuthenticated])
def create_purchase_order(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        form = PurchaseForm(data)
        
        if form.is_valid():
            purchase_order = form.save()
            return JsonResponse({'success': True, 'purchase_order_id': purchase_order.id})
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'success': False, 'errors': errors}, status=400)

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@permission_classes([IsAuthenticated])
def list_all_purchases(request):
    print(request.user)

    if request.method == 'GET':
        purchases = Purchase.objects.all().values()

        return JsonResponse({'purchases': list(purchases)})

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)


@csrf_exempt
@permission_classes([IsAuthenticated])
def get_purchase_by_id(request, id):
    if request.method == 'GET':
        try:
            purchase = get_object_or_404(Purchase, id=id)
        except:
            return JsonResponse({'error': 'Purchase with the specified ID does not exist'}, status=404)

        purchase_data = {
            'po_number': purchase.id,
            'vendor': {
                'id': purchase.vendor.id,
                'name': purchase.vendor.name,
                'vendor_code': purchase.vendor.vendor_code,
                # add other vendor fields as needed
            },
            'order_date': purchase.order_date,
            'delivery_date': purchase.delivery_date,
            'items': purchase.items,
            'quantity': purchase.quantity,
            'status': purchase.status,
            'quality_rating': purchase.quality_rating,
            'issue_date': purchase.issue_date,
            'acknowledgment_date': purchase.acknowledgment_date,
            # add other purchase fields as needed
        }

        return JsonResponse({'purchase': purchase_data})

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
@permission_classes([IsAuthenticated])
def update_purchase_order(request, id):
    try:
        purchase = get_object_or_404(Purchase, id=id)
    except:
        return JsonResponse({'error': 'Purchase with the specified ID does not exist'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body.decode('utf-8'))
        form = PurchaseForm(data, instance=purchase)

        if form.is_valid():
            form.instance.update_status_fields()
            form.save()
            return JsonResponse({'success': True, 'message': f'Purchase order with ID {id} updated successfully'})
        else:
            errors = {field: form.errors[field][0] for field in form.errors}
            return JsonResponse({'success': False, 'errors': errors}, status=400)

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
@permission_classes([IsAuthenticated])
def delete_purchase_order(request, id):
    purchase = get_object_or_404(Purchase, id=id)

    if request.method == 'DELETE':
        purchase.delete()
        return JsonResponse({'success': True, 'message': f'Purchase order with ID {id} deleted successfully'})

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)



def calculate_on_time_delivery_rate(vendor_id):
    # getting all entries whose status is completed
    completed_pos = Purchase.objects.filter(vendor__id=vendor_id, status='completed')
    # checking delivery dates and comparing it with the today 
    # check it before final submit
    on_time_delivered_pos = completed_pos.filter(delivery_date__lte=timezone.now())

    total_completed_pos = completed_pos.count()
    on_time_delivered_pos_count = on_time_delivered_pos.count()

    on_time_delivery_rate = (on_time_delivered_pos_count / total_completed_pos) * 100 if total_completed_pos > 0 else 0
    return on_time_delivery_rate


def calculate_quality_rating_average(vendor_id):
    completed_pos_with_rating = Purchase.objects.filter(vendor__id=vendor_id, status='completed', quality_rating__isnull=False)
    
    quality_rating_avg = completed_pos_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg']
    return quality_rating_avg

def calculate_average_response_time(vendor_id):
    acknowledged_pos = Purchase.objects.filter(vendor__id=vendor_id, acknowledgment_date__isnull=False)
    
    total_response_time = sum((pos.acknowledgment_date - pos.issue_date).total_seconds() for pos in acknowledged_pos)
    average_response_time = total_response_time / acknowledged_pos.count() if acknowledged_pos.count() > 0 else 0
    return average_response_time

def calculate_fulfilment_rate(vendor_id):
    total_pos = Purchase.objects.filter(vendor__id=vendor_id)
    successful_pos = total_pos.filter(status='completed')

    fulfilment_rate = (successful_pos.count() / total_pos.count()) * 100 if total_pos.count() > 0 else 0
    return fulfilment_rate


@csrf_exempt
@permission_classes([IsAuthenticated])
def get_vendor_metrics(request, vendor_id):
    if request.method == 'GET':
        on_time_delivery_rate = calculate_on_time_delivery_rate(vendor_id)
        quality_rating_avg = calculate_quality_rating_average(vendor_id)
        average_response_time = calculate_average_response_time(vendor_id)
        fulfilment_rate = calculate_fulfilment_rate(vendor_id)

        metrics_data = {
            'on_time_delivery_rate': on_time_delivery_rate,
            'quality_rating_avg': quality_rating_avg,
            'average_response_time': average_response_time,
            'fulfilment_rate': fulfilment_rate,
        }

        return JsonResponse({'metrics': metrics_data})

    # other errors
    return JsonResponse({'error': 'Invalid request method'}, status=400)
