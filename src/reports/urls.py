from django.urls import include, re_path
from .views import (
		InvoiceStatementCreate,
		InvoiceStatementDetail,
		export_PurinvoiceSt_report,
		DateWiseInvoiceReportCreate,
		DateWisePurchaseInvoiceReportDetail,
		DateWiseSaleInvoiceReportDetail,
		ItemWiseReport,
		ItemWiseReportDetail,
		ItemSupplierWiseReport,
		ItemSupplierWiseReportDetail,
		ExpiryReport,
		export_sale_report,
		export_purchase_report,
		InventoryReportView,
		InventoryReportDetail,
		SupplierWiseReport,
		SupplierWiseReportDetail,
		export_supplier_wise_report,
	)


urlpatterns = [
	re_path(r'^api/', include("reports.api.urls"), name = "reports-api"),

	re_path(r'^sales/InvoiceStatement$', InvoiceStatementCreate.as_view(), name = "SalesInvSt"),
	re_path(r'^sales/InvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})$', \
						 InvoiceStatementDetail, name = "SalesInvSt_rep"),

	re_path(r'^purchase/InvoiceStatement$', InvoiceStatementCreate.as_view(), name = "PurInvSt"),
	re_path(r'^purchase/InvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/$', \
						 InvoiceStatementDetail, name = "PurInvSt_rep"),

	re_path(r'^purchase/InvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/export_report$', \
						 export_PurinvoiceSt_report, name = "export_PurinvoiceSt_report"),


	# Date wise Report [Month Wise]
	re_path(r'^sales/MonthlyInvoiceStatement$', DateWiseInvoiceReportCreate.as_view(), name = "MonhlyInvSale"),
	re_path(r'^sales/MonthlyInvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/$', \
						 DateWiseSaleInvoiceReportDetail, name = "MonhlyInvSale_det"),
	re_path(r'^purchase/MonthlyInvoiceStatement$', DateWiseInvoiceReportCreate.as_view(), name = "MonhlyInvPur"),
	re_path(r'^purchase/MonthlyInvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/$', \
						 DateWisePurchaseInvoiceReportDetail, name = "MonhlyInvPur_det"),

	# Date wise Report [Day Wise]
	re_path(r'^sales/DayInvoiceStatement$', DateWiseInvoiceReportCreate.as_view(), name = "DateInvSale"),
	re_path(r'^sales/DayInvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/$', \
						 DateWiseSaleInvoiceReportDetail, name = "DateInvSale_det"),
	re_path(r'^purchase/DayInvoiceStatement$', DateWiseInvoiceReportCreate.as_view(), name = "DateInvPur"),
	re_path(r'^purchase/DayInvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/$', \
						 DateWisePurchaseInvoiceReportDetail, name = "DateInvPur_det"),

	# export to xlsv
	re_path(r'^purchase/MonthlyInvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/export_report$', \
						 export_purchase_report, name = "PurMonthReport"),
	re_path(r'^purchase/DayInvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/export_report$', \
					 export_purchase_report, name = "PurDayReport"),
	re_path(r'^sales/MonthlyInvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/export_report$', \
						 export_sale_report, name = "SaleMonthReport"),
	re_path(r'^sales/DayInvoiceStatement/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/export_report$', \
					 export_sale_report, name = "SaleDayReport"),


	#Item WISE report
	re_path(r'^sales/ItemWiseReport$', ItemWiseReport.as_view(), name = "ItemWiseSale"),
	re_path(r'^sales/ItemWiseReport/(?P<item_id>\d+)/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})$', \
						 ItemWiseReportDetail, name = "item_wise_sale_det"),

	re_path(r'^purchase/ItemWiseReport$', ItemWiseReport.as_view(), name = "ItemWisePur"),
	re_path(r'^purchase/ItemWiseReport/(?P<item_id>\d+)/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})$', \
						 ItemWiseReportDetail, name = "item_wise_pur_det"),


	re_path(r'^purchase/SupplierItemWiseReport$', ItemSupplierWiseReport.as_view(), name = "ItemSuppWisePur"),
	re_path(r'^purchase/SupplierItemWiseReport/(?P<item_id>\d+)/(?P<supp_id>\d+)/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})$', \
						 ItemSupplierWiseReportDetail, name = "item_supp_wise_pur_det"),


	# supplier wise report
	re_path(r'^purchase/SupplierWiseReport$', SupplierWiseReport.as_view(), name = "supplier_wise_report"),
	re_path(r'^purchase/SupplierWiseReport/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/$', \
						 SupplierWiseReportDetail, name = "supplier_wise_report_det"),

	re_path(r'^purchase/SupplierWiseReport/(?P<from_dt>\d{4}-\d{2}-\d{2})/(?P<to_dt>\d{4}-\d{2}-\d{2})/export_report', \
					 export_supplier_wise_report, name = "export_supplier_wise_report"),



	re_path(r'^ExpiryReport$', ExpiryReport.as_view(), name = "exp_rep"),

	re_path(r'^InventoryReport/(?P<u_type>\w+)/$', InventoryReportView.as_view(), name = "inventory_report"),
	re_path(r'^InventoryReport/(?P<u_type>\w+)/(?P<id>\d+)/$', InventoryReportDetail, name = "inventory_report_det"),

]
