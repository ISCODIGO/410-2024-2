# Tipos de Campos
A continuación se muestran una lista de los tipos de campos comunes en la creación de modelos.

| Tipo de Campo        | Descripción                              | Atributos Comunes                          |
|----------------------|------------------------------------------|--------------------------------------------|
| **CharField**        | Cadena de caracteres de longitud limitada| `max_length`                               |
| **TextField**        | Texto largo                              | `blank`                                    |
| **IntegerField**     | Números enteros                          | `default`                                  |
| **FloatField**       | Números flotantes                        | `None`                                     |
| **DecimalField**     | Números decimales con precisión fija     | `max_digits`, `decimal_places`             |
| **BooleanField**     | Verdadero/Falso                          | `default`                                  |
| **DateField**        | Solo fecha                               | `auto_now`, `auto_now_add`                 |
| **DateTimeField**    | Fecha y hora                             | `auto_now`, `auto_now_add`                 |
| **EmailField**       | Direcciones de correo electrónico        | `max_length`                               |
| **FileField**        | Archivos                                 | `upload_to`, `max_length`                  |
| **ImageField**       | Imágenes                                 | `upload_to`, `max_length`                  |
| **ForeignKey**       | Relación de muchos a uno                 | `on_delete`, `related_name`                |
| **ManyToManyField**  | Relación de muchos a muchos              | `related_name`                             |
| **OneToOneField**    | Relación de uno a uno                    | `on_delete`, `related_name`                |
| **JSONField**        | Almacenamiento de datos JSON             | `default`                                  |
