# inventory/analytics.py
from django.db.models import Count

def create_chart_div(df, x_col, y_col, title, color):
    """
    Builds and returns a Plotly chart HTML <div>.
    Heavy imports happen ONLY when this function is called.
    """
    import plotly.express as px
    import plotly.offline as pyo

    fig = px.bar(df, x=x_col, y=y_col, title=title, text=y_col)
    fig.update_traces(
        marker=dict(
            color=color,
            line=dict(color="black", width=1),
            opacity=0.9,
        ),
        textfont_size=14,
        width=0.35,
    )
    fig.update_layout(
        paper_bgcolor="#f8f9fa",
        plot_bgcolor="white",
        xaxis=dict(title=x_col, tickangle=-30),
        yaxis=dict(title=y_col, gridcolor="lightgray", zerolinecolor="gray"),
        font=dict(family="Arial", size=14, color="black"),
        bargap=0.4,
        margin=dict(l=50, r=50, t=30, b=20),
        showlegend=False,
    )
    return pyo.plot(fig, output_type="div")


def build_dashboard_chart(query_name, Product, Shipment, Order):
    """
    Returns chart div (or None).
    Heavy import of pandas happens only here.
    """
    import pandas as pd

    if query_name == "product":
        products = Product.objects.values("name", "quantity")
        df = pd.DataFrame(list(products))
        if not df.empty:
            return create_chart_div(df, "name", "quantity", "Product Quantity", "#3B82F6")

    elif query_name == "shipment":
        shipments = Shipment.objects.annotate(
            num_products=Count("shipment_items__product", distinct=True)
        ).values("factory_name", "num_products")
        df = pd.DataFrame(list(shipments))
        if not df.empty:
            return create_chart_div(df, "factory_name", "num_products", "Products Per Shipment", "#14B8A6")

    elif query_name == "order":
        orders = Order.objects.annotate(
            num_products=Count("order_items__product", distinct=True)
        ).values("supermarket_name", "num_products")
        df = pd.DataFrame(list(orders))
        if not df.empty:
            return create_chart_div(df, "supermarket_name", "num_products", "Products Per Order", "#10B981")

    return None