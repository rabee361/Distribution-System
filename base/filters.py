import django_filters
from .models import *
from django_filters import rest_framework as filters
from datetime import datetime
  

class ProductFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category__name", lookup_expr='iexact')
    barcode = django_filters.CharFilter(field_name="barcode", lookup_expr='iexact')
    name = django_filters.CharFilter(field_name="name", lookup_expr='startswith')
    product_type = django_filters.CharFilter(field_name="category__product_type__name" , lookup_expr="iexact")

    class Meta:
        model = Product
        fields = ['category','name','barcode','product_type']


class EmployeeFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='startswith')
    job_position = django_filters.CharFilter(field_name='job_position', lookup_expr='iexact')

    class Meta:
        model = Employee
        fields = ['name','job_position']


class SupplierFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='startswith')
    company_name = django_filters.CharFilter(field_name='company_name', lookup_expr='startswith')

    class Meta:
        model = Supplier
        fields = ['name','company_name']


class ClientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='startswith')
    category = django_filters.CharFilter(field_name='category', lookup_expr='iexact')

    class Meta:
        models = Client
        fields = ['name','category']


class SalesEmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['name','truck_num']


class CategoryFilter(django_filters.FilterSet):
    product_type = django_filters.CharFilter(field_name="product_type__name" , lookup_expr="iexact")
    class Meta:
        model = Category
        fields = ['name','product_type']


class ProductTypeFilter(django_filters.FilterSet):
    class Meta:
        model = ProductType
        fields = ['name']

############################### Registry #################################


class WithdrawFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(field_name='client__name', lookup_expr='startswith')
    withdraw_name = django_filters.CharFilter(field_name='withdraw_name',lookup_expr='startswith')
    class Meta: 
        model = WithDraw
        fields = ['withdraw_name','client_name']


class DepositeFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(field_name='client__name', lookup_expr='startswith')
    deposite_name = django_filters.CharFilter(field_name='deposite_name',lookup_expr='startswith')
    class Meta: 
        model = Deposite
        fields = ['deposite_name','client_name']


class ExpenseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='startswith')
    expense_name = django_filters.CharFilter(field_name='expense_name',lookup_expr='startswith')
    class Meta: 
        model = Expense
        fields = ['expense_name','name']


class Recieved_PaymentFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name='employee__name',lookup_expr='startswith')
    class Meta:
        model = Recieved_Payment
        fields = ['employee_name','payment_method']


class PaymentFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name='employee__name',lookup_expr='startswith')
    class Meta:
        model = Payment
        fields = ['employee_name','payment_method']


class DebtClientFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(field_name='client_name__name', lookup_expr='startswith')
    class Meta: 
        model = Debt_Client
        fields = ['client_name','payment_method']


class DebtSupplierFilter(django_filters.FilterSet):
    supplier_name = django_filters.CharFilter(field_name='supplier_name__name', lookup_expr='startswith')
    class Meta: 
        model = Debt_Supplier
        fields = ['supplier_name','payment_method']


################################# HR #############################################
        
# class MonthFilter(filters.Filter):
#     def filter(self, qs, value):
#         if value:
#             date = datetime.strptime(value, "%Y-%m")
#             return qs.filter(date__year=date.year, date__month=date.month)
#         return qs

# class SalaryFilter(django_filters.FilterSet):
#     date = MonthFilter(field_name="date")

#     class Meta: 
#         model = Salary
#         fields = ['date']










class DateRangeFilter(filters.Filter):
    def filter(self, qs, value):
        if value:
            # Assuming value is a dictionary with 'from_date' and 'to_date' keys
            from_date = value.get('from_date')
            to_date = value.get('to_date')

            if from_date and to_date:
                # Parse the dates and filter the queryset
                from_date_obj = datetime.strptime(from_date, "%Y-%m-%d")
                to_date_obj = datetime.strptime(to_date, "%Y-%m-%d")
                return qs.filter(date__range=(from_date_obj, to_date_obj))
            elif from_date:
                # Filter by from_date only
                from_date_obj = datetime.strptime(from_date, "%Y-%m-%d")
                return qs.filter(date__gte=from_date_obj)
            elif to_date:
                # Filter by to_date only
                to_date_obj = datetime.strptime(to_date, "%Y-%m-%d")
                return qs.filter(date__lte=to_date_obj)
        return qs

class SalaryFilter(django_filters.FilterSet):
    date_range = DateRangeFilter(field_name="date")

    class Meta:  
        model = Salary
        fields = ['date_range']















class OverTimeFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='startswith')
    class Meta: 
        model = OverTime
        fields = ['employee_name']


class AbsenceFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='startswith')
    class Meta: 
        model = Absence
        fields = ['employee_name']


class DiscountFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='startswith')
    class Meta: 
        model = Discount
        fields = ['employee_name']


class BonusFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='startswith')
    class Meta: 
        model = Bonus
        fields = ['employee_name']


class Advance_On_salaryFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='startswith')
    class Meta: 
        model = Advance_On_salary
        fields = ['employee_name']


class Extra_ExpenseFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='startswith')
    class Meta: 
        model = Extra_Expense
        fields = ['employee_name']


################################ Damaged & Returned Products ####################################
        

class DamagedProductFilter(django_filters.FilterSet):
    product_name = django_filters.CharFilter(field_name='product__name' , lookup_expr='startswith')
    
    class Meta:
        model = DamagedProduct
        fields = ['product_name']


class ReturnedGoodsClientFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(field_name='client__name',lookup_expr='startswith')
    product_name = django_filters.CharFilter(field_name='product__name',lookup_expr='startswith')
    employee_name = django_filters.CharFilter(field_name='employee_name' , lookup_expr='startswith')
    
    class Meta:
        model = ReturnedGoodsClient
        fields = ['product_name','client_name','employee_name']



class ReturnedGoodsSupplierFilter(django_filters.FilterSet):
    supplier_name = django_filters.CharFilter(field_name='supplier__name',lookup_expr='startswith')
    product_name = django_filters.CharFilter(field_name='product__name',lookup_expr='startswith')
    employee_name = django_filters.CharFilter(field_name='employee_name' , lookup_expr='startswith')
    
    class Meta:
        model = ReturnedGoodsSupplier
        fields = ['product_name','supplier_name','employee_name']



################################################## Receipts #############################################
        


class IncomingFilter(django_filters.FilterSet):
    supplier_name = django_filters.CharFilter(field_name="supplier__name", lookup_expr="startswith")
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='startswith')
    

    class Meta:
        model = Incoming
        fields = ['supplier_name', 'employee_name', 'id','freeze']


class OutputFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(field_name='client__name', lookup_expr="startswith")
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='startswith')

    class Meta:
        model = Output
        fields = ['client_name', 'employee_name', 'id']


class ManualFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(field_name='client__name', lookup_expr='startswith')
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='startswith')

    class Meta:
        model = ManualReceipt
        fields = ['client_name', 'employee_name', 'id','freeze']


class OrderFilter(django_filters.FilterSet):
    client_name = django_filters.CharFilter(field_name='client__name', lookup_expr='startswith')

    class Meta:
        model = Order
        fields = ['client_name']


class DelivaryFilter(django_filters.FilterSet):
    employee_name = django_filters.CharFilter(field_name='employee__name', lookup_expr='startswith')

    class Meta:
        model = DelievaryArrived
        fields = ['employee_name']