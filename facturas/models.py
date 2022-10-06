from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator
from productos.models import Producto

from usuarios.models import Usuario


class Sucursal(models.Model):
    nombre=models.TextField(max_length=80, verbose_name="Nombre Sucursal")
    #empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name="Empresa")
    direccion=models.CharField(max_length=70, verbose_name="Dirección")
    telefono=models.CharField(max_length=20, verbose_name="Teléfono", blank=True)
    #administrador=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Administrador")
    #municipio=models.ForeignKey(Municipio, on_delete=models.CASCADE, verbose_name="Municipio")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

# Create your models here.
class Factura(models.Model):
    fecha=models.DateField(verbose_name="Fecha Factura", help_text=u"MM/DD/AAAA")
    numeroSerie=models.TextField(max_length=80, verbose_name="Número de Serie")
    monto=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Monto")
    class TipoFactura(models.TextChoices):
        VENTA='Venta', _('Venta')
        COMPRA='Compra', _('Compra')
    tipoFactura=models.CharField(max_length=6, choices=TipoFactura.choices, default=TipoFactura.Venta, verbose_name="Tipo de Factura")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    #empleado=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Empleado")

class Detalle_Factura(models.Model):
    numeroFactura=models.ForeignKey(Factura, on_delete=models.CASCADE, verbose_name="Número Factura")
    codigoProducto=models.ForeignKey(Producto, on_delete=models.CASCADE, verbose_name="Código Producto")
    cantidad=models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Cantidad")
    precio=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Precio")
    lote=models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Lote")
    fechaExpiracion=models.DateField(verbose_name="Fecha Expiración", help_text=u"MM/DD/AAAA")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

class Detalle_Compra(models.Model):
    cantidad=models.IntegerField(validators=[MinValueValidator(0)], verbose_name="Cantidad")
    precio=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Precio")
    numeroFactura=models.ForeignKey(Factura, on_delete=models.CASCADE, verbose_name="Número Factura")
    detalleFactura=models.ForeignKey(Detalle_Factura, on_delete=models.CASCADE, verbose_name="Detalle Factura")
    class Estado(models.TextChoices):
        ACTIVO='1', _('Activo')
        INACTIVO='0', _('Inactivo')
    estado=models.CharField(max_length=1, choices=Estado.choices, default=Estado.ACTIVO, verbose_name="Estado")

class Devolucion(models.Model):
    fechaDevolucion=models.DateField(verbose_name="Fecha Devolución", help_text=u"MM/DD/AAAA")
    observaciones=models.TextField(max_length=200, verbose_name="Observaciones")
    usuario=models.ForeignKey(Usuario, on_delete=models.CASCADE, verbose_name="Usuario")
    monto=models.BigIntegerField(validators=[MinValueValidator(0)], verbose_name="Monto")
    detalleCompra=models.ForeignKey(Detalle_Compra, on_delete=models.CASCADE, verbose_name="Detalle Compra")