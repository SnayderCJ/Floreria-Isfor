from django.shortcuts import render, get_object_or_404
from .models import ArregloFloral, Categoria

def index(request):
    # Obtenemos solo los 4 arreglos más recientes que estén disponibles
    recientes = ArregloFloral.objects.filter(disponible=True).order_by('-id')[:4]
    return render(request, 'pages/index.html', {
        'recientes': recientes
    })

def catalogo(request):
    # Obtenemos todas las categorías y todos los productos
    categorias = Categoria.objects.all()
    productos = ArregloFloral.objects.filter(disponible=True)
    
    # Lógica de filtrado por categoría si se selecciona una
    categoria_id = request.GET.get('categoria')
    if categoria_id:
        productos = productos.filter(categoria_id=categoria_id)
        
    return render(request, 'pages/catalogo.html', {
        'productos': productos,
        'categorias': categorias
    })

def detalle_arreglo(request, pk):
    # Buscamos el arreglo por su ID (Primary Key) o devolvemos un error 404
    arreglo = get_object_or_404(ArregloFloral, pk=pk)
    return render(request, 'pages/detalle.html', {
        'arreglo': arreglo
    })