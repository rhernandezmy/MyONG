# MyONG

Este proyecto va a crear una aplicacion para gestionar una asociación.
La asociación esta compuesta por unos socios.
De cada socio tendremos una serie de datos personales y su dirección.

## Modelo: Socio
* Identificador UUID
[X] DNI/NIE
* [X] Nombre y apellidos por separado
* [X] Fecha de nacimiento
* [X] Teléfono
* Dirección con:
    * calle
    * numero
    * piso / puerta / extras (texto libre)
    * codigo postal
    * ciudad (localidad)
    * provincia
    * pais

* [X] IBAN (opcional, solo si quiere domiciliación bancaria)
* [X] Fecha de alta (auto)
* Info tutor si es menor: DNI tutor, nombre tutor, apellidos tutor y telefono